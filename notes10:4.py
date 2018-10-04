#we want the computer to pick a random number in a given range
#pick a random elelemnts from a list, pick a random card from a deck, flip a coin, etc
#when making your password database more secure or powering

import random
number = random.randint(0,100)
print(number)
#generates a random number between your two values

import random
myList = [1, "hello", 10, "sacred heart", "long weekend"]
selectItem = random.choice(myList)
#.choice is a function
print(selectItem)

#import random as rand
#rand.int
#type of shorthand
