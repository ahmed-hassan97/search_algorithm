import struct
import heapq
import tkinter
import itertools

######################################################################
# A function that mimics "enumerated datatypes"
######################################################################
def enum(*args):
    enums = dict(zip(args, range(len(args))))
    return type('Enum', (), enums)

######################################################################
# A FIFO queue to keep track of the nodes at the frontier
# Public functions: add, pop, isEmpty, find, size
######################################################################
class FifoQueue:
    # Initialize the queue
    def __init__(self):
        self.front = 0
        self.back = 0
        self.data = {}

    # Add an element at the back
    def add(self, value):
        self.data[self.back] = value
        self.back += 1

    # Remove the element at the front
    def pop(self):
        value = self.data[self.front]
        del self.data[self.front]
        self.front += 1
        return value

    # Check whether the queue is empty
    def isEmpty(self):
        return self.back == self.front

    # Find an element that satisfies a given criterion
    # i.e., return an element "e" where "f(e)" is true  
    def find(self,f):
        return (f in self.data)
        # for value in self.data.values():
        #     if f(value): return value
        # return None

    # Get the size of the queue
    def size(self):
        return len(self.data)

######################################################################
# A LIFO queue (stack) keeping track of the nodes at the frontier
# Public functions: add, pop, isEmpty, find, size
######################################################################
class LifoQueue:
    # Initialize the stack
    def __init__(self):
        self.top = 0
        self.data = {}

    # Push an element to the stack
    def add(self, value):
        self.data[self.top] = value
        self.top += 1

    # Pop an element from the stack
    def pop(self):
        self.top -= 1
        value = self.data[self.top]
        del self.data[self.top]
        return value

    # Check whether the stack is empty
    def isEmpty(self):
        return self.top==0

    # Find an element that satisfies a given criterion
    # i.e., return an element "e" where "f(e)" is true
    def find(self,f):
        return (f in self.data)


    # Get the size of the stack
    def size(self):
        return len(self.data)

######################################################################
# A priority queue keeping track of the nodes at the frontier
# Public functions: add, remove, pop, isEmpty, find, size
######################################################################
class PriorityQueue:
    # Initialize the queue
    def __init__(self):
        self.pq = []                    # list of entries arranged in a heap
        self.entry_finder = {}          # mapping of tasks to entries
        self.REMOVED = '<removed-task>' # placeholder for a removed task
        self.counter = itertools.count()# unique sequence count

    # Add a new element or update the priority of an existing element 
    def add(self,task, priority=0):
        if task in self.entry_finder:
            self.remove(task) 
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    # Mark an element as REMOVED. Raise KeyError if not found
    def remove(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    # Remove and return the lowest priority element. Raise KeyError if empty
    def pop(self):
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    # Check whether the queue is empty
    def isEmpty(self):
        return self.entry_finder=={}

    # Find an element that satisfies a given criterion
    # i.e., return an element "e" where "f(e)" is true
    def find(self,f):
        for task in self.entry_finder:
            if f(task): return task
        return None

    # Get the size of the queue
    def size(self):
        return len(self.entry_finder)

######################################################################
# A data structure to capture the set of explored states
# Public functions: add, contains, isEmpty, size
######################################################################
class Set:
    a=PriorityQueue()
    # Initialize the set
    def __init__(self):
        self.elements = set()

    # Add an element to the set 
    def add(self,element):
        self.elements.add(element)

    # Find an element in the set
    def contains(self,element):
         return element in self.elements

    # Get the size of the set
    def size(self):
        return len(self.elements)

    def find(self,f):
        for task in self.a.entry_finder:
            if f(task): return task
        return None

######################################################################
# A class for drawing objects (line, rectangle, ...)
# Public functions: display, line, rectangle
######################################################################
class Window:
    # Initialize the graphics environment and create a window
    def __init__(self,title,s,h,w,rgb):
        (x,y) = s
        h *= 1.5
        w *= 1.5
        x *= 1.5
        y *= 1.5
        self.root = tkinter.Tk()
        self.root.title(title)
        self.root.geometry("%d"%(w+2*x)+"x"+"%d"%(h+2*y))
        self.canvas = tkinter.Canvas(self.root, height=h+2*y, width=w+2*x)
        self.rectangle((x/1.5,y/1.5),h/1.5,w/1.5,rgb)

    # Display the drawings
    def display(self):
        # Display TK
        self.canvas.pack()  
        self.root.mainloop()

    # Draw a line
    def line(self,s1,s2):
        (x1,y1) = s1
        (x2,y2) = s2
        x1 *= 1.5
        y1 *= 1.5
        x2 *= 1.5
        y2 *= 1.5
        self.canvas.create_line(x1,y1,x2,y2,fill="#000000")
                
    # Draw a rectangle
    def rectangle(self,s,h,w,rgb):
        (x,y) = s
        x *= 1.5
        y *= 1.5
        h *= 1.5
        w *= 1.5
        self.canvas.create_polygon(x,y,x+w,y,x+w,y+h,x,y+h,\
                                   fill=rgb,outline="#000000")
