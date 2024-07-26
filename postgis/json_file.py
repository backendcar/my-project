import json

with open('all_nodes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for i in range(0, 1800):
    print('insert into public.nodes (car,location,date) values (',data[i]['car'],',','st_geometryfromtext(',"'",data[i]['location'],"'",',','4326',')',',' ,"'" ,data[i]['date'],"'",')',';')
    
    
    


