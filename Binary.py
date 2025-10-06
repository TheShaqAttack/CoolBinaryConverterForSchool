# BinaryCalculator
# Author: David Russell
# Date: 10/5/2025
# Description: A super awesome program that calculates the binary value of an integer
binary_output = []
binary_starting_space = 0
i = 0
x = 0
even = 100 #placeholder value
value_found = False
integer_check = False
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
if num_1 % 2 == 0:
    even = True
else:
    even = False
while value_found == False: 
    if (num_sacrifice - 2**i) > 0:
        i+=1
    elif (num_sacrifice - 2**i) == 0:
        if num_1 == num_sacrifice:
            binary_output = ["1"]
            while x != i:#+1#
                binary_output.append("0")
                x+=1
        if even == False:
            binary_output[(binary_starting_space-(i))] = "1"
        value_found = True
        break
    elif (num_sacrifice - 2**i) < 0:
        i-=1
        if num_1 == num_sacrifice:
            binary_output = ["1"]
            while x != i:#+1#
                binary_output.append("0")
                x+=1
            binary_starting_space = i  
        num_sacrifice = num_sacrifice - 2**i
        binary_output[binary_starting_space-(i)] = "1"
        i = 0
        x = 0
        if num_sacrifice == 0:
            break
binary_output = "".join(binary_output)
print(f"{num_1} in binary is: {binary_output}")
