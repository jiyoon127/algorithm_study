import sys
input = sys.stdin.readline

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def preorder(node):
    print(node, end = '')
    if node.left != '.': preorder(m_tree[node.left])
    if node.right != '.': preorder(m_tree[node.right])

def inorder(node):
    if node.left != '.': inorder(m_tree[node.left])
    print(node, end = '')
    if node.right != '.': inorder(m_tree[node.right])

def postorder(node):
    if node.left != '.': postorder(m_tree[node.left])
    if node.right != '.': postorder(m_tree[node.right])
    print(node, end = '')

m_tree = {}
for _ in range(int(input())):
    node, left, right = input().split()
    m_tree[node] = Node(node, left, right)


preorder(m_tree['A'])
print() ; inorder(m_tree['A'])
print() ; postorder(m_tree['A'])
