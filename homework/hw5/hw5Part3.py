'''
 This file takes the number of simulation as input and exectue the simulation about the trainer in the grid about certain time 
 
 Junwei Tan
'''

# importing the random moduel and defining three mandatory function accroding to the requirement on pdf
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
# define the function that the result grid is returned 
def run_one_simulation( grid, prob ):
    # initializing
    number_false = 3
    number_true = 1    
    turn =1
    xposition=yposition = len(grid)//2
    # copying the loop from part2 and change the pop out message to the change in the list grid
    while True:
        if xposition <= 0 or xposition>=size-1 or yposition<= 0 or yposition>=size-1:
            return turn-1
        movement = move_trainer()        
        if movement[0]=='N':
            xposition-=1
        elif movement[0]=='S':
            xposition+=1
        elif movement[0] =='E':
            yposition+=1
        elif movement[0]=='W':
            yposition-=1
        if movement[1] < p :
            catch = throw_pokeball(number_false,number_true)
            if catch == True :
                grid[xposition][yposition]+=1
                number_true +=1
            else:
                grid[xposition][yposition]-=1
        turn+=1    
# get input from user
size = int(input("Enter the integer grid size => "))
print(size)
random_seed = 10*size + size
random.seed(random_seed)
p = input("Enter a probability (0.0 - 1.0) => ")
# i had to print out the exact input as the user typed in so float function had to be another line instead of writing them together
print(p)
p=float(p)
number_simulation = int(input("Enter the number of simulations to run => "))
print(number_simulation)
print()
#initializing
count_grid = []
total_turn =0
max_number = (0,0)
min_number=(999,0)
# creating a all-0 grid
for i in range(size):
    count_grid.append( [0]*size )
    # let the grid record the simulation 
    # the simulation has multiple times according to the user input
for i in range(number_simulation):
    turn = run_one_simulation(count_grid, p)
    # record the maximum turn and minimum turn 
    if turn>max_number[0]:
        max_number=(turn,i+1)
    
    if turn<min_number[0]:
        min_number=(turn,i+1)
        # record the total turn to calculate the average turns
    total_turn+=turn
    
for i in count_grid:
    row_grid = ""
    for o in i:
        o=str(o)
        # print out the result grid,according to the length of the string, moderate the number of space to make the grid neat
        if len(o)==3:
            row_grid+="  "+o
        elif len(o)==4:
            row_grid+=" "+o
        elif len(o)==2:
            row_grid+="   "+o
        else:
            row_grid+="    "+o
    print(row_grid)
    
    # pop out the stat message about the simulation accoding to the data stored in the variable previously
avg_turn = total_turn/number_simulation
print("Average number of turns in a simulation was {0:.2f}".format(avg_turn))
print("Maximum number of turns was {0} in simulation {1}".format(max_number[0],max_number[1]))
print("Minimum number of turns was {0} in simulation {1}".format(min_number[0],min_number[1]))
pokemonlst =[]
pokemon = 0
# from the result grid to derive the best net missed pokemon data
for i in count_grid:
    for o in i:
        if o>pokemon:
            pokemon=o
print("Best net missed pokemon versus caught pokemon is {0}".format(pokemon))
# from the result grid to derive the worst net missed pokemon data
for i in count_grid:
    for o in i:
        if o<pokemon:
            pokemon=o
print("Worst net missed pokemon versus caught pokemon is {0}".format(pokemon))