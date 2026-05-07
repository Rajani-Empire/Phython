item1 = "bread"
item2 = "pasta"
item3 = "fruits"
items = ["bread","pasta","fruits","veggies"]
print(items)

print(items[0])
print(items[-1])


# append
items = ["bread","pasta","fruits","veggies"]
items.append("butter")
print(items)


#insert
items = ["bread","pasta","fruits","veggies"]
items.insert(1,"butter")
print(items)



# join two list
food =["bread","pasta","fruits","veggies"]
bathroom = ["shampoo","shop"]
item = food+bathroom
print(item)
print(len(item))

print("bread" in item)