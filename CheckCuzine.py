indian = ["samosa","naan","rotti"]
chinese = ["raman","squid"]

dish = input("Enter dish :")
if dish in indian:
    print("Indian cuisine")
elif dish in chinese:
    print("Chinese cuisine")
else:
    print("None of the cuisine matches")