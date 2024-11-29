class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None    
    
    # insert:
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self,current,key):
        if key < current.key:
            if current.left :
                self._insert_recursive(current.left, key)
            else:
                current.left = TreeNode(key)
        elif key>current.key:
            if current.right:
                self._insert_recursive(current.right, key)
            else:
                current.right = TreeNode(key)
    
    # Search:
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self,current,key):
        if not current:
            return "File not found"
        if key == current.key:
            return f"File {key} found"
        elif key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right,key)
    
    # Inorder:
    def inorder(self):
        result=[]
        self._inorder_recursive(self.root,result)
        return result
    
    def _inorder_recursive(self,current,result):
        if current:
            self._inorder_recursive(current.left,result)
            result.append(current.key)
            self._inorder_recursive(current.right,result)

# bst=BinarySearchTree()
# bst.insert(5)
# bst.insert(3)
# bst.insert(7)
# bst.insert(2)
# bst.insert(4)
# bst.insert(6)
# print(bst.search(4)) # Output: File 4 found
# print(bst.search(9)) # Output: File not found
# print(bst.search(2))
# print(bst.inorder()) 
