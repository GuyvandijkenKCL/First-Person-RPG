from monster import Monster

class Stock:
    def __init__(self, size):
        self.stock = [None] * size
        
    def expand_stock(self, x):
        self.stock = self.stock + ([None] * x)

    def get_size(self):
        return len(self.stock)
    
    def get_used_space(self):
        count = 0
        for slot in self.stock:
            if slot:
                count += 1
        return count
    
    def add_monster(self, monster):
        for i in range(len(self.stock)):
            if not self.stock[i]:
                self.stock[i] = monster
                break
    

                