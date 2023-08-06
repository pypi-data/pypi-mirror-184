from enum import Enum
from typing import Any, Callable, Dict, List, Union

from requests import ConnectionError, JSONDecodeError
import requests

from error import BotError
from message import TelegramMessage
from parser import Response, TelegramParser


_RegistryCallback = Callable[[Response, TelegramMessage], Any]
_ErrorCallback = Callable[[Response, BotError], Any]


class _ResponseState(Enum):
    PENDING = 1
    SUCCESS = 2
    ERROR = 3


class TelegramBot:
    def __init__(self, api_url: str) -> None:
        self._api_url = api_url  # assuming token is embedded
        self._started_polling = False

        self._parser = TelegramParser()

        self._registry: Dict[str, List[_RegistryCallback]] = {}
        self._error_callbacks: List[_ErrorCallback] = []

        self._request_params: Dict[str, Any] = {
            "offset": None,
            "limit": 1,
            "timeout": 3,
        }

    # decorator
    def register(self, commands: List[str]) -> Callable:
        if self._started_polling:
            raise RuntimeError(
                "Registering callback allowed only before calling start()"
            )

        def wrapper_register(callback: _RegistryCallback) -> None:
            for command in commands:
                if command not in self._registry:
                    self._registry[command] = []

                self._registry[command].append(callback)

        return wrapper_register

    # decorator
    def error(self) -> Callable:
        if self._started_polling:
            raise RuntimeError(
                "Registering error handler allowed only before calling start()"
            )

        def wrapper_error(callback: _ErrorCallback) -> None:
            self._error_callbacks.append(callback)

        return wrapper_error

    def _acquire_response_state(self, data: Dict) -> _ResponseState:
        if data["ok"] is False:
            return _ResponseState.ERROR

        if len(data["result"]) <= 0:
            return _ResponseState.PENDING

        return _ResponseState.SUCCESS

    def _handle_error(self, data: Response, err: BotError) -> None:
        for error_handler in self._error_callbacks:
            error_handler(data, err)

    def _handle_success(self, data: Response) -> None:
        message = self._parser.parse_telegram_message(data)

        if message is None:
            return self._handle_error(
                data,
                BotError(
                    "No command provided. Only text messages are supported"
                ),
            )

        if message.command not in self._registry:
            return self._handle_error(
                data, BotError(f'Command "{message.command}" is not supported')
            )

        for handler in self._registry[message.command]:
            handler(data, message)

    def _update_params_offset(self, data: Response) -> None:
        if self._acquire_response_state(data) is not _ResponseState.SUCCESS:
            return

        update_id = TelegramParser().parse_update_id(data)

        if update_id is None:
            return

        self._request_params["offset"] = update_id + 1

    def send(
        self, *, text: str, chat_id: str, parse_mode: Union[str, None] = None
    ) -> Union[BotError, None]:
        request_params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
        }

        data = requests.get(
            f"{self._api_url}/sendMessage", request_params
        ).json()

        if data["ok"] is True:
            return None

        return BotError(data["description"])

    def start(self) -> None:
        self._started_polling = True

        while True:
            try:
                data = requests.get(
                    f"{self._api_url}/getUpdates", self._request_params
                ).json()

                state: _ResponseState = self._acquire_response_state(data)

                if state == _ResponseState.SUCCESS:
                    self._handle_success(data)
                elif state == _ResponseState.ERROR:
                    self._handle_error(data, BotError(data["description"]))

                self._update_params_offset(data)

            except (ConnectionError, JSONDecodeError) as err:
                print(
                    f"'ConnectionError' or 'JSONDecodeError' error occured: {err}"
                )
