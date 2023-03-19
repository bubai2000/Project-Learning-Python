#precedence 
def seg1():
  print(end=" ")
  for col in range(3):
    print("*",end="")
  print()

def seg2():
  for i in range(3):
    print("*")
  print()

def seg3():
  for i in range(3):
    for j in range(3):
      print(end=" ")
    print("*")
  print()

def seg23():
  for i in range(3):
    print("*",end="")
    for j in range(2):
      print(end=" ")
    print("*")
  print()

def seg4():
  print(end=" ")
  for i in range(3):
    print("*",end="")
  print()

def seg5():
  for i in range(3):
    print("*")
  print()

def seg6():
  for i in range(3):
    for j in range(3):
      print(end=" ")
    print("*")
  print()

def seg56():
  for i in range(3):
    print("*",end="")
    for j in range(2):
      print(end=" ")
    print("*")
  print()

def seg7():
  print(end=" ")
  for i in range(3):
    print("*",end="")
  print()

p=int(input("Enter Number=>"))
if(p==1):
  seg1()
  seg3()
  seg5()
elif(p==2):
  seg1()
  seg3()
  seg4()
  seg5()
  seg7()
elif(p==3):
  seg1()
  seg3()
  seg4()
  seg6()
  seg7()
elif(p==4):
  seg23()
  seg4()
  seg6()
elif(p==5):
  seg1()
  seg2()
  seg4()
  seg6()
  seg7()
elif(p==6):
  seg1()
  seg3()
  seg4()
  seg56()
  seg7()
elif(p==7):
  seg1()
  seg3()
  seg6()
elif(p==8):
  seg1()
  seg23()
  seg4()
  seg56()
  seg7()
elif(p==9):
  seg1()
  seg23()
  seg4()
  seg6()
  seg7()
elif(p==0):
  seg1()
  seg23()
  seg56()
  seg7()
else:
  print("Enter a number in the range 0 to 9!")