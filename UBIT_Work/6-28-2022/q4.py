# Q4:Write a program that takes input from user and find the all possible devisor(s) of a given number and store and display the answer, using

def devisor():
    n = int(input("Enter a number: "))
    for i in range(1, n):
        if n % i == 0:
            print(i)
        

devisor()