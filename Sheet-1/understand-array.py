data = []

print(data)

data.append("Hello")
data.append(1)

print(data)
print(data.index("Hello"))

data.insert(0, "Okay")

print(data)

del data[1]
print(data)

data.remove("Okay")
print(data)
