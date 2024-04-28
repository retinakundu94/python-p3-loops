#!/usr/bin/env python3

def happy_new_year():
    i = 0
    while i < 10:
        print("Happy New Year!")
    i += 1

def square_integers(int_list):
    squared_list = []  # Create an empty list to store squared elements
    for num in int_list:  # Iterate through each integer in the input list
        squared_list.append(num ** 2)  # Square the integer and add it to the squared list
    return squared_list  # Return the list of squared elements

def fizzbuzz():
    for i in range(1, 101):  # Iterate from 1 to 100
        if i % 3 == 0 and i % 5 == 0:  # Check if the number is divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if the number is divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if the number is divisible by 5
            print("Buzz")
        else:
            print(i)  # Print the number if it's not divisible by 3 or 5
