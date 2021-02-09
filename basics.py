#Luke Byrne
#Python basics
#2021-02-07

print("Hello, World!")

a = 1
b= 1.0
s= "Hello, world from a string!"
t= '"hello", from a different string'
print(a,b,s,t)

print(s[15:20:2])

x = [1,2,3]
print(x)
print(x[0])
print(x[-2])
 #::2 skips 
for i in x[::2]:
    print(i)
    print(i+i)

for i in range(10):
    print(i)

d= {"no. wheels": 4, "Make": "Mazda"}

d["Model"]= "MX5"

z=[1,2,3,4]

print(z)

s= [i*i for i in z]

print(s)
