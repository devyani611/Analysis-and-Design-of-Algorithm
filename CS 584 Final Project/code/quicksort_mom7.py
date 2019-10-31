# QuickSort using median-of-median (group 7) as a pivot.

#imports
import copy , time

#Method definition of quicksort
def quicksort(A, first, last):
    if first < last:
        #calling function to choose the pivot
        pivot = median_quick(A[first: last+1], len(A))
        par = partition(A, first, last, pivot)
        #recursive calls to quicksort
        quicksort(A, first, par - 1)
        quicksort(A, par + 1, last)

        
#defining function to select pivot
def median_quick(q, n):
    sublist = []
    median = []
    pivot = None   
    if len(q) >= 1:
        #dividing the arrays into subarrays of 5 elements each
        for i in range(0, n, 7):
            sublist.append(q[i:i + 7])                                 
        for j in sublist:
             #sort the subarrays
            s = sorted(j)
            if len(s) > 0:
                #storing the median element of all subarrays
                median.append(s[(len(s) // 2)])                          
        if len(median) <= 7:
            sorted(median)
             # MoM element as a pivot selection
            pivot = median[len(median) // 2]                            
        else:
            sorted(median)
            #recursive calls to find MoM element as a pivot
            pivot = median_quick(median, len(median) // 2) 
            
    return pivot


#defining partition to fix the position of pivot
def partition(A, p, r, pivot):                      
    for i in range(0, r+1):
        if A[i] == pivot:
            break
    A[i], A[r] = A[r], A[i]
    #fixing the position of pivot
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


#Defining the main function
if __name__ == '__main__':
    #initialize the list
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