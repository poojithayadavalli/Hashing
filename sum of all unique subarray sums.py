#unique subarray sums sum
"""

Given an array of n-positive elements. Sub-array sum is defined as the sum of all elements of a 

particular sub-array, the task is to find the sum of all unique contiguous sub-array sum.

Note: Unique Sub-array sum means no other sub-array will have the same sum value.

Constraints:
1<=n<=1000

Input:
Firstline contains size of array n
secondline indicates elements of array

Output:
print the sum of all unique subarray sums

Example:

Input:
3
3 4 5

Output:
40

Explanation: All possible unique sub-array with their sum are as:
(3), (4), (5), (3+4), (4+5), (3+4+5). Here all are unique so required sum = 40

Input:
3
2 4 2

Output:
12
"""
def findSubarraySum(arr, n):
    res = 0
    m = dict() 
    for i in range(n): 
        Sum = 0
        for j in range(i, n): 
            Sum += arr[j] 
            m[Sum] = m.get(Sum, 0) + 1
    for x in m: 
        if m[x] == 1: 
            res += x 
  
    return res
n=int(input())
arr=[int(x) for x in input().split()]
print(findSubarraySum(arr,n))
