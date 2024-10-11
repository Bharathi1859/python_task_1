l=list(input("enter list: "))
print(l)
l.append(3)
print(l)
l.pop()
print(l)

t=tuple(input("enter tuple: "))
x=list(t)
x.append("t")
print(tuple(x))
x.pop()
print(tuple(x))

s=set(input("enter set: "))
s.add("rat")
print(s)
s.remove("rat")
print(s)

dict1={}
dict=int(input("enter dict: "))
for i in range(dict):
    key=input("enter key")
    value=input("enter value")
    dict1[key]=value
dict1[2]=8
print(dict1)

print(l)
print(t)
print(s)
print(dict1)
