
# # Python3 implementation of the approach

# # Function that prints
# # the required sequence
# def split(x, n):
#     num  = []
#     if(x < n):
#         print(-1)
#     elif (x % n == 0):
#         for i in range(n):
#             num.append(x//n, end =" ")
#     else:
#         zp = n - (x % n)
#         pp = x//n
#         for i in range(n):
#             if(i>= zp):
#                num.append(pp + 1)
#             else:
#                num.append(pp)

#     return num
# Driver code


def LengthDistribution(length, numberOfBreaks, index):
        distributedList = []
        if length < numberOfBreaks:
            print(-1)
        elif length % numberOfBreaks == 0:
            for i in range(numberOfBreaks):
                distributedList.append(length // numberOfBreaks)
        else:
            calculate = numberOfBreaks - (length % numberOfBreaks)
            final = length // numberOfBreaks
            for i in range(numberOfBreaks):
                if i >= calculate:
                    distributedList.append(final + 1)
                else:
                    distributedList.append(final)
                    
        distributedList.reverse()
        
        return distributedList[index]

x = 15
n = 4
print(LengthDistribution(x, n ,0))
