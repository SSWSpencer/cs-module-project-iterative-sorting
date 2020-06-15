# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index


        for j in range(i+1, len(arr)): 
            if arr[smallest_index] > arr[j]: 
                smallest_index = j 


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] 

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr) 
    
    for i in range(n-1): 
        for x in range(0, n-i-1): 
            if arr[x] > arr[x+1] : 
                arr[x], arr[x+1] = arr[x+1], arr[x] 

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
    if len(arr) > 0:
        size = len(arr)
        output = [0] * size
        max = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
        count = [0] * (max + 1)

        for i in range(0, size):
            count[arr[i]] += 1

        for i in range(1, max+1):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            i -= 1

        for i in range(0, size):
            arr[i] = output[i]

    return arr
