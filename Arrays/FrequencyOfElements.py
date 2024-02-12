# Input :  arr[] = {10, 20, 20, 10, 10, 20, 5, 20}
# Output : 10 3
#          20 4
#          5  1


def findFrequency(data):
    res = {}
    for i in data:
        res[i] = 1 if res.get(i) is None else res[i] + 1
    return res

print(findFrequency([10, 20, 20, 10, 10, 20, 5, 20]))
