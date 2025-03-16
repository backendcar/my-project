# list1 = [1,2,3]
# list2 = ["a","b","c"]

# zipped = zip(list1,list2)
# print(list(zipped))

zipped_list = [(1,"a"),(2,"b"),(3,"c")]

list1,list2 = zip(*zipped_list)
print(list1)
print(list2)