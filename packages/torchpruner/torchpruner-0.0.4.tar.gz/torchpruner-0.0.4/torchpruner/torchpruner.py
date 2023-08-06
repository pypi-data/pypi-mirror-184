import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch
import time
import copy
import os
import pickle
import numpy as np


def get_mask_from_pruned_model(model):
    '''
    works purely on the model to get
    mask
    '''
    mask_whole_model=[]
    for nm, params in model.named_parameters():
        if "weight" in nm and "bn" not in nm and "linear" not in nm:
            mask_layer=torch.ones(params.shape)
            mask_layer[params==0]=0            
            mask_whole_model.append(mask_layer)
    return mask_whole_model    




def get_mask_compression(mask_whole_model):
    '''
    calculate compression of mask
    '''
    num_total=0
    num_non_zeros=0
    for mask_each_layer in mask_whole_model:
        num_total+=torch.numel(mask_each_layer)
        num_non_zeros+=torch.count_nonzero(mask_each_layer)
        
    return (num_total-num_non_zeros)/num_total


def get_prune_rate_for_compression(model,target_compression):
    prune_rates=np.arange(0.1,2.5,0.1)
    for prune_rate in prune_rates:
        mask_whole_model=prune_model_get_mask(model,prune_rate)
        mask_compression=get_mask_compression(mask_whole_model)
        print(prune_rate,"=>",mask_compression)
        if mask_compression>=target_compression:
            return prune_rate



def nonzero(tensor):
    """Returns absolute number of values different from 0

    Arguments:
        tensor {numpy.ndarray} -- Array to compute over

    Returns:
        int -- Number of nonzero elements
    """
    return np.sum(tensor != 0.0)


def model_size(model, as_bits=False):
    """Returns absolute and nonzero model size

    Arguments:
        model {torch.nn.Module} -- Network to compute model size over

    Keyword Arguments:
        as_bits {bool} -- Whether to account for the size of dtype

    Returns:
        int -- Total number of weight & bias params
        int -- Out total_params exactly how many are nonzero
    """

    total_params = 0
    nonzero_params = 0
    for tensor in model.parameters():
        t = np.prod(tensor.shape)
        nz = nonzero(tensor.detach().cpu().numpy())
        if as_bits:
            bits = dtype2bits[tensor.dtype]
            t *= bits
            nz *= bits
        total_params += t
        nonzero_params += nz
    return int(total_params), int(nonzero_params)    



def getAvg(epoch,prevAvgs,currVals):
    sum_t=prevAvgs*torch.sum(torch.arange(1,epoch+1))+(epoch+1)*currVals 
    sum_t=sum_t/torch.sum(torch.arange(1,epoch+2))
    return sum_t.detach()


def combineMasks(mask1,mask2):
    mask_new=[]
    for i in range(len(mask1)):
        m_1=mask1[i]
        m_2=mask2[i]
        m_new=np.multiply(m_1,m_2)
        mask_new.append(m_new)
    return mask_new

        
def prune_model_get_mask(model,prune_rate):
    '''
    works purely on the model to get
    mask
    '''
    mask_whole_model=[]
    for nm, params in model.named_parameters():
        if "weight" in nm and "bn" not in nm and "linear" not in nm:
            mask_layer=torch.ones(params.shape)
#             print(nm,params.shape)
            all_vals=torch.abs(params.data)
#             print(all_vals.shape)
            all_vals=all_vals[all_vals!=0]
#             print(all_vals.shape)
            abs_var=torch.std(all_vals)            
#             print(abs_var)
#             print(params)
            threshold=abs_var*prune_rate
            num_components=params.shape[0]
            for index_component in range(num_components):
                values=params[index_component]     
                
                
                re_shaped_values=values.flatten()                
                mask_vals = (torch.abs(re_shaped_values)>threshold).float()
                mask_vals=mask_vals.reshape(values.shape)
#                 print(mask_vals.shape)
                mask_layer[index_component]=mask_vals
            mask_whole_model.append(mask_layer)
    return mask_whole_model    



def create_mask_from_mean_wt(model,mean_weight_description,prune_rate):
    mask_whole_model=[]
    for nm, params in model.named_parameters():
        if "weight" in nm and "bn" not in nm and "linear" not in nm:
            mask_layer=torch.ones(params.shape)    
            mean_wt_layer=mean_weight_description[nm]
            wts_this_layer=[]
            for neuron_index in list(mean_wt_layer.keys()):
                all_wts_this_neu=mean_wt_layer[neuron_index]
                all_wts_this_neu=np.asarray(all_wts_this_neu)
                all_wts_this_neu=all_wts_this_neu.flatten()
                all_wts_this_neu=all_wts_this_neu.astype(float)
                all_wts_this_neu=torch.tensor(all_wts_this_neu)
