# Universe class store the information in the file into the unvierse class and simplify the complexity of the program so that the logic in the program seems simpler
class Universe(object):
    # the initialization method of the universe class
    def __init__(self,name, rewards=[],portals=[]):
        self.name=name
        self.rewards=rewards
        self.portals=portals
    # special string method of the unvierse class, enabling the Universe variables can be printed 
    # the printed out information including its reward attribute and portal attribute
    def __str__(self):
        str1 = "Universe: {} ({} rewards and {} portals)\n".format(self.name,len(self.rewards),len(self.portals))
        str1+="Rewards:\n"
        if len(self.rewards)==0:
            str1+="None\n"
        else:
            for reward in self.rewards:
                str1+="at ({},{}) for {} points: {}\n".format(reward[0],reward[1],reward[2],reward[3])
        str1+="Portals:\n"
        if len(self.portals)==0:
            str1+="None\n"
        else:
            for portal in self.portals:
                str1+="{}:({},{}) -> {}:({},{})\n".format(self.name,portal[0],portal[1],portal[2],portal[3],portal[4])    
        return str1
    