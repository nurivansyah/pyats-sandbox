from typing import Protocol


class AppTask(Protocol):
    def start() -> None:
        """Reference to create task class"""
