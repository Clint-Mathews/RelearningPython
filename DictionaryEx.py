data = {'size': 'fat', 'color': 'gray', 'disposition': 'loud','numbers':12}

for i in data.keys():
    print(i)

for i in data.values():
    print(i)

for i in data.items():
    print(i)

for k,v in data.items():
    print("{} - {}".format(k,v))

print('colors' in data.keys())
print('color' in data.keys())
print('fats' in data.values())
print('fat' in data.values())

# Omiting the keys since we are checking for a key
print('colors' not in data)
print('color' in data)


print("{} is there".format(str(data.get('numbers',0))))
print("{} is there".format(str(data.get('numberss',0))))

# Adding to a dictinory

print(data)

if 'name' not in data:
    data['name'] = 'Clint'

print(data)

data.setdefault('change',10)
print(data)
data.setdefault('change',20)
data['name'] = 'Clints'
print(data)
