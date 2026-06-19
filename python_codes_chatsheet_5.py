#1.create a generator to produce frist n prime numbers
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def prime(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
x=10
t=prime(x)
for i in t:
    print(i,end=" ")

#2.implementing variable lenght arguments in python
n=(32,5,65,22,87,34,2,57)
avg=sum(n)/len(n)
print(avg)

#3. creating instance member variables in python
class test:
    def __init__(self):
        self.a=5
    def f(self):
        self.b=10
t1=test()
t2=test()
t1.f()
t1.c=15
print(t1.__dict__)
print(t2.__dict__)

#4.Addition using lambda functions
a=lambda a,b : a+b
r=a(3,7)
print(a)

#5.Findinng factorial using lambda function
f=lambda n:1 if n==0 else n*f(n-1)
s=f(5)
print(s)

n=int(input("enter the number:"))
f=1
if n<0:
    print("negative number")
elif n==0:
    print("zero")
else:
    for i in range(1,n+1):
        f=f*i
    print(f)
