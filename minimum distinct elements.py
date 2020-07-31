"""

Given an array of n items, an i-th index element denotes the item id’s and given a number m, the task is to remove m elements 

such that there should be minimum distinct id’s left.Print the number of distinct id’s.

Constraints:

1<=m<=n<=1000

Input:
Firstline indicates integer n and integer m
Secondline indicates elements of array

Output:
print the minimum number of distinct elements after removing m elements

Example:

Input:
6 3
2 2 1 3 3 3

Output:
1

Explanation:
Remove 1 and both 2's.So, only 3 will be left that's why distinct id is 1.

Input:
4 2
1 1 2 2

Output:
1

Input:
8 2
2 4 1 5 3 5 1 3

Output:
3
"""
def minDistinct(arr,n,m):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d=sorted(d.items(), key=lambda x:x[1])
    i=0
    while i<m:
        if d[i][1]<=m:
            m=m-d[i][1]
            d=d[1:]
        else:
            break
    return len(d)
        
x,y=map(int,input().split())
arr=list(map(int,input().split()))
print(minDistinct(arr,x,y))

