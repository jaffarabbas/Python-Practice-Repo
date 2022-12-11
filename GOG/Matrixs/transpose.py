#Back-end complete function Template for Python 3

class Solution:
    
    #Function to find transpose of a matrix.
    def transpose(self,matrix, n):
        # code here
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix


# if __name__ == '__main__': 
#     t = int (input ())
#     for _ in range (t):
#         n = int(input())
#         matrix = [[0 for j in range(n)] for i in range(n)]
#         line1 = [int(x) for x in input().strip().split()]
#         k=0
#         for i in range(n):
#             for j in range (n):
#                 matrix[i][j]=line1[k]
#                 k+=1
#         obj = Solution()
#         obj.transpose(matrix,n)
#         for i in range(n):
#             for j in range(n):
#                 print(matrix[i][j],end=" ")
#         print()
            
