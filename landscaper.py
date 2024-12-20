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






class Tool:
    def __init__(self, name, earnings, cost):
        self.name = name
        self.earnings = earnings
        self.cost = cost

tools = [
    Tool("Teeth", 1, 0),
    Tool("Rusty Scissors", 5, 5),
    Tool("Old Lawn Mower", 25, 50),
    Tool("Push Lawn Mower", 50, 500),
    Tool("Electric Lawn Mower", 100, 100),
    Tool("Riding Mower", 200, 200),
    Tool("Hedge Trimmer", 300, 300),
    Tool("Leaf Blower", 400, 400),
    Tool("Chainsaw", 500, 500),
    Tool("Garden Tractor", 600, 600),
    Tool("Mini Excavator", 700, 700),
    Tool("Backhoe Loader", 800, 800),
    Tool("Skid-Steer Loader", 900, 900),
    Tool("Front-End Loader", 1000, 1000),
    Tool("Bulldozer", 1500, 1500)
]

class User:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.tool_index = 0

    def cut_grass(self):
        current_tool = tools[self.tool_index]
        self.money += current_tool.earnings
        print(f"{self.name} cut grass with {current_tool.name} and earned {current_tool.earnings} dollars!")

    def upgrade_tool(self):
        next_tool_index = self.tool_index + 1
        if next_tool_index < len(tools):
            next_tool = tools[next_tool_index]
            if self.money >= next_tool.cost:
                self.money -= next_tool.cost
                self.tool_index = next_tool_index
                print(f"{self.name} upgraded to {next_tool.name}!")
            else:
                print("Not enough money to upgrade.")
        else:
            print("No more tools to upgrade to.")

    def display_tools(self):
        for tool in tools:
            print(f"Tool: {tool.name}, Earnings: {tool.earnings}, Cost: {tool.cost}")


def choiceFunction():
    print(f"you have ${user.money} what would you like to do?")
    print(prompt)
    choice = int(input("Please choose 1, 2, 3, or  4        "))
    if choice == 1:
        user.cut_grass()
        choiceFunction()
    elif choice == 2:
        user.upgrade_tool()
        choiceFunction()
    elif choice == 3:
        user.display_tools()
        choiceFunction()
        
    elif choice == 4:
        quit()
    else:
        print(f"{user.name}... you know better... dont make me come over there.")

prompt = f'''
1 = cut grass 
2 = upgrade to next tool
3 = display list of all tools
4 = quit game
















'''


user = User(input("enter your name  "))
print(f"hello {user.name} you are about to cut some grass. please choose from the following {prompt}")


choiceFunction() 

# print(f"{user.current_tool}")
# user.cut_grass() 
# user.cut_grass() 
# user.upgrade_tool()  
# user.display_tools()  

