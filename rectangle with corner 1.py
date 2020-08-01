"""

Rani found a task as follows:

There is a given binary matrix of size M x N, task is to find if there exists any rectangle or square in the given matrix whose all four corners are equal to 1.

Print "Yes" if such rectangle exists else  print "No".

Constraints:

1<=m<=1000
1<=n<=1000

Input:
Firstline indicates row size m and column size n
next m lines contains elements of each row

Output:
print whether it contains the rectangle or not

Example:

Input:
4 5
1 0 0 1 0
0 0 1 0 1
0 0 0 1 0
1 0 1 0 1

Output:
Yes

Explanation:
here 1 0 1  forms a rectangle with corner 1
     0 1 0
     1 0 1

Input:
3 3
1 0 1
0 0 0
1 0 1

Output:
Yes

"""
def isRectangle(matrix): 
    rows = len(matrix) 
    if (rows == 0): 
        return False
  
    columns = len(matrix[0])
    table = {}
    for i in range(rows):
        for j in range(columns - 1):
            for k in range(j + 1, columns):  
                if (matrix[i][j] == 1 and
                    matrix[i][k] == 1):  
                    if (j in table and k in table[j]): 
                        return True
  
                    if (k in table and j in table[k]): 
                        return True  
                    if j not in table: 
                        table[j] = set() 
                    if k not in table: 
                        table[k] = set() 
                    table[j].add(k)  
                    table[k].add(j) 
    return False
m,n=map(int,input().split())
matrix=[]
for i in range(m):
    matrix.append(list(map(int,input().split())))
if isRectangle(matrix):
    print("Yes")
else:
    print("No")
