import random
import string
from typing import List
from dataclasses import dataclass, field


@dataclass
class Song:
    name: str
    artist: str
    has_video: bool = False
    # default_factory lets you assign attribute with the result of a function
    featuring_artists: List[str] = field(default_factory=list)
    # you can assign private attributes
    _id: str = field(init=False)

    def __post_init__(self) -> None:
        self._id = f"{self.name} - {self.artist}"

    @property
    def id(self) -> str:
        return self._id


if __name__ == "__main__":
    song = Song(name="Yo No Soy Celoso", artist="Bad Bunny", has_video=True)
    print(song.id)