#                 print(all_wts_this_neu)
                wts_this_layer.append(all_wts_this_neu) 
#             print(wts_this_layer)
            abs_var=torch.std(torch.stack(wts_this_layer).flatten())
            threshold=abs_var*prune_rate
            num_components=params.shape[0]          
            for index_component in range(num_components):
                values=params[index_component]          
                re_shaped_values=values.flatten()             
                mask_vals = (torch.abs(re_shaped_values)>threshold).float()
                mask_vals=mask_vals.reshape(values.shape)
                mask_layer[index_component]=mask_vals
            mask_whole_model.append(mask_layer)

    return mask_whole_model


def store_weights_in_dic_conti(weight_description,model,epoch):
    print("store_weights_in_dic_conti")
    if epoch==0:
        for nm, params in model.named_parameters():
            if "weight" in nm and "bn" not in nm and "linear" not in nm:
                if nm not in weight_description:
                    weight_description[nm]={}        
                num_components=params.shape[0]
                for index_component in range(num_components):
                    if index_component not in weight_description[nm]:
                        weight_description[nm][index_component]={}            
                    values=params[index_component]
#                     print(values.shape)
                    weight_description[nm][index_component]=values
        return weight_description
    for nm, params in model.named_parameters():
        if "weight" in nm and "bn" not in nm and "linear" not in nm:
            num_components=params.shape[0]
            for index_component in range(num_components):                
                curr_values=params[index_component]
                old_values=weight_description[nm][index_component]
#                 print(curr_values)
#                 print(old_values)
                new_values=getAvg(epoch,old_values,curr_values)
                
                weight_description[nm][index_component]=new_values                
    return weight_description




