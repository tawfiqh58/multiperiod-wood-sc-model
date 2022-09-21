myDict = {
    "a": "a value",
    "b": "b value",
    "c": "c value",
    "d": "d value",
}

# print(myDict)

# xVal = [i for i in myDict]
# print(xVal) # Got the KEYS

# xVal = [i+j for i in myDict for j in myDict]
# print(xVal) # Array of the KEY combination not value

# xVal = [(i,j) for i in myDict for j in myDict]
# print(xVal) # Array value of (KEY combination of myDict as TUPLE)

xVal = [0 for i in myDict for j in myDict]
print(xVal) # Array of the KEY combination as TUPLE
print(xVal[6]) # Array has it's own position property I am assigning value to each position