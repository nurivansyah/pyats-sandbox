from enum import Enum
from app.cmds.base import ConnectedDeviceCmd
from app.cmds.test_cmd import TestCmd
from app.cmds.bp_ospf_auth_iosxe_cmd import BPOSPFAuthIOSXECmd
from app.cmds.bp_ospf_auth_iosxr_cmd import BPOSPFAuthIOSXRCmd
from app.cmds.show_pre_post_check_ios_cmd import ShowPrePostCheckIOSCmd
from app.cmds.show_pre_post_check_iosxe_cmd import ShowPrePostCheckIOSXECmd
from app.cmds.check_ospf_connectivity_iosxe_cmd import CheckOSPFConnectivityIOSXECmd
from app.cmds.check_ospf_connectivity_iosxr_cmd import CheckOSPFConnectivityIOSXRCmd


class CmdOption(Enum):
    TEST = "test_cmd"
    BP_OSPF_AUTH_IOSXE = "bp_ospf_auth_iosxe"
    BP_OSPF_AUTH_IOSXR = "bp_ospf_auth_iosxr"
    SHOW_PRE_POST_CHECK_IOS = "show_pre_post_check_ios"
    SHOW_PRE_POST_CHECK_IOSXE = "show_pre_post_check_iosxe"
    CHECK_OSPF_CONNECTIVITY_IOSXE = "check_ospf_connectivity_iosxe"
    CHECK_OSPF_CONNECTIVITY_IOSXR = "check_ospf_connectivity_iosxr"


CMD_FACTORIES = {
    CmdOption.TEST: TestCmd,
    CmdOption.BP_OSPF_AUTH_IOSXE: BPOSPFAuthIOSXECmd,
    CmdOption.BP_OSPF_AUTH_IOSXR: BPOSPFAuthIOSXRCmd,
    CmdOption.SHOW_PRE_POST_CHECK_IOS: ShowPrePostCheckIOSCmd,
    CmdOption.SHOW_PRE_POST_CHECK_IOSXE: ShowPrePostCheckIOSXECmd,
    CmdOption.CHECK_OSPF_CONNECTIVITY_IOSXE: CheckOSPFConnectivityIOSXECmd,
    CmdOption.CHECK_OSPF_CONNECTIVITY_IOSXR: CheckOSPFConnectivityIOSXRCmd,
}


def get_cmd(cmd_name: str, connected_device) -> ConnectedDeviceCmd:
    try:
        cmd = CMD_FACTORIES[cmd_name]
        return cmd(connected_device)
    except KeyError:
        print(f"Unknown cmd option: {cmd_name}")
        return ""
