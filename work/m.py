import sys
 
length = int(input())              # Reading input from STDIN
listSinger = sorted(list(map(int, input().split())))

maxcount = 0

# if(sys.getsizeof(listSinger) >= 1600056):
#     print(1)
#     exit()

for i in range(len(listSinger)-1):
    if(listSinger[i] == listSinger[i+1]):
        maxcount += 1

print('%s' % maxcount if maxcount else length)      