'''
plan for project.

person/ business object.

tool object (on person maybe?) to check what tool the user has and change values to that
money.
inputs. 
1.cut grass with current tool
2.upgrade to next tool
3.display list of all tools with stats
4.quit game

list of tools? each tool can be the object/dictonary to determain what it does.



'''

tools = [
    {"name": "Teeth", "earnings": 1, "cost": 0},
    {"name": "Rusty Scissors", "earnings": 5, "cost": 5},
    {"name": "Old Lawn Mower", "earnings": 25, "cost": 50},
    {"name": "Push Lawn Mower", "earnings": 50, "cost": 500},
    {"name": "Electric Lawn Mower", "earnings": 100, "cost": 100},
    {"name": "Riding Mower", "earnings": 200, "cost": 200},
    {"name": "Hedge Trimmer", "earnings": 300, "cost": 300},
    {"name": "Leaf Blower", "earnings": 400, "cost": 400},
    {"name": "Chainsaw", "earnings": 500, "cost": 500},
    {"name": "Garden Tractor", "earnings": 600, "cost": 600},
    {"name": "Mini Excavator", "earnings": 700, "cost": 700},
    {"name": "Backhoe Loader", "earnings": 800, "cost": 800},
    {"name": "Skid-Steer Loader", "earnings": 900, "cost": 900},
    {"name": "Front-End Loader", "earnings": 1000, "cost": 1000},
    {"name": "Bulldozer", "earnings": 1500, "cost": 1500}
]


class User:
    def __init__(self, name, money, tool):
        self.name = name
        self.money = 0
        self.tool_index = 0
    def cutGrass(self):
        self.money += self.tool.earnings
    def upgradeTool(self, money, tool):
        #upgrade from current tool to next tool. incriment i to keep up with it. 
        


class tools:
    def __init__(self, name, earnings, cost):
        
        self.name = name
        self.earnings = earnings
        self.cost = cost
    
    
        