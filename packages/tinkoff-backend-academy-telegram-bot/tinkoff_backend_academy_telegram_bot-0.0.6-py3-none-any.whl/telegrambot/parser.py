from typing import Any, Dict, Union

from telegrambot.message import TelegramMessage

Response = Dict[str, Any]
Message = Dict[str, Any]


class TelegramParser:
    def __init__(self) -> None:
        pass

    def _parse_message(self, data: Response) -> Union[Message, None]:
        # assume only first message required
        if data.get("result") is None or len(data["result"]) <= 0:
            return None

        message = data["result"][0].get("message")

        if message is None:
            message = data["result"][0].get("edited_message")

        return message

    def parse_text(self, data: Response) -> Union[str, None]:
        message = self._parse_message(data)

        text = None

        if message is not None:
            text = message.get("text")

        return text

    def parse_user_id(self, data: Response) -> Union[str, None]:
        message = self._parse_message(data)

        user_id = None

        if message and message.get("from") and message["from"].get("id"):
            user_id = message["from"]["id"]

        return user_id

    def parse_update_id(self, data: Response) -> Union[int, None]:
        if (
            data.get("result") is None
            or len(data["result"]) <= 0
            or data["result"][0].get("update_id") is None
        ):
            return None

        return int(data["result"][0]["update_id"])

    def parse_telegram_message(
        self, data: Response
    ) -> Union[TelegramMessage, None]:
        text = self.parse_text(data)

        if text is None:
            return None

        [command, *args] = filter(
            lambda str: len(str) > 0, text.strip().split(" ")
        )
        return TelegramMessage(command, args)
