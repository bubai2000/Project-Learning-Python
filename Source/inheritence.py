class A:
    def __init__(self,a):
        self.a=a
        print("Class A created! with a=",self.a)
    def feature1(self):
        print("Feature 1 working!")
    def featur2(self):
        print("Feature 2 working!")
class B(A): #single inheritence
    def __init__(self, a):
        super().__init__(a) #parent constructor inheritence
        print("Class B created!")
    def feature3(self):
        print("Feature 3 working!")

class C(B): #multilevel inheritence
    def __init__(self): #if we don't have this init method, then super class constructor will be called automatically
        print("Class C created!") #not inheriting parent constructor
    def feature4(self):
        print("Feature 4 working!")

class D:
    def __init__(self):
        print("Class D created!")
    def feature5(self):
        print("Feature 5 working!")

class E(A,D): #multiple inhertience
    def __init__(self, a):
        super().__init__(a)
        print("Class E created!")
    def feature1(self):
        print("Feature 1 of E working!")
    def superfeature1(self):
        return super().feature1()


c1=C()
c1.feature1()
c1.feature4()  

e1=E(2)
e1.feature1()
e1.superfeature1()
