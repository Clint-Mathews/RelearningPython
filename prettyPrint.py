import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for i in list(message):
    count.setdefault(i,0)
    count[i] +=1

pprint.pprint(count)
