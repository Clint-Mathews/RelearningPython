data = [1,2,3,4]

print(data)
data[-1] = 10
data.append(188)
del data[0]
print(data)
print(data[-1])
i=0
j= len(data)-1
while i<=j:
    temp = data[i]
    data[i]=data[j]
    data[j]= temp
    i,j = i+1, j-1


print(data)
data.sort()
print(data)
data.reverse()
print(data)
print(max(data), min(data), sum(data), sum(data)/len(data))

newarray = data[2:-1]
print(newarray)

# 2D Array

ddata = [[1,2,3],[2,3,4]]
print(ddata)

for i in range(len(ddata)):
    for j in range(len(ddata[i])):
        print(ddata[i][j])