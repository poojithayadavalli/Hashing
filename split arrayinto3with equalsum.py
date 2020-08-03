"""

Consider an array A of n integers. Determine if array A can be split into three consecutive parts such that sum of each part is equal. 

If yes then print any index pair(i, j) such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise print -1.

Input:
Firstline indicates integer n
Secondline contains integers of array A

Output:
print index i and index j

Examples:

Input :
5
1 3 4 0 4

Output :
1 2
Explanation:
Sum of subarray arr[0..1] is equal to
sum of subarray arr[2..3] and also to
sum of subarray arr[4..4]. The sum is 4. 

Input :
3
2 3 4

Output :
-1
Explanation:
No three subarrays exist which have equal sum.
"""

def findSplit(arr, n): 
    preSum = 0 
    ind1 = -1 
    ind2 = -1
    S = arr[0] 
    for i in range(1, n): 
        S += arr[i]
    if(S % 3 != 0): 
        return -1 
    S1 = S / 3
    S2 = 2 * S1 
  
    for i in range(0,n): 
        preSum += arr[i]
        if (preSum == S1 and ind1 == -1): 
            ind1 = i         
        elif(preSum == S2 and ind1 != -1): 
            ind2 = i
            break
    if (ind1 != -1 and ind2 != -1): 
        return str(ind1)+" "+str(ind2)
    return -1
n=int(input())
arr=list(map(int,input().split()))
print(findSplit(arr,n))
