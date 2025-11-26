#Reducing code duplication
# def print_order(name,type):
#     print(f"Preparing {type} for {name}")

# print_order("tea","chai")


def fetch_sales():
    print("Fetching the sales data")

def filter_valid_sales():
    print("Filtering valid sales  data")
    
def summarize_data():
    print("Summarizing the sales data")
    
def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Generating report")

# generate_report()

#Scopes and name resolution
#LEGB - Local , Enclosing , Global , Built-in   
#Local - inside function
#Enclosing - nested function
#Global - module level
#Built-in - python built-in names

def serve_chai():
    chai_type="Masala Chai"
    print(f"Inside function:{chai_type}")

serve_chai()
# print(chai_type) #Error - NameError: name 'chai_type' is not defined

def chai_counter():
    chai_order="lemon"
    def inner_function():
        chai_order="ginger"
        print(f"Inner function:{chai_order}")
    inner_function()
    print(f"Outer function:{chai_order}")
chai_counter()

def update_order():
    chai_type="Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type="Ginger"
    kitchen()
    print(f"Updated chai type is {chai_type}")
update_order()

def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

special_chai("ginger","lemon",sugar=True,milk=False)

def chai_order(order=[]):
    order.append("Ginger Chai")
    print("Order details:",order)
chai_order()
chai_order()


def chai_report():
    return 100,20,10

# sold,remaining,_ =chai_report()
sold,remaining,not_paid = chai_report()
print(f"Sold:{sold}, Remaining:{remaining}")

#Lambda functions , Pure vs Impure functions
# Pure functions - Given same input will always return same output and has no side effects
# Impure functions - Given same input may return different output or has side effects

#Pure function
# def pure_chai(cups):
#     return cups*10

# total_chai=0

#not recommended - Impure function
# def impure_chai(cups):
#     global total_chai
#     total_chai+=cups*10
#     return total_chai


#Recurisve functions means a function calling itself
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1) 

#Lamdas functions means anonymous functions- functions without a name
double=lambda x:x*2
result=double(5)
print("Double:",result)

chai_types=["Masala","Ginger","Lemon","Masala"]

strong_chai=list(filter(lambda chai:chai=="Masala",chai_types))
print("Strong chai:",strong_chai)

# Built in functions 
def chai_flavor(flavor="masala"):
    """Returns the flavor of chai"""
    return f"The flavor of chai is {flavor}"

print(chai_flavor.__doc__)  # Accessing docstring
print(chai_flavor.__name__)

# Accessing function type







