a=int(input ("Enter a= "))
b=int(input ("Enter b= "))

print(id(a))
print(id(b))

print(a is b)
print(a is not b)

if(a is b):
    print("Both address are same")
else:
    print("Both are different")
    
