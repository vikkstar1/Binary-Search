import random
import time 


#Simple search
def simple_search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1        

#Binary search
def binary_search(list,target,low_index = None,high_index=None):
    if low_index is None:                   
        low_index = 0
    if high_index is None:
        high_index = len(list)-1    
    if high_index < low_index:
        return -1
    
    #Mid index in the list
    mid_ind = (low_index+ high_index) // 2
    if(target == list[mid_ind]):
        return mid_ind
    elif(target < list[mid_ind]):
        return binary_search(list,target,low_index,mid_ind-1)   
    else:
        return binary_search(list,target,mid_ind+1,high_index)
    
if __name__ == "__main__":
    #Sample List
    u = [81,42,47,3,9,16,22,99,360]
    l = sorted(u)
    target = 3
    print(simple_search(l,target))
    print(binary_search(l,target))