# Tuple in python (we can not change the indvisual value in a tuple)

tp = 1,2,'robin',5.6,True
print(tp)
print(type(tp))

# access item 
print(tp[0],tp[1],tp[2],tp[3],tp[4])

# tuple iletration
t1 = 1,2,3
t2 = 1,2,3
for x in t1:
    print(x)
  
# tuple compare 
if t1 == t2 :
    print("equal") 

# assing tuple vlaue in some variable
t1 = 5,7,11
x,y,w =t1
print(x,y,w,sep=" ,")
t1 = 5,7,11
x,y,_ =t1
print(x,y,sep=" ,")