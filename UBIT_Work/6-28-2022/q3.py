# Q3. Write a program that takes input from the user and find the sum of all number from 0 to the user-defined number using

from attr import s


def sum():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(0, n):
        sum = sum + i
    print(sum)

sum()