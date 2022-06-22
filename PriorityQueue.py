from Webpages import *

class WebpagePriorityQueue():
    def __init__(self, query, container):
        self.query = query
        self.container = container
        self.heap = []
        querySplit = re.split("\W", guery)  # splits query into words
        for i in container:  # creating the heap upon initalization and sort the list from the start and sort whenever changed so it will always be sorted and peek will work
            total = 0
            for word in querySplit:
                total += i.getCount(word)  # adds the occurances of every word in the query into a total
            self.heap.append([i, total])
        self.heap.sort(reverse=True, key = self.heapSort)  # key is [i, total]
    
    def heapSort(self, key):
        return key[1]  # returning the second value in the key arraylist which is total so the heap is sorted by total in descending order since reverse = True
    
    def peek(self):
        return self.heap[0]  # returns the first WebpageIndex and its priority from the already sorted heap array

    def poll(self):
        delete = pop(self.heap[0])  # delete first WebpageIndex and its priority from the already sorted heap array
        self.heap.sort(reverse=True, key = self.heapSort)  # sort the heap again after deleting
        return delete  # return deleted value

    def reheap(self, query, container):
        querySplit = re.split("\W", guery)  # splits query into words
        for word in querySplit:
            total += i.getCount(word)  # adds the occurances of every word in the query into a total
        self.heap.append([container, total])  # adds new query into the heap
        self.heap.sort(reverse=True, key = self.heapSort)  # sorts the heap again after inserting
        
