s = {1,2,3,4,5,5,7,8}

c = set([10,7,2,3,6])

print(s)
print(c)

x = set()
print(type(x))
print(x)

# No index case get for sets
# print(s[0])

x.add(2)
x.add(3)
x.add(3)

print(x)

x.update([2,3,4,4,7,5,6,7])

print(s)

x.remove(7)

print(s)
# x.remove(7)  Error since key value already removed
print(s)

x.discard(6)
print(s)

x.discard(6)
print(s)


print(s.union(c))
print(s.intersection(c))
print(s.difference(c))
print(s.symmetric_difference(c))
