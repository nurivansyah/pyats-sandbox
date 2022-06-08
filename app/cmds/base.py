from typing import Protocol


class ConnectedDeviceCmd(Protocol):
    def prepare_data(self) -> dict:
        """Collect/Prepare data from connected device and return into dictionary data"""

    def run(self) -> str:
        """Run the cmd and return result in string format"""
