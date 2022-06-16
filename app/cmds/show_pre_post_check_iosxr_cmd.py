class ShowPrePostCheckIOSXRCmd:
    def __init__(self, connected_device):
        self.device = connected_device

    def prepare_data(self) -> dict:

        command_file = "./templates/cmd/pre_post_check/iosxr.txt"
        with open(command_file, "r") as f:
            command_list = f.readlines()

        output = ""
        for command in command_list:
            output += "\n\n>>>>>>>> " + command + "\n"
            output += self.device.execute(command, error_pattern=[], timeout=300)

        return {"show_result": output}

    def run(self) -> str:

        data = self.prepare_data()

        return data["show_result"]
