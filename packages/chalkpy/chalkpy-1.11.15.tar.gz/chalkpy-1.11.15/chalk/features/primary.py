from typing import TypeVar

T = TypeVar("T")

from typing_extensions import Annotated


class PrimaryMeta(type):
    def __getitem__(self, item: T) -> Annotated[T, "primary"]:
        return Annotated[item, "__chalk_primary__"]


Primary = PrimaryMeta("Primary", (object,), {})
