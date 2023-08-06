from typing import List


class TelegramMessage:
    command: str = ""
    args: List[str] = []

    def __init__(self, command: str, args: List[str]) -> None:
        self.command = command
        self.args = args

    def __str__(self) -> str:
        return f"[Message: command='{self.command}' args={self.args}]"

    def __repr__(self) -> str:
        return self.__str__()
