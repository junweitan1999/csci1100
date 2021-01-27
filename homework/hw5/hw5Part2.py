'''
 This file get the grid size and probbability as the input and output the information about where the trainer meet pokemon inside the grid and how many he caught
 Junwei Tan
'''


# importing random moduel
import random
# defining the function about the movement of the trainer
def move_trainer():
    directions=['N', 'E', 'S', 'W']
    return(random.choice(directions),random.random())
# defining the function whether the pokeball catch the pokemon     
def throw_pokeball(num_false, num_true):
    lst=[]
    for m in range(num_false):
        lst.append(False)
    for n in range(num_true):
        lst.append(True)
    random_boolean = random.choice(lst)
    return random_boolean
# geting input from user
size = input("Enter the integer grid size => ")
print(size)
size = int(size)
random_seed = 10*size + size
random.seed(random_seed)
p = input("Enter a probability (0.0 - 1.0) => ")
print(p)
p = float(p)
# initializing
xposition=size//2
yposition=size//2
number_false = 3
number_true = 1
pokemon_number = 0
pokemon_catch = 0
turn=1
while True:
# call function and store the result in movement variable
    movement = move_trainer()   
    # move the trainer according to the selected direction
    if movement[0]=='N':
        xposition-=1
    elif movement[0]=='S':
        xposition+=1
    elif movement[0] =='E':
        yposition+=1
    elif movement[0]=='W':
        yposition-=1    
# if the trainer reach the edge of the grid, pop out message and break the loop
    if xposition < 0 or xposition>size-1 or yposition< 0 or yposition>size-1:
        
        xposition=max(xposition,0)
        xposition=min(xposition,size-1)
        yposition=max(yposition,0)
        yposition=min(yposition,size-1)
        print("Trainer left the field at turn {0}, location ({1}, {2}).".format(turn-1,xposition,yposition))
        print("{0} pokemon were seen, {1} of which were captured.".format(pokemon_number,pokemon_catch))
        break
# pop out message if the trainer meet a pokemon in the grid, and store the number of pokemon the trainer meet in the variable pokemon_number
    if movement[1] < p :
        print("Saw a pokemon at turn {0}, location ({1}, {2})".format(turn,xposition,yposition))
        pokemon_number +=1
        catch = throw_pokeball(number_false,number_true)
        if catch == True :
            # store the number of catched pokemon  in the variable pokemon_catch
            pokemon_catch +=1
            print("Caught it!")
            number_true +=1
        else:
            print("Missed ...")
# let the number of turn be stored in the variable turn
    turn+=1