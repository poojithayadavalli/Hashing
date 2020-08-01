#root to leaf path with maximum distinct nodes
"""

Tanya found a task on binary tree and felt difficulty in solving.The task is given below:

Given a Binary Tree with n nodes, find count of distinct nodes in a root to leaf path with maximum distinct nodes.

Constraints:
1<=n<=1000
Input must be given as complete binary tree

Input:

Firstline indicates number of nodes n
secondline indicates the nodes of binary tree

Output:
print the count of distinct nodes in a root to leaf path with maximum distinct nodes

Example:

Input:
9
1 2 3 4 5 6 7 null null null null 8 null 9 null

Output:
4

Explanation:

The root to leaf path with maximum distinct nodes is 1-3-6-8.

"""
class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None
  
def largestUinquePathUtil(node, m): 
    if (not node): 
        return len(m) 
    if node.data in m: 
        m[node.data] += 1
    else: 
        m[node.data] = 1
  
    max_path = max(largestUinquePathUtil(node.left, m),largestUinquePathUtil(node.right, m)) 
    m[node.data] -= 1
    if (m[node.data] == 0):  
        del m[node.data]  
  
    return max_path 
def largestUniquePath(node): 
    if (not node): 
        return 0  
    Hash = {} 
    return largestUinquePathUtil(node, Hash)
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = newNode(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root
n=int(input())
x=input().split()
root=None
root=insertLevelOrder(x,root,0,len(x))
print(largestUniquePath(root))
