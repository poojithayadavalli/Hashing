"""
Given an array with n positive numbers.The task is that we find largest subset from array that contain elements which are Fibonacci numbers.

Input:
Firstline indicates the integer n
secondline indicates the elements of array

Output:
print the largest subarray with fibonacci numbers

Examples :

Input :
7
1 4 3 9 10 13 7

Output :
1 3 13

Explanation:
The output three numbers are Fibonacci numbers.

Input  :
9
0 2 8 5 2 1 4 13 23

Output :
0 2 8 5 2 1 13 23
"""

def fibSubset(arr, n):
    m= max(arr) 
    a = 0
    b = 1
    hash = [] 
    hash.append(a) 
    hash.append(b) 
    while (b < m):
        c = a + b 
        a = b 
        b = c 
        hash.append(b) 
    l=[] 
    for i in range (n): 
        if arr[i] in hash : 
            l.append(str(arr[i]))
    return " ".join(l)
n=int(input())
arr=list(map(int,input().split()))
print(fibSubset(arr,n))
