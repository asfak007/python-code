# declire a functon :

def welcome():
    print('Hellow world')
    for x in range(0,10):
        print(f"hi {x}")

welcome()
print()

# pass a perameter in a funncton

def call(name):
    print(f"hi {name}")

call('robin')
call('sajal')
print()

def personal_info(name,age,country):
    print(f"hellow my name is {name}")
    print(name,age,country,sep='|')

personal_info('robin','20','bangladesh')
personal_info('bruce','18','egypt')
personal_info(country="us",name="hok",age=22) # in keyword argument order does not matter
print()

# use Default vlaue
def information (name,phone,country = 'Banglades'):
    print(name,phone,country, sep=' ')

information(name = "bill", phone = 978787746 ,country = "us")
information(name ="robin",phone = 21 )
information('robin',768687897)
print()

# a function which return some value :
def square(num1,num2):
    return num1+num2
print(type(square(1,5)))
print(square(7,8))
print()

# a name functon 
def name(first_name,last_name):
    return first_name +" "+ last_name
print(name("sajal asfak","robin"))
print(name("sazan abrar","fhime"))

# optional argument 
def get_name(fname,lname,mname=''):
    complete_name = fname
    if mname:
        complete_name += ' '+ mname
        
    complete_name += ' ' + lname
    return complete_name
print(get_name('sajal','robin','asfak'))
print(get_name('sajal','robin'))
print()

# value type
num = 100 
def change_num(num):
    num += 100
    print("Inner Num:{num}".format(num=num))
change_num(num)
print("outside:"+str(num))
print()

# Arbitrary number of arguments :
def student(*name):
    print(name,type(name))
    for x in name:
        print(x)

student('sajal','asfak','robin')
student()
student("hok")
print()

# positonal and arbitarary arguments mixing :
def student(best_programmer,*losers_in_class): # *(prarameter) revcive the as a elements of a truple
    print(f"Best programmer in the class :",best_programmer)
    print(f"loser in the class {losers_in_class}")

student('Robin','sazan','ali','kawser','anik')

#  Arbitary keyword arguments :
def student(best_programmer,**losers_in_class): # using **(prarameter) recive the value as a keyword
    print(f"Best programmer in the class :",best_programmer)
    print(f"loser in the class {losers_in_class}")

student(best_programmer='robin',snd_programmer = 'masud',trd_programmer = 'Foysal')

