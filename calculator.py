n1=input('enter n1-  ')
n2=input('enter n2-  ')
nnn= input(" *,-,+,/    -  ")

n1=int(n1)
n2=int(n2)
if nnn=="*":
  x1=n1*n2
  print(x1)

elif nnn=="-":
  x2=n1-n2
  print(x2)

elif nnn=="+":
  x3=n1+n2
  print(x3)

elif nnn=="/":
  x4=n1/n2
  print(x4)

else:
  print("error")