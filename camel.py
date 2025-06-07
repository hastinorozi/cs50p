user=input("camelCase :")
print("Snake Case: ",end="")

for i in user:
    if i.islower():
        print(i,end="")
    if i.isupper():
        print("_",i.lower(),end="",sep="")