sugar_amount=2
print(sugar_amount)
print(f"Initial sugar :{sugar_amount}")
sugar_amount=12
print(f"ID of 2:{id(2)}")
print(f"ID of sugar_amount:{id(12)}")

spice_mix=set()
print(f"Initial spice mix id:{id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
print(f"Spice mix after additions:{id(spice_mix)}")

#Numbers- Integers , Booleans , Real , Complex
integer_num=10
print(f"Integer number:{integer_num} with ID:{id(integer_num)}")
boolean_val=True
print(f"Boolean value:{boolean_val} with ID:{id(boolean_val)}")

real_num=10.5
print(f"Real number:{real_num} with ID:{id(real_num)}")
complex_num=2+3j
print(f"Complex number:{complex_num} with ID:{id(complex_num)}")

print(type(integer_num))

#String 
string_val="Hello Python"
print(f"String value:{string_val}")
print(type(string_val))
print(string_val[:8])
print("Last word:",string_val[2:9:2])
print("reverse string",string_val[::-1])

label_text="chai sushil"
ecoded_label=label_text.encode("utf-8")
print(f"Encoded label:{ecoded_label}")
decoded_label=ecoded_label.decode("utf-8")
print({decoded_label})

#Data types in Python
#Tuples definition-Tuples is immutable, ordered collection of elements , allows duplicate elements
spices_tuple=("cinnamon","clove","cardamom","cinnamon")
print(f"Spices tuple:{spices_tuple}")

#Mutable data types- List , Set , Dictionary
#List definition- List is mutable , ordered collection of elements , allows duplicate elements
spices_list=["cinnamon","clove","cardamom","cinnamon"]
print(f"Spices list before modification:{spices_list} with ID:{id(spices_list)}")
spices_list.append("ginger")
print(f"Spices list after modification:{spices_list} with ID:{id(spices_list)}")
spices_list.remove("clove")
print(f"Spices list after removing water:{spices_list}")

spiciesoption=["spicy","mild","medium"]
spices_list.extend(spiciesoption)
print(f"Spices list after extending:{spices_list}")
spices_list.insert(1,"nutmeg")
print(f"Spices list after inserting nutmeg at index 1:{spices_list}")

lastspice=spices_list.pop()
print(f"Popped spice:{lastspice}")
print(f"Spices list after popping last element:{spices_list}")

spices_list.sort()
print(f"Spices list after sorting:{spices_list}")

# Operator overloading and bytearry in python
base_liquid=["water","milk","almond milk"]
additional_liquid=["coconut milk","soy milk"]
all_liquids=base_liquid+additional_liquid
print(f"All liquids:{all_liquids}")

strong_brew=["black tea","water"] * 3
print(f"Strong brew:{strong_brew}")

raw_spice_data=bytearray(b"CINNAMON")
raw_spice_data=raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Raw spice data:{raw_spice_data}")

#Set definition- Set is mutable , unordered collection of elements , does not allow duplicate elements
spices_set={"cinnamon","clove","cardamom","cinnamon"}
print(f"Spices set before addition:{spices_set} ")

frozenset_spices=frozenset(["cinnamon","clove","cardamom","cinnamon"])
print(f"Frozenset spices:{frozenset_spices} ")


#Dictionary Definition- Dictionary is mutable , unordered collection of key-value pairs , keys do not allow duplicate elements
spices_dict={"cinnamon":5,"clove":10,"cardamom":15}
print(f"Spices dictionary before modification:{spices_dict} with ID:{id(spices_dict)}")

chai=dict(type="Masala Chai",size="Large",sugar=2)
print(f"Chai dictionary:{chai}")
del chai["sugar"]
print(f"Chai dictionary after deleting sugar:{chai}")


chai_order={"type":"Ginger Chai","size":"Medium","sugar":1}
print(f"Chai order before update:{chai_order.keys()}")
print(f"Chai order before update:{chai_order.values()}")
print(f"Chai order before update:{chai_order.items()}")

extra_spices={"cardamom":"crushed","clove":"whole"}
chai_order.update(extra_spices)
print(f"Chai order after update:{chai_order.items()}")


# import arrow
# brewing_time=arrow.utcnow()
# brewing_time.to("Europe/Rome")

from collections import namedtuple
ChaiOrder=namedtuple("ChaiOrder",["type","size","sugar"])
order1=ChaiOrder(type="Masala Chai",size="Large",sugar=2)
print(f"Chai order 1:{order1}")

kettel_status=True
if kettel_status==True:
    print("kettle is boiling")


#Build snack conditionally
list=["cookies","samosa","tea"]
# snack=input("Enter your snack choice:")
# if snack in list:
#     print(f"Preparing your {snack}")
# else:
#     print(f"Sorry, we don't have {snack}")
  
  
# Snack price calculation
# snack_size=input("Enter snack size (small/medium/large):")
# if snack_size=="small":
#     price=5
#     print(f"Price of small snack is:{price}")
# elif snack_size=="medium":
#     price=10
#     print(f"Price of medium snack is:{price}")
# elif snack_size=="large":
#     price=15
#     print
# else:
#     price=0
#     print("Invalid size selected")
    
#Match case statement
#Train seat - Ac , Sleeper , General
# seat_type=input("Enter seat type (AC/Sleeper/General):")
# match seat_type:
    
#     case "AC":
#         price=500
#         print(f"Price of AC seat is:{price}")
#     case "Sleeper":
#         price=300
#         print(f"Price of Sleeper seat is:{price}")
#     case "General":
#         price=100
#         print(f"Price of General seat is:{price}")
#     case _:
#         price=0
#         print("Invalid seat type selected"
#         f"Price of large snack is:{price}")