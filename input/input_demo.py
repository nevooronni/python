##import sys

##name = sys.argv[1]
##age = sys.argv[2]

##print(name)
##print(age)

height = 68 # The unit is inches
if height > 70 :
    print("You are really tall") #python uses indents if we don't indent our code we get an indentationError and our program won't run
elif height > 60:
    print("You are average height")

else:
    print("You are really short")


list_a = list(range(0,5))#range function takes two parameters
print(list_a)

for i in range(0,7) :
    print("I would love " + str(i) + " cookies")


numbers = [1,2,3,4,5]
for i in numbers:
    if i % 2 == 0:
        print(i)


players = 11

while players >= 5 :
    print("The remaining players are",players)
    players -= 1 #loop will run again
