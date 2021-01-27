# person class for hw8 that largely simplify the complexity of the code

class Person (object):
    # initialization method of the class
    def __init__(self,name,radius,home_universe,x,y,dx,dy,current_universe,rewards):
        self.name=name
        self.radius=radius
        self.home_universe=home_universe
        self.x=float(x)
        self.y=float(y)
        self.dx=float(dx)
        self.dy=float(dy)
        self.current_universe=current_universe
        self.rewards=rewards
        self.point=0
        self.stopvx=float(self.dx)
        self.stopvy=float(self.dy)
        self.movingstep=0
    # the special string method that enable the main programa can print out the person variable in the main program
    def __str__(self):
        return("{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points".format(self.name,self.home_universe,self.current_universe,self.x,self.y,self.stopvx,self.stopvy,len(self.rewards),self.point))
    
    # move method that enable person class to move by changing its x and y attribute 
    def move(self):
        if self.dx!=0 and self.dy!=0:
            self.x+=self.dx
            self.y+=self.dy
            self.stopvx=self.dx
            self.stopvy=self.dy
    # if a person get out of the board or velcoity below10 , it will get stop
    def stop(self,step):
        if self.dx!=0 and self.dy!=0:
            if self.x<=0 or self.y<=0 or self.x>=1000 or self.y>=1000 or abs(self.dx)<10 or abs(self.dy)<10: 
                self.stopvx=self.dx
                self.stopvy=self.dy
                self.dx=0
                self.dy=0
                print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(self.name,step,self.x,self.y))
                print()
    # method about picking up reward and specifies the change about a person that pick up the reward 
    def pick_reward(self,reward,step):
        if len(reward)==6:
            pass
        self.rewards.append(reward)
        self.dx = self.dx - (len(self.rewards)%2)* (len(self.rewards)/6)*self.dx
        self.dy = self.dy - ((len(self.rewards)+1)%2)* (len(self.rewards)/6)*self.dy
        self.point+=reward[2]
        reward.append(self.name)
        print('{} picked up "{}" at simulation step {}'.format(self.name,reward[3],step))
        print('{} of {} in universe {}'.format(self.name,self.home_universe,self.current_universe))
        print('    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.format(self.x,self.y,self.dx,self.dy,len(self.rewards),self.point))
        print()
        # method about 2 person get collide and the change in these 2 person 
    def collision(self,other,step):
        print("{} and {} crashed at simulation step {} in universe {}".format(self.name,other.name,step+1,self.current_universe))
        if len(self.rewards)>0:            
 
            original_universe = self.rewards[0][4]
            self.point-=self.rewards[0][2]
            self.rewards[0].pop()
        
            print('{} dropped "{}", reward returned to {} at ({:.0f},{:.0f})'.format(self.name,self.rewards[0][3],original_universe,self.rewards[0][0],self.rewards[0][1]))
            self.rewards.pop(0)
            self.dx = -(self.dx + (len(self.rewards)%2)* (len(self.rewards)/6)*self.dx)
            self.dy = -(self.dy + ((len(self.rewards)+1)%2)* (len(self.rewards)/6)*self.dy) 
            self.stopvx=self.dx
            self.stopvy=self.dy
        if len(other.rewards)>0:            

            original_universe = other.rewards[0][4]
            other.point-=other.rewards[0][2]
            other.rewards[0].pop()
            print('{} dropped "{}", reward returned to {} at ({:.0f},{:.0f})'.format(other.name,other.rewards[0][3],original_universe,other.rewards[0][0],other.rewards[0][1]))
            other.rewards.pop(0)
            other.dx = -(other.dx + (len(other.rewards)%2)* (len(other.rewards)/6)*other.dx)
            other.dy = -(other.dy + ((len(other.rewards)+1)%2)* (len(other.rewards)/6)*other.dy) 
            other.stopvx=other.dx
            other.stopvy=other.dy
        print(self)
        print(other)
        print()
        # the method about the portal that if a person get near to a portal, the portal change its current unvierse and xy attributes
    def pick_portal(self,portal,step):
        self.current_universe=portal[2]
        self.x=portal[3]
        self.y=portal[4]
        print('{} passed through a portal at simulation step {}'.format(self.name,step))
        print(self)
        print()