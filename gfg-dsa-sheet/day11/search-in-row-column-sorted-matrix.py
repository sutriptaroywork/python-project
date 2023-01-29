class Solution:
    def search_in_matrix(self, matrix, n, m ,x):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == x:
                    return 1
                    
        return 0


# Driver code
obj = Solution()
matrix = [[3, 30, 38], [36, 43, 60], [40, 51, 69]]
x = 55
n = 3
m = 3
res = obj.search_in_matrix(matrix, n, m ,x)
print(res) 


# here we need to find the a number is exist in a the matrix or not.
# so basically we need to iterate the matrix and check every time if we are getting our desired number or not.
# if found return 1, else return 0 after the loop ends. Because if we are coming after loop, that means we have not found the number within the matrix. 

# here time complexity of the solution will be - O(n + m) and space complexity will be - O(1).
# as we are iterating the matrix, it is dependant on the combined size of the outer array and inner arrays. So the time complexity is  - O(n + m).
# as we are not using any variable, the space complexity will be O(1).

