#radixsort implementation

#imports
import copy
import time

#defining method for counting sort
def countingSort(A, exp1): 
    #calculating the length of the array
    length = len(A)   
    # initializing the output array to store the sorted elements
    output = [0] * (length)   
    # initialize count array as 0 
    count = [0] * (10)   
    # Store count of occurrences in count[] 
    for i in range(0, length): 
        index = (A[i]/exp1) 
        count[ int((index)%10) ] += 1  
    # Change count[i] so that count[i] now contains actual position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1]   
    # Build the output array 
    i = length-1
    while i>=0: 
        index = (A[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = A[i] 
        count[ int((index)%10) ] -= 1
        i -= 1 
    # copying the sorted elements from output array to original array 
    i = 0
    for i in range(0,len(A)): 
        A[i] = output[i] 

        
# defining method for radix sort 
def radixSort(Array):  
    # Find the maximum number to know number of digits 
    largest_digit = max(Array)   
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while largest_digit/exp > 0: 
        #calling the countingSort function
        countingSort(Array,exp) 
        exp *= 10
 
    
#defining the main function
if __name__ == "__main__":  
    #initializing the input list
    input_list = []
    #reading the input from the generated file
    file = open('Input_unique_1000.txt','r')
    for val in file.read().split():
        #copying the numbers from the input file to input list
        input_list.append(int(val))
    
    # Make copy of original list
    input_list_copy = copy.deepcopy(input_list)                 
 
    # Execution start time of timsort
    start = time.time() 
    #calling timsort function
    radixSort(input_list) 
    # Execution finish time of timsort
    finish = time.time() 
                            
    print("\n Execution Time of RadixSort: ", (finish - start))
    
    #create a file to store the sorted list
    fileOutput = open('Output_unique_1000.txt', 'w')
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
     
