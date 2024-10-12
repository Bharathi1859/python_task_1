#list
userlist=input("Enter the list elements: ")
mylist=userlist.split()
print("list",mylist)
mylist.append("object")
print("list",mylist)
mylist.pop(2)
print("list",mylist)
mylist[1]="yellow"
print("list",mylist)
mylist.insert(3,"sky blue")
print("list",mylist)


#tuple
usertuple=input("Enter the tuple elements: ")
my_tuple=tuple(usertuple.split())
print("tuple ",my_tuple)
x=list(my_tuple)
x.append("45")
print("tuple ",tuple(x))
x.insert(2,46)
print("tuple ",tuple(x))
x.pop(0)
print("tuple ",tuple(x))
x.reverse()
print("tuple ",tuple(x))

#set
userset=input("Enter the set elements: ")
my_set=set(userset.split(','))
print("set",my_set)
y={20,40,56}
my_set.update(y)
print("set ",my_set)
my_set.clear()
print("set ",my_set)

#dictionary
userdict=int(input("Enter the dictiobary: "))
my_dict={}
for i in range(userdict):
    key=input("key: ")
    my_dict[key]=input("values: ")
print("dict",my_dict)
my_dict["black"]=2
print("dict",my_dict)
my_dict.pop("red")
print("dict",my_dict)
my_dict.update({"pink":8})
print("dict",my_dict)



output//

Enter the list elements: red black pink blue yellow
list ['red', 'black', 'pink', 'blue', 'yellow']
list ['red', 'black', 'pink', 'blue', 'yellow', 'object']
list ['red', 'black', 'blue', 'yellow', 'object']
list ['red', 'yellow', 'blue', 'yellow', 'object']
list ['red', 'yellow', 'blue', 'sky blue', 'yellow', 'object']
Enter the tuple elements: 34 56 tree 90 black
tuple  ('34', '56', 'tree', '90', 'black')
tuple  ('34', '56', 'tree', '90', 'black', '45')
tuple  ('34', '56', 46, 'tree', '90', 'black', '45')
tuple  ('56', 46, 'tree', '90', 'black', '45')
tuple  ('45', 'black', '90', 'tree', 46, '56')
Enter the set elements: red,pink,ring,35,70
set {'pink', '35', 'red', 'ring', '70'}
set  {'pink', 40, '35', 'red', 20, 56, 'ring', '70'}
set  set()
Enter the dictiobary: 4
key: yellow
values: 5
key: black
values: 7
key: pink
values: 3
key: red
values: 8
dict {'yellow': '5', 'black': '7', 'pink': '3', 'red': '8'}
dict {'yellow': '5', 'black': 2, 'pink': '3', 'red': '8'}
dict {'yellow': '5', 'black': 2, 'pink': '3'}
dict {'yellow': '5', 'black': 2, 'pink': 8}



