from .reading_item import Reading
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
import time
import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast
MS_IN_DAY = 86400000

T = TypeVar("T")


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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Note:
    note: Optional[str]
    type: Optional[str]
    timestamp: Optional[int]
    status: Optional[str]

    def __init__(self, note: Optional[str], type: Optional[str], timestamp: Optional[int], status: Optional[str]) -> None:
        self.note = note
        self.type = type
        self.timestamp = timestamp
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'Note':
        assert isinstance(obj, dict)
        note = from_union([from_str, from_none], obj.get("note"))
        type = from_union([from_str, from_none], obj.get("type"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        status = from_union([from_str, from_none], obj.get("status"))
        return Note(note, type, timestamp, status)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.note is not None:
            result["note"] = from_union([from_str, from_none], self.note)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.timestamp is not None:
            result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        return result


class Created:
    seconds: Optional[int]
    nanoseconds: Optional[int]

    def __init__(self, seconds: Optional[int], nanoseconds: Optional[int]) -> None:
        self.seconds = seconds
        self.nanoseconds = nanoseconds

    @staticmethod
    def from_dict(obj: Any) -> 'Created':
        assert isinstance(obj, dict)
        seconds = from_union([from_int, from_none], obj.get("_seconds"))
        nanoseconds = from_union([from_int, from_none], obj.get("_nanoseconds"))
        return Created(seconds, nanoseconds)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.seconds is not None:
            result["_seconds"] = from_union([from_int, from_none], self.seconds)
        if self.nanoseconds is not None:
            result["_nanoseconds"] = from_union([from_int, from_none], self.nanoseconds)
        return result


class Step:
    actual_time: Optional[int]
    step_temp: Optional[float]
    display_pressure: None
    ramp: None
    name: Optional[str]
    pressure: None
    display_step_temp: Optional[int]
    step_time: Optional[float]
    type: Optional[str]

    def __init__(self, actual_time: Optional[int], step_temp: Optional[float], display_pressure: None, ramp: None, name: Optional[str], pressure: None, display_step_temp: Optional[int], step_time: Optional[float], type: Optional[str]) -> None:
        self.actual_time = actual_time
        self.step_temp = step_temp
        self.display_pressure = display_pressure
        self.ramp = ramp
        self.name = name
        self.pressure = pressure
        self.display_step_temp = display_step_temp
        self.step_time = step_time
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        assert isinstance(obj, dict)
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        step_temp = from_union([from_float, from_none], obj.get("stepTemp"))
        display_pressure = from_none(obj.get("displayPressure"))
        ramp = from_none(obj.get("ramp"))
        name = from_union([from_str, from_none], obj.get("name"))
        pressure = from_none(obj.get("pressure"))
        display_step_temp = from_union([from_int, from_none], obj.get("displayStepTemp"))
        step_time = from_union([from_float, from_none], obj.get("stepTime"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Step(actual_time, step_temp, display_pressure, ramp, name, pressure, display_step_temp, step_time, type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.actual_time is not None:
            result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        if self.step_temp is not None:
            result["stepTemp"] = from_union([to_float, from_none], self.step_temp)
        if self.display_pressure is not None:
            result["displayPressure"] = from_none(self.display_pressure)
        if self.ramp is not None:
            result["ramp"] = from_none(self.ramp)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.pressure is not None:
            result["pressure"] = from_none(self.pressure)
        if self.display_step_temp is not None:
            result["displayStepTemp"] = from_union([from_int, from_none], self.display_step_temp)
        if self.step_time is not None:
            result["stepTime"] = from_union([to_float, from_none], self.step_time)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        return result


class Fermentation:
    hidden: Optional[bool]
    created: Optional[Created]
    rev: Optional[str]
    name: Optional[str]
    timestamp_ms: Optional[int]
    id: Optional[str]
    timestamp: Optional[Created]
    steps: Optional[List[Step]]
    version: Optional[str]

    def __init__(self, hidden: Optional[bool], created: Optional[Created], rev: Optional[str], name: Optional[str], timestamp_ms: Optional[int], id: Optional[str], timestamp: Optional[Created], steps: Optional[List[Step]], version: Optional[str]) -> None:
        self.hidden = hidden
        self.created = created
        self.rev = rev
        self.name = name
        self.timestamp_ms = timestamp_ms
        self.id = id
        self.timestamp = timestamp
        self.steps = steps
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentation':
        assert isinstance(obj, dict)
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        name = from_union([from_str, from_none], obj.get("name"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        id = from_union([from_none, from_str], obj.get("_id"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        steps = from_union([lambda x: from_list(Step.from_dict, x), from_none], obj.get("steps"))
        version = from_union([from_str, from_none], obj.get("_version"))
        return Fermentation(hidden, created, rev, name, timestamp_ms, id, timestamp, steps, version)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.hidden is not None:
            result["hidden"] = from_union([from_bool, from_none], self.hidden)
        if self.created is not None:
            result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        if self.rev is not None:
            result["_rev"] = from_union([from_str, from_none], self.rev)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.timestamp_ms is not None:
            result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        if self.id is not None:
            result["_id"] = from_union([from_none, from_str], self.id)
        if self.timestamp is not None:
            result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        if self.steps is not None:
            result["steps"] = from_union([lambda x: from_list(lambda x: to_class(Step, x), x), from_none], self.steps)
        if self.version is not None:
            result["_version"] = from_union([from_str, from_none], self.version)
        return result


class Recipe:
    name: Optional[str]
    fermentation: Optional[Fermentation]

    def __init__(self, name: Optional[str], fermentation: Optional[Fermentation]) -> None:
        self.name = name
        self.fermentation = fermentation

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        fermentation = from_union([Fermentation.from_dict, from_none], obj.get("fermentation"))
        return Recipe(name, fermentation)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.fermentation is not None:
            result["fermentation"] = from_union([lambda x: to_class(Fermentation, x), from_none], self.fermentation)
        return result


class BatchItem:
    id: Optional[str]
    name: Optional[str]
    batch_no: Optional[int]
    status: Optional[str]
    brewer: Optional[str]
    brew_date: Optional[int]
    recipe: Optional[Recipe]
    notes: Optional[List[Note]]
    measured_og: Optional[float]
    #Add the readings to fermentingBatch with a fake property
    readings: Optional[List[Reading]]

    def __init__(self, id: Optional[str], name: Optional[str], batch_no: Optional[int], status: Optional[str], brewer: Optional[str], brew_date: Optional[int], recipe: Optional[Recipe], notes: Optional[List[Note]], measured_og: Optional[float]) -> None:
        self.id = id
        self.name = name
        self.batch_no = batch_no
        self.status = status
        self.brewer = brewer
        self.brew_date = brew_date
        self.recipe = recipe
        self.notes = notes
        self.measured_og = measured_og

    @staticmethod
    def from_dict(obj: Any) -> 'BatchItem':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        batch_no = from_union([from_int, from_none], obj.get("batchNo"))
        status = from_union([from_str, from_none], obj.get("status"))
        brewer = from_union([from_none, from_str], obj.get("brewer"))
        brew_date = from_union([from_int, from_none], obj.get("brewDate"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        notes = from_union([lambda x: from_list(Note.from_dict, x), from_none], obj.get("notes"))
        measured_og = from_union([from_float, from_none], obj.get("measuredOg"))
        return BatchItem(id, name, batch_no, status, brewer, brew_date, recipe, notes, measured_og)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["_id"] = from_union([from_str, from_none], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.batch_no is not None:
            result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.brewer is not None:
            result["brewer"] = from_union([from_none, from_str], self.brewer)
        if self.brew_date is not None:
            result["brewDate"] = from_union([from_int, from_none], self.brew_date)
        if self.recipe is not None:
            result["recipe"] = from_union([lambda x: to_class(Recipe, x), from_none], self.recipe)
        if self.notes is not None:
            result["notes"] = from_union([lambda x: from_list(lambda x: to_class(Note, x), x), from_none], self.notes)
        if self.measured_og is not None:
            result["measuredOg"] = from_union([to_float, from_none], self.measured_og)
        return result

    def to_attribute_entry_hassio(self) -> dict:
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

        result["target_temperature"] = None
        current_time = time.time()
        days_to_ferment = 0
        for (index, step) in enumerate[Step](
                self.recipe.fermentation.steps
        ):
            days_to_ferment += step.step_time
            step_start_datetime = step.actual_time / 1000
            step_end_datetime = (step.actual_time + step.step_time * MS_IN_DAY) / 1000
            if step_start_datetime < current_time < step_end_datetime:
                result["target_temperature"] = from_union([from_float, from_none], step.step_temp)

        finish_time = fermenting_start + (days_to_ferment * 86400)
        result["fermentingEnd"] = datetime.datetime.fromtimestamp(finish_time)
        result["fermentingLeft"] = (finish_time - current_time) / 86400
        result["status"] = from_union([from_str, from_none], self.status)
        result["measuredOg"] = from_union([from_float, from_none], self.measured_og)
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


def batch_item_to_dict(x: BatchItem) -> Any:
    return to_class(BatchItem, x)
