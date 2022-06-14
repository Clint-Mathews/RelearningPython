catdesc = ["Hello","Hello2","Hello3"]
cat1 = catdesc[0]
cat2 = catdesc[1]
cat3 = catdesc[2]

print("{} {} {}".format(cat1,cat2,cat3))
catdesc.append("Hahaha")
cat,dog,jet = catdesc[0:3]

print("{} {} {}".format(cat,dog,jet))

a,b = "oP",12

print("{} {}".format(a,b))

a += str(b)
print(a)

backup = ["POI"]

backup *= 10

print(backup)

print(backup.index("POI"))

backup.append("POIOUI")
backup.insert(10,"POIO")
print(backup)

del backup[10]
print(backup)
backup.remove('POI')
print(backup)


v = [1,2,3,423,-56,23232,3,21,-734364]
j = v
print(v)
v.sort()
print(v)

print(j)
j.sort(reverse=True)
print(j)

s = ['P','p','Z','z','a','A']
print(s)
s.sort(key=str.lower)
print(s)


spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam1 = sorted(spam)
print(spam1)

