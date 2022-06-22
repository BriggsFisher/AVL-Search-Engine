class AVLnode():  # class for each node
    def __init__(self, k = None, v = None):  # sets key and value equal to None as default
        self.k = k
        self.v = v
        self.right = None
        self.left = None
        self.height = 1
        self.balanceFactor = 0

    def is_a_leaf(self):
        if self.left == None and self.right == None:  # if no children its a leaf
            return True
        else:
            return False

def Hello():
    return "Hello"

class AVLTreeMap():  # tree class setting up all the nodes
    def __init__(self):  # initalizes with no root
        self.root = None
    
    def getHeight(self, cur):
        if cur == None:
            return 0
        else:
            return cur.height

    def getWeightBalance(self, cur):
        if cur == None:
            return 0
        else:
            return cur.getHeight(cur.left) - cur.getHeight(cur.right)
    
    def get(self, key):
        if self.root == None:  # if no root exists there is no tree and thus no keys with values
            return None
        else:
            return self.rec_get(self.root, key)
    
    def rec_get(self, cur, key):
        if cur == None:  # can't find key of empty node
            return None
        if cur.k == key:  # key found
            return cur.v
        else:
            if cur.k > key:  # if current key is greater than the input key go to left child and stop when there is no left child
                if (cur.left == None):
                    return None  # not found
                else:
                    curValue = self.rec_get(cur.left, key)
                    return curValue  # returns to previous recursion with the cur.v
            else:
                if (cur.right == None):  # current key is smaller than input key so go to right child and stop when there is no right child
                    return None  # not found
                else:
                    curValue = self.rec_get(cur.right, key)
                    return curValue  # returns to previous recursion with the cur.v
    
    def put(self, key, val):
        if self.root == None:  # if no root exists there is no tree, set None root to a Node
            self.root = AVLnode(key, val)
            return
        self.root = self.rec_put(self.root, key, val)  # sets root to return of recursive put

    def rec_put(self, cur, key, val):
        if cur == None:
            return AVLnode(key,val)  # return new node to be set as the root in put
        elif cur.k > key:  # if current key is greater than the input key go to left child and stop when there is no left child
                cur.left = self.rec_put(cur.left, key, val)
        else:  # current key is less than input key and go to right child
                cur.right = self.rec_put(cur.right, key, val)

        cur.height = max(self.getHeight(cur.left), self.getHeight(cur.right)) + 1  # update current's height
        cur.balanceFactor = self.getHeight(cur.left) - self.getHeight(cur.right)  # update current's balanceFactor

        if cur.balanceFactor > 1:  # Left Left
            if key < cur.left.k:
                return self.rightRotate(cur)
            elif key > cur.left.k:  # Left Right
                cur.left = self.leftRotate(cur.left)
                return self.rightRotate(cur)

        if cur.balanceFactor < -1:  # Right Right
            if key > cur.right.k:
                return self.leftRotate(cur)
            elif key < cur.right.k:  # Right Left
                cur.right = self.rightRotate(cur.right)
                return self.leftRotate(cur)

        return cur  # if no rotation return original root node as node because there was no change in order

    def leftRotate(self, cur):
        pivot = cur.right
        pivotLeft = pivot.left
        pivot.left = cur
        cur.right = pivotLeft
        cur.height = max(self.getHeight(cur.left), self.getHeight(cur.right)) + 1  # update current's height
        pivot.height = max(self.getHeight(cur.left), self.getHeight(cur.right)) + 1  # update pivot's height, don't need to update pivotLeft's height because cur is taking it as a right child in pivot's place and is updated
        return pivot  # return pivot to be new root

    def rightRotate(self, cur):
        pivot = cur.left
        pivotRight = pivot.right
        pivot.right = cur
        cur.left = pivotRight
        cur.height = max(self.getHeight(cur.left), self.getHeight(cur.right)) + 1  # update current's height
        pivot.height = max(self.getHeight(pivot.left), self.getHeight(pivot.right)) + 1  # update pivot's height, don't need to update pivotLeft's height because cur is taking it as a right child in pivot's place and is updated
        return pivot  # return pivot to be new root

    COUNT = [10]  

        # Function to print binary tree in 2D  
    # It does reverse inorder traversal  
    def print2DUtil(self, root, space) : 
    
        # Base case  
        if (root == None) : 
            return
    
        # Increase distance between levels  
        space += self.COUNT[0] 
    
        # Process right child first  
        self.print2DUtil(root.right, space)  
    
        # Print current node after space  
        # count  
        print()  
        for i in range(self.COUNT[0], space): 
            print(end = " ")
        if root.k != None:
            print(root.v)  
        print("")
    
        # Process left child  
        self.print2DUtil(root.left, space)  
    
    # Wrapper over print2DUtil()  
    def print2D(self, root) : 
        
        # space=[0] 
        # Pass initial space count as 0  
        self.print2DUtil(root, 0)  
    
    # This code is contributed by 
    # Shubham Singh(SHUBHAMSINGH10) 


if __name__ == '__main__':
    tree = AVLTreeMap()
    print(tree.get(4))  # testing get function on a tree that doesn't exist, should return None

    tree.put(15, "bob")  # testing put function, insert node into empty tree
    tree.put(20, "anna")  # testing put function that is not a root
    tree.put(24, "tom")  # testing put function and rotation (Left rotation in this case where anna is the pivot and bob is the root and pivotLeft is None)
    tree.put(10, "david")
    tree.put(13, "david")
    tree.put(7, "ben")
    tree.put(30, "karen")
    tree.put(36, "erin")
    tree.put(25, "david")
    tree.print2D(tree.root)

    print(tree.get(15))  # testing get function, should return key's value bob
    print(tree.get(2))  # checking get on a value that doesn't exist, should return None

