from enum import Enum
from app.cmds.base import ConnectedDeviceCmd
from app.cmds.test_cmd import TestCmd


class CmdOption(Enum):
    TEST = "test_cmd"


CMD_FACTORIES = {
    CmdOption.TEST: TestCmd,
}


def get_cmd(cmd_name: str, connected_device) -> ConnectedDeviceCmd:
    try:
        cmd = CMD_FACTORIES[cmd_name]
        return cmd(connected_device)
    except KeyError:
        print(f"Unknown cmd option: {cmd_name}")
        return ""
