class BSTnode():  # class for each node
    def __init__(self, value = None):  # sets value equal to None as default
            self.value = value
            self.right = None
            self.left = None
    
    def is_a_leaf(self):
        if self.left == None and self.right == None:  # if no children its a leaf
            return True
        else:
            return False

class BinarySearchTree():  # tree class setting up all the nodes
    def __init__(self):  # initalizes with no root
        self.root = None
    
    def insert(self, val):
        if self.root == None:  # if no root exists there is no tree, set None root to a Node
            self.root = BSTnode(val)
            return
        self.rec_insert(self.root,val)

    def rec_insert(self, cur, val):
        if cur.value > val:  # if current node is greater than the input value go to left child and stop to place when child is None
            if (cur.left == None):
                cur.left = BSTnode(val)
            else:
                self.rec_insert(cur.left,val)
        
        else:
            if (cur.right == None):  # current node is smaller than input value so go to right child and stop to place when child is None
                cur.right = BSTnode(val)
            else:
                self.rec_insert(cur.right,val)


    def getTotalHeight(self):
        if self.root == None:  # height is not defined for an empty tree and is denoted as -1
            return -1
        longestHeight, totalHeight = self.rec_getHeight(self.root)  # longestHeight is height of the root, totalHeight is root height + total height of left subtree + total height of right subtree height
        return totalHeight

    def rec_getHeight(self, cur):
        if cur == None:  # return once the node is empty (Base case)
            return -1, 0
        leftHeight, leftTotal = self.rec_getHeight(cur.left)  # finding the height of left subtree recursively, leftTotal keeps the left child's height
        rightHeight, rightTotal = self.rec_getHeight(cur.right)  # finding the height of right subtree recursively
        tallestHeight = max(leftHeight, rightHeight) + 1  # height of the root calculated as the largest height of either subtree + 1 to add the edge from the root to the subtree, recursively increasing height by 1 starting at 0
        return tallestHeight, leftTotal+rightTotal+tallestHeight  # totalHeight is adding each recusrive total left subtree height with each recursive total right subtree height with root height

    def getWeightBalanceFactor(self):
        if self.root == None:  # weight balance is equal to 0 for an empty tree
            return 0
        maxWeight = max(self.rec_weightBalanceFactor(self.root)[1])  # find max of the totalWeight array list 
        return maxWeight

    def rec_weightBalanceFactor(self, cur):
        if cur == None:  # return once the node is empty
            return 0, []
        numLeftNodes, leftWeight = self.rec_weightBalanceFactor(cur.left)  # finding the num nodes and weight of the left subtree recursively
        numRightNodes, rightWeight = self.rec_weightBalanceFactor(cur.right)  # finding the num nodes and weight of the right subtree recursively
        totalNodes = numLeftNodes + numRightNodes + 1  # counts number of nodes below this node and + 1 to include the node itself
        totalWeight = [abs(numLeftNodes - numRightNodes)] + leftWeight + rightWeight  # totalWeight is an array with absolute of left nodes - right nodes for the current node weight + recursive weight of left children + recursive weight of right children
        return totalNodes, totalWeight  # return to use in next recursion

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
        if root.value != None:
            print(root.value)  
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
    inputdata = [8,18,5,15,17,25,40,80]  # testing standard tree with multiple levels and children
    tree = BinarySearchTree()
    for item in inputdata:
        tree.insert(item)  # testing insert function
    tree.print2D(tree.root)  
    print(f"Total height of tree is {tree.getTotalHeight()}")  # testing getTotalHeight function
    print(f"Weight balance of tree is {tree.getWeightBalanceFactor()}")  # testing getWeightBalanceFactor function


    inputdata2 = []  # testing empty tree
    tree2 = BinarySearchTree()
    for item2 in inputdata2:
        tree2.insert(item2)
    tree2.print2D(tree2.root)  
    print(f"Total height of tree2 is {tree2.getTotalHeight()}")
    print(f"Weight balance of tree2 is {tree2.getWeightBalanceFactor()}")

    
    inputdata3 = [5]  # testing tree with root only
    tree3 = BinarySearchTree()
    for item3 in inputdata3:
        tree3.insert(item3)
    tree3.print2D(tree3.root)  
    print(f"Total height of tree3 is {tree3.getTotalHeight()}")
    print(f"Weight balance of tree3 is {tree3.getWeightBalanceFactor()}")


    inputdata4 = [5,3,7]  # testing tree with root with two children
    tree4 = BinarySearchTree()
    for item4 in inputdata4:
        tree4.insert(item4)
    tree4.print2D(tree4.root)  
    print(f"Total height of tree4 is {tree4.getTotalHeight()}")
    print(f"Weight balance of tree4 is {tree4.getWeightBalanceFactor()}")


    inputdata5 = [5,1,0]  # testing tree with a node valued at 0
    tree5 = BinarySearchTree()
    for item5 in inputdata5:
        tree5.insert(item5)
    tree5.print2D(tree5.root)  
    print(f"Total height of tree5 is {tree5.getTotalHeight()}")
    print(f"Weight balance of tree5 is {tree5.getWeightBalanceFactor()}")

    
    # Tests were made with the assumption of no duplicate values or negative values inputted