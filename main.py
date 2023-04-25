x=input("put the first number: ")
x=int(x)
z=input("put the operator '+' or '-' or '*' or '/' ")
y=input("put the second number: ")
y=int(y)
if z=="+":
  print(x+y)
elif z=="-":
  print(x-y)
elif z=="*":
  print(x*y)
elif z=="/":
  print(x/y)
else:
  print("invalid operator")

