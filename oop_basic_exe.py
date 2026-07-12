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

#mission 8
class order():
    def __init__(self,customer_name,items):
        self.customer_name=customer_name
        self.items=items
    def item_counts(self):
        return len(self.items)
    def print_order(self):
        print(f"order for {self.customer_name} \nitems: {self.item_counts()}")
        for item in self.items:
            print(f"- {item}")
dana_order=order("dana",["latte","croissant","oj"]) 
dana_order.print_order()             

#mission 9
class barista():
    def __init__(self,name,specialty):
        self.name=name
        self.specialty=specialty
        self.drinks_made=0
    def make_dirnk(self,drink_name):
        print(f"{self.name} made a {drink_name}")
        self.drinks_made+=1
    def is_speciatly(self,drink_name):
        return True if self.specialty==drink_name else  False
    def shift_summary(self):
        print(f"{self.name} made {self.drinks_made} drinks today")
yossi_bar=barista("yossi","esppreso")
yossi_bar.make_dirnk("makiato")
yossi_bar.make_dirnk("oj")
yossi_bar.make_dirnk("latte")
yossi_bar.make_dirnk("esppreso")
print(yossi_bar.is_speciatly("esppreso"))
yossi_bar.shift_summary()

#mission 10
class receipt():
    def __init__(self,tax_rate):
        self.tax_rate=tax_rate
        self.items=[]
    def add_item(self,name,price):
        items=(name,price)
        self.items.append(items)
    def subtotal(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def tax_amount(self):
        return self.subtotal()*self.tax_rate
    def total(self):
        return self.subtotal()+self.tax_amount()
    def print_reciept(self):
        for item in self.items:
            print(f"-{item[0]}: {item[1]}")
        print(f"subtotal {self.subtotal()}")
        print(f"tax{self.tax_rate*100}%: {self.tax_amount()} ")
        print(f"total ${self.total()}")
receipt1=receipt(0.17)
receipt1.add_item("latte",4.5)
receipt1.add_item("oj",2.0)
receipt1.add_item("watter",1.5)
receipt1.print_reciept()

#extra exe
#mission 1 
class menuitem():
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    def is_drink(self):
        return True if "drink" in self.category else False
    def is_cheap(self,limit):
        return True if self.price<limit else False
item1=menuitem("espreso",3.5,"hot drink")
print(item1.is_drink())
print(item1.is_cheap(3.5))
item2=menuitem("muffin",2.0,"food")
print(item2.is_drink())
print(item2.is_cheap(3.5))

#mission 2
class customer():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.points=0
    def purchase(self,item_name,price):
        if price>=self.balance:
            self.balance-price
            self.points+=10
        else:
            print(f"not enough balance for {item_name}")
    def redeem(self):
        if self.points>=50:
            self.balance+=5
            self.points=0
    def status(self):
        print(f"name: {self.name} | balance: ${self.balance} |points: {self.points} ")
customer1=customer("noa",15.0)  
customer1.purchase("pen",12) 
customer1.redeem()
customer1.status()
customer1.purchase("pen",16)     
customer1.redeem()
customer1.status()

#mission 3
class order():
    def __init__(self,customer_name,items):
        self.customer_name=customer_name
        self.items=items
    def total_prep_time(self):
        total_time=0
        for item in self.items:
            total_time+=item[1]
        return total_time
    def ready_by(self,minutes):
        return True if self.total_prep_time()<=minutes else False
    def print_order(self):
        for item in self.items:
            print(item)
    def slowest_item(self):
        time=0
        item1=""
        for item in self.items:
            if item[1]>time:
                time=item[1]
                item1=item[0]
        return item1
moshe=order("moshe",[("latte",3),("sandwitch",7),("smoo",5)]) 
print(moshe.total_prep_time())
print(moshe.ready_by(10))
print(moshe.ready_by(20))
moshe.print_order()
print(moshe.slowest_item())

#mission 4
class Coffeshop():
    def __init__(self,name):
        self.name=name
        self.revenue=0.0
    def cell(self,item_name,price):
        self.revenue+=price
        print("revenue added successfully")
    def sell_dicounted(self,item_name,price,dicount):
        self.revenue+=price*(1-dicount)
    def daily_summary(self):
        print(f"{self.name}| daily revenue: ${self.revenue}")
bean=Coffeshop("the bean")
bean.cell("cookie",9)
bean.cell("coffe",12)
bean.cell("watter",7)
bean.sell_dicounted("juice",16,0.8)
bean.sell_dicounted("ice coffe",10,0.15)
bean.daily_summary()

#mission 5
class drink():
    def __init__(self,name,base_price,size):
        self.name=name
        self.base_price=base_price
        self.size=size
    def finel_price(self):
        if self.size=="small":
            return self.base_price
        elif self.size=="medium":
            return self.base_price*1.3
        elif self.size=="large":
            return self.base_price*1.6
    def describe(self):
        print(f"{self.name} ({self.size}) $ {self.finel_price()}")
latte=drink("latte",3.0,"small")
latte.describe()
latte=drink("latte",3.0,"medium")
latte.describe()
latte=drink("latte",3.0,"large")
latte.describe()

#mission 6
class Shift:
    def __init__(self, barista_name, start_hour, end_hour, drinks_target):
        self.barista_name = barista_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.drinks_target = drinks_target

    def duration(self):
        return self.end_hour - self.start_hour

    def drinks_per_hour(self):
        return self.drinks_target / self.duration()

    def is_long_shift(self):
        return self.duration() > 6

    def describe(self):
        print(f"Barista: {self.barista_name}")
        print(f"Hours: {self.duration()}")
        print(f"Target: {self.drinks_target}")
        print(f"Per hour: {self.drinks_per_hour()}")
        print(f"Long shift: {self.is_long_shift()}")


shift = Shift("Lior", 8, 16, 120)
shift.describe()

#mission 7
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class HappyHour:
    def __init__(self, start_hour, end_hour, discount_percent):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.discount_percent = discount_percent
    def is_active(self, current_hour):
        return self.start_hour <= current_hour < self.end_hour
    def discounted_price(self, item):
        return item.price * (1 - self.discount_percent / 100)
item = MenuItem("Beer", 20.0)
happy = HappyHour(16, 18, 20)
print(happy.is_active(17))
print(happy.discounted_price(item))
print(happy.is_active(19))
        