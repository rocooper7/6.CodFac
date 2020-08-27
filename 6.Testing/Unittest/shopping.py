class NotExistsItemError(Exception):
    pass

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def code(self):
        return f'{self.name}-123456'

class ShoppingCart():
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)

    def total(self):
        return sum([item.price for item in self.items])
    
    def remove_item(self,item):
        self.items.remove(item)

    def contain_items(self):
        return len(self.items) > 0

    def get_item(self,item):
        if item not in self.items:
            raise NotExistsItemError('Item does not exists')
        else:
            return self.items[self.items.index(item)-1]

    
