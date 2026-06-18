# What are iterators in python
l=[22,33,44,55,76,66,77,31]
l1=iter(l)
while True:
    try:
        print(next(l1))
    except StopIteration:
            break

#What are Genarator in python ?create a genarator for frist n natural even number
def Even_number(num):
    i=1
    while num:
        yield 2*i
        i+=1
        num-=1
it=Even_number(10)
even_list=[]
while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break
print(even_list)

#overloading allowed in python
def greet(name,greeting="hello"):
    return f"{greeting} {name}"
print(greet("Mohan"))
print(greet("Mohan",greeting="hi"))
#Add
def add(*t):
    return sum(t)
print(add(1,2))
print(add(1,3,5,6))
