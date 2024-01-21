x=int(input("put the first number: "))
z=input("put the operator '+' or '-' or '*' or '/' ")
y=int(input("put the second number: "))
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

