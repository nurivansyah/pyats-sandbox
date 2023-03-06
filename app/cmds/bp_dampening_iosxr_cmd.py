class BPDampeningIOSXRCmd:
    def __init__(self, connected_device):
        self.device = connected_device

    def prepare_data(self) -> dict:
        parsed_data = self.device.parse("show interfaces description")

        configured_dampening = self.device.execute(
            "show running-config formal | include dampening",
            error_pattern=[],
            timeout=300,
        )

        # if need to filter interface status
        # filtered = parsed_data.q.contains_key_value("status", "admin-down").get_values("interfaces")

        filter_string = [".", "BV", "Lo", "Nu", "Mg", "PT"]
        unconfigured_dampening_interfaces = []
        for interface_name in parsed_data["interfaces"]:
            if not any(word in interface_name for word in filter_string):
                if not interface_name in configured_dampening:
                    unconfigured_dampening_interfaces.append(interface_name)

        return {
            "hostname": self.device.name,
            "unconfigured_dampening_interfaces": unconfigured_dampening_interfaces,
        }

    def run(self) -> str:
        data = self.prepare_data()

        bp_dampening_config = ""
        for interface_name in data["unconfigured_dampening_interfaces"]:
            bp_dampening_config += "interface " + interface_name + " dampening\n"

        return bp_dampening_config
