#first half sorted number generator

#imports
import  random
import numpy as np

#generate unique random integers
input_list= random.sample(range(1, 2000000),1000)

#convert list into array
input_array = np.array(input_list)

#Sort the first half input
input_array[0:500].sort()

#create a file to save the input
input_file = open("Input_first_half_sorted_1000.txt", "w")

#write the generated input in the created file
for i in input_array:
    input_file.write('{}\n'.format(i))
                       
#Close the file
input_file.close()

