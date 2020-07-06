name = "sajal asfak robin"
my_tok = "My name is "

ff = my_tok + name

print(name.find("robin"))

print(ff.replace("sajal","SAJAL"))

ff = ff.replace("robin","Robin")

print(name.upper())
print(name.lower())

print(ff) 

x = "dhaka"
y = "tangail"
z = "kumilla"

print(x + "|" + y +"|"+z)
print(x,y,z, sep="|")

# if i use 'f' key word i sould not need "+" key to print a variable with a string  
print(f"{x}|{y}|{z}")

person = "{name}'s age is {age}"


print(person.format(name='asfak',age = 46))


first_name = name[6:]

print(first_name)