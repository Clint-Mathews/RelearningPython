supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i,data in enumerate(supplies):
    print("{} {}".format(i,data))


supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
places = ['Cal','Flor',"CIAL","POP"]
for i,j in zip(places,supplies):
    print("{} {}".format(i,j))

print('pens' in supplies)
print('pens2' not in supplies)
