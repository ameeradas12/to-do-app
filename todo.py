import os
import json

class toDoList():
    def __init__(self):
        saved = saver()
        self.tasks = saved.load()


  

    def printMenu(self):
        print("1. Show tasks")
        print("2. Mark task done")
        print("3. Delete task")
        print("4. Add task")
        print("5. Quit")

    def showTasks(self):
        if not self.tasks:
            print("No tasks yet.")
        for number, task in enumerate(self.tasks, start=1):
            if task["done"]:
                print(f"{number}. [x] {task['name']}")
            else:
                print(f"{number}. [ ] {task['name']}")

    def addTask(self, taskName):
        self.tasks.append({"name": taskName, "done": False})

    def markTaskDone(self, taskName):
        for task in self.tasks:
            if task["name"] == taskName:
                task["done"] = not task["done"]
                break
        else:
            print("No task with that name.")

    def removeTask(self, taskName):
        for task in self.tasks:
            if task["name"] == taskName:
                self.tasks.remove(task)
                break
        else:
            print("No task with that name.")
class saver():
    def load(self):
        if os.path.exists("userList.json"):
            with open("userList.json") as f:
                return json.load(f)
        else:
            return []

    def save(self, userList):
        with open("userList.json", "w") as f:
            json.dump(userList, f, indent=2)



            
    
if __name__ == "__main__":
    running = True
    userList = toDoList()
    saved = saver()
    while running:
        userList.printMenu()
        choice = input("Select an option. ").strip()

        match choice:
            case "1": userList.showTasks()
            case "2": 
                taskName = input("Which task is complete? ")
                userList.markTaskDone(taskName)
                saved.save(userList.tasks)
            case "3": 
                taskName = input("Remove which task? ")
                userList.removeTask(taskName)
                saved.save(userList.tasks)
            case "4": 
                taskName = input("Add which task? ")
                userList.addTask(taskName)
                saved.save(userList.tasks)
            case "5": 
                running = False
                saved.save(userList.tasks)

            
        print()

   

            
                



