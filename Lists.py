spam = ["Hello",12,[12,12]]
print(spam[len(spam)-1])
subList = spam[0:2]
print(subList)
subList2 = spam[0:-1]
print(subList2)
subList3 = spam[:3]
print(subList3)

copy = spam[:]
copy.append("Hello")
print(copy)
del copy[0]
print(copy)

print("{}".format(copy+subList3))
print("{}".format(copy*subList2))