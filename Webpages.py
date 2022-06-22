from AVLTree import *
import re

class WebPageIndex():
    def __init__(self,file):
        self.path = file
        self.AVLpath = AVLTreeMap()
        f = open(self.path, "r")
        textWithUpper = f.read()
        self.text = textWithUpper.lower()  # lower case all the words
        self.text = re.split("\W", self.text)  # split all the words into a list to be searched
        usedWords = []
        for i in self.text:
            if i not in usedWords:
                self.AVLpath.put(i, self.getIndexes(i))  # inputs value as a list of each index for every occurance of the key
                usedWords.append(i)  # adds each used word to an array and only adds more words if the word isn't in the array

    def getCount(self, s):
        if self.AVLpath.get(s) == None:
            return 0
        else:
            count = len(self.AVLpath.get(s))  # counts the len of the list of indecies
            return count

        # for i in self.text:
        #     if i == s:
        #         count += 1  # add 1 to count for every word in the list of all words appearing in the web page
        # return count

    def getIndexes(self, s):
        indices = [i for i, x in enumerate(self.text) if x == s]  # list comprehension to return a list of all indexes of the inputted key
        return indices
        

COUNT = [10]  

def print2DUtil(root, space): 

    # Base case  
    if (root == None):
        return
    # Increase distance between levels  
    space += COUNT[0] 

    # Process right child first  
    print2DUtil(root.right, space)  

    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.k,'-',root.v)  

    # Process left child  
    print2DUtil(root.left, space)

def print2D(root): 
    
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)


if __name__ == '__main__':
    page = WebPageIndex("C:\\Users\Briggs\Desktop\data\doc1-arraylist.txt")  # inputs data file 1 into the WebPageIndex class
    print(page.getCount("java"))  # testing getCount function of a key with one occurance
    print(page.getCount("you"))  # testing getCount function of a key with multiple occurances
    print(page.getIndexes("want"))  # testing getIndexes function
    print2DUtil(page.AVLpath.root, 10)  # testing WebPageIndex using data/doc1.txt in an AVL tree
