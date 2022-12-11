def snakePattern(matrix): 
    # code here
    for i in range(len(matrix)):
        if i%2==0:
            for j in range(len(matrix[0])):
                print(matrix[i][j],end=" ")
        else:
            for j in range(len(matrix[0])-1,-1,-1):
                print(matrix[i][j],end=" ")
    print()

m=[[1,2,3],[4,5,6],[7,8,9]]
snakePattern(m)