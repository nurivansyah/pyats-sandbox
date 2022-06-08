from app.core import AppTestBed
from app.utils import get_current_time, get_current_date, ScriptExporter
from app.factories.cmd import CmdOption


class CheckOSPFConnectivityTask:
    def start(
        tb: AppTestBed,
        export: ScriptExporter,
        rtr: str,
        conn_cli_proxy: str = "",
    ):
        device = tb.get_device(rtr, conn_cli_proxy)

        print(
            "Task Starts : "
            + device.get_attr("name")
            + " - starts at: "
            + get_current_time()
        )
        device.connect()

        result = device.run_cmd(
            CmdOption("check_ospf_connectivity_" + device.get_attr("os"))
        )

        filename = (
            str(get_current_date())
            + "_"
            + device.get_attr("name")
            + "_ospf_connectivity_"
            + str(get_current_time())
        )
        export.to_txt(result, filename)

        device.disconnect()
        print(
            "Task Done   : "
            + device.get_attr("name")
            + " - ends at: "
            + get_current_time()
        )
