#Example
Mobile = {
    "brand" : "Samsung",
    "model" : "S10",
    "Screen size" : 6.1
}
print(Mobile)

#Accessing
X = Mobile["model"]
Y = Mobile.get("model")
print(X)
print(Y)

#Modifing/ Updating exixting value
Mobile["model"] = "S11"
print(Mobile)

#Adding new element:
Mobile["color"] = 'blue'
print(Mobile)

#Deleting:
del Mobile["color"]
print(Mobile)

#Remove last inserted item
Mobile.popitem()

#Lopping through a dictionary
#Print all keys
for key in Mobile:
    print(key)
#Print all values
for key in Mobile:
    print(Mobile[key])

#Dictionary Functions: dict.values(),dict.items()
#Print all values
for value in Mobile.values():
    print(value)
#Print keys ans values 
for key, value in Mobile.items():
    print(key,value)

#checking key existance
if "model" in Mobile:
    print("Yes, 'model' is a key in Mobile dictionary")

#Copying a directory
Mobilephone = Mobile.copy()
