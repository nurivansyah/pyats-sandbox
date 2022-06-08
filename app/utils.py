import datetime
from jinja2 import Template
from unicon.eal.dialogs import Statement, Dialog


class ScriptExporter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir if output_dir[-1] == "/" else output_dir + "/"

    def to_txt(self, command_string: str, file_name: str = None):
        output_file_name = file_name if file_name is not None else get_timestamp()
        output_file = f"{self.output_dir}{output_file_name}.txt"
        with open(output_file, "w+") as f:
            f.write(command_string)


def get_device_list() -> list:
    print("\n======================")
    print("Enter the hostname (followed by enter): ")
    rtr_list = []
    while True:
        hostname = input()
        if hostname:
            rtr_list.append(hostname)
        else:
            return rtr_list


def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def get_current_date():
    return datetime.datetime.now().strftime("%Y%m%d")


def get_current_time():
    return datetime.datetime.now().strftime("%H%M%S")


def get_template(template_file: str):
    with open(template_file) as f:
        return Template(f.read(), keep_trailing_newline=True)


def get_custom_dialog(self):
    return Dialog(
        [
            Statement(
                pattern=r"Permission denied",
                action=None,
                args=None,
                loop_continue=True,
                continue_timer=False,
            )
        ]
    )
