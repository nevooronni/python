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


number = 0
while True:
    print("I love candy "+ str(number))
    number +=1
    if number == 7 :
        break

'''
in a team of members 20, some numbers are taken and want to display the numbers
that are not taken so others don't pick the picked numbers
'''

# taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

# loop
for i in range(1,21):
    if i in numTaken:
        continue #continue does not print the numbers under the numTaken list
    print(i) #prints numbers from 1-20 but skip over the numTaken list.
