from app.core import AppTestBed
from app.factories.task import select_task
from app.utils import get_device_list, ScriptExporter
import multiprocessing
from app.config import get_conf


def main():

    testbed_yaml = get_conf("TESTBED_YAML")
    export_dir = get_conf("EXPORT_DIR")
    conn_cli_proxy = get_conf("CONN_CLI_PROXY")

    ## init and load yaml testbed
    tb = AppTestBed(testbed_yaml)
    exporter = ScriptExporter(export_dir)
    task = select_task()

    ## get router list by input
    rtr_list = get_device_list()

    ## start task per device with parallel processing
    processes = [
        multiprocessing.Process(
            target=task.start, args=(tb, exporter, rtr, conn_cli_proxy)
        )
        for rtr in rtr_list
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("\n======== ALL TASK DONE ======== \n")


if __name__ == "__main__":
    main()
