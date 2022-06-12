items = [1, 12, 32, 23, "Hello"]
print(items)
print(items[0])
print(items[4])
items[4] = "Oddikow"
print(items[4])
print(items[-1])
items.append("Hahah")
print(items)
items.insert(1, "Inserted")
print(items)

items1 = ["po", "pi"]
items2 = ["op", "io"]
itemList = items1 + items2;
print(itemList)
print(len(itemList))
print("po" in itemList)
print("pos" in itemList)

for i in itemList: print(i)
