class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        """Adds a task to the local list."""
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def delete_task(self, display_id):
        """Removes task and re-indexes the remaining ones automatically."""
        try:
            index = display_id - 1
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                return True
            return False
        except (ValueError, IndexError):
            return False

