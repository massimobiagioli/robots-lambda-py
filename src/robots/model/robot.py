from dataclasses import dataclass


@dataclass(frozen=True)
class Robot:
    id: str
    name: str