class PruneModel:
    def __init__(self, model,
                 wt_description_path=None,weight_description=None,
                model_state_path=None,device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):

        if wt_description_path is not None:
            self.wt_description_path=wt_description_path
        if weight_description is not None:
            self.weight_description=weight_description
        if weight_description is None and wt_description_path is not None:      
            self.load_weight_description()
        if model_state_path is not None:
            model.load_state_dict(torch.load(model_state_path,map_location=device))
            
        self.model=model
        
    def load_weight_description(self):
        self.weight_description = pickle.load( open( self.wt_description_path, "rb" ) )
            
        
    def train_model(self, train_loader, test_loader, 
                             criterion = nn.CrossEntropyLoss(), 
                             optimizer = None, 
                             scheduler = None,
                             device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
                             num_epochs=25, 
                             model_state_path=None):
        

        
        dataloaders={}
        dataloaders["train"]=train_loader
        dataloaders["val"]=test_loader
        
                                                             
        dataset_sizes={}
        dataset_sizes["train"]=len(train_loader.dataset)
        dataset_sizes["val"]=len(test_loader.dataset)
        
        model=self.model
        
        if optimizer==None:
            optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
        if scheduler==None:
            scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)


                
        since = time.time()
        best_model_wts = copy.deepcopy(model.state_dict())
        best_acc = 0.0
        val_acc_history=[]


        for epoch in range(num_epochs):
            print(f'Epoch {epoch}/{num_epochs - 1}')
            print('-' * 10)

            # Each epoch has a training and validation phase
            for phase in ['train', 'val']:
                if phase == 'train':
                    model.train()  # Set model to training mode
                else:
                    model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()                        
                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)
                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]

                print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

                # deep copy the model
                if phase == "val":
                    val_acc_history.append(epoch_acc)
                if phase == 'val' and epoch_acc > best_acc:

                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())
                    if model_state_path:
                        torch.save(model.state_dict(), model_state_path)



        time_elapsed = time.time() - since
        print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
        print(f'Best val Acc: {best_acc:4f}')
        
        # load best model weights
        model.load_state_dict(best_model_wts)    
        self.model=model
    
        

    def evaluate_model(self,test_dataloader,
                       device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")):        
        model=self.model
        
        
        dataloader=test_dataloader
        dataset_sizes=len(dataloader.dataset)
        
        phase="val"
    #     was_training = model.training
    #     model.eval()
        with torch.no_grad():
            running_corrects=0
            total=0
            sum_diff_time=0
            for i, (inputs, labels) in enumerate(dataloader):
                inputs = inputs.to(device)
                labels = labels.to(device)

                outputs = model(inputs)

                _, preds = torch.max(outputs, 1)
                running_corrects += torch.sum(preds == labels.data)
        accuracy = running_corrects.double() /dataset_sizes


        return accuracy        
        
    def train_model_record_weight(self, train_loader, test_loader, 
                             criterion = nn.CrossEntropyLoss(), 
                             optimizer = None, 
                             scheduler = None,
                             device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
                             num_epochs=25, 
                             model_state_path=None,
                             weight_pickle_location=None):


        
        '''
        train and at the same time save the weights in a dictionary
        '''
        

        dataloaders={}
        dataloaders["train"]=train_loader
        dataloaders["val"]=test_loader


        dataset_sizes={}
        dataset_sizes["train"]=len(train_loader.dataset)
        dataset_sizes["val"]=len(test_loader.dataset)

        model=self.model
        
        if optimizer==None:
            optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
        if scheduler==None:
            scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
        

        weight_description={}
        since = time.time()
        best_model_wts = copy.deepcopy(model.state_dict())
        best_acc = 0.0
#         print("going to save init weight")
#         weight_description=store_weights_in_dic(weight_description,model)            


        for epoch in range(num_epochs):
            print(f'Epoch {epoch}/{num_epochs - 1}')
            print('-' * 10)

            # Each epoch has a training and validation phase
            for phase in ['train', 'val']:
                if phase == 'train':
                    model.train()  # Set model to training mode
                else:
                    model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()                        
                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)
                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]

                print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')

                # deep copy the model
                if phase == 'val' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())
                    if model_state_path:
                        torch.save(model.state_dict(), model_state_path)
                # at the end of training epoch save weight
                if phase=="train":
                    print("At the end of an epoch, training, saving weights")                    
                    weight_description=store_weights_in_dic_conti(weight_description,model,epoch)                    


        time_elapsed = time.time() - since
        print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
        print(f'Best val Acc: {best_acc:4f}')

        # load best model weights
        model.load_state_dict(best_model_wts)
        
        self.model=model
        self.weight_description=weight_description
        
        # can we save the weights some where
        if weight_pickle_location==None:
            if not os.path.isdir("pickle_wt"):
                os.mkdir("pickle_wt")
            pkl_file_name="pickle_wt/"+str(time.time())+"_weights.pkl"
        pickle.dump(weight_description, open(pkl_file_name, "wb" ) )
        self.wt_description_path=pkl_file_name
        print("Weighted avg of wt mags stored at ",pkl_file_name)
                

    def filter_threshold(self,threshold):

        model=self.model
        with torch.no_grad():
            for nm,params in model.named_parameters():
                if "weight" in nm and "bn" not in nm and "linear" not in nm:    
        #             print(nm,params.shape)
                    count_addl_filters_removed=0
                    for i in range(params.shape[0]):
            #             print(params[i])
                        compression=(torch.numel(params[i])-torch.count_nonzero(params[i]))/torch.numel(params[i])
                        if compression>threshold and compression<1:
        #                     print(i,compression)
                            params[i]=params[i]*0
                            count_addl_filters_removed+=1
                    if count_addl_filters_removed>0:
                        print(nm,count_addl_filters_removed)


        self.model=model
        

        
        
        
    def apply_mask_model(self,list_mask_whole_model,layer_to_prune=None):
        model=self.model
        mask_layer_count=0
        for nm, params in model.named_parameters():        
            if "weight" in nm and "bn" not in nm and "linear" not in nm:
    #             print(mask_layer_count,layer_to_prune)
                if layer_to_prune is not None:
                    if mask_layer_count>layer_to_prune:
    #                     print(mask_layer_count,layer_to_prune,"returning model")
                        return model


                mask_layer=list_mask_whole_model[mask_layer_count]
                with torch.no_grad():
                    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    #                 print("pruning layer",mask_layer_count)
                    mask_layer=mask_layer.to(device)    
                    params.data=params.data*mask_layer            
                mask_layer_count+=1
        self.model=model

        

    def train_mask_weight(self,train_loader,test_loader, mask_whole_model,
                          criterion = nn.CrossEntropyLoss(), 
                                 optimizer = None, 
                                 scheduler = None,
                                 device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
                                 num_epochs=25, 
                             model_state_path=None,
                          batch_gap_between_prunes=None,
                          layer_to_prune=None,
                         plot_filters=None):

        '''
        apply the mask on weight values
        '''


        if optimizer==None:
            optimizer = optim.SGD(self.model.parameters(), lr=0.001, momentum=0.9)
        if scheduler==None:
            scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)


        dataloaders={}
        dataloaders["train"]=train_loader
        dataloaders["val"]=test_loader


        dataset_sizes={}
        dataset_sizes["train"]=len(train_loader.dataset)
        dataset_sizes["val"]=len(test_loader.dataset)

        since = time.time()
        best_model_wts = copy.deepcopy(self.model.state_dict())
        best_acc = 0.0

        overall_batch_count=0
        for epoch in range(num_epochs):
            print(f'Epoch {epoch}/{num_epochs - 1}')
            print('-' * 10)

            # Each epoch has a training and validation phase
            for phase in ['train', 'val']:
                if phase == 'train':
                    self.model.train()  # Set model to training mode
                else:
                    self.model.eval()   # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for inputs, labels in dataloaders[phase]:
                    overall_batch_count+=1
                    inputs = inputs.to(device)
                    labels = labels.to(device)

                    # zero the parameter gradients
                    optimizer.zero_grad()

                    # forward
                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = self.model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            optimizer.step()       

                            if batch_gap_between_prunes:

                                if overall_batch_count%batch_gap_between_prunes==0:
    #                                 print("This is overall batch number",overall_batch_count)
    #                                 print("Going to prune till layer number",layer_to_prune)                                

                                    # apply mask on weights
                                    self.apply_mask_model(mask_whole_model,layer_to_prune)
                                    layer_to_prune+=1
                            else: 
    #                             print("going to apply mask on whole")
                                self.apply_mask_model(mask_whole_model)

                    # statistics
                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)

                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects.double() / dataset_sizes[phase]

                print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')
                print("plot filters=",plot_filters,"and phase=",phase)
                # end of an epoch, should we plot the filters
                if plot_filters==True and phase=="train":
                    for nm,params in self.model.named_parameters():
                        if "weight" in nm:        
    #                         print(nm,params.data.shape)        
    #                         if len(params.data.shape)==4:
                            plt=plot_filters_of_layer(nm,params)
                            plt.show()


                # deep copy the model
    #             if phase == 'val' and epoch_acc > best_acc:
    #                 best_acc = epoch_acc
    #                 best_model_wts = copy.deepcopy(model.state_dict())
    #                 if model_state_path:
    #                     torch.save(model.state_dict(), model_state_path)



        # probably apply the whole mask here for safe keeping
        print("going to apply mask on whole at the end of all epochs")
        self.apply_mask_model(mask_whole_model)    

        time_elapsed = time.time() - since
        print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
        # calculate final compression
        print("Compression =",self.get_compression())
        if model_state_path:
            print("saving model")
            torch.save(self.model.state_dict(), model_state_path)

        # load best model weights
    #     model.load_state_dict(best_model_wts)


                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        

    def smart_prune(self,target_compression,train_loader,test_loader,max_count=2,num_epochs=10,
                    criterion = nn.CrossEntropyLoss(), 
                                 optimizer = None, 
                                 scheduler = None,
                   device=None,
                   prune_rate=None):


        if target_compression<=0 or target_compression>=1:
            print("Incorrect target compression value, returning without pruning")
            return None
        if num_epochs<10:
            print("Number of epochs need to be >= 10 for pruning method, setting num_epochs=10")
            num_epoch=10

        weight_description=self.weight_description
        
        if prune_rate is None:
            print("Calculaitng prune rate for ",target_compression,"compression")
            prune_rate=get_prune_rate_for_compression(self.model,target_compression)
        print("Prune rate for ",target_compression,"=",prune_rate)
        mask_whole_model=get_mask_from_pruned_model(self.model)
        real_prune_rate=prune_rate
        count=0
        thresh_percentage=1
        rate_reduction=0.0005
        prune_power=0.005


        while True:
            print("Count is",count)
            if count==0:
                # first try use evolution of weights
                mask_whole_model_now=create_mask_from_mean_wt(self.model,weight_description,real_prune_rate)
            else:
                # other tries, use the weights in model
                mask_whole_model_now=prune_model_get_mask(self.model,real_prune_rate)

            mask_whole_model=combineMasks(mask_whole_model,mask_whole_model_now)

            num_batches=len(train_loader)
            num_layers=len(mask_whole_model)
            batch_gap_between_prunes=int(num_batches*(num_epochs-1)/num_layers)
            print("At least ",batch_gap_between_prunes,"batches between every consequent layer prune")

            layer_to_prune=0
            print("Forward propagation")
            self.train_mask_weight(train_loader,test_loader, mask_whole_model,
                                    criterion=criterion, 
                                    optimizer=optimizer, 
                                    scheduler=scheduler,
                                    device=device,
                                    num_epochs=num_epochs, 
                                    batch_gap_between_prunes=batch_gap_between_prunes,
                                    layer_to_prune=layer_to_prune)

            print("Fine pruning")
            self.filter_threshold(thresh_percentage)


            mask_whole_model=get_mask_from_pruned_model(self.model)
    #         mask_whole_model=get_mask_from_pruned_model(pm.model)        
            self.train_mask_weight(train_loader,test_loader, mask_whole_model,
                                    criterion=criterion, 
                                    optimizer=optimizer, 
                                    scheduler=scheduler,
                                    device=device,
                                    num_epochs=num_epochs)   

            thresh_percentage=thresh_percentage-rate_reduction
            real_prune_rate=real_prune_rate+prune_power
            count+=1
            print("count max_count",count,max_count)
            if count>=max_count:
                break


            
        
        
    def get_compression(self):
        model=self.model
        total_size,nz_size=model_size(model)
        compression=(total_size-nz_size)/total_size
        return compression

