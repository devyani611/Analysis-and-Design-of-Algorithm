#quicksort with randomized pivot selection

#imports
import copy , time
import random 


#defining quicksort method
def quicksort(A, first, last):

    if first < last:
        #calling partition method to get pivot
        pivot = randomized_partition(A, first, last)
        #recursive calls to quicksort
        quicksort(A, first, pivot-1)
        quicksort(A, pivot + 1, last)


#defining randomized partition method
def randomized_partition(A, p, r):
    #randomly choose a number between first and last element
    i = random.randint(p, r)    
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


#defining partition function
def partition(A, p, r):                             # Partition function to fix the pivot position
    #fix the position of pivot
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        #check if the first element is less than the pivot
        if A[j] <= pivot:
            i += 1
        #exchange A[i] and A[j]
            A[i], A[j] = A[j], A[i]
    #exchange A[i+1] and A[r]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


#defining the main function
if __name__ == '__main__':
    #initializing the input list
    input_list = []
    #initialize variable to count the number of elements in an input
    count = 0
    #open the generated input file
    file = open('Input_few_unique_1000.txt', 'r')                   
    #read the input from the file
    for i in file.read().split():
        #increment the count as we add element in the list
        count += 1
        #append the input in quick[] list from the input file
        input_list.append(int(i))                     

    #make copy of the original list
    input_list_copy = copy.deepcopy(input_list)              

    # Execution start time of quicksort
    start = time.time()                 
    #calling the quicksort function
    quicksort(input_list, 0, count - 1)
    # Execution finish time of quicksort
    finish = time.time()               

    #print the execution time of sorting
    print("\n Execution Time of quick sort: ", (finish - start))

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