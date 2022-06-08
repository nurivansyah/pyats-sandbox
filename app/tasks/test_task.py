from app.core import AppTestBed
from app.utils import get_current_time, get_current_date, ScriptExporter
from app.factories.cmd import CmdOption, get_cmd


class TestTask:
    def start(
        tb: AppTestBed,
        export: ScriptExporter,
        rtr: str,
        conn_cli_proxy: str = "",
    ):
        # check if rtr in yaml
        # device = tb.load_device(rtr, conn_cli_proxy)
        tb_device = tb.get_device(rtr, conn_cli_proxy)

        ## connect to device
        print(
            "Task Starts : "
            + tb_device.get_attr("name")
            + " - starts at: "
            + get_current_time()
        )
        # device.connect(connect_reply=get_custom_dialog(), log_stdout=False)
        # tb_device.connect()

        ## run cmd to generate script
        # cmd = get_cmd("test_cmd", device)
        # result = cmd.run()
        result = tb_device.run_cmd(CmdOption.TEST)

        ## write config script
        filename = (
            str(get_current_date())
            + "_"
            + tb_device.get_attr("name")
            + "_Test_"
            + str(get_current_time())
        )
        export.to_txt(result, filename)

        ## disconnect device
        # device.disconnect()
        # tb_device.disconnect()
        print(
            "Task Done   : "
            + tb_device.get_attr("name")
            + " - ends at: "
            + get_current_time()
        )
