"""
Problem Statement
Given an unsorted array Arr with n positive integers. Find the  ππ‘β  smallest element in the given array, using Divide & Conquer approach.

Input: Unsorted array Arr and an integer k where  1β€πβ€π 
Output: The  ππ‘β  smallest element of array Arr

Example 1
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
Output = 99

Example 2
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 5
Output = 12

The Pseudocode - fastSelect(Arr, k)
Break Arr into  π5  (actually it is  βπ5β ) groups, namely  πΊ1,πΊ2,πΊ3...πΊπ5 
For each group  πΊπ,β1β€πβ€π5 , do the following:
Sort the group  πΊπ 
Find the middle position i.e., median  ππ  of group  πΊπ 
Add  ππ  to the set of medians  π 
The set of medians  π  will become as  π={π1,π2,π3...ππ5} . The "good" pivot element will be the median of the set  π . We can find it as  πππ£ππ‘=πππ π‘ππππππ‘(π,π10) .
Partition the original Arr into three sub-arrays - Arr_Less_P, Arr_Equal_P, and Arr_More_P having elements less than pivot, equal to pivot, and bigger than pivot respectively.
Recurse based on the sizes of the three sub-arrays, we will either recursively search in the small set, or the big set, as defined in the following conditions:

If k <= length(Arr_Less_P), then return fastSelect(Arr_Less_P, k). This means that if the size of the "small" sub-array is at least as large as k, 
then we know that our desired  ππ‘β  smallest element lies in this sub-array. Therefore recursively call the same function on the "small" sub-array.
If k > (length(Arr_Less_P) + length(Arr_Equal_P)), then return fastSelect(Arr_More_P, (k - length(Arr_Less_P) - length(Arr_Equal_P))). 
This means that if k is more than the size of "small" and "equal" sub-arrays, then our desired  ππ‘β  smallest element lies in "bigger" sub-array.
Return pivot otherwise. This means that if the above two cases do not hold true, then we know that  ππ‘β  smallest element lies in the "equal" sub-array.
"""
def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    n = len(Arr)            
    setOfMedians = []
    Arr_Less_P = []
    Arr_Equal_P = []
    Arr_More_P = []
    i = 0
    while (i< n//5):
        median = findMedian(Arr,i*5,5)
        setOfMedians.append(median)
        i+=1
    # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
    if (5*i < n):
        median = findMedian(Arr, 5*i, n % 5)
        setOfMedians.append(median)
     
    # Step 3 - Find the median of setOfMedians
    if (len(setOfMedians) == 1):            # Base case for this task
        pivot = setOfMedians[0]
    elif (len(setOfMedians)>1):
        pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))
        
    # Step 4 - Partition the original Arr into three sub-arrays
    for element in Arr:
        if (element<pivot):
            Arr_Less_P.append(element)
        elif (element>pivot):
            Arr_More_P.append(element)
        else:
            Arr_Equal_P.append(element)
        
    # Step 5 - Recurse based on the sizes of the three sub-arrays
    if (k <= len(Arr_Less_P)):
        return fastSelect(Arr_Less_P, k)
    elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
        return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))  
    else:
         return pivot     


# Helper function
def findMedian(Arr, start, size): 
    myList = [] 
    for i in range(start, start + size): 
        myList.append(Arr[i])
        

          
    # Sort the array  
    myList.sort() 
  
    # Return the middle element 
    return myList[size // 2] 

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99