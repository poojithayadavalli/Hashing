"""

Given a string of size n. The task is to print longest possible substring that has exactly M unique characters.

If there are more than one substring of longest possible length, then print any one of them.

Input:
Firstline contains size of string n
Secondline contains the string
Third line indicates integer m

Output:
print the length of longest possible substring that has exactly m unique characters

Examples:

Input:
6
aabbcc
1
Output:
2

Explanation:
Max substring can be any one from {"aa" , "bb" , "cc"}.

Input:
6
aabbcc
2

Output:
4

Explanation:
Max substring can be any one from {"aabb" , "bbcc"}.

Input:
6
aaabbb
3
Output:
-1
Explanation:
There are only two unique characters,thus no substring is possible

"""

MAX_CHARS = 26  
def isValid(count, k):  
    val = 0
    for i in range(MAX_CHARS):  
        if count[i] > 0:  
            val += 1 
    return (k >= val)  

def kUniques(s, k):  
    u = 0
    n = len(s) 
    count = [0] * MAX_CHARS  
    for i in range(n):  
        if count[ord(s[i])-ord('a')] == 0:  
            u += 1
        count[ord(s[i])-ord('a')] += 1
    if u < k: 
        return -1
    curr_start = 0
    curr_end = 0 
    max_window_size = 1
    max_window_start = 0 
    count = [0] * len(count)  
  
    count[ord(s[0])-ord('a')] += 1   
    for i in range(1,n):  
        count[ord(s[i])-ord('a')] += 1
        curr_end+=1 
        while not isValid(count, k):  
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1
            
        if curr_end-curr_start+1 > max_window_size:  
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start  
  
    m=s[max_window_start:max_window_start  + max_window_size]
    return max_window_size
n=int(input())
arr=input()
k=int(input())
print(kUniques(arr,k))
