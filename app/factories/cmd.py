from enum import Enum
from app.cmds.base import ConnectedDeviceCmd
from app.cmds.test_cmd import TestCmd
from app.cmds.bp_ospf_auth_iosxe_cmd import BPOSPFAuthIOSXECmd
from app.cmds.bp_ospf_auth_iosxr_cmd import BPOSPFAuthIOSXRCmd


class CmdOption(Enum):
    TEST = "test_cmd"
    BP_OSPF_AUTH_IOSXE = "bp_ospf_auth_iosxe"
    BP_OSPF_AUTH_IOSXR = "bp_ospf_auth_iosxr"


CMD_FACTORIES = {
    CmdOption.TEST: TestCmd,
    CmdOption.BP_OSPF_AUTH_IOSXE: BPOSPFAuthIOSXECmd,
    CmdOption.BP_OSPF_AUTH_IOSXR: BPOSPFAuthIOSXRCmd,
}


def get_cmd(cmd_name: str, connected_device) -> ConnectedDeviceCmd:
    try:
        cmd = CMD_FACTORIES[cmd_name]
        return cmd(connected_device)
    except KeyError:
        print(f"Unknown cmd option: {cmd_name}")
        return ""
