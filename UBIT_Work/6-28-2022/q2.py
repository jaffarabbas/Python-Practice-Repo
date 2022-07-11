# Q2. Write a program that takes input from the user and find all the prime number from 0 to user-defined numebr, using

def prime():
    n = int(input("Enter a number: "))
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break 
    else:
        print(n, "is a prime number")


prime()