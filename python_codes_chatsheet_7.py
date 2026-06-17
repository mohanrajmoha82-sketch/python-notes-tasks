#1.tyoe Conversion
x=5
print(type(x))
s1="123"
print(type(s1))
print(str(x)+s1)
print(x+int(s1))

#2.What is python decorator
def welcome(fx):
    def mfx (*t,**d):
        print("Welcome to Python!")
        fx(*t,**d)
        print("thanks for using the function")
    return mfx
@welcome
def hello():
    print("Hello World!")
@welcome
def add(a,b):
    print(a+b)
hello()
add(1,3)
print("End".center(30,"*"))
def greething(n):
    def fun(*t,**d):
        print("welcome to python")
        n(*t,**d)
        print("thanks for using python ")
    return fun
@greething
def f():
    print("Hello world")
@greething
def add(a,b):
    print(a+b)
f()
add(1,3)
print("End".center(30,"*"))
class calculator:
    def __init__(self,func):
        self.func=func
    def __call__(self,*t,**d):
        r= self.func(*t,**d)
        print(r**2)
@calculator
def f1(a,b):
    return a+b
f1(10,20)
print("End".center(30,"*"))
def mark_result(resuld_fun):
    def distinction(mark):
        r=[]
        for i in mark:
            if i >= 75:
                print("Distinction")
            r.append(resuld_fun([i]))
        print(r)
    return distinction
@mark_result
def result(mark):
    for i in mark:
        if i >= 33:
            pass
        else:
            print("Pass")
            return "Fail"
    else:
         print("Fail")
         return "Pass"
r=result([54,78,80,34,66,90])
print("result",result)