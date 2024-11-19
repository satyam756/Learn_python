# Dictonery's in python
# dict keyword or {}
chai_types = {"Masala": "Spicy", "Ginger":"Zesty", "Green":"Mild"}

print(chai_types)

# print(chai_types["Masala"])

# for chai in chai_types:
#     print(chai,chai_types[chai])

for key,value in chai_types.items():
    print(key,value)

if "Ginger" in chai_types:
    print("it's present")

print(len(chai_types))

# add values in dict

chai_types["Earl Grey"] = "Citrus"

print(chai_types)

# pop method in dict

# dict.(key)
# dict.popitem() removes last element

# del chai_types["key"]

tea_shop = {
    "chai":{
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },
    "Tea":{
        "Green": "Mild",
        "Black": "Strong"
    }
}

print(tea_shop)

squared_num = {x:x**2 for x in range(1,11)}
print(squared_num)

# squared_num.clear() clear the dict