class TaskManager:
    """
    Handles the storage and management (add/delete) of tasks.
    """

    def init (self):
        self.tasks = []

    def add_task (self, task):
        self.tasks.append(task)

    def delete_task (self, task):
        self.task.remove(task)