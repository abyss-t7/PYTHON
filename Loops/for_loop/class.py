class countdown:
    def __init__(self, n):
        self.n= n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n<=0:
            raise StopIteration
            self.n -=1
            return self.n +1
for n in countdown(5):
    print(n)