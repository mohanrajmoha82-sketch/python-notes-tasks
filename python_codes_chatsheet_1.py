#1.converting an integer in to decimals
import decimal
int=10
print(decimal.Decimal(int))
print(type(decimal.Decimal(int)))

#2.converting an string of integers into decimals
import decimal
str="123450987"
print(decimal.Decimal(str))
print(type(decimal.Decimal(str)))


#3.Reversing a string using an extended slicing technique
slicing="Wllcome to python"
print(slicing)
print(slicing[::-1])


#4.counting VOWELS in a given Word
vowele=list("aeiouAEIOU")
words="python programming"
count=0
for i in words:
    if i in vowele:
        count+=1
print(count)

#5.counting CONSONANTS in a given word
vowels = list("aeiouAEIOU")
words="python programming"
count=0
for i in words:
    if i not in vowels:
        count+=1
print(count)
