"""

Given an array of n integers. Count total number of contiguous sub-array having total distinct elements same as that of total distinct elements of original array.

Constraints:

1<=n<=10000

Input:

Firstline indicates integer n
Secondline contains elements of array

Output:
print the count of contiguous subarray that follows given condition

Example:

Input:
5
2 1 3 2 3

Output:
5

Explanation:
Total distinct elements in array is 3
Total sub-arrays that satisfy the condition 
are:  Subarray from index 0 to 2
      Subarray from index 0 to 3
      Subarray from index 0 to 4
      Subarray from index 1 to 3
      Subarray from index 1 to 4
      
Input:
5
2 4 5 2 1

Output:
2


"""

def countDistinctSubarray(arr, n):
    vis = dict() 
    for i in range(n): 
        vis[arr[i]] = 1
    k = len(vis)
    vid = dict() 
    ans = 0
    right = 0
    window = 0
    for left in range(n): 
      
        while (right < n and window < k): 
  
            if arr[right] in vid.keys(): 
                vid[ arr[right] ] += 1
            else: 
                vid[ arr[right] ] = 1
  
            if (vid[ arr[right] ] == 1): 
                window += 1
  
            right += 1
        if (window == k): 
            ans += (n - right + 1)
        vid[ arr[left] ] -= 1
        if (vid[ arr[left] ] == 0): 
            window -= 1
      
    return ans
x=int(input())
arr=list(map(int,input().split()))
print(countDistinctSubarray(arr,x))
