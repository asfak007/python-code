myFriends = ['emon' ,'noyon','lotif','arnold','futonto','masud','foysal' ]

print(myFriends)

print(myFriends[5])

print(f"{myFriends[0]} and {myFriends[5]} they would not know each other ")
print()
# in python we are able to create a mixed lis.
#it's like that we can make a list using all type of variable

mixedList = ["robin",1,6.9,True,'hacker']
print(mixedList)
print()

print(mixedList[-1]) #aceass list element of the 

for char in range(0,5):

    print(mixedList[char])
print()
#enpety list 

em = []

#nested list:(like a matrix )
'''
   1 2 3 4 5
   6 7 8 9 1
   1 2 3 4 5 
'''

matrix = [[1,2,3,4,5],
          [6,7,8,9,1],
          [1,2,3,4,5]
          ]

for x in matrix:
    # here the x verialbe is store the list elements of the matrix lsis
    for y in x:
      # and here y variable is acecss the each contain of the x list
      print(y,end=',') # end='' is use for to print a lsit in a row 
                          
    print()

# list slicing
number = [1,2,3,4,5]

print(number[0:4]) 
print(number[2:-2])

# list iteration by loop:
print()
phones  = ['nokia','samsun','iphone','ximoie','howaie']

for x in phones:
    # x is acess the indivetual item for phones list
    print(x)
    if x == 'iphone':
        print("its expansive.")
    elif x == 'howaie':
        print("google band it.")
    elif x == "ximoie":
        print("its sucks.")

print()            
number_lsidt = [1,2,3,4,5,6]
sum = 0
for x in number_lsidt:
    sum+=x
print(f"sum is :{sum}")
print()

worng = [1,2,4.5,'dxd',7,89,]
sum = 0 
for x in worng:            #there is a another to do this:
    if type(x) != int:     # for x in worng:
        continue           #    if type(x) != int:
    sum += x               #        continue
print(sum)                 #sum += x

#change/replace item  in list :

worng[3] = 8
worng[2] = 3
print(worng)
print()
# add any item in the list:
worng.append("sajal")
print(worng)
print()

worng +=["asfak"]
print(worng)
print()

worng.insert(8,'robin')
print(worng)
print()

#delete elemants in list 
del worng[0]
print(worng)
del worng[0:3]
print(worng)
print()

#get and remove using pop functon 

last_Item = worng.pop() # last_Item = worng.pop(1)
print(worng)
print(last_Item)
print()

# remove  a list item  by value

num = [1,2,53,4,5,6,7,8]
print(num)
num.remove(5)
print(num) 
print()

# convart a string to a list.
# we need to import re libeary 
import re 

visle = "cars,bus,train,plane,ship"
v = re.split(",",visle)
print(v)
print()

# convart a list  to a string 
any = ['python', 'is' , 'best']
print(any)
any_str = ' '.join(any) # using join functon we can convart a list to a list 
print(any_str)

# sort a list to reverse order

v.sort(reversed=True)
#print(sorted(cars))
print(v)

# convart a list reverse order
number4 = [1,2,3,4,5]
number4.reverse()
print(number4)
print(len(number4)) # len function is use to see the lenangth of a list 

# checking any value exsist in the list 

if 3 in number4:
    print("3 is exist in the list")
if 6 not in number4:
    print("6 is not exist in the lsit")
