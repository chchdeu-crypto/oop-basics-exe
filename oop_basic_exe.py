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

#misison 4
class customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def can_afford(self,price):
        print(True) if price<=self.balance else print(False)
customer_bob=customer("bob",10)
customer_bob.can_afford(8.0)
customer_bob.can_afford(12.0)

#mission 5
class Menuitem():
    def __init__(self,name,price,in_stock):
        self.name=name
        self.price=price
        self.in_stock=in_stock
    def sell(self):
        self.in_stock=False
    def restock(self):
        self.in_stock=True
    def status(self):
        if self.in_stock==True:
            print(f"{self.name} is in stock")
        else:
            print(f"{self.name} is sold out")
item=Menuitem("muffin",2.5,in_stock=True)
item.status()
item.sell()
item.status()
item.restock()
item.status()

#mission 6
class Coffeeshop():
    def __init__(self,name,city,capacity):
        self.name=name
        self.city=city
        self.capacity=capacity
    def open_shop(self):
        print(f"{self.name} is now open in {self.city}! capacity: {self.capacity} seats" )
    def close_shop(self):
        print(f"{self.name} is now closed see you tomorrow")
shop=Coffeeshop("brew house","tel aviv",40)
shop.open_shop()
shop.close_shop()

#mission 7
class menuitem():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.order_count=0
    def order(self):
        self.order_count+=1
        print(f"{self.name} orderd. total orders:{self.order_count}")
cappuccino=menuitem("cappuccino",4.0)
cappuccino.order()
cappuccino.order()
cappuccino.order()
