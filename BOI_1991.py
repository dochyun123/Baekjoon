def preorder(root):
    if root == '.' or None:
        return 
    print(root,end = '')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.' or None:
        return  
    inorder(tree[root][0])
    print(root,end = '')
    inorder(tree[root][1])


def postorder(root): 
    if root == '.' or None:
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root,end = '')



tree = {}
N = int(input())
for i in range(N):
    root,left,right = map(str,input().split())
    tree[root] = [left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')