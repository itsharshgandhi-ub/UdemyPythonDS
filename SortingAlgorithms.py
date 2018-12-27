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
if __name__ =="__main__":
    a = [1,5,4,3,55,32,232,122]
    
    print("Bubble Sort")
    print(bubblesort(a))
    
    print("\nSelection sort")
    print(selectionsort(a))