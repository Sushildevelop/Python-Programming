#Walrus operator - :=
#It allows assignment and return of a value in the same expression
#Useful in while loops and list comprehensions


# value=13
# remainder=value %5

# if remainder:
#     print(f"Remainder is {remainder}")

#Using walrus operator
value=13
if(remainder := value %5):
    print(f"Not divisible , remainder is {remainder}")

size=["small","medium","large","extra large"]

if(snack_size := input("Enter snack size:").lower()) in size:
    print(f"Serving {snack_size},chai")
else:
    print("Invalid size selected")