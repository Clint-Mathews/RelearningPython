def printDetails(name, age, rollno):
    print(f"{name} : {age} : {rollno}")

def printDetailsArgs(*args):
    print(type(args))
    if(len(args) == 3):
        print(f"{args[0]} : {args[1]} : {args[2]}")
    else:
        print(f"{args[0]} : {args[1]}")

def printKwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

def allCases(param,*args,**kwargs):
    print(param)
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,v)


printDetails("Clint",12,12)
printDetailsArgs("Clint",12,12)
printDetailsArgs("Clint",4)
list = ["Clint", 1212, 12]
printDetailsArgs(*list)

data = {"Clint":13,"PO":32321}
printKwargs(**data)

allCases("Hello",*list,**data)