# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = batch_item_from_dict(json.loads(json_string))
import time
import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


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
        except Exception as e:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class TypeEnum(Enum):
    STATUS_CHANGED = "statusChanged"


@dataclass
class Note:
    note: Optional[str] = None
    status: Optional[str] = None
    timestamp: Optional[int] = None
    type: Optional[TypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> "Note":
        assert isinstance(obj, dict)
        note = from_union([from_str, from_none], obj.get("note"))
        status = from_union([from_str, from_none], obj.get("status"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        return Note(note, status, timestamp, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["note"] = from_union([from_str, from_none], self.note)
        result["status"] = from_union([from_str, from_none], self.status)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["type"] = from_union(
            [lambda x: to_enum(TypeEnum, x), from_none], self.type
        )
        return result


@dataclass
class Created:
    seconds: Optional[int] = None
    nanoseconds: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Created":
        assert isinstance(obj, dict)
        seconds = from_union([from_int, from_none], obj.get("_seconds"))
        nanoseconds = from_union([from_int, from_none], obj.get("_nanoseconds"))
        return Created(seconds, nanoseconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_seconds"] = from_union([from_int, from_none], self.seconds)
        result["_nanoseconds"] = from_union([from_int, from_none], self.nanoseconds)
        return result


@dataclass
class Step:
    ramp: Optional[int] = None
    pressure: Optional[float] = None
    display_pressure: Optional[int] = None
    display_step_temp: Optional[int] = None
    type: Optional[str] = None
    actual_time: Optional[int] = None
    step_temp: Optional[float] = None
    name: Optional[str] = None
    step_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "Step":
        assert isinstance(obj, dict)
        ramp = from_union([from_int, from_none], obj.get("ramp"))
        pressure = from_union([from_float, from_none], obj.get("pressure"))
        display_pressure = from_union([from_int, from_none], obj.get("displayPressure"))
        display_step_temp = from_union([from_int, from_none], obj.get("displayStepTemp"))
        type = from_union([from_str, from_none], obj.get("type"))
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        step_temp = from_union([from_float, from_none], obj.get("stepTemp"))
        name = from_union([from_str, from_none], obj.get("name"))
        step_time = from_union([from_int, from_none], obj.get("stepTime"))
        return Step(
            ramp,
            pressure,
            display_pressure,
            display_step_temp,
            type,
            actual_time,
            step_temp,
            name,
            step_time,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["ramp"] = from_union([from_int, from_none], self.ramp)
        result["pressure"] = from_union([from_float, from_none], self.pressure)
        result["displayPressure"] = from_union([from_int, from_none], self.display_pressure)
        result["displayStepTemp"] = from_union(
            [from_int, from_none], self.display_step_temp
        )
        result["type"] = from_union([from_str, from_none], self.type)
        result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        result["stepTemp"] = from_union([to_float, from_none], self.step_temp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["stepTime"] = from_union([from_int, from_none], self.step_time)
        return result


@dataclass
class FermentationStep:
    timestamp: Optional[Created] = None
    rev: Optional[str] = None
    id: Optional[str] = None
    version: Optional[str] = None
    created: Optional[Created] = None
    name: Optional[str] = None
    steps: Optional[List[Step]] = None
    timestamp_ms: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "FermentationStep":
        assert isinstance(obj, dict)
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        id = from_union([from_none, from_str], obj.get("_id"))
        version = from_union([from_str, from_none], obj.get("_version"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        name = from_union([from_str, from_none], obj.get("name"))
        steps = from_union(
            [lambda x: from_list(Step.from_dict, x), from_none], obj.get("steps")
        )
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        return FermentationStep(
            timestamp, rev, id, version, created, name, steps, timestamp_ms
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["_timestamp"] = from_union(
            [lambda x: to_class(Created, x), from_none], self.timestamp
        )
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_id"] = from_union([from_none, from_str], self.id)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["_created"] = from_union(
            [lambda x: to_class(Created, x), from_none], self.created
        )
        result["name"] = from_union([from_str, from_none], self.name)
        result["steps"] = from_union(
            [lambda x: from_list(lambda x: to_class(Step, x), x), from_none], self.steps
        )
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        return result


@dataclass
class Recipe:
    name: Optional[str] = None
    fermentation: Optional[FermentationStep] = None

    @staticmethod
    def from_dict(obj: Any) -> "Recipe":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        fermentation = from_union(
            [FermentationStep.from_dict, from_none], obj.get("fermentation")
        )
        return Recipe(name, fermentation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["fermentation"] = from_union(
            [lambda x: to_class(FermentationStep, x), from_none], self.fermentation
        )
        return result


@dataclass
class Reading:
    temp: Optional[int] = None
    sg: Optional[float] = None
    comment: Optional[str] = None
    time: Optional[int] = None
    id: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Reading":
        assert isinstance(obj, dict)
        temp = from_union([from_int, from_none], obj.get("temp"))
        sg = from_union([from_float, from_none], obj.get("sg"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        time = from_union([from_int, from_none], obj.get("time"))
        id = from_union([from_str, from_none], obj.get("_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Reading(temp, sg, comment, time, id, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["temp"] = from_union([from_int, from_none], self.temp)
        result["sg"] = from_union([to_float, from_none], self.sg)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["time"] = from_union([from_int, from_none], self.time)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["type"] = from_union([from_str, from_none], self.type)

        return result


@dataclass
class BatchItem:
    id: Optional[str] = None
    name: Optional[str] = None
    batch_no: Optional[int] = None
    status: Optional[str] = None
    brewer: Optional[str] = None
    brew_date: Optional[int] = None
    recipe: Optional[Recipe] = None
    notes: Optional[List[Note]] = None
    readings: Optional[List[Reading]] = None

    @staticmethod
    def from_dict(obj: Any) -> "BatchItem":
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        batch_no = from_union([from_int, from_none], obj.get("batchNo"))
        status = from_union([from_str, from_none], obj.get("status"))
        brewer = from_union([from_none, from_str], obj.get("brewer"))
        brew_date = from_union([from_int, from_none], obj.get("brewDate"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        notes = from_union(
            [lambda x: from_list(Note.from_dict, x), from_none], obj.get("notes")
        )
        return BatchItem(id, name, batch_no, status, brewer, brew_date, recipe, notes, None)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        result["status"] = from_union([from_str, from_none], self.status)
        result["brewer"] = from_union([from_none, from_str], self.brewer)
        result["brewDate"] = from_union([from_int, from_none], self.brew_date)
        result["recipe"] = from_union(
            [lambda x: to_class(Recipe, x), from_none], self.recipe
        )
        result["notes"] = from_union(
            [lambda x: from_list(lambda x: to_class(Note, x), x), from_none], self.notes
        )
        result["readings"] = from_union(
            [lambda x: from_list(lambda x: to_class(Reading, x), x), from_none], self.readings
        )
        return result

    def to_attribute_entry(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], from_union(
            [lambda x: to_class(Recipe, x), from_none], self.recipe
        )["name"])
        result["brewDate"] = datetime.datetime.fromtimestamp(self.brew_date / 1000)
        result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        fermenting_start = self.recipe.fermentation.steps[0].actual_time / 1000
        result["fermentingStart"] = datetime.datetime.fromtimestamp(fermenting_start)

        if self.readings is not None and len(self.readings) > 0:
            result["current_temperature"] = self.readings[0].temp
        else:
            result["current_temperature"] = None

        days_to_ferment = 0
        for (index, step) in enumerate[FermentationStep](
                self.recipe.fermentation.steps
        ):
            days_to_ferment += step.step_time

        current_time = time.time()
        finish_time = fermenting_start + (days_to_ferment * 86400)
        result["fermentingEnd"] = datetime.datetime.fromtimestamp(finish_time)
        result["fermentingLeft"] = (finish_time - current_time) / 86400
        result["status"] = from_union([from_str, from_none], self.status)
        result["recipe"] = from_union(
            [lambda x: to_class(Recipe, x), from_none], self.recipe
        )
        result["notes"] = from_union(
            [lambda x: from_list(lambda x: to_class(Note, x), x), from_none], self.notes
        )
        result["readings"] = from_union(
            [lambda x: from_list(lambda x: to_class(Reading, x), x), from_none], self.readings
        )
        return result


def batch_item_from_dict(s: Any) -> BatchItem:
    return BatchItem.from_dict(s)


def readings_item_from_dict(s: Any) -> List[Reading]:
    return from_list(Reading.from_dict, s)
