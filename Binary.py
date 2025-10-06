# BinaryCalculator
# Author: David Russell
# Date: 10/5/2025
# Description: A super awesome program that calculates the binary value of an integer
import math
integer_check = False
binary_output = []
while integer_check == False:
    num_1 = input("Please enter an integer: ")
    if num_1.isalpha() == False:
        if num_1.isdecimal() == True:
            integer_check = True
            num_1 = int(num_1)
        else:
            print("That is not an integer")
    else:
        print("That is not an integer")
num_sacrifice = num_1
if num_1 == 1:
    print(f"{num_1} in binary is: 1")
elif num_1 == 0:
    print(f"{num_1} in binary is: 0")
else:
    exp = int(math.log(num_sacrifice, 2))
    for x in range(exp+1):
        binary_output.append("0")
    index_count = exp
    for x in range(index_count+1):
        if num_sacrifice-(2**exp) != 0:
            binary_output[index_count-exp] = "1"
            num_sacrifice = num_sacrifice-(2**exp)
            exp = int(math.log(num_sacrifice, 2))
        elif num_sacrifice-(2**exp) == 0:
            binary_output[index_count-exp] = "1"
            break
            
    binary_output = "".join(binary_output)
    print(f"{num_1} in binary is: {binary_output}")
