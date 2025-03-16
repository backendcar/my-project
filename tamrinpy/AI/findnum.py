def find_num(myList):
    myDict = {}
    for item in myList:
        try:
            myDict[item] += 1
        except KeyError:
            myDict[item] = 1
    return myDict

nums = find_num([1,1,1,2,2,3,3])
print(nums)
    