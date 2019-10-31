#random number generator (few unique)

#imports
import random

#create a file to save the input
input_file = open("Input_few_unique_1000.txt", "w")

#generate random integers
for i in range(1000):
    input_list = str(random.randint(1, 2000000))
	#write the input in the generated file
    input_file.write(input_list+str("\n"))                 

#close the file
input_file.close()