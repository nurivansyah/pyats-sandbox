import os
from dotenv import load_dotenv

load_dotenv()

APP_CONFIG = {
    "TESTBED_YAML": os.getenv("TESTBED_YAML", {}),
    "EXPORT_DIR": os.getenv("EXPORT_DIR", "./export"),
    "CONN_CLI_PROXY": os.getenv("CONN_CLI_PROXY", ""),
}


def get_conf(conf_name: str):
    try:
        config = APP_CONFIG[conf_name]
        return config
    except KeyError:
        return ""
