#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

__fork_name__ = "PyroFork"
__version__ = "2.3.67"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>"

from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums  # pylint: disable=wrong-import-position
from .client import Client  # pylint: disable=wrong-import-position
from .sync import idle, compose  # pylint: disable=wrong-import-position

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")

__all__ = [
    "Client",
    "idle",
    "compose",
    "crypto_executor",
    "StopTransmission",
    "StopPropagation",
    "ContinuePropagation",
    "raw",
    "types",
    "filters",
    "handlers",
    "emoji",
    "enums",
]
