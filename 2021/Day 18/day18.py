import ast

filename = "test2.txt"

class TreeNode:
    def __init__(self, parent, children):
        self.parent = parent
        self.children = children
    
    def left(self):
        # If not leaf node, go right until leaf node
        print(type(self.children))
        if type(self.children) is list:
            return self.children[0].left()
        # If parent's left, take parent's right
        if self is self.parent.children[1]:
            return self.parent.left()
        if self is self.parent.children[0]:
            node = self
            while node is node.parent.children[0]:
                node = node.parent
            return node.parent.children[0].right()
    
    def right(self):
        # If not leaf node, go right until leaf node
        if type(self.children) is list:
            return self.children[1].right()
        # If parent's left, take parent's right
        if self is self.parent.children[0]:
            return self.parent.right()
        if self is self.parent.children[1]:
            node = self
            while node is node.parent.children[1]:
                node = node.parent
            return node.parent.children[1].left()
    
    def __str__(self):
        if type(self.children) is int:
            return f"{self.children}"
        if type(self.children) is list:
            return f"[{', '.join([str(child) for child in self.children])}]"

n = []

with open(filename) as f:
    n = ast.literal_eval(f.readline().strip())
    for line in f:
        n = [n, ast.literal_eval(line.strip())]

print(n)

def treeify(parent, children):
    if type(children) is int:
        return TreeNode(parent, children)
    if type(children) is list:
        node = TreeNode(parent, None)
        node.children = [treeify(node, sub) for sub in children]
        return node

tree = treeify(None, n)
print(tree)

node = tree.left()
print(node)

def traverse(l, path):
    sub_l = l
    for i in path:
        sub_l = sub_l[i]
    return sub_l

def explode(l, path):
    if len(path) < 4:
        return
    
    sub_l = traverse(l, path)
    print(sub_l)

# def split(l, path):
#     if len(path) == 1:
#         
#     sub_l = l[path[0]][path[1]][path[2]]
#     l[path[0]][path[1]][path[2]][path[3]] = [sub_l[path[-1]]//2, -(-sub_l[path[-1]]//2)]

# explode(n, [0,0,0,1])

# split(n, [1,1])

# print(n)
