# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = batches_item_from_dict(json.loads(json_string))

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Name(Enum):
    BATCH = "Batch"


@dataclass
class Recipe:
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Recipe":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        return Recipe(name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class BatchesItemElement:
    id: Optional[str] = None
    name: Optional[Name] = None
    batch_no: Optional[int] = None
    status: Optional[str] = None
    brewer: Optional[str] = None
    brew_date: Optional[int] = None
    recipe: Optional[Recipe] = None

    @staticmethod
    def from_dict(obj: Any) -> "BatchesItemElement":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        name = from_union([Name, from_none], obj.get("name"))
        batch_no = from_union([from_int, from_none], obj.get("batchNo"))
        status = from_union([from_str, from_none], obj.get("status"))
        brewer = from_union([from_none, from_str], obj.get("brewer"))
        brew_date = from_union([from_int, from_none], obj.get("brewDate"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        return BatchesItemElement(id, name, batch_no, status, brewer, brew_date, recipe)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([lambda x: to_enum(Name, x), from_none], self.name)
        result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        result["status"] = from_union([from_str, from_none], self.status)
        result["brewer"] = from_union([from_none, from_str], self.brewer)
        result["brewDate"] = from_union([from_int, from_none], self.brew_date)
        result["recipe"] = from_union(
            [lambda x: to_class(Recipe, x), from_none], self.recipe
        )
        return result


def batches_item_from_dict(s: Any) -> List[BatchesItemElement]:
    return from_list(BatchesItemElement.from_dict, s)


def batches_item_to_dict(x: List[BatchesItemElement]) -> Any:
    return from_list(lambda x: to_class(BatchesItemElement, x), x)
