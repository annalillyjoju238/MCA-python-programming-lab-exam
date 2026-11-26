num=list(map(int,input("enter the numbers:").split()))
print("list:",num)
search=int(input("enter the number to search:"))
if search in num:
    print(search,"is found")
else:
    print(search, "is not found")
old=int(input("enter the old number:"))
new=int(input("enter the new number:"))
i=num.index(old)
num[i]=new
print("updated:",num)
num.append(int(input("enter the number:")))
print(num)
print("min:",min(num))
print("max:",max(num))
print("length:",len(num))
print( search for search in num if num > 5)