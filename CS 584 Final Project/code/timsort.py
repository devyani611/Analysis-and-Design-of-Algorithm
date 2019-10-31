#TimSort implementation. 

#imports
import copy
import time

#defining the maximum size of the run
RUN = 32
    
# defining the function to perform insertion sort,sorting from left to right of size atmost RUN
def insertionSort(A, first, last): 
    for i in range(first + 1, last+1):        
        temp = A[i]  
        j = i - 1 
        while A[j] > temp and j >= first:             
            A[j+1] = A[j]  
            j -= 1           
        A[j+1] = temp  

        
# defining the merge function to merge the sorted runs  
def merge(A, l, mid, r): 
    # original array is broken in two parts  
    # left and right array  
    len1, len2 =  mid - l + 1 , r - mid  
    left, right = [], [] 
    for i in range(0, len1):
        left.append(A[l + i])  
    for i in range(0, len2):  
        right.append(A[mid + 1 + i])  
        
    i, j, k = 0, 0, l 
    # after comparing, we merge those two arrays in larger sub array  
    while i < len1 and j < len2:         
        if left[i] <= right[j]:  
            A[k] = left[i]  
            i += 1            
        else: 
            A[k] = right[j]  
            j += 1            
        k += 1       
    # copy remaining elements of left, if any  
    while i < len1:         
        A[k] = left[i]  
        k += 1 
        i += 1    
    # copy remaining elements of right, if any  
    while j < len2:  
        A[k] = right[j]  
        k += 1
        j += 1

        
#Defining timsort function  
def timSort(A, n):      
    # Sort individual subarrays of size RUN  
    for i in range(0, n, RUN): 
        #calling the insertion sort function to sort subarrays
        insertionSort(A, i, min((i+31), (n-1)))       
    size = RUN
    #start merging the subarrays
    while size < n:   
        # After every merge, we increase left by 2*size  
        for left in range(0, n-size, 2*size):  
            # find ending point of left sub array  
            # mid+1 is starting point of right sub array  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
           #calling merge function to merge left and right subarrays 
            merge(A, left, mid, right)            
        size = 2*size 
        

   #defining the main function
if __name__ == "__main__":  
    #initializing the input list
    input_list = []
    #reading the input from the generated file
    file = open('Input_few_unique_1000.txt','r')
    for val in file.read().split():
        #copying the numbers from the input file to input list
        input_list.append(int(val))
    
    # Make copy of original list
    input_list_copy = copy.deepcopy(input_list)               
    #calculating the length of the input list
    n = len(input_list)  
 
    # Execution start time of timsort
    start = time.time() 
    #calling timsort function
    timSort(input_list, n) 
    # Execution finish time of timsort
    finish = time.time() 
                            
    print("\n Execution Time of timSort: ", (finish - start))
    
    #create a file to store the sorted list
    fileOutput = open('Output_few_unique_1000.txt', 'w')
    for i in input_list:
        #write sorted list in output file
        fileOutput.write(str(i)+str("\n"))        

                  
    #apply inbuilt sort function to the unsorted list
    input_list_copy.sort()                       

#Program to check if the list sorted by quicksort is in increasing order
    for index in range(len(input_list)):                    
        #compare the sorted input_list with inbuilt sorted list
        if input_list[index] != input_list_copy[index]:                    
            print(index)
            
    #close the file
    file.close() 
     