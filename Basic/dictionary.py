# dictionary syntax dict = {key : value}
phone_number ={'robin':'01752334603','stive':'01933227774'}
print(phone_number) 
print(phone_number['robin'])
print(len(phone_number))
print(type(phone_number))
print()


dict = {}
dict['name'] = 'swift'
dict['age'] = 20
dict[56] = 123
print(dict['name'],dict['age'],dict[56],sep=' , ') 
print()

item = {'rice':44,'flour':32}
item['oil'] = 78
print(item)
print()

# delete item for a dictionary
del item['oil']
print(item)
print()


# Iletriat dictionary 
for key,value in item.items():
    print(f"{key}={value}",end = " ")
    print()

#sort key 
for key in sorted(item.keys()):
    print(key,item[key],end=' ')
