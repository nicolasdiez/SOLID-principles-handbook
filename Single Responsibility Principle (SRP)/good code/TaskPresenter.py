"""
This class now follows the SRP because it has one only responsibility.
"""

class TaskPresenter:
    """
    Displays tasks.
    """

    @staticmethod
    def display_task (tasks):
        for task in tasks:
            print (task)