#https://app.quicktype.io/
#Name: Readings
#Python version: 3.6
#Transform property names to be Pythonic
#Make all properties optional
#Tip: Make sure no enums are used and set all ints to floats

from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Reading:
    rssi: Optional[int]
    temp: Optional[float]
    sg: Optional[float]
    angle: Optional[float]
    time: Optional[int]
    id: Optional[str]
    type: Optional[str]
    battery: Optional[float]
    comment: Optional[str]

    def __init__(self, rssi: Optional[int], temp: Optional[float], sg: Optional[float], angle: Optional[float], time: Optional[int], id: Optional[str], type: Optional[str], battery: Optional[float], comment: Optional[str]) -> None:
        self.rssi = rssi
        self.temp = temp
        self.sg = sg
        self.angle = angle
        self.time = time
        self.id = id
        self.type = type
        self.battery = battery
        self.comment = comment

    @staticmethod
    def from_dict(obj: Any) -> 'Reading':
        assert isinstance(obj, dict)
        rssi = from_union([from_int, from_none], obj.get("rssi"))
        temp = from_union([from_float, from_none], obj.get("temp"))
        sg = from_union([from_float, from_none], obj.get("sg"))
        angle = from_union([from_float, from_none], obj.get("angle"))
        time = from_union([from_int, from_none], obj.get("time"))
        id = from_union([from_str, from_none], obj.get("id"))
        type = from_union([from_str, from_none], obj.get("type"))
        battery = from_union([from_float, from_none], obj.get("battery"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        return Reading(rssi, temp, sg, angle, time, id, type, battery, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.rssi is not None:
            result["rssi"] = from_union([from_int, from_none], self.rssi)
        if self.temp is not None:
            result["temp"] = from_union([to_float, from_none], self.temp)
        if self.sg is not None:
            result["sg"] = from_union([to_float, from_none], self.sg)
        if self.angle is not None:
            result["angle"] = from_union([to_float, from_none], self.angle)
        if self.time is not None:
            result["time"] = from_union([from_int, from_none], self.time)
        if self.id is not None:
            result["id"] = from_union([from_str, from_none], self.id)
        if self.type is not None:
            result["type"] = from_union([from_str, from_none], self.type)
        if self.battery is not None:
            result["battery"] = from_union([to_float, from_none], self.battery)
        if self.comment is not None:
            result["comment"] = from_union([from_str, from_none], self.comment)
        return result


def readings_from_dict(s: Any) -> List[Reading]:
    return from_list(Reading.from_dict, s)


def readings_to_dict(x: List[Reading]) -> Any:
    return from_list(lambda x: to_class(Reading, x), x)
