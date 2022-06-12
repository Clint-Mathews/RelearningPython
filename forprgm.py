exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for item in exp:
    total += item
    print(item)

print("Total :", total)


for i in range(1,11):
    print(i)
    print("Square : ",i,i*i)
total = 0
for i in range(len(exp)):
    total += exp[i]
    print("Month",i+1,"Expense",exp[i])
print("Total :", total)


key_loc = "chair"
loc = ["garage","living room","chair","closet"]
for i in loc:
    if i == key_loc:
        print("Key found in",i)
        break;
for i in range(1,6):
    if i%2 == 0:
        continue
    print(i*i)

i =1;
while(i<=5):
    print(i)
    i+=1


