class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None



class BinarySearchTree:
    def __init__(self):
        self.root = Node()

    def add (self,value):
        if self.root.value is None:
            self.root.value = value
            return
        self.add_data(self.root, value)

    def add_data(self, cn, value):
        if cn.value > value:
            if cn.left is None:
                cn.left = Node()
                cn.left.value = value
                cn.left.parent = cn
            else:
                self.add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = Node()
                cn.right.value = value
                cn.right.parent = cn
            else:
                self.add_data(cn.right, value)                


    def find(self, value):
        if self.root.value is None:
            return False
        
        if self.root.value == value:
            return True
        
        node = self.find_node(self.root, value)
        if node is None:
            return False
        
        return True

    def find_node(self, cn, value):
        if cn is None:
            return None
        
        if cn.value == value:
            return True

        if cn.value > value:
            res = self.find_node(cn.left,value)
            return res
        else:
            res = self.find_node(cn.right, value)
            return res                

    def find_min(self):
        node = self.find_min_node(self.root)
        return node.value
    
    def find_min_node(self, cn):
        if cn.left is None:
            return cn
        
        node = self.find_min_node(cn.left)
        return node
        
    
    def find_max(self):
        node = self.find_max_node(self.root)
        return node.value
    
    def find_max_node(self, cn):
        if cn.right is None:
            return cn
        
        node = self.find_max_node(cn.right)
        return node


bst = BinarySearchTree()
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(10)
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(8) 
print(bst.find(10), bst.find(8), bst.find(20)) 
bst.add(9)   
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(7)  
print(bst.find(10), bst.find(8), bst.find(20))
bst.add(20)       
print(bst.find(10), bst.find(8), bst.find(20))

print(bst.find_min(), bst.find_max())

a = 10