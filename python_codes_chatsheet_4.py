#1.counding Digits, letters, and Spaces in a string
name="python is 1"
digite=0
letter=0
spaces=0
for i in name:
    if i.isdigit():
        digite+=1
    elif i.isalpha():
        letter+=1
    elif i.isspace():
        spaces+=1
print(name)
print("digite:",digite)
print("letter:",letter)
print("spaces:",spaces)

#2.counting Special characters in astring
text='hello how are you? #specialchars! 123'
spacial_character=0
for char in text:
    if not char.isalnum() and not char.isspace():
        spacial_character+=1
print(spacial_character)

#3.Removing All Whitespace in a string
string="P y t h o n "
space=string.replace(" ","")
print(space)

#4.Buildinng a pyramid in python
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()

#5.Randomizing the items of a list in python
import random
list=["python", "java", "c"]
random.shuffle(list)
print(list)
