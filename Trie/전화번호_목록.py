# simplified trie--------------------------------------------------------------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

t = int(input())
ans = []
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, num):
        current_node = self.head

        for n in num:
            if n not in current_node.children:
                current_node.children[n] = Node(n)
            current_node = current_node.children[n]

        if not current_node.children: return False
        else: return True

def findCase():
    n = int(input())
    trie = Trie()
    num_list = [input().strip() for _ in range(n)]
    num_list.sort(reverse=True)

    for num in num_list:
        if trie.insert(num):
            print("NO")
            return

    print("YES")

for _ in range(t):
    findCase()
    
    
# dictionary-------------------------------------------------------------------------------------------------------------------------------------------------------


import sys
input = sys.stdin.readline

t = int(input())

def findCase():
    n = int(input())
    num_list = [input().strip() for _ in range(n)]
    dict = {}

    for num in num_list:
        dict[num] = 1

    for num in num_list:
        temp = ''
        for n in num:
            temp += n
            if temp in dict and temp != num:
                return False
    return True


for _ in range(t):
    if findCase(): print("YES")
    else: print("NO")
