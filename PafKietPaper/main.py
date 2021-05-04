# Question-4	(10-Marks)
# Using Queues Operation Enqueue,Dequeue, Write a algorithm of method names Contain_Equal that takes the strrings “aaabbb” in queue form as input and returns that the strings contain equal numbers of a’s and b’s
# A	A	A	B	B	B
# Ouput Must be Like: Both A’s and B’s are Equal In Quantity Which Is 3.

def Contain_Equal(queue):
    temp = []
    first = queue.pop()
    count = 1
    count2 = 0
    while len(queue) != 0:
        second = queue.pop()
        if first == second:
            temp.append(second)
            count += 1
        elif first != second:
            temp.clear()
            temp.append(second)
            count2 += 1
    print(count, count2)
    if count == count2:
        print("They Are Equal")
    else:
        print("They Are Not Equal")


def main():
    # Initializing a queue
    queue = []
    print("Size : ")
    size = int(input())
    for i in range(size):
        element = input()
        queue.append(element)

    Contain_Equal(queue)


if __name__ == '__main__':
    main()
