class TaskPresenter:
    """
    Displays tasks.

    (This class follows SRP because it has one only responsibility)
    """

    @staticmethod
    def display_task (tasks):
        for task in tasks:
            print (task)