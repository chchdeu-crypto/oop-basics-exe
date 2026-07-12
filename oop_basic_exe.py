class menu_item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def describe(self):
        print(f"{self.name} price id {self.price}")
item=menu_item("espreso",3.5)
item.describe()