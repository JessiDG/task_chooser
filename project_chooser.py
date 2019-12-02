#This is a little utility project I built to help me choose between a few different tasks today

import random

class project_chooser:

    def __init__(self, projects=[]):
        self.projects = self.set_projects(projects)

    def set_projects(self, projects):
        return projects

    def choose_for_me(self):
        rand = random.randrange(len(self.projects))
        return self.projects[rand]

    def __str__(self):
        rand_project = self.choose_for_me()
        return "\nYour randomly selected task is: " + str(rand_project)


class task:

    def __init__(self, title="<default>", task="<default>"):
        self.title = self.set_title(title)
        self.task = self.set_title(task)

    def set_title(self, title):
        return title

    def set_task(self, task):
        return task

    def __str__(self):
        return_str = self.title + ": " + self.task
        return return_str


if __name__ == "__main__":
    t0 = task("Undertow", "Send to 7 agents")
    t1 = task("A Scarcity of Light", "Edit all existing chapters")
    t2 = task("Citizen Diplomacy", "Write cover letter")
    t3 = task("Citizen Diplomacy", "Edit chapters")
    t4 = task("How can I keep from singing?", "Edit 10k words")

    tlist = [t0, t1, t2, t3, t4]

    for i in tlist:
        print(i)

    pc = project_chooser(tlist)

    print(pc)
