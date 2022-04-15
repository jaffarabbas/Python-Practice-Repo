# 1- Ask the user to enter their name and then display their name three times.

userName = input("Enter User name : ")
for i in range(0,3):
    print(userName)

# 2- Ask the user to enter their name and display each letter in their name on a separate line.
userName = input("Enter User name : ")
for i in userName:
    print(i)

# 3- Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them 
# if they want that number included. If they do, then add the number to the total. If they do not want it 
# included, don’t add it to the total. After they have entered all five numbers, display the total.

total = 0
for i in range(0,5):
    num = int(input("Enter number : "))
    print("Wnat to add number in total ? ")
    value = input("y / n : ")
    if value == "y":
        print("current total : ",total)
        total += num
        print("new total : ",total)
    else:
        continue

print("Total : ",total)

# 4- Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the 
# names and after each name display “[name] has been invited”. If they enter a number that is 10 or higher, 
# display the message “Too many people”.

peopleCount = 0
counter = 0

peopleCount = int(input("How many people wnat to invite : "))
if peopleCount < 10:
    for i in range(0,peopleCount):
        counter+=1
        pn = input(f"Enter Person {counter} name : ")
        print(f"{pn} has been invited")
else:
    print("Too many people")