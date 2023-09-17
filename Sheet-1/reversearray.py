
class ReverseIt:
    def __init__(self, data):
        self.items = data
    def revereIt(self):
        start=0
        end = len(self.items)-1
        while start<end:
            self.items[start], self.items[end] = self.items[end], self.items[start]
            start+=1
            end-=1
    def print(self):
        print(f'Items: {self.items}')

if __name__=='__main__':
    data = ReverseIt([1,2,3,4,5])
    data.print()
    data.revereIt()
    data.print()