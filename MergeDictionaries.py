x = {'a':1,'b':2}
y = {'a':1,'b':5,'c':3}

z = {**x,**y}
print(x)
print(y)
print(z)

v = dict(x,**y)
print(v)