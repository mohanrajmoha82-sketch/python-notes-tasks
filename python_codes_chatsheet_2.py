#1.counting the number of occurance of a characte in a string
word="python programming"
charcate="g"
count=0
count_word=0
for char in word:
    if char == charcate:
        count+=1
    else:
        count_word+=1
print("g word count charcate:",count)
print("Remaninig  count of charcate:",count_word)

# 2.Writing FIBONACCI Series
# method1
n1=0
n2=1
print(n1)
print(n2)
for i in range(1,6):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
# method2
default=[0,1]
n=5
for i in range(n):
    default.append(default[-1] + default[-2])
print(",".join(str(x) for x in default))

#3.Finding the Maximum Number in a list
list=[12,3,55,23,6,78,33,4]
max=0
for i in list:
    if i>max:
        max=i
print(max)

#4.finding the minimum number in a list
list = [12, 3, 55, 23, 6, 78, 33, 4]
mininum=list[0]
for i in list:
    if i<mininum:
        mininum=i
print(mininum)

#5.Finding the Middle Element in a list
list = [12, 3, 55, 23, 6, 78, 33, 4]
middle=list[len(list)//2]
print(middle)