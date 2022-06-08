import ipaddress
from unicon.core.errors import SubCommandFailure


class CheckOSPFConnectivityIOSXRCmd:
    def __init__(self, connected_device):
        self.device = connected_device

    def prepare_data(self) -> dict:
        # Find the ospf neighbor count for interface that has /30 subnet
        ospf_int_nbr = self.device.parse("show ospf interface brief")
        p2p_iface = ospf_int_nbr.q.contains(
            "\d+.\d+.\d+.\d+\/30", regex=True
        ).get_values("interfaces")
        nbr_regex = "|".join(p2p_iface)
        ospf_nbr_count = ospf_int_nbr.q.contains(nbr_regex, regex=True).get_values(
            "nbrs_count"
        )

        # Use different parser for "ospf_int" in IOS-XR.
        ospf_int = self.device.parse("show ospf interface")

        # Find ALL the local ospf interface ip address with /30 subnet
        local_ip_add = (
            ospf_int.q.contains("ip_address")
            .contains("\d+.\d+.\d+.\d+\/30", regex=True)
            .get_values("ip_address")
        )
        neigh_ip_add = []

        # Find ALL the local ospf interface name with /30 subnet
        local_ospf_iface = (
            ospf_int.q.contains("interfaces")
            .contains("\d+.\d+.\d+.\d+\/30", regex=True)
            .get_values("interfaces")
        )
        iface_desc_all = self.device.parse("show interfaces description")

        # Find ALL the local ospf interface physical (L1) status with /30 subnet
        ospf_iface_stat = []
        ospf_iface_desc = []
        for iface_regex in local_ospf_iface:
            iface_stat = iface_desc_all.q.contains(iface_regex, regex=True).get_values(
                "status"
            )
            iface_desc = iface_desc_all.q.contains(iface_regex, regex=True).get_values(
                "description"
            )
            ospf_iface_stat.extend(iface_stat)
            ospf_iface_desc.extend(iface_desc)

        # Find the ospf neighbor / peer ip address with /30 subnet and try to ping that address.
        for ip in local_ip_add:
            net4 = ipaddress.ip_network(
                ip, strict=False
            )  # "strict=False" paramater for disabling network address check for input, so the input doesn't have to be network address.
            for x in net4.hosts():
                if (str(x) + "/30") != ip:
                    neigh_ip_add.append(str(x))

        # Create the table for all the data provided above
        output = ""
        output += "Interface - Description <> Phy Status\n"
        output += "=====================================\n"
        for idx in range(len(local_ospf_iface)):
            output += (
                local_ospf_iface[idx]
                + " - "
                + ospf_iface_desc[idx]
                + " <> "
                + ospf_iface_stat[idx]
                + "\n"
            )

        output += (
            "\nInterface - Local ip address <> Neighbor ip address - Neighbor count\n"
        )
        output += (
            "====================================================================\n"
        )
        for idx in range(len(local_ospf_iface)):
            output += (
                local_ospf_iface[idx]
                + " - "
                + local_ip_add[idx]
                + " <> "
                + neigh_ip_add[idx]
                + "/30 - "
                + str(ospf_nbr_count[idx])
                + "\n"
            )

        # Start the ping test
        output += "\nPing Test using TOS 192\n"
        output += "=======================\n"
        for ipdestination in neigh_ip_add:
            output += ">> Ping to " + ipdestination
            try:
                output += (
                    self.device.execute(
                        "ping " + ipdestination + " repeat 100 type 192", timeout=15
                    )
                    + "\n\n"
                )
            except SubCommandFailure:
                # if ping fail or timeout occur then send break character to stop the ping and continue to ping the next ip
                output += "\n" + self.device.execute("\x03") + "\n\n"
                continue

        return {"check_result": output}

    def run(self) -> str:

        data = self.prepare_data()

        return data["check_result"]
