from project.task import Task

class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
        self.cleaned = 0

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        for task in self.tasks:
            if task.completed:
                self.cleaned += 1
                self.tasks.remove(task)

        return f"Cleared {self.cleaned} tasks."

    def view_section(self):
        final = []

        final.append(f"Section {self.name}:")

        for task in self.tasks:
            final.append(f"{task.details()}")

        return '\n'.join(final)

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed","27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

# The Section class should receive a name (string) upon initialization.
# The task also has one instance attribute: tasks (empty list)
# The Section class should also have four methods:
#     • add_task(new_task: Task)
#         ◦ Adds a new task to the collection and returns "Task {task details} is added to the section"
#         ◦ If the task is already in the collection, return "Task is already in the section {section_name}"
#     • complete_task(task_name: str)
#         ◦ Changes the task to completed (True) and returns "Completed task {task_name}"
#         ◦ If the task is not found, returns "Could not find task with the name {task_name}"
#     • clean_section()
#         ◦ Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
#     • view_section()
#         ◦ Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"