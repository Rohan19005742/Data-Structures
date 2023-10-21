class List:
    def __init__(self):
        self.elements = []

    def append(self, value):
        self.elements.append(value)

    def extend(self, values):
        self.elements.extend(values)

    def insert(self, index, value):
        self.elements.insert(index, value)

    def remove(self, value):
        self.elements.remove(value)

    def pop(self, index=-1):
        return self.elements.pop(index)

    def index(self, value):
        return self.elements.index(value)

    def count(self, value):
        return self.elements.count(value)

    def sort(self):
        self.elements.sort()

    def reverse(self):
        self.elements.reverse()

    def clear(self):
        self.elements.clear()

    def length(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __delitem__(self, index):
        del self.elements[index]

    def __iter__(self):
        return iter(self.elements)

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return repr(self.elements)