#unique random number generator

#imports
import  random

#generate unique random integers
input_list= random.sample(range(1, 2000000),1000)

#create a file to save the input
input_file = open("Input_unique_1000.txt", "w")

#write the generated input in the created file
for i in input_list:
    input_file.write('{}\n'.format(i))
                       
#Close the file
input_file.close()