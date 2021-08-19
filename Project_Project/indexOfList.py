letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
value = "jaffar"

password = 'jaffar'

def userInputShuffleIntoNumber():
    print("hii : ", password)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    letterListOfNumber = ''
    try:
        for i in password:
            indexes = [x for x in range(len(letters)) if letters[x] == i]
            letterListOfNumber += str(indexes.pop())

    except ValueError:
        return ValueError

    return letterListOfNumber


print(userInputShuffleIntoNumber())

# lst = [10, 20, 30, 10, 50, 10, 45, 10]
#
# print("List : ", lst)
#
# res = [x for x in range(len(lst)) if lst[x] == 10]
#
# print("Indices at which element 10 is present: " + str(res))
