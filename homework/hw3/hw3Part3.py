def move(x,y,direction):
    direction = direction.upper()
    if direction == "N":
        y-=20
    elif direction =="E":
        x+=20
    elif direction =="S":
        y+=20
    elif direction =="W":
        x-=20
    x=max(x,0)
    y=max(y,0)
    x=min(x,150)
    y=min(y,150)
    return (x,y)

def remain_power (command,power):
    if command == "N" or command == "E" or command == "S" or command == "W":
        power -=1
    elif command == "ATTACK" :
        power -=5
    elif command =="REST":
        power = 10
    else :
        power -=1
    return power

position_x = 75
position_y = 75
power = 10
list=[]
#1
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
    
#2
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
#3
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)

#4
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
#5
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)


#6
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
#7
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
#8
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
#9
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)

#10
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
cmd = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
print(cmd)
list.append(cmd)
cmd=cmd.upper()
power=remain_power(cmd,power)
if power<0:
    (position_x,position_y)=(position_x,position_y)
else:
    (position_x,position_y) = move(position_x,position_y,cmd)
if power<0:
    if cmd=="ATTACK":
        print("Pffft, It's a dud ...")
    else:
        print("Pikachu is too tired!")
elif cmd=="ATTACK":
    print("Bzzzt, Pikachu zaps its foe!")
power=max(power,0)
print("Pikachu at ({0}, {1}) with power {2}".format(position_x,position_y,power))
print()
print("All commands entered:")
print(list)
list.sort()
print("All commands sorted:")
print(list)