"""numbers={0:[1,2,3,4,5,6,7,8,9],
         10:[11,12,13,14,15,16,17,18,19],
         20:[21,22,23,24,25,26,27,28,29]}
#non error
print(numbers.get(30,"nice imagination but no"))
#basic values
print(numbers[20][-2])
#just keys
print(numbers.keys())
#just values
print(numbers.values())
#print all without dict
for i in numbers:
    print(i,numbers[i])
for i,j in numbers.items():
    print(i,j)
#add a key value pair
numbers[30]=[31,32,33,34,35,36,37,48,39,"delete"]
print(numbers)
#edit
numbers[30][-3]=38
print(numbers[30])
#delete
del numbers[30][-1]
print(numbers[30])

#list in a list
classroom={"Dave":{"age":27,"marks":[50,45,69,42]},
           "Pheobe":{"age":28,"marks":[89,67,98,59]}}
print(classroom["Pheobe"]["age"])"""
#clear=cls
import random
Countries={"France":"Paris",
           "England":"London",
           "Pakistan":"Islamabad",
           "Brazil":"Brassilia",
            "Canada":"Ottawa",
            "Gremany":"Berlin",
            "India":"New Dehli",
            "Japan":"Tokyo",
            "Mexico":"Mexico City",
            "New Zealand":"Wellington",
            "Norway":"Oslo",
            "Scotland":"Edingburgh",
            "Spain":"Madrid",
            "UAE":"Abu Dhabi",
            "US":"Washington",
            "Wales":"Cardiff"}

while True:
 choice=int(input("\n 1 for viewing all capitals\n 2 for viewing all countries\n 3 for contry guessing game\n 4 for editing\n"))

 if choice==1:
     for i in Countries:
         print(i,Countries[i],"\n")

 elif choice==2:
     for i in Countries:
         print(i)

 chances=3
 score=0
 if choice==3:
  while chances>0:
   country=random.choice(list(Countries.keys()))
   answer=input("What's the capital of... {}? ".format(country))
   if answer.capitalize()==Countries[country]:
        score+=1
        print("YAYYYYY YOU GOT IT RIGHT! Your score is {}".format(score))
        
   else:
        chances-=1
        print("Ohhhh tough luck.The answer was {}. You have {} more chances.".format(Countries[country],chances))

  print("STOP!!! You ran out of chances! Your final score was {}".format(score))

 if choice==4:
         countrie=input("Whats the country?")
         cap=input("What's the capital of {}?".format(countrie))
         Countries[countrie.capitalize()]=cap.capitalize()

        