from dataclasses import dataclass


@dataclass
class BotError:
    reason: str = ""

    def __str__(self) -> str:
        return f'[BotError: reason="{self.reason}"]'

    def __repr__(self) -> str:
        return self.__str__()
