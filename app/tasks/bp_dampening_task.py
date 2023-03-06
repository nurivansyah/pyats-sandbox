from app.core import AppTestBed
from app.utils import get_current_time, get_current_date, ScriptExporter
from app.factories.cmd import CmdOption


class BPDampeningTask:
    def start(
        tb: AppTestBed,
        export: ScriptExporter,
        rtr: str,
        conn_cli_proxy: str = "",
    ):
        # check if rtr in yaml
        device = tb.get_device(rtr, conn_cli_proxy)

        ## connect to device
        print(
            "Task Starts : "
            + device.get_attr("name")
            + " - starts at: "
            + get_current_time()
        )
        device.connect()

        ## run cmd to generate script
        result = device.run_cmd(CmdOption.BP_DAMPENING_IOSXR)

        ## write config script
        filename = (
            str(get_current_date())
            + "_"
            + device.get_attr("name")
            + "_Dampening_"
            + str(get_current_time())
        )
        export.to_txt(result, filename)

        ## disconnect device
        device.disconnect()
        print(
            "Task Done   : "
            + device.get_attr("name")
            + " - ends at: "
            + get_current_time()
        )
