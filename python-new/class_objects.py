class Chai:
    pass

class chaitime:
    pass

print(type(Chai))
print(type(chaitime))

ginger_chai=Chai()

print(type(ginger_chai))
print(isinstance(ginger_chai,Chai))


class Chai:
    origin="India"

print(Chai.origin)
Chai.is_hot=True
print(Chai.is_hot)


#creating object of class Chai
masala_chai=Chai()
print(masala_chai.origin)
print(masala_chai.is_hot)


#Attribute  shadowing means creating an attribute with the same name as class attribute in object
class Tea:
    country="China"
    is_warm=True

cutting_tea=Tea()
print(cutting_tea.country)

cutting_tea.country="Sri Lanka"
print(cutting_tea.country)

del cutting_tea.country   # deleting the object attribute 
print(cutting_tea.country)
cutting_tea.nice="No"
print(cutting_tea.nice)
del cutting_tea.nice
# print(cutting_tea.nice) # accessing class attribute again after deleting object attribute throw error because of no such attribute in object and class attribute is also deleted.


# Self Aruguments in Methods
class Beverage:
    size="Medium"
    def drink(self):
        return f"A {self.size} beverage is being consumed."

cup=Beverage()
print(cup.drink())


#Constructor Method and __init__
# A constructor is a special method that is automatically called when an object of a class is created.

# The __init__ method is used to initialize the attributes of the object.

class ChaiOrder:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
    
    def summary(self):
        return f"You have ordered a {self.size} {self.type} chai."

order=ChaiOrder("Masala","Large")
print(order.summary())




#Inheritance in Classes - means deriving a new class from an existing class, inheriting its attributes and methods.
class BaseChai:
    def __init__(self,type):
        self.type=type
    
    def prepare(self):
        print(f"Preparing a cup of {self.type} chai.")

class SpecialChai(BaseChai):
    def add_spices(self):
        print(f"Adding special spices to the {self.type} chai.")

class ChaiShop:
    chai_cls=BaseChai
    def __init__(self):
        self.chai=self.chai_cls("Regular")
    def serve_chai(self):
        print(f"Serving a cup of {self.chai.type} chai.")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = SpecialChai
    
shop=ChaiShop()
fancy=FancyChaiShop()
shop.serve_chai()


#Accessing Base Class - Using super() , code duplication , explicit call
class PremiumChai():
    def __init__(self, type,strength):
        self,type=type
        self.strength=strength

# class GingerChai(PremiumChai):
#     def __init__(self,type,strength,ginger_level):
#         self.type=type
#         self.strength=strength
#         self.ginger_level=ginger_level
    
#     def prepare(self):
#         print(f"Adding ginger level: {self.ginger_level}")

class GingerChai(PremiumChai):
    def __init__(self,type,strength,ginger_level):
        super().__init__(type,strength)
        self.ginger_level=ginger_level
    
    def prepare(self):
        print(f"Adding ginger level: {self.ginger_level}")


#Method Resolution Order (MRO)- the order in which base classes are searched when executing a method.
class A:
    label="Class A"

class B(A):
    label="Class B"
    
class C(A):
    label="Class C"
    
class D(B,C):
    pass

cup=D()
print(cup.label)  # Output: Class B
print(D.__mro__)
    

# Static Methods and Class Methods- means methods that are not bound to an instance of the class.
class ChaiUtilities:
    @staticmethod
    def boil_water(clas):
        return f"{clas}Boiling water for chai."

    @classmethod
    def chai_info(cls):
        return f"{cls} is a class for chai-related utilities."
clas="s ChaiUtilities"
# # object=ChaiUtilities()
# # object.boil_water(clas)

# #static method call without creating an object
# print(ChaiUtilities.boil_water(clas))


# #class method call without creating an object
print(ChaiUtilities.chai_info())


# Property Decorators - used to define methods in a class that act like attributes.
# They allow you to define getters, setters, and deleters for class attributes.
#Getter - means to access the value of a private attribute.
#Setter - means to set or update the value of a private attribute.
#Deleter - means to delete a private attribute.
class TeaLeaf:
    
    def __init__(self,quality):
        self._quality=quality  # private attribute
    
    @property # means getter - to access the private attribute
    def quality(self):
        return self._quality
    
    @quality.setter
    def quality(self,quality):
        self._quality=quality
    
    @quality.deleter
    def quality(self):
        del self._quality


    





