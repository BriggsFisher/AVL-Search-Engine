from Webpages import *
from PriorityQueue import *

def readFiles(path):  # folder path as input
    instanceList = []
    for instance in WebPageIndex():
        instanceList.append(WebPageIndex(path))
    return(instanceList)  # returns list of WebPageIndex instances

if __name__ == '__main__':
    queryFile = ("C:\\Users\Briggs\Desktop\queries.txt")
    # read each line in a for loop, and set each index of each line to be the query that I use with my class called WebpagePriorityQueue()
    data1 = readFiles("C:\\Users\Briggs\Desktop\data\doc1-arraylist.txt")
    WebpagePriorityQueue(queryFile)
    for line in Page:
        newQuery = WebpagePriorityQueue(queryFile)

        # use new query to reheap instances in the created instance
