

def checkInlist(list):
    temp = []
    for i in list:
        if i not in temp:
            temp.append(i)

    print("With Dublicate : ",list)
    print("Remove Dublicate: ",temp)


def parent():
    def child():
        return 33
    return child()


def checkInList(list, spesific):
    a = list.count(spesific)
    print(spesific, ': ',a)


def main():
    list = [1,2,3,3,3,3]
    checkInlist(list)
    print("Assigend : ",parent())
    colors = ["red", "green", "green", "green"]
    checkInList(colors,'red')
    checkInList(colors, 'green')
    print('numeric')
    checkInList(list, 3)

if __name__ == '__main__':
     main()