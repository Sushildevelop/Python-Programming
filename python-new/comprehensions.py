#Comprehensions in python
#Comprehensions are a concise way to create lists,sets,dictionaries or generators 
# in python using a single line of code 
# They provide a more readable and expressive way to generate collections compared to traditional loops

#List Comprehension
squares=[x**2 for x in range(10)]
print("Squares:",squares)

menu=["chai tea","coffee","juice tea","water"]
iced_tea=[tean for tean in menu if "tea" in tean]

print("Iced tea options:",iced_tea)

#Set Comprehension
favorite_numbers=[1,2,3,4,5,2,3,4,5,6,7,8,9,1]
unique_sq={num*2 for num in favorite_numbers}
print("Unique squares:",unique_sq)

recipes={
    "chai":["tea,spices,milk,sugar"],
    "coffee":["coffee beans,water,milk,sugar"],
    "fruits":["tea,water,sugar"]
}

unique_spices={spice for recipe in recipes.values() for spice in recipe}
print("Unique spices:",unique_spices)

#Dictionary Comprehension
tea_prices={
    "Masala":40,
    "Ginger":50,
    "Lemon":200
}

tea_prices_usd={tea:price/80 for tea, price in tea_prices.items()}
print("Tea prices in USD:",tea_prices_usd)

#Generator Comprehension used for large datasets to save memory
dail_sales=[100,200,300,400,500]

total_sales=sum(sale for sale in dail_sales)
print("Total sales:",total_sales)

#generator - yeild  means to produce a series of values over time, pausing after each one until the next value is requested.
def serve_chai():
    yield "Cup 1: Chai served",
    yield "Cup 2: Chai served",
    yield "Cup 3: Chai served",

stall=serve_chai()
# for cup in stall:
#     print(cup)
    
def get_chai_list():
    return ["Cup 1: Chai served",
            "Cup 2: Chai served",]

chai_list=get_chai_list()
print(chai_list)


#generator function
def get_chai_gen():
    yield "Cup 1: Chai served"
    yield "Cup 2: Chai served"
chai=get_chai_gen()
print(next(chai))
print(next(chai))
    

#Infinite Generator - means it can produce values indefinitely without stopping.
def infinite_chai():
    cup_number=1
    while True:
        yield f"Cup {cup_number}: Chai served"
        cup_number+=1
infinite_stall=infinite_chai()
# print(next(infinite_stall))

for _ in range(5):
    print(next(infinite_stall))


#Send Generator - means to send a value into a generator function at the point where it is currently paused.
def chai_customer():
    print("Welcome ! what chai would you like?")
    order=yield
    while True:
        print(f"Preparing your {order} chai")
        order=yield

stall=chai_customer()
next(stall)

stall.send("Masala Chai")
stall.send("Ginger Chai")

#Yield from - means to delegate part of a generator's operations to another generator.

#Yield close - means to terminate a generator and release any resources it holds.

# yeild from example
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai():
    yield "Lemon Chai"
    yield "Cardamom Chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)
    
def chai_stall():
    try:
        while True:
            order=yield "Waiting for chai order"
    except:
        print("Closing the chai stall. Thank you!")

stall=chai_stall()
print(next(stall))
stall.close() # Cleaning up resources

#Decorators with Generators - means to modify or enhance the behavior of generator functions using decorators.
def my_decorator(func):
    def wrapper():
        print("Starting the generator")
        func()
        print("Generator has ended")
    return wrapper

@my_decorator
def greet():
    print("Hello, welcome to the chai stall!")

greet()

#Build a logger using decorators
from functools import wraps

def log_activity(func):
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"Function '{func.__name__}' was called.")
        return result
    return wrapper
@log_activity
def brew_chai(type):
    print(f"Brewing a cup of {type} chai.")

brew_chai("Masala")

#Build an Authorization Decorator
def require_admin(func):
    @wraps(func)
    def wrapper(user_role,*args,**kwargs):
        if user_role!="admin":
            print("Access denied. Admins only.")
            return
        return func(*args,**kwargs)
    return wrapper

@require_admin
def access_sensitive_data():
    print("Accessing sensitive data...")

access_sensitive_data("admin")