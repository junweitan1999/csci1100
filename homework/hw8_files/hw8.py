'''
This program is supposed to simulate a game process that several people in several universe move, collide, pickup reward, pass the portal and stop. The program will print out the issue happens in the game process during 100 step and eventually print out the final result such as the winner's name, the reward on that player , and the point belongs to that player. 
Junwei Tan
'''
# import 2 classes written in the other file 
# import json and math moduel to facilitate the writting process of the code
from Person import *
from Universe import *
import json
import math
# ask user for the input filename
fname=input("Input file => ") 
print(fname)
data=json.loads(open(fname).read())
list_universe=[]
# print out the basic information of the universe and store the information in the file into the class Universe and person variable
for i in range(len(data)):
    new_universe=Universe(data[i]["universe_name"],data[i]["rewards"],data[i]["portals"])
    list_universe.append(new_universe)
    for reward in new_universe.rewards:
        reward.append(data[i]["universe_name"])
    for portal in new_universe.portals:
        portal.append(data[i]["universe_name"])
list_person=[]
for i in range(len(data)):
    for person in data[i]["individuals"]:
        new_person = Person(person[0],person[1],data[i]["universe_name"],person[2],person[3],person[4],person[5],data[i]["universe_name"],[])
        list_person.append(new_person)

# print out the basic information of the universe and person
print("All universes")
print("-"*40)
for universe in list_universe:
    print(universe)
print("All individuals")
print("-"*40)
for person in list_person:
    print("{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points".format(person.name,person.home_universe,person.current_universe,person.x,person.y,person.dx,person.dy,len(person.rewards),person.point))
print()
# start the simulation of 100 step by using for loop
print("Start simulation")
print("-"*40) 
for step in range(100):
    for person in list_person:    
        # at the begin of each step , check whether each person is eligible to stop
        person.stop(step)   
        # if people's attribute dx and dy is not 0, increasing its attribute movingstep by 1 
        if person.dx != 0 and person.dy!= 0:
            person.movingstep+=1
        for universe in list_universe:
            for reward in universe.rewards:
                # for each reward in each universe, check whether the people is near to the reward and able to pick it up
                if len(reward)==5:
                    if (math.sqrt((person.x-reward[0])**2+(person.y-reward[1])**2)<= person.radius) and person.dx!=0:
                        person.pick_reward(reward,step)
                        person.stop(step)          
                        # after picking up the reward, the velocity will decrease in its magnitude,check if it will stop 
        for universe in list_universe:
            # for each portal in each universe, the people will be transport to another position if it is near to a portal
            for portal in universe.portals:
                if (math.sqrt((person.x-portal[0])**2+(person.y-portal[1])**2)<= person.radius)and(person.current_universe==portal[5]) and person.dx!=0:     
                    person.pick_portal(portal,person.movingstep-1)
        # move the person by 1 step each 
        person.move()    
    # carefully check each person whether they collide with another peroson for each step
    for i in range(len(list_person)-1):
        for j in range(i+1,len(list_person)):
            if (math.sqrt((list_person[i].x-list_person[j].x)**2+(list_person[i].y-list_person[j].y)**2)<= (list_person[i].radius+list_person[j].radius)):
                if list_person[i].dx!=0 and list_person[i].dy!=0 and list_person[j].dx!=0 and list_person[j].dy!=0 and list_person[i].current_universe== list_person[j].current_universe and list_person[i] != list_person[j]:
                    list_person[i].collision(list_person[j],step) 
# the stop method isnt valid for the last step
for person in list_person:
    person.stop(step+1)  
max_step = 0
# find out the maximum moving step by for loop
for person in list_person:
    if person.movingstep>max_step:
        max_step = person.movingstep
print()
print('-'*40)
# nested if that print out the output of the simulation such as the step that simulation stops and the maximum step, the number of the moving person until the simulation that stops
if max_step<100:
    print("Simulation stopped at step {}".format(max_step))
    print("0 individuals still moving")
else:
    still_moving=[]
    for person in list_person:  
        if person.dx != 0 and person.dy!=0:
            still_moving.append(person)
    if len(still_moving)==0:
        print("Simulation stopped at step 100")
        print("0 individuals still moving") 
    else:
        print("Simulation stopped at step 100")
        moving_name=str(still_moving[0].name )
        if len(still_moving)>1:
            for i in range(1,len(still_moving)):
                moving_name+=", "+still_moving[i].name
        print("{} individuals still moving: ".format(len(still_moving))+str(moving_name))
        
      # print out the winner of the simulation and the rewaard on it  
print("Winners:")
max_points=-100
winner=[]
for person in list_person:
    if person.point > max_points:
        max_points = person.point
for person in list_person:
    if person.point ==max_points:
        winner.append(person)
for i in range(len(winner)):
    print(winner[i])
    print("Rewards:")
    if len(winner[i].rewards)!=0:
        for reward in winner[i].rewards:
            print("    {}".format(reward[3]))
    print()