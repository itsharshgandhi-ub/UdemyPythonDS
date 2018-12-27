'''
Created on Dec 27, 2018

@author: harsh
'''
def bubblesort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1], nums[j]
    return nums

def selectionsort(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                index = j
        if index is not i:
            nums[i],nums[index] = nums[index], nums[i]
    return nums

def insertionsort(nums):
    for i in range(len(nums)):
        j = i
        while j>0 and nums[j-1]>nums[j]:
            nums[j],nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums


def quickPartition(nums,low,high):
    pivot = (low + high)//2
    nums[high],nums[pivot] = nums[pivot],nums[high]
    
    i = low
    for j in range(low,high):
        if nums[j]<=nums[high]:
            nums[i],nums[j] = nums[j] , nums[i]
            i+=1
    
    nums[i],nums[high] = nums[high],nums[i]
    return i

def quicksort(nums,low,high):
    if low>=high:
        return
    pivot  = quickPartition(nums,low,high)
    quicksort(nums, low, pivot-1)
    quicksort(nums, pivot+1, high)
    






if __name__ =="__main__":
    a = [1,5,4,3,55,32,232,122]
    
    print("Bubble Sort")
    print(bubblesort(a))
    
    print("\nSelection sort")
    print(selectionsort(a))
    
    print("\nInsertion Sort")
    print(insertionsort(a))
    
    print("\n Quick Sort")
    print(a)
    quicksort(a, 0, len(a)-1)
    print(a)