#1.positional arguments in python
def num(a,b):
    print("a=",a,", b=",b)
num(1,2)
num(3,40)
num(23,34)

#2.sorted and sort function in python
#Sorted
l=(34,64,32,78,88,83,95,64)
l1=sorted(l)
print(l1)
#sort
l=[34,64,32,78,88,83,95,64]
l.sort()
print(type(l))
print(l)

#3.create static member variables in class
class create:
    a=5
    def __init__(self):
        self.x=10
        y=4
        create.b=34
    def f(self):
        create.c=65
    @staticmethod
    def f2(seif):
        create.d=66
    @classmethod
    def f3(seif):
        cls.e=15
        create.f=16
create.g=11

#4.loop
#1
i=1
while i<10:
    print(i,end=" ")
    if(i==5):
        break
    i=i+1
#2
i=1
while i<10:
    print(i,end=" ")
    if i==12:
        break
    i=i+1
else:
    print("\nyou are in else")

#3
for i in range (10):
    print(i,end=" ")
    if i==12:
        break
else:
    print("you are in else")

