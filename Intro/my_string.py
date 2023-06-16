import re

name = "Cool"
name1= "naah"
name2 = "Boring"
name3 = name2[2:]
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# print(re.split( "re", str))
print('n'.join(str.split()[6:9]))
# print(f"{name} {name1} {name2}" * 3)
# print(name + name1 + name2)
# print(name * 3)
# print(name[2:])
# print(name * 3, end=" ")