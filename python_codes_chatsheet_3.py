#1.converting a list into a string
#string method
list=["P","Y","T","H","O","N"]
string="".join(list)
print(string)
#loop method
str=""
for i in list:
    str+=i
print(str)

#2.adding two list Elements together
list1=[1,2,3]
list2=[4,5,6]
list3=[]
for i in range(0, len(list1)):
    list3.append(list1[i] + list2[i] )
print(list3)

#3.comparing two strings for ANAGRAMS
s1="listen"
s2="silent"
s1=s1.replace(" ","").upper()
s2=s2.replace(" ","").upper()
if sorted(s1) ==sorted(s2):
    print(True)
else:
    print(False)

#4.checking for PALINDROME using Extended slicing Techinque
s="kayak".lower()
if s==s[::-1]:
    print(True)
else:
    print(False)

#5.counting the white spaces in a string
l="P r ogram in g"
l1=l.count(" ")
print(l1)

