class TaskInput:
    """
    Handles user input for adding or removing tasks.

    (This class follows SRP because it has one only responsibility)
    """

    @staticmethod   
    def input_task ():
        return input("Enter a task to add: ")

    @staticmethod
    def remove_task ():
        return input ("Enter the task to remove: ")