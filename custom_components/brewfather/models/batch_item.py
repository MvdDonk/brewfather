from .reading_item import Reading
from typing import Optional, Any, List, TypeVar, Callable, Type, cast
import time
import datetime
import logging
from ..const import (
    MS_IN_DAY
)

_LOGGER = logging.getLogger(__name__)
T = TypeVar("T")


def parse_field(obj: dict, field_name: str, parser: Callable, class_name: str, errors: list) -> Any:
    """Helper to parse a field with error handling and logging."""
    try:
        return parser(obj.get(field_name))
    except Exception as e:
        errors.append(f"{field_name}: {e}")
        _LOGGER.warning("Failed to parse %s.%s: %s", class_name, field_name, e)
        return None


def raise_if_errors(errors: list, class_name: str) -> None:
    """Raise ValueError if errors list is not empty."""
    if errors:
        error_msg = f"Failed to parse {class_name} fields: {', '.join(errors)}"
        _LOGGER.error(error_msg)
        raise ValueError(error_msg)


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
        except Exception:
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
        errors = []
        
        note = parse_field(obj, "note", lambda x: from_union([from_str, from_none], x), "Note", errors)
        type = parse_field(obj, "type", lambda x: from_union([from_str, from_none], x), "Note", errors)
        timestamp = parse_field(obj, "timestamp", lambda x: from_union([from_int, from_none], x), "Note", errors)
        status = parse_field(obj, "status", lambda x: from_union([from_str, from_none], x), "Note", errors)
        
        raise_if_errors(errors, "Note")
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


class Step:
    actual_time: Optional[int]
    step_temp: Optional[float]
    ramp: Optional[float]
    step_time: Optional[float]

    def __init__(self, actual_time: Optional[int], step_temp: Optional[float], ramp: Optional[float], step_time: Optional[float]) -> None:
        self.actual_time = actual_time
        self.step_temp = step_temp
        self.ramp = ramp
        self.step_time = step_time

    @staticmethod
    def from_dict(obj: Any) -> 'Step':
        assert isinstance(obj, dict)
        errors = []
        
        actual_time = parse_field(obj, "actualTime", lambda x: from_union([from_int, from_none], x), "Step", errors)
        step_temp = parse_field(obj, "stepTemp", lambda x: from_union([from_float, from_none], x), "Step", errors)
        ramp = parse_field(obj, "ramp", lambda x: from_union([from_float, from_none], x), "Step", errors)
        step_time = parse_field(obj, "stepTime", lambda x: from_union([from_float, from_none], x), "Step", errors)
        
        raise_if_errors(errors, "Step")
        return Step(actual_time, step_temp, ramp, step_time)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.actual_time is not None:
            result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        if self.step_temp is not None:
            result["stepTemp"] = from_union([to_float, from_none], self.step_temp)
        if self.ramp is not None:
            result["ramp"] = from_union([to_float, from_none], self.ramp)
        if self.step_time is not None:
            result["stepTime"] = from_union([to_float, from_none], self.step_time)
        return result


class Fermentation:
    steps: Optional[List[Step]]

    def __init__(self, steps: Optional[List[Step]]) -> None:
        self.steps = steps

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentation':
        assert isinstance(obj, dict)
        errors = []
        
        steps = parse_field(obj, "steps", lambda x: from_union([lambda x: from_list(Step.from_dict, x), from_none], x), "Fermentation", errors)
        
        raise_if_errors(errors, "Fermentation")
        return Fermentation(steps)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.steps is not None:
            result["steps"] = from_union([lambda x: from_list(lambda x: to_class(Step, x), x), from_none], self.steps)
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
        errors = []
        
        name = parse_field(obj, "name", lambda x: from_union([from_str, from_none], x), "Recipe", errors)
        fermentation = parse_field(obj, "fermentation", lambda x: from_union([Fermentation.from_dict, from_none], x), "Recipe", errors)
        
        raise_if_errors(errors, "Recipe")
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
    brew_date: Optional[int]
    recipe: Optional[Recipe]
    notes: Optional[List[Note]]
    measured_og: Optional[float]
    #Add the readings to fermentingBatch with a fake property
    readings: Optional[List[Reading]]

    def __init__(self, id: Optional[str], name: Optional[str], batch_no: Optional[int], status: Optional[str], brew_date: Optional[int], recipe: Optional[Recipe], notes: Optional[List[Note]], measured_og: Optional[float]) -> None:
        self.id = id
        self.name = name
        self.batch_no = batch_no
        self.status = status
        self.brew_date = brew_date
        self.recipe = recipe
        self.notes = notes
        self.measured_og = measured_og

    @staticmethod
    def from_dict(obj: Any) -> 'BatchItem':
        assert isinstance(obj, dict)
        errors = []
        
        id = parse_field(obj, "_id", lambda x: from_union([from_str, from_none], x), "BatchItem", errors)
        name = parse_field(obj, "name", lambda x: from_union([from_str, from_none], x), "BatchItem", errors)
        batch_no = parse_field(obj, "batchNo", lambda x: from_union([from_int, from_none], x), "BatchItem", errors)
        status = parse_field(obj, "status", lambda x: from_union([from_str, from_none], x), "BatchItem", errors)
        brew_date = parse_field(obj, "brewDate", lambda x: from_union([from_int, from_none], x), "BatchItem", errors)
        recipe = parse_field(obj, "recipe", lambda x: from_union([Recipe.from_dict, from_none], x), "BatchItem", errors)
        notes = parse_field(obj, "notes", lambda x: from_union([lambda x: from_list(Note.from_dict, x), from_none], x), "BatchItem", errors)
        measured_og = parse_field(obj, "measuredOg", lambda x: from_union([from_float, from_none], x), "BatchItem", errors)
        
        raise_if_errors(errors, "BatchItem")
        return BatchItem(id, name, batch_no, status, brew_date, recipe, notes, measured_og)

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
            result["current_temperature"] = sorted(self.readings, key=lambda x: x.time, reverse=True)[0].temp
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
