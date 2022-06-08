from genie.testbed import load
from unicon.core.errors import ConnectionError
import sys
import yaml
from app.utils import get_custom_dialog
from app.factories.cmd import get_cmd


class AppTestBed:
    def __init__(self, device_yaml: str):
        self.device_dict = self.parse_yaml_to_dict(device_yaml)

    def parse_yaml_to_dict(self, device_yaml):
        with open(device_yaml, "r") as f:
            try:
                parsed_yaml = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                sys.exit(exc)
        return parsed_yaml

    def load_device(self, rtr: str, conn_cli_proxy: str = ""):

        filtered_device = {"devices": {}}

        try:
            filtered_device["devices"][rtr] = self.device_dict["devices"][rtr]
            if conn_cli_proxy != "":
                filtered_device["devices"][conn_cli_proxy] = self.device_dict[
                    "devices"
                ][conn_cli_proxy]
        except KeyError:
            sys.exit("Not on YAML : " + rtr)

        tb = load(filtered_device)
        return tb.devices[rtr]

    def get_device(self, rtr: str, conn_cli_proxy: str = ""):
        tb_device = self.load_device(rtr, conn_cli_proxy)
        return AppDevice(tb_device)


class AppDevice:
    def __init__(self, tb_device):
        self.device = tb_device

    def get_attr(self, attr_name):
        return getattr(self.device, attr_name)

    # def get_object(self):
    #     return self.device

    def connect(self):
        try:
            self.device.connect(
                connect_reply=get_custom_dialog(),
                log_stdout=False,
                connection_timeout=480,
                learn_hostname=True,
            )  # Change log_stdout value to True to display all the "show ...." proccess on linux terminal
        except ConnectionError:
            sys.exit("Connection Error : " + self.device.name)

    def disconnect(self):
        self.device.disconnect()

    def run_cmd(self, cmd_name):
        cmd = get_cmd(cmd_name, self.device)
        return cmd.run()
