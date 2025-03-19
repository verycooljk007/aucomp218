# For Comp 218 Assignment 1 Part 2 Question 1
# Write a program that will read 3 numbers from the user and then print out the biggest number among the three

# Reading three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the biggest number using the max() function
biggest = max(num1, num2, num3)

# Print the biggest number
print("The biggest number is:", biggest)