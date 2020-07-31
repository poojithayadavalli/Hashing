"""

Guna is learning about logical operators .He found a task as follows

Given an array A[]  of size N. Find the number of pairs (i, j) such that  A[i]  XOR  A[j]  = 0, and 1 <= i < j <= N.

Constraints:

1<=N<=10000

Input:

Firstline indicates integer N
Next line contains integers of array A

Output:

print the count of pairs that follows given condition

Example:

Input:
5
1 3 4 1 4

Output:
2

Explanation : Index (0, 3) and (2, 4)

Input:
3
2 2 2

Output:
3
"""
def calculate(a) :
    a.sort()
    count = 1
    answer = 0 
    for i in range(1, len(a)) :
        if a[i] == a[i - 1] : 
            count += 1
        else :
            answer = answer + count * (count - 1) // 2
            count = 1
    answer = answer + count * (count - 1) // 2
    return answer
x=int(input())
arr=list(map(int,input().split()))
print(calculate(arr))


