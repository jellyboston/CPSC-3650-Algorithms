import random
import sys

class PQHeap:
    """ A priority queue implemented as a min-heap. """
    class Entry:
        def __init__(self, key, pri):
            self._key = key
            self._pri = pri
            
        def __repr__(self):
            return str((self._key, self._pri))

    
    def __init__(self, priorities):
        """ Creates a priority queue with keys 0, ..., len(priorities) - 1 with initial
            priorities given by the corresponding element in the given array.

            priorities -- a list of numbers
        """
        # keep track of where in the heap the keys are -- self._loc[i] is the index in self._heap where key i is
        self._loc = [i for i in range(len(priorities))]
        self._heap = [PQHeap.Entry(i, pri) for i, pri in enumerate(priorities)]
        self._heapify()


    def _left(self, i):
        return i * 2 + 1


    def _right(self, i):
        return i * 2 + 2


    def _parent(self, i):
        return (i - 1) // 2


    def _swap(self, i, j):
        # swap elements in the heap
        temp = self._heap[i]
        self._heap[i] = self._heap[j]
        self._heap[j] = temp
        # remember where the keys have gone
        self._loc[self._heap[i]._key] = i
        self._loc[self._heap[j]._key] = j

        
    def _heapify(self):
        # linear-time heapification
        for i in range(self._parent(len(self._heap) - 1), -1, -1):
            self._sink(i)


    def _float(self, i):
        parent = self._parent(i)
        while i > 0 and self._heap[i]._pri < self._heap[parent]._pri:
            self._swap(i, parent)
            i = parent
            parent = self._parent(i)
            
            
    def _sink(self, i):
        right = self._right(i)
        left = self._left(i)
        size = len(self._heap)
        
        if left < size:
            smallest = left
            if right < size and self._heap[right]._pri < self._heap[left]._pri:
                smallest = right
            if self._heap[i]._pri > self._heap[smallest]._pri:
                self._swap(i, smallest)
                self._sink(smallest)


    def extract_min(self):
        """ Removes and returns the key with the lowest priority in this queue. """
        min_key = self._heap[0]._key
        self._swap(0, len(self._heap) - 1)
        del self._heap[-1]
        self._loc[min_key] = None
        self._sink(0)
        return min_key


    def decrease_key(self, key, pri):
        """ Decreases the priority of the given key in this priority queue.

            key -- a key in this priority queue
            pri -- a number no greater than the current priority of key
        """
        loc = self._loc[key]
        if loc is not None:
            self._heap[loc]._pri = pri
            self._float(loc)


    def is_empty(self):
        """ Determines if this priority queue is empty. """
        return len(self._heap) == 0
    

    def contains(self, key):
        """ Determines if this priority queue contains the given key.

            key -- an integer
        """
        return key >= 0 and key < len(self._loc) and self._loc[key] is not None

    
if __name__ == "__main__":
    n = int(sys.argv[1])

    input = list(range(n))
    random.shuffle(input)
    
    q = PQHeap(input)
    sorted = []
    while not q.is_empty():
        sorted.append(q.extract_min())

    sorted = [input[i] for i in sorted]
    print([(i, j) for i, j in enumerate(sorted) if i != j])
