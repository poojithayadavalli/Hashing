"""
Given an unsorted array of n integers, find the number of contiguous subarrays having sum exactly equal to a given number k.

Constraints:
1<=n<=1000

Input:
Firstline indicates the array size n
Secondline indicates the elements of array
Thirdline consists of integer k

Output:
Print the count of subarrays whose sum is equal to k

Examples:

Input :
5
10 2 -2 -20 10
-10

Output : 
3

Explanation: arr[0...3], arr[1...4], arr[3..4] have sum exactly equal to -10.

Input :
6
9 4 20 3 10 5
33

Output :
2

Explanation: arr[0...2], arr[2...4] have sum exactly equal to 33.
"""

from collections import defaultdict 
def subarraySum(arr, n, Sum):
    prevSum = defaultdict(lambda : 0)
    
    res = 0 
    currsum = 0
    for i in range(0, n):  
        currsum += arr[i]
        if currsum == Sum:   
            res += 1  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]
        prevSum[currsum] += 1 
       
    return res
x=int(input())
arr=list(map(int,input().split()))
k=int(input())
print(subarraySum(arr,x,k))


