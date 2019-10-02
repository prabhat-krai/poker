"""
A disorganized handyman has mixed up his nuts and bolts in a bag and your task is to match them as 
quickly as possible. 
"""
import random

n = int(input("Number of nut and bolts in total"))
nuts = [0]*n
bolts = [0]*n
types = int(input("The different categories of nuts and bolts available:"))
for i in range (n):
    number_generated = random.randint(1, types)
    nuts[i] = bolts[i] = number_generated
random.shuffle(bolts)

"""
Now to solve this naively would be take one nut and try it with n bolts. But that will be an 
O(n^2) solution. 
So, we can should look to sort the lists and then each nut will be matched to its bolt.
We will use quicksort and that too inplace so that we can work with small memory.
"""
def pivot_partition_inplace(lst, start, end):
    pivot = lst[end] 
    bottom = start - 1       
    top = end

    done = False
    while not done: 

        while not done:
            bottom += 1 
            if (bottom == top): 
                done = True 
                break
            if (lst[bottom] > pivot): 
                lst[top] = lst[bottom] 
                break 

        while not done:
            top -= 1
            if (top == bottom): 
                done = True 
                break
            if (lst[top] < pivot): 
                lst[bottom] = lst[top] 
                break 

    lst[top] = pivot 
    return top 


def quicksort(lst, start, end):
    if start < end: 
        split = pivot_partition_inplace(lst, start, end) 
        quicksort(lst, start, split - 1)
        quicksort(lst, split + 1, end)
    return
    
quicksort(nuts, 0, n - 1)
quicksort(bolts, 0, n - 1)

print(nuts, bolts)
