#Iterate over a list
fruits = ["apple","mango","banana"]
for fruit in fruits:
    print(fruit)
    
print()
#Iterate with index
for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")
    
print()
#Range loop
for i in range(1,6):
    print(f"Count:{i}")