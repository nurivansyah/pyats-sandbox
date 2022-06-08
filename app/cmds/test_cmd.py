from app.utils import get_template


class TestCmd:
    def __init__(self, connected_device):
        self.device = connected_device
        template_file = "./templates/cmd/test.j2"
        self.template = get_template(template_file)

    def prepare_data(self) -> dict:
        """Collect/Prepare data from connected device and return into dictionary data"""
        return {"hostname": self.device.name, "os": self.device.os}

    def run(self) -> str:
        """Run the cmd and return result in string format"""
        data = self.prepare_data()

        script_string = self.template.render(
            hostname=data["hostname"], platform=data["os"]
        )

        return script_string
