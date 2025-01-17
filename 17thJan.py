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

sent=input()

sent=sent.lower()

words=sent.split()

word={}.fromkeys(words,0)

print(word)