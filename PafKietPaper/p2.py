# Question-3	(10-Marks)
# Write an algorithm for a method named Delete_Prime_Numbers_From_Stack which takes the stack of integers values as input and removes all the prime values that a stack contains. No need to write whole/extra code of push, pop functions. You have to write only the above method procedure.
# Note: Make sure that there is no change of order in the remaining stack values after removing the prime values from it.
# If we have a Stack S of integer values like
# 23
# 18
# 8
# 3
# 21
# 2
# After calling the above mentioned method the remaining values which are in the stack like
# 18
# 8
# 21


def Delete_Prime_Numbers_From_Stack(stack):
    temp = []
    for count in stack:
        for i in range(2, count):
            if count % i == 0:
                break
            elif i == count - 1:
                temp.append(count)

    for newList in temp:
        while newList in stack:
            stack.remove(newList)

    for i in stack:
        print(i)


def main():
    # from collections import deque
    stack = [23, 18, 8, 3, 21, 2]
    Delete_Prime_Numbers_From_Stack(stack)


if __name__ == '__main__':
    main()
