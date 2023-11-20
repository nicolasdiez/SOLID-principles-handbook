"""
SRP: 
Every software component component should have one and only one responsibility. 
I.e. Every software component should have only one reason to change.
"""

class ToDoList:
    def init (self):
        self.tasks = []

    def add_task (self, task):
        self.tasks.append(task)

    def delete_task (self, task):
        self.task.remove(task)
    
    def display_task (self):
        for task in self.tasks:
            print (task)

    def input_task (self):
        task = input("Enter a task to add: ")
        self.add_task(task)

    def remove_task (self):
        task = input ("Enter the task to remove: ")
        self.delete_task(task)

