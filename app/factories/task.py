import sys
from enum import Enum
from app.tasks.base import AppTask
from app.tasks.test_task import TestTask


class TaskOption(Enum):
    TEST = "Test Task"


TASK_FACTORIES = {
    TaskOption.TEST: TestTask,
}


def get_task(task_name: str) -> AppTask:
    try:
        task = TASK_FACTORIES[task_name]
        return task
    except KeyError:
        sys.exit("Unknown task option : " + task_name)


def select_task() -> AppTask:
    print("\nNetwork Automation Sandbox")
    print("======================")
    print("Enter the Task Number you want to run (followed by enter): ")

    task_list = []
    index = 1
    for task in TASK_FACTORIES:
        task_list.append(task)
        print(f"- {task.value} -> {index}")
        index += 1

    try:
        selected_task_number = int(input())
        if selected_task_number > 0:
            selected_index = selected_task_number - 1
            selected_task_name = task_list[selected_index]
            return get_task(selected_task_name)
    except Exception:
        print("Invalid input")

    sys.exit("Please select correct task number")
