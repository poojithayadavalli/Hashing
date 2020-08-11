"""

Given an array A[], find a subset of maximum size in which sum of every pair of elements is a prime number.

Print its length and the subset. Consider many queries for different arrays and maximum value of an element as 100000.

Examples :

Input :
3
2 1 2

Output : 
2
1 2

Explanation :
Here, we can only form subsets with size 1 and 2.
maximum sized subset = {1, 2}, 1 + 2 = 3, which 
is prime number.
So, Answer = 2 (size), {1, 2} (subset)

Input :
3
2 1 1
Output : 
3
1 1 2

Explanation :
Maximum subset = {2, 1, 2}, since 1 + 2 = 3,
1 + 1 = 2, both are prime numbers.
Answer = 3 (size), {2, 1, 1} (subset).

"""
import math as mt 
  
MAX = 100001
  
isPrime = [0 for i in range(MAX)] 
  
def sieve(): 
  
    for p in range(2, mt.ceil(mt.sqrt(MAX))):
        if (isPrime[p] == 0) :
            for i in range(2 * p, MAX, p): 
                isPrime[i] = 1
  
def findSubset(a, n): 
  
    cnt1 = 0
    for i in range(n):  
        if (a[i] == 1): 
            cnt1+=1
    if (cnt1 > 0): 
  
        for i in range(n):
            if ((a[i] != 1) and
                (isPrime[a[i] + 1] == 0)): 
  
                print(cnt1 + 1) 
                for j in range(cnt1): 
                    print("1", end = " ") 
  
                print(a[i]) 
                return 0 
    if (cnt1 >= 2): 
  
        print(cnt1) 
  
        # Print all ones(1s). 
        for i in range(cnt1): 
            print("1", end = " ") 
  
        print() 
        return 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (isPrime[a[i] + a[j]] == 0): 
                print(2) 
                print(a[i], " ", a[j]) 
    print(-1) 
sieve()
n=int(input())
arr=list(map(int,input().split()))
findSubset(arr,n)

