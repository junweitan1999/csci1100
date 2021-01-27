'''
 This file execute 2 function each for 5 times to let student get familiar to the random moduel and facilitate the function for the latter part of the hw
 Junwei Tan
'''
# importing random moduel
import random
#  defining the function about the movement of the trainer
def move_trainer():
    directions=['N', 'E', 'S', 'W']
    # print out the direction list and randomly choose a direction from the list and choose a number from 0 to 1 randomly
    print("Directions:",directions)
    print("Selected",random.choice(directions)+", value {0:.2f}".format(float(random.random())))
    
# defining the function whether the pokeball catch the pokemon 
def throw_pokeball(num_false, num_true):
    #initializing and put several False and True boolean variable into the list according to the integer argument
    lst=[]
    for m in range(num_false):
        lst.append(False)
    for n in range(num_true):
        lst.append(True)
    # randomly choose a boolean from the list
    random_boolean = random.choice(lst)
    print("Booleans:",lst)
    print("Selected",random_boolean)
    # get input from user
size = int(input("Enter the integer grid size => "))
print(size)
random_seed = 10*size + size
random.seed(random_seed)
number_false = int(input("Enter the integer number of Falses => "))
print(number_false)
number_true = int(input("Enter the integer number of Trues => "))
print(number_true)
print("Setting seed to {0}".format(random_seed))
# according to the requirement call function move_trainer and throw_pokeball each for 5 times
for i in range(5):
    move_trainer()
    
for i in range(5):
    throw_pokeball(number_false,number_true)