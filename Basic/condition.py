num = int(input("please Enter a number :"))

if num % 2 == 0:
    print("event number")
    print("thank you")

else:
    print("odd number")
    print("come again")


run1 = int(input("Enter the run :"))

if run1 == 100 or run1 > 100:
    print("century")

elif run1  > 49 and run1 >= 50:
    print("half century")

name1 = input("Enter the first name :")
name2 = input("Enter the seacnd name :")

if name1.lower() == name2.upper:
    print("same")
else:
    print("name are not same :")


x = 1

# loops in python program :

while x <= 5:
    print(x)
    x += 1

# infinet loop :

while True:
    print(x)
    x += 1
    # use the brak keyword to berak infinet loop:
    if x > 10 :
        break 

i = 1 
print("event numbers on 1 - 20 :")
while i < 20 :
    i += 1
    if i % 2 != 0:
        continue   #ues the continue key word is  this conditon true the loop print statemant is not print anything.
                   # it will be jump to the next process in the loop  
    
    print(i)
    

    


#{for element in iterable:

#    body}

sum = 0

for num in range(1,11):
    sum +=num
print(f"sum is : {sum}")


# use for loop in string 

NyName = "sajal Asfak Robin"

for char in NyName:
    print(char)


