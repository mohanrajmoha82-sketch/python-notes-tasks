#1.list compression (to create a list in single line)
l=[2*i for i in range(10)]
print(l)

list=[23,56,65,22,62,32,65,76,33,99]
l1=[i for i in list if i%2==0]
print(l1)

#2.what is the use of split and join function of string
s="what is right in your mind is right in your world"
s1=s.split(" ")
print(s1)
s1=s1[::-1]
print(" ".join(s1))

# #3.global and local variable
def f1():
    global x
    x=15
    y=10
    print("x=%d y=%d"%(x,y))
f1()
print(x)

#4.golbals function
def fun():
    x=10
    d=globals()
    print("local x=%d global x=%d"%(x,d['x']))
fun()

#5.type conversion basics
a=int("123")
b=float("1234.5")
c=complex("3+4j")
d=str(12)
f=bool("True")
g=bin(25)
h=oct(25)
i=hex(25)
j=ord("A")
k=chr(98)
print(a,b,c,d,f,g,h,i,j,k,sep="\n")