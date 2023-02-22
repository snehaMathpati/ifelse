#  Write a python program to check whether a character is an alphabet or not.

a=input("enter character")
if a>="a" and a<="z" : 
    print(a,"is alphabet")
elif a>="A" and a<="Z":
     print(a,"is alphabet")
    
else:
    print(a,"is not alphabet")