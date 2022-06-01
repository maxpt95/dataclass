import random
import string
from typing import List
from dataclasses import dataclass, field


@dataclass
class Song:
    name: str
    artist: str
    has_video: bool = False
    featuring_artists: List[str] = field(default_factory=list)
    id: str = field(init=False)

    def __post_init__(self) -> None:
        self.id = f"{self.name} - {self.artist}"


if __name__ == "__main__":
    song = Song(name="Yo No Soy Celoso", artist="Bad Bunny", has_video=True)
    print(song.id)
