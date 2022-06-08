import sys
from enum import Enum
from app.tasks.base import AppTask
from app.tasks.test_task import TestTask
from app.tasks.bp_ospf_auth_task import BPOSPFAuthTask
from app.tasks.show_pre_post_check_task import ShowPrePostCheckTask
from app.tasks.check_ospf_connectivity_task import CheckOSPFConnectivityTask


class TaskOption(Enum):
    TEST = "Test Task"
    BP_OSPF_AUTH = "BP OSPF Auth"
    SHOW_PRE_POST_CHECK = "Show Pre/Post Check"
    CHECK_OSPF_CONNECTIVITY = "Check OSPF Connectivity"


TASK_FACTORIES = {
    TaskOption.TEST: TestTask,
    TaskOption.BP_OSPF_AUTH: BPOSPFAuthTask,
    TaskOption.SHOW_PRE_POST_CHECK: ShowPrePostCheckTask,
    TaskOption.CHECK_OSPF_CONNECTIVITY: CheckOSPFConnectivityTask,
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
