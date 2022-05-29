
import random

memes=[]
floop='testingwew'
for letter in floop:
    memes.append(letter)
    #print(letter)
print(memes[2])

vowelset = ['a','e','i','o','u']
guess = str(input("vowel: "))
a=False
if guess in vowelset:
    a = True
    print(a)


