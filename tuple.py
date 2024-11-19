# Tupple's in python 

tea_types = ("Black","Green","Oolong")

print(tea_types)

more_tea = ("Herbal","Earl Grey")

all_tea = more_tea + tea_types

print(all_tea)

if "Green" in all_tea:
    print("Available")

my_new = ("Black","Green","Oolong")
(black,green,oolong) = my_new
# assigns variables 
print(black)