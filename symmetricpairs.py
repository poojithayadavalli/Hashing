"""

Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d. 

For example, (10, 20) and (20, 10) are symmetric. Given an array of n pairs find all symmetric pairs in it.

It may be assumed that the first elements of all pairs are distinct.

Constraints:
2<=n<=1000

Input:
Firstline indicates integer n
Next n lines indicates the pairs of elements

Output:
Print all the symmetric pairs

Example:

Input:
5
11 20
30 40
5 10
40 30
10 5

Output:
30 40
5 10

"""

def symPairs(arr, row): 
    h = dict()
    l=[]
    for i in range(row):
        first = arr[i][0] 
        sec = arr[i][1] 
        if (sec in h.keys() and h[sec] == first):
            l.append(str(sec)+" "+str(first))
  
        else:h[first] = sec
    for i in l:
        print(i)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
symPairs(arr,n)
