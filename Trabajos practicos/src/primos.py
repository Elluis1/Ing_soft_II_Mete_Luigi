#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
           # Si el num despues de realizar el mod da 0 genera un break
       else:
           print(num)
