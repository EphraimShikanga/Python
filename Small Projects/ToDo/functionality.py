import json
from enum import Enum, auto
import random
from datetime import datetime


class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()


class Task:

    def __init__(self,
                 title, due_date, description, task_status,
                 task_id=None, date_created=None):
        if task_id is None:
            self.ID = "T-" + str(random.randint(100, 999))
        else:
            self.ID = task_id
        self.Title = title
        if isinstance(task_status, TaskStatus):
            self.Status = task_status
        else:
            raise ValueError("Invalid Status value. "
                             "It must be a value of TaskStatus enum.")
        if date_created is None:
            self.Date_Created = datetime.now().strftime("%a %d, %B %Y %H:%M")
        else:
            self.Date_Created = date_created
        self.Due_Date = self.convert_date(due_date)
        # self.due_in = int(self.Due_Date) - int(self.Date_Created)
        self.Description = description

    def __str__(self):
        return f"{self.Title} ({self.Status.name})"

    @staticmethod
    def convert_date(date_str):
        if date_str is None:
            return None
        try:
            date_obj = datetime.strptime(date_str, "%a %d, %B %Y")
            return date_obj.strftime("%a %d, %B %Y")
        except ValueError:
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            return date_obj.strftime("%a %d, %B %Y")


class TaskOperations:

    def __init__(self, file_path):
        self.file_path = file_path
        self.task_list = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.task_list = []
                for task_dict in data:
                    Title = task_dict['Title']
                    Due_Date = task_dict['Due_Date']
                    Description = task_dict['Description']
                    Status = TaskStatus[task_dict['Status']]
                    task_id = task_dict['ID']
                    task_created = task_dict['Date_Created']
                    task = Task(Title, Due_Date, Description,
                                Status, task_id, task_created)
                    self.task_list.append(task)
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = []
        return self.task_list

    def save_tasks(self):
        task_dicts = []
        for task in self.task_list:
            task_dict = task.__dict__
            task_dict['Status'] = task.Status.name
            task_dicts.append(task_dict)

        with open(self.file_path, 'w') as file:
            json.dump(task_dicts, file, indent=4)

    def add_task(self, task):
        self.load_tasks()
        self.task_list.append(task)
        self.save_tasks()

    def delete_task(self, task_ids):
        deleted = False
        self.task_list_copy = list(self.task_list)
        self.load_tasks()
        self.task_list = [
            task for task in self.task_list if task.ID not in task_ids]
        if len(self.task_list) < len(self.task_list_copy):
            deleted = True
            self.save_tasks()
        del self.task_list_copy
        return deleted

    def delete_all_tasks(self):
        self.load_tasks()
        self.task_list.clear()
        self.save_tasks()

    def update_task(self,
                    task_id,
                    new_title=None,
                    new_description=None,
                    new_due_date=None,
                    new_status=None):
        self.load_tasks()
        for task in self.task_list:
            if task.ID == task_id:
                if new_title is not None:
                    task.Title = new_title
                if new_description is not None:
                    task.Description = new_description
                if new_due_date is not None:
                    task.Due_Date = new_due_date
                if new_status is not None:
                    task.Status = new_status
                self.save_tasks()
                return True
        return False

    def get_task(self, task_id):
        self.load_tasks()
        for task in self.task_list:
            if task.ID == task_id:
                return task
        return None

    def sort_tasks(self, sort_by, reverse=False):
        self.load_tasks()
        if sort_by == "Status":
            self.task_list.sort(key=lambda x: x.__dict__[
                                sort_by].value, reverse=reverse)
        else:
            self.task_list.sort(key=lambda x: x.__dict__[
                                sort_by], reverse=reverse)
        self.save_tasks()
