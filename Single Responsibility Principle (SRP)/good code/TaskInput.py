"""
This class now follows the SRP because it has one only responsibility.
"""

class TaskInput:
    """
    Handles user input for adding or removing tasks.
    """

    @staticmethod   
    def input_task ():
        return input("Enter a task to add: ")

    @staticmethod
    def remove_task ():
        return input ("Enter the task to remove: ")