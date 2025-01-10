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
           "England":"London"}
choice=int(input(" 1 for viewing all capitals\n 2 for viewing all countries\n 3 for contry guessing game\n 4 for editing"))
if choice==1:
    for i in Countries:
        print(i,Countries[i],"\n")
elif choice==2:
    for i in Countries:
        print(i)
elif choice==3:
    print("What's the capital of... {}".format(random.choice(list(Countries.keys()))))