#mission 1
class menu_item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def describe(self):
        print(f"{self.name} price is ${self.price}")
item=menu_item("espreso",3.5)
item.describe()

#mission 2
class customer():
    def __init__(self,name,fav_drink):
        self.name=name
        self.fav_drink= fav_drink
    def greet(self):
        print(f"Hi! i i'm {self.name} and i would like a {self.fav_drink}")
customer_with_name=customer("alice","latte")
customer_with_name.greet()

#misison 3
item1=menu_item("laate",4.5)
item1.describe()
item2=menu_item("croissant",2.0)
item2.describe()
item3=menu_item("cold brew",5.0)
item3.describe()