#precedence 
def seg1:
  print(end=" ")
  for col in range(3):
    print("*",end="")
  print()

def seg2:
  for i in range(3):
    print("*")
  print()

def seg3:
  for i in range(3):
    for j in range(3):
      print(end=" ")
    print("*")
  print()

def seg23:
  for i in range(3):
    print("*",end="")
    for j in range(2):
      print(end=" ")
    print("*")
  print()

def seg4:
  print(end=" ")
  for i in range(3):
    print("*",end="")
  print()

def seg5:
  for i in range(3):
    print("*")
  print()

def seg6:
  for i in range(3):
    for j in range(3):
      print(end=" ")
    print("*")
  print()

def seg56:
  for i in range(3):
    print("*",end="")
    for j in range(2):
      print(end=" ")
    print("*")
  print()

def seg7:
  print(end=" ")
  for i in range(3):
    print("*",end="")
  print()

p=int(input("Enter Number=>"))
if(p==1):
  seg1()
  seg3()
  seg5()
if(p==2):
  seg1()
  seg3()
  seg4()
  seg5()
  seg7()

#