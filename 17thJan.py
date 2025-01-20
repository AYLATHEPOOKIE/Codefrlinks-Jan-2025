#vowels
"""vowels={"a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0}

word=input()
for i in word:
    if i in vowels:
        vowels[i]+=1
print(vowels)"""

#panagram
"""import string

letters={}

for i in string.ascii_lowercase:
    letters[i]=0

panagram=input("Enter a panagram. Let's see how many letters you get! ")

for i in panagram:
    if i.lower() in letters:
        letters[i.lower()]+=1

check=True
wrong=[]
for i,j in letters.items():
    if j==0:
        check=False
        wrong.append(i)

if check:
    print("Congrats! You did it! You made a panagram!")
else:
    print("Oh no! You forgot {}".format(wrong))"""

#frequent words

"""sent=input("Input a sentence: ")

sent=sent.lower()

words=sent.split()

word={}

for i in words:
    if i in word:
        word[i]+=1
    word[i]=0

print("Your most used word is ",max(word))
"""
#number thing 

numbers=input("Input a number: ")

num={}

for i in numbers:
    if i in num:
        num[i]+=1
    num[i]=0

print("Your most used number is ",max(num))

