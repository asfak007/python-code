num_list = [1,2,3,4,5,6]
num_dict ={'one':1,'two':2,"three":3}

def change_num_list(list,dict):
     del list[0]
     list[-1] = 50

     del dict['one']
     dict['three'] = 22
     print("innerlist :",list)
     print("Iner dic",dict)
     

print("before :")
print("Outer list :",num_list)
print("Outer Dict :",num_dict)
print("before :")
change_num_list(list = num_list,dict = num_dict)

print("before :")
print("Outer list :",num_list)
print("Outer Dict :",num_dict)