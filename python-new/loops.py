# orders=['hitesh',"Aman","Becky","charlie"]

# for name in orders:
    # print(f"Preparing chai for {name}:{index}")
    
 #enumerate function means - gives index and value both
# for index,name in enumerate(orders):
#     print(f"Order number {index+1}: Preparing chai for {name}")
    
    
    
temp=40
while temp <100:
    print(f"Current temperature is {temp}C")
    temp+=15
    
print("Boiling point reached")    

flavurs=["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]

for flavour in flavurs:
    if flavour=="Out od Stock":
        continue
    if flavour=="Discontinued":
        print("Discontinued item found")
        break

stock=[("Ginger",10),("Lemon",0),("Tulsi",5),("Masala",2)]

for item,qt in stock:
    print(item)   
    
    
#Walrus    
