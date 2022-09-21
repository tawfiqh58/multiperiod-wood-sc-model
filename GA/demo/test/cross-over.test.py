myDict = [
    "a",
    "b",
    "c",
    "d",
]
# [:1] all values before position 1
# [3:] all values after position 3
c1 = myDict[:1] + myDict[3:] # 1 no & and 4 no value
print(c1)  # ['a', 'd'] 
