from app.utils import get_template


class BPOSPFAuthIOSXECmd:
    def __init__(self, connected_device):
        self.device = connected_device
        template_file = "./templates/cmd/bp_ospf_auth_iosxe_template.j2"
        self.template = get_template(template_file)

    def prepare_data(self) -> dict:
        parsed_data = self.device.parse("show ip ospf interface brief")

        # ospf_id = parsed_data.q.contains("instance", regex=True).get_values("instance")
        ospf_int = parsed_data.q.contains("instance", regex=True).get_values(
            "interfaces"
        )
        ospf_nbrs_full = parsed_data.q.contains("interfaces", regex=True).get_values(
            "nbrs_full"
        )

        return {
            "hostname": self.device.name,
            "ospf_int": ospf_int,
            "ospf_nbrs_full": ospf_nbrs_full,
        }

    def run(self) -> str:

        data = self.prepare_data()

        script_string = self.template.render(
            hostname=data["hostname"],
            ospf_int=data["ospf_int"],
            ospf_nbrs_full=data["ospf_nbrs_full"],
        )

        return script_string
