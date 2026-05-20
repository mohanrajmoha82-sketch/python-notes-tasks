
"""
refernce type
1.Iteratar
2.Generater
3.closuer
4.Dearatar
"""
#1.Iteratar ---> iter() , next() , __next__()
l=[3,4,5,2,6,8]
x=iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(x.__next__())

#2.Generater ----> yield-keyworld , next()-function , __next__()-build function
def demo():
    name="mohanraj"
    id="105"
    yield name
    yield id
    yield "salem"
    yield "python developer"
d=demo()
print(d)
print(next(d))
print(next(d))
city=next(d)
print(city)
dept=d.__next__()
print(dept)

#3.closuer
def outer():
    print("Wlecome to python world")
    def inner():
        print("hello java")
    inner()
outer()

#4.Decorater
def greething(n):
    x=n
    def contend():
        print("Hello mohanraj")
        x()
        print("Welcome to office")
    contend()
@greething
def data ():
    print("I am praveen")