# Python Project 2 
# Programmer:         Roman Archer
# Date Of Completion: 23rd May 2024
# Description:        Calculator Responsive To User Input That Can Add, Subtract, Divide or Multiply 2 Numbers
#                     And Present The Sum After Input. I Used if Statements To Distinct Each Operator And Their 
#                     Given Value Of The Two Numbers The User Uses.

operator = input("Enter An Operator You'd Like To Use [- + / x] : ")
number_1 = input("Enter The First Number: ")
number_2 = input("Enter The Second Number: ")

float(number_1)
float(number_2)

if operator == "-":
    result = float(number_1) - float(number_2)
    print (f"Sum: {result}")
elif operator == "+":
    result = float(number_1) + float(number_2)
    print(f"Sum: {result}")
elif operator == "x":
    result = float(number_1) * float(number_2)
    print(f"Sum: {result}")
elif operator == "/":
    result = float(number_1) / float(number_2)
    print(f"Sum: {result}")
else:
    print(f"{operator} Is Not Valid, Please Enter The Operator In The Supported Field Above")
