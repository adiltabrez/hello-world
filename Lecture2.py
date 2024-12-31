# # WAP to check if a number entered by the user is odd or even. 

# num1 = int(input("Enter a number to check: "))

# if num1%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.") 

# check = "even" if num1%2 == 0 else "odd"
# print(check)
#================================================================================================ 

a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))

compare = "a is greatest" if a > b and a > c else "b is greatest" if b > a and b > c else "c is greatest" 
print(compare)