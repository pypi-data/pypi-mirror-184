import typing
import dataclasses

import requests

from rsapi import USER_AGENT

API_URL = "https://prices.runescape.wiki"
MAPPING_PATH = "api/v1/osrs/mapping"


@dataclasses.dataclass(frozen=True)
class Item:
    examine: str
    id: int
    members: bool
    value: int
    icon: str
    name: str
    lowalch: typing.Optional[int] = dataclasses.field(default=None)
    highalch: typing.Optional[int] = dataclasses.field(default=None)
    limit: typing.Optional[int] = dataclasses.field(default=None)


def items() -> typing.Iterable[Item]:
    return [
        Item(**i) for i in requests.get(
            f"{API_URL}/{MAPPING_PATH}",
            headers={
                "User-Agent": USER_AGENT,
            }
        ).json()
    ]
