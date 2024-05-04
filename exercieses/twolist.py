def towlist(x,y):
    newList = []    
    for i in x:
        if i % 5 == 0 and i % 10 != 0:
            newList.append(i)
    for j in y:
        if j % 10 == 0:
            newList.append(j)
    print(newList)
towlist(x=[1,5,10,15],y=[20,25,30,35,40])
