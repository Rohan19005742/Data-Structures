class Array:
    def __init__(self):
        self.data=[]

    def add(self, item):
        self.data.append(item)

    def insert(self, index, item):
        self.data.insert(index, item)

    def remove(self, item):
        self.data.remove(item)
        
    def remove_at_index(self, index):
        if 0 <= index < len(self.data):
            item = self.data[index]
            self.data.remove(item)
        else:
            pass
    
    def size(self):
        return len(self.data)
    
    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data(index)
        else:
            return None

    def __str__(self):
        return str(self.data)
        