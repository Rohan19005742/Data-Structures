import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.elements)
            return item

    def peek(self):
        if not self.is_empty():
            priority, item = self.elements[0]
            return item

    def size(self):
        return len(self.elements)