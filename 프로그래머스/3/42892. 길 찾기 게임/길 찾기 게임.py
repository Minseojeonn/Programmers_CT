import sys
sys.setrecursionlimit(1000000000)
from collections import deque
class Node():
    def __init__(self,node_idx,x,y):
        self.parent = None
        self.left = None
        self.right = None
        self.node_idx = node_idx
        self.x = x
        self.y = y
    
    def isleft(self):
        if self.left is None:
            return False
        else:
            return True
    
    def isright(self):
        if self.right is None:
            return False
        else:
            return True
    
    def set_left(self,left):
        self.left = left
    def set_right(self,right):
        self.right = right
    def set_parent(self,parent):
        self.parent = parent
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_idx(self):
        return self.node_idx

def build_tree(nodeinfo):
    #print(nodeinfo)
    root = Node(nodeinfo[0][2],nodeinfo[0][0],nodeinfo[0][1]) #idx, x, y
    root.set_parent = None
    for idx,i in enumerate(nodeinfo[1:]):
        current_x, current_y, current_idx = i[0], i[1], i[2]
        current = Node(current_idx,current_x,current_y)
        parent = root
        count = 0
        while True: #x는 중복되지 않는다.
            if parent.get_x() > current_x:
                if parent.isleft() is False:
                    current.set_parent(parent)
                    parent.set_left(current)
                    break
                else:
                    parent = parent.get_left()
            elif parent.get_x() < current_x: 
                if parent.isright() is False:
                    current.set_parent(parent)
                    parent.set_right(current)
                    break
                else:
                    parent = parent.get_right()
    return root

def preorder(root):
    stack = [root]
    #print(root.get_idx())
    visited = []
    while stack:
        visit = stack.pop()
        visited.append(visit.get_idx())
        if visit.isright():
            stack.append(visit.get_right())
        if visit.isleft():
            stack.append(visit.get_left())
    return visited

def postorder(root):
    visited = []
    if root.isleft() == False and root.isright() == False:
        return [root.get_idx()]
    if root.isleft():
        visited+=postorder(root.get_left())
    if root.isright():
        visited+=postorder(root.get_right())
    return visited + [root.get_idx()]

def solution(nodeinfo):
    nodeinfo = [[i[0],i[1],idx+1] for idx,i in enumerate(nodeinfo)]
    #print(nodeinfo)
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x:(-x[1],x[0]))
    #print(sorted_nodeinfo)
    root = build_tree(sorted_nodeinfo)
    print()
    answer = [preorder(root),postorder(root)]
    
    return answer
    