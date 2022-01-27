# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = batch_item_from_dict(json.loads(json_string))

# https://app.quicktype.io/

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class Created:
    seconds: Optional[int] = None
    nanoseconds: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Created':
        assert isinstance(obj, dict)
        seconds = from_union([from_int, from_none], obj.get("_seconds"))
        nanoseconds = from_union([from_int, from_none], obj.get("_nanoseconds"))
        return Created(seconds, nanoseconds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_seconds"] = from_union([from_int, from_none], self.seconds)
        result["_nanoseconds"] = from_union([from_int, from_none], self.nanoseconds)
        return result


class Substitutes(Enum):
    EMPTY = ""
    PALE_LIQUID_EXTRACT = "Pale Liquid Extract"


class TypeEnum(Enum):
    GRAIN = "Grain"


class Version(Enum):
    THE_280 = "2.8.0"


@dataclass
class Fermentable:
    ibu_per_amount: None
    friability: None
    manufacturing_date: None
    fan: None
    cgdb: None
    timestamp_ms: Optional[int] = None
    grain_category: Optional[str] = None
    origin: Optional[str] = None
    diastatic_power: Optional[int] = None
    not_in_recipe: Optional[bool] = None
    acid: Optional[int] = None
    supplier: Optional[str] = None
    best_before_date: Optional[int] = None
    display_amount: Optional[int] = None
    amount: Optional[float] = None
    notes: Optional[str] = None
    attenuation: Optional[float] = None
    protein: Optional[float] = None
    potential: Optional[float] = None
    moisture: Optional[int] = None
    removed_from_inventory: Optional[bool] = None
    removed_amount: Optional[float] = None
    timestamp: Optional[Created] = None
    coarse_fine_diff: Optional[float] = None
    potential_percentage: Optional[float] = None
    max_in_batch: Optional[int] = None
    version: Optional[Version] = None
    rev: Optional[str] = None
    used_in: Optional[str] = None
    type: Optional[TypeEnum] = None
    created: Optional[Created] = None
    hidden: Optional[bool] = None
    name: Optional[str] = None
    cost_per_amount: Optional[int] = None
    not_fermentable: Optional[bool] = None
    fgdb: Optional[int] = None
    checked: Optional[bool] = None
    total_cost: Optional[int] = None
    user_notes: Optional[str] = None
    id: Optional[str] = None
    substitutes: Optional[Substitutes] = None
    inventory: Optional[float] = None
    color: Optional[float] = None
    lovibond: Optional[float] = None
    percentage: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentable':
        assert isinstance(obj, dict)
        ibu_per_amount = from_none(obj.get("ibuPerAmount"))
        friability = from_none(obj.get("friability"))
        manufacturing_date = from_none(obj.get("manufacturingDate"))
        fan = from_none(obj.get("fan"))
        cgdb = from_none(obj.get("cgdb"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        grain_category = from_union([from_str, from_none], obj.get("grainCategory"))
        origin = from_union([from_str, from_none], obj.get("origin"))
        diastatic_power = from_union([from_int, from_none], obj.get("diastaticPower"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        acid = from_union([from_int, from_none], obj.get("acid"))
        supplier = from_union([from_str, from_none], obj.get("supplier"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        attenuation = from_union([from_float, from_none], obj.get("attenuation"))
        protein = from_union([from_float, from_none], obj.get("protein"))
        potential = from_union([from_float, from_none], obj.get("potential"))
        moisture = from_union([from_int, from_none], obj.get("moisture"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        coarse_fine_diff = from_union([from_float, from_none], obj.get("coarseFineDiff"))
        potential_percentage = from_union([from_float, from_none], obj.get("potentialPercentage"))
        max_in_batch = from_union([from_int, from_none], obj.get("maxInBatch"))
        version = from_union([Version, from_none], obj.get("_version"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        used_in = from_union([from_str, from_none], obj.get("usedIn"))
        type = from_union([TypeEnum, from_none], obj.get("type"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        name = from_union([from_str, from_none], obj.get("name"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        not_fermentable = from_union([from_bool, from_none], obj.get("notFermentable"))
        fgdb = from_union([from_int, from_none], obj.get("fgdb"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        total_cost = from_union([from_int, from_none], obj.get("totalCost"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        id = from_union([from_str, from_none], obj.get("_id"))
        substitutes = from_union([Substitutes, from_none], obj.get("substitutes"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        color = from_union([from_float, from_none], obj.get("color"))
        lovibond = from_union([from_float, from_none], obj.get("lovibond"))
        percentage = from_union([from_float, from_none], obj.get("percentage"))
        return Fermentable(ibu_per_amount, friability, manufacturing_date, fan, cgdb, timestamp_ms, grain_category, origin, diastatic_power, not_in_recipe, acid, supplier, best_before_date, display_amount, amount, notes, attenuation, protein, potential, moisture, removed_from_inventory, removed_amount, timestamp, coarse_fine_diff, potential_percentage, max_in_batch, version, rev, used_in, type, created, hidden, name, cost_per_amount, not_fermentable, fgdb, checked, total_cost, user_notes, id, substitutes, inventory, color, lovibond, percentage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ibuPerAmount"] = from_none(self.ibu_per_amount)
        result["friability"] = from_none(self.friability)
        result["manufacturingDate"] = from_none(self.manufacturing_date)
        result["fan"] = from_none(self.fan)
        result["cgdb"] = from_none(self.cgdb)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["grainCategory"] = from_union([from_str, from_none], self.grain_category)
        result["origin"] = from_union([from_str, from_none], self.origin)
        result["diastaticPower"] = from_union([from_int, from_none], self.diastatic_power)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["acid"] = from_union([from_int, from_none], self.acid)
        result["supplier"] = from_union([from_str, from_none], self.supplier)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["attenuation"] = from_union([to_float, from_none], self.attenuation)
        result["protein"] = from_union([to_float, from_none], self.protein)
        result["potential"] = from_union([to_float, from_none], self.potential)
        result["moisture"] = from_union([from_int, from_none], self.moisture)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["coarseFineDiff"] = from_union([to_float, from_none], self.coarse_fine_diff)
        result["potentialPercentage"] = from_union([to_float, from_none], self.potential_percentage)
        result["maxInBatch"] = from_union([from_int, from_none], self.max_in_batch)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["usedIn"] = from_union([from_str, from_none], self.used_in)
        result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["name"] = from_union([from_str, from_none], self.name)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["notFermentable"] = from_union([from_bool, from_none], self.not_fermentable)
        result["fgdb"] = from_union([from_int, from_none], self.fgdb)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["totalCost"] = from_union([from_int, from_none], self.total_cost)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["substitutes"] = from_union([lambda x: to_enum(Substitutes, x), from_none], self.substitutes)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["color"] = from_union([to_float, from_none], self.color)
        result["lovibond"] = from_union([to_float, from_none], self.lovibond)
        result["percentage"] = from_union([to_float, from_none], self.percentage)
        return result


@dataclass
class Hop:
    humulene: None
    cohumulone: None
    beta: None
    year: None
    oil: None
    myrcene: None
    farnesene: None
    hsi: None
    temp: None
    caryophyllene: None
    inventory: Optional[float] = None
    usage: Optional[str] = None
    substitutes: Optional[str] = None
    type: Optional[str] = None
    actual_time: Optional[int] = None
    removed_amount: Optional[float] = None
    checked: Optional[bool] = None
    best_before_date: Optional[int] = None
    hidden: Optional[bool] = None
    name: Optional[str] = None
    time: Optional[int] = None
    manufacturing_date: Optional[int] = None
    not_in_recipe: Optional[bool] = None
    id: Optional[str] = None
    version: Optional[str] = None
    total_cost: Optional[float] = None
    use: Optional[str] = None
    created: Optional[Created] = None
    edit_flag: Optional[bool] = None
    cost_per_amount: Optional[float] = None
    timestamp_ms: Optional[int] = None
    used_in: Optional[str] = None
    origin: Optional[str] = None
    ibu: Optional[float] = None
    rev: Optional[str] = None
    removed_from_inventory: Optional[bool] = None
    user_notes: Optional[str] = None
    notes: Optional[str] = None
    display_amount: Optional[int] = None
    amount: Optional[float] = None
    day: Optional[int] = None
    alpha: Optional[float] = None
    timestamp: Optional[Created] = None
    time_unit: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Hop':
        assert isinstance(obj, dict)
        humulene = from_none(obj.get("humulene"))
        cohumulone = from_none(obj.get("cohumulone"))
        beta = from_none(obj.get("beta"))
        year = from_none(obj.get("year"))
        oil = from_none(obj.get("oil"))
        myrcene = from_none(obj.get("myrcene"))
        farnesene = from_none(obj.get("farnesene"))
        hsi = from_none(obj.get("hsi"))
        temp = from_none(obj.get("temp"))
        caryophyllene = from_none(obj.get("caryophyllene"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        usage = from_union([from_str, from_none], obj.get("usage"))
        substitutes = from_union([from_str, from_none], obj.get("substitutes"))
        type = from_union([from_str, from_none], obj.get("type"))
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        name = from_union([from_str, from_none], obj.get("name"))
        time = from_union([from_int, from_none], obj.get("time"))
        manufacturing_date = from_union([from_int, from_none], obj.get("manufacturingDate"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        id = from_union([from_str, from_none], obj.get("_id"))
        version = from_union([from_str, from_none], obj.get("_version"))
        total_cost = from_union([from_float, from_none], obj.get("totalCost"))
        use = from_union([from_str, from_none], obj.get("use"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        edit_flag = from_union([from_bool, from_none], obj.get("_editFlag"))
        cost_per_amount = from_union([from_float, from_none], obj.get("costPerAmount"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        used_in = from_union([from_str, from_none], obj.get("usedIn"))
        origin = from_union([from_str, from_none], obj.get("origin"))
        ibu = from_union([from_float, from_none], obj.get("ibu"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        day = from_union([from_int, from_none], obj.get("day"))
        alpha = from_union([from_float, from_none], obj.get("alpha"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        time_unit = from_union([from_str, from_none], obj.get("timeUnit"))
        return Hop(humulene, cohumulone, beta, year, oil, myrcene, farnesene, hsi, temp, caryophyllene, inventory, usage, substitutes, type, actual_time, removed_amount, checked, best_before_date, hidden, name, time, manufacturing_date, not_in_recipe, id, version, total_cost, use, created, edit_flag, cost_per_amount, timestamp_ms, used_in, origin, ibu, rev, removed_from_inventory, user_notes, notes, display_amount, amount, day, alpha, timestamp, time_unit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["humulene"] = from_none(self.humulene)
        result["cohumulone"] = from_none(self.cohumulone)
        result["beta"] = from_none(self.beta)
        result["year"] = from_none(self.year)
        result["oil"] = from_none(self.oil)
        result["myrcene"] = from_none(self.myrcene)
        result["farnesene"] = from_none(self.farnesene)
        result["hsi"] = from_none(self.hsi)
        result["temp"] = from_none(self.temp)
        result["caryophyllene"] = from_none(self.caryophyllene)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["usage"] = from_union([from_str, from_none], self.usage)
        result["substitutes"] = from_union([from_str, from_none], self.substitutes)
        result["type"] = from_union([from_str, from_none], self.type)
        result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["name"] = from_union([from_str, from_none], self.name)
        result["time"] = from_union([from_int, from_none], self.time)
        result["manufacturingDate"] = from_union([from_int, from_none], self.manufacturing_date)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["totalCost"] = from_union([to_float, from_none], self.total_cost)
        result["use"] = from_union([from_str, from_none], self.use)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_editFlag"] = from_union([from_bool, from_none], self.edit_flag)
        result["costPerAmount"] = from_union([to_float, from_none], self.cost_per_amount)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["usedIn"] = from_union([from_str, from_none], self.used_in)
        result["origin"] = from_union([from_str, from_none], self.origin)
        result["ibu"] = from_union([to_float, from_none], self.ibu)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["day"] = from_union([from_int, from_none], self.day)
        result["alpha"] = from_union([to_float, from_none], self.alpha)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["timeUnit"] = from_union([from_str, from_none], self.time_unit)
        return result


@dataclass
class BatchMisc:
    time: None
    total_cost: Optional[int] = None
    version: Optional[Version] = None
    cost_per_amount: Optional[int] = None
    inventory: Optional[float] = None
    timestamp: Optional[Created] = None
    amount: Optional[float] = None
    id: Optional[str] = None
    use: Optional[str] = None
    checked: Optional[bool] = None
    type: Optional[str] = None
    rev: Optional[str] = None
    not_in_recipe: Optional[bool] = None
    display_amount: Optional[int] = None
    created: Optional[Created] = None
    removed_amount: Optional[float] = None
    removed_unit: Optional[str] = None
    timestamp_ms: Optional[int] = None
    unit: Optional[str] = None
    inventory_unit: Optional[str] = None
    hidden: Optional[bool] = None
    water_adjustment: Optional[bool] = None
    removed_from_inventory: Optional[bool] = None
    time_is_days: Optional[bool] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchMisc':
        assert isinstance(obj, dict)
        time = from_none(obj.get("time"))
        total_cost = from_union([from_int, from_none], obj.get("totalCost"))
        version = from_union([Version, from_none], obj.get("_version"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        id = from_union([from_str, from_none], obj.get("_id"))
        use = from_union([from_str, from_none], obj.get("use"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        type = from_union([from_str, from_none], obj.get("type"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        removed_unit = from_union([from_str, from_none], obj.get("removedUnit"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        unit = from_union([from_str, from_none], obj.get("unit"))
        inventory_unit = from_union([from_str, from_none], obj.get("inventoryUnit"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        water_adjustment = from_union([from_bool, from_none], obj.get("waterAdjustment"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        time_is_days = from_union([from_bool, from_none], obj.get("timeIsDays"))
        name = from_union([from_str, from_none], obj.get("name"))
        return BatchMisc(time, total_cost, version, cost_per_amount, inventory, timestamp, amount, id, use, checked, type, rev, not_in_recipe, display_amount, created, removed_amount, removed_unit, timestamp_ms, unit, inventory_unit, hidden, water_adjustment, removed_from_inventory, time_is_days, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = from_none(self.time)
        result["totalCost"] = from_union([from_int, from_none], self.total_cost)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["use"] = from_union([from_str, from_none], self.use)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["type"] = from_union([from_str, from_none], self.type)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["removedUnit"] = from_union([from_str, from_none], self.removed_unit)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["unit"] = from_union([from_str, from_none], self.unit)
        result["inventoryUnit"] = from_union([from_str, from_none], self.inventory_unit)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["waterAdjustment"] = from_union([from_bool, from_none], self.water_adjustment)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["timeIsDays"] = from_union([from_bool, from_none], self.time_is_days)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class BatchYeast:
    max_attenuation: None
    manufacturing_date: None
    max_abv: None
    min_attenuation: None
    removed_from_inventory: Optional[bool] = None
    best_before_date: Optional[int] = None
    inventory: Optional[int] = None
    removed_unit: Optional[str] = None
    min_temp: Optional[int] = None
    cost_per_amount: Optional[int] = None
    removed_amount: Optional[int] = None
    ferments_all: Optional[bool] = None
    user_notes: Optional[str] = None
    product_id: Optional[str] = None
    type: Optional[str] = None
    max_temp: Optional[int] = None
    name: Optional[str] = None
    rev: Optional[str] = None
    checked: Optional[bool] = None
    form: Optional[str] = None
    timestamp: Optional[Created] = None
    version: Optional[Version] = None
    laboratory: Optional[str] = None
    inventory_unit: Optional[str] = None
    amount: Optional[int] = None
    unit: Optional[str] = None
    total_cost: Optional[int] = None
    timestamp_ms: Optional[int] = None
    created: Optional[Created] = None
    id: Optional[str] = None
    hidden: Optional[bool] = None
    attenuation: Optional[int] = None
    not_in_recipe: Optional[bool] = None
    flocculation: Optional[str] = None
    description: Optional[str] = None
    display_amount: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchYeast':
        assert isinstance(obj, dict)
        max_attenuation = from_none(obj.get("maxAttenuation"))
        manufacturing_date = from_none(obj.get("manufacturingDate"))
        max_abv = from_none(obj.get("maxAbv"))
        min_attenuation = from_none(obj.get("minAttenuation"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        inventory = from_union([from_int, from_none], obj.get("inventory"))
        removed_unit = from_union([from_str, from_none], obj.get("removedUnit"))
        min_temp = from_union([from_int, from_none], obj.get("minTemp"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        removed_amount = from_union([from_int, from_none], obj.get("removedAmount"))
        ferments_all = from_union([from_bool, from_none], obj.get("fermentsAll"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        product_id = from_union([from_str, from_none], obj.get("productId"))
        type = from_union([from_str, from_none], obj.get("type"))
        max_temp = from_union([from_int, from_none], obj.get("maxTemp"))
        name = from_union([from_str, from_none], obj.get("name"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        form = from_union([from_str, from_none], obj.get("form"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        version = from_union([Version, from_none], obj.get("_version"))
        laboratory = from_union([from_str, from_none], obj.get("laboratory"))
        inventory_unit = from_union([from_str, from_none], obj.get("inventoryUnit"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        unit = from_union([from_str, from_none], obj.get("unit"))
        total_cost = from_union([from_int, from_none], obj.get("totalCost"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        id = from_union([from_str, from_none], obj.get("_id"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        attenuation = from_union([from_int, from_none], obj.get("attenuation"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        flocculation = from_union([from_str, from_none], obj.get("flocculation"))
        description = from_union([from_str, from_none], obj.get("description"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        return BatchYeast(max_attenuation, manufacturing_date, max_abv, min_attenuation, removed_from_inventory, best_before_date, inventory, removed_unit, min_temp, cost_per_amount, removed_amount, ferments_all, user_notes, product_id, type, max_temp, name, rev, checked, form, timestamp, version, laboratory, inventory_unit, amount, unit, total_cost, timestamp_ms, created, id, hidden, attenuation, not_in_recipe, flocculation, description, display_amount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxAttenuation"] = from_none(self.max_attenuation)
        result["manufacturingDate"] = from_none(self.manufacturing_date)
        result["maxAbv"] = from_none(self.max_abv)
        result["minAttenuation"] = from_none(self.min_attenuation)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["inventory"] = from_union([from_int, from_none], self.inventory)
        result["removedUnit"] = from_union([from_str, from_none], self.removed_unit)
        result["minTemp"] = from_union([from_int, from_none], self.min_temp)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["removedAmount"] = from_union([from_int, from_none], self.removed_amount)
        result["fermentsAll"] = from_union([from_bool, from_none], self.ferments_all)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["productId"] = from_union([from_str, from_none], self.product_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["maxTemp"] = from_union([from_int, from_none], self.max_temp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["form"] = from_union([from_str, from_none], self.form)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["laboratory"] = from_union([from_str, from_none], self.laboratory)
        result["inventoryUnit"] = from_union([from_str, from_none], self.inventory_unit)
        result["amount"] = from_union([from_int, from_none], self.amount)
        result["unit"] = from_union([from_str, from_none], self.unit)
        result["totalCost"] = from_union([from_int, from_none], self.total_cost)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["attenuation"] = from_union([from_int, from_none], self.attenuation)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["flocculation"] = from_union([from_str, from_none], self.flocculation)
        result["description"] = from_union([from_str, from_none], self.description)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        return result


@dataclass
class BoilStep:
    name: Optional[str] = None
    time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BoilStep':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        time = from_union([from_int, from_none], obj.get("time"))
        return BoilStep(name, time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["time"] = from_union([from_int, from_none], self.time)
        return result


@dataclass
class Cost:
    per_bottling_liter: Optional[float] = None
    miscs: Optional[int] = None
    yeasts: Optional[int] = None
    fermentables_share: Optional[int] = None
    hops_share: Optional[int] = None
    hops: Optional[float] = None
    total: Optional[float] = None
    miscs_share: Optional[int] = None
    fermentables: Optional[int] = None
    yeasts_share: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Cost':
        assert isinstance(obj, dict)
        per_bottling_liter = from_union([from_float, from_none], obj.get("perBottlingLiter"))
        miscs = from_union([from_int, from_none], obj.get("miscs"))
        yeasts = from_union([from_int, from_none], obj.get("yeasts"))
        fermentables_share = from_union([from_int, from_none], obj.get("fermentablesShare"))
        hops_share = from_union([from_int, from_none], obj.get("hopsShare"))
        hops = from_union([from_float, from_none], obj.get("hops"))
        total = from_union([from_float, from_none], obj.get("total"))
        miscs_share = from_union([from_int, from_none], obj.get("miscsShare"))
        fermentables = from_union([from_int, from_none], obj.get("fermentables"))
        yeasts_share = from_union([from_int, from_none], obj.get("yeastsShare"))
        return Cost(per_bottling_liter, miscs, yeasts, fermentables_share, hops_share, hops, total, miscs_share, fermentables, yeasts_share)

    def to_dict(self) -> dict:
        result: dict = {}
        result["perBottlingLiter"] = from_union([to_float, from_none], self.per_bottling_liter)
        result["miscs"] = from_union([from_int, from_none], self.miscs)
        result["yeasts"] = from_union([from_int, from_none], self.yeasts)
        result["fermentablesShare"] = from_union([from_int, from_none], self.fermentables_share)
        result["hopsShare"] = from_union([from_int, from_none], self.hops_share)
        result["hops"] = from_union([to_float, from_none], self.hops)
        result["total"] = from_union([to_float, from_none], self.total)
        result["miscsShare"] = from_union([from_int, from_none], self.miscs_share)
        result["fermentables"] = from_union([from_int, from_none], self.fermentables)
        result["yeastsShare"] = from_union([from_int, from_none], self.yeasts_share)
        return result


@dataclass
class LastData:
    angle: Optional[float] = None
    type: Optional[str] = None
    status: Optional[str] = None
    id: Optional[str] = None
    battery: Optional[float] = None
    time: Optional[int] = None
    temp: Optional[float] = None
    rssi: Optional[int] = None
    sg: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LastData':
        assert isinstance(obj, dict)
        angle = from_union([from_float, from_none], obj.get("angle"))
        type = from_union([from_str, from_none], obj.get("type"))
        status = from_union([from_str, from_none], obj.get("status"))
        id = from_union([from_str, from_none], obj.get("id"))
        battery = from_union([from_float, from_none], obj.get("battery"))
        time = from_union([from_int, from_none], obj.get("time"))
        temp = from_union([from_float, from_none], obj.get("temp"))
        rssi = from_union([from_int, from_none], obj.get("rssi"))
        sg = from_union([from_float, from_none], obj.get("sg"))
        return LastData(angle, type, status, id, battery, time, temp, rssi, sg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["angle"] = from_union([to_float, from_none], self.angle)
        result["type"] = from_union([from_str, from_none], self.type)
        result["status"] = from_union([from_str, from_none], self.status)
        result["id"] = from_union([from_str, from_none], self.id)
        result["battery"] = from_union([to_float, from_none], self.battery)
        result["time"] = from_union([from_int, from_none], self.time)
        result["temp"] = from_union([to_float, from_none], self.temp)
        result["rssi"] = from_union([from_int, from_none], self.rssi)
        result["sg"] = from_union([to_float, from_none], self.sg)
        return result


@dataclass
class ItemSettings:
    temp_offset: None
    gravity_offset: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemSettings':
        assert isinstance(obj, dict)
        temp_offset = from_none(obj.get("tempOffset"))
        gravity_offset = from_union([from_int, from_none], obj.get("gravityOffset"))
        return ItemSettings(temp_offset, gravity_offset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tempOffset"] = from_none(self.temp_offset)
        result["gravityOffset"] = from_union([from_int, from_none], self.gravity_offset)
        return result


@dataclass
class Item:
    last_data: Optional[LastData] = None
    settings: Optional[ItemSettings] = None
    hidden: Optional[bool] = None
    type: Optional[str] = None
    series: Optional[List[str]] = None
    last_log: Optional[int] = None
    name: Optional[str] = None
    key: Optional[str] = None
    enabled: Optional[bool] = None
    batch_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        last_data = from_union([LastData.from_dict, from_none], obj.get("lastData"))
        settings = from_union([ItemSettings.from_dict, from_none], obj.get("settings"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        type = from_union([from_str, from_none], obj.get("type"))
        series = from_union([lambda x: from_list(from_str, x), from_none], obj.get("series"))
        last_log = from_union([from_int, from_none], obj.get("lastLog"))
        name = from_union([from_str, from_none], obj.get("name"))
        key = from_union([from_str, from_none], obj.get("key"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        batch_id = from_union([from_str, from_none], obj.get("batchId"))
        return Item(last_data, settings, hidden, type, series, last_log, name, key, enabled, batch_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lastData"] = from_union([lambda x: to_class(LastData, x), from_none], self.last_data)
        result["settings"] = from_union([lambda x: to_class(ItemSettings, x), from_none], self.settings)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["type"] = from_union([from_str, from_none], self.type)
        result["series"] = from_union([lambda x: from_list(from_str, x), from_none], self.series)
        result["lastLog"] = from_union([from_int, from_none], self.last_log)
        result["name"] = from_union([from_str, from_none], self.name)
        result["key"] = from_union([from_str, from_none], self.key)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["batchId"] = from_union([from_str, from_none], self.batch_id)
        return result


@dataclass
class BrewPiLess:
    enabled: Optional[bool] = None
    items: Optional[List[Item]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BrewPiLess':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        items = from_union([lambda x: from_list(Item.from_dict, x), from_none], obj.get("items"))
        return BrewPiLess(enabled, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["items"] = from_union([lambda x: from_list(lambda x: to_class(Item, x), x), from_none], self.items)
        return result


@dataclass
class Gfcc:
    brew_device_id: None
    enabled: Optional[bool] = None
    items: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Gfcc':
        assert isinstance(obj, dict)
        brew_device_id = from_none(obj.get("brewDeviceId"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        items = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("items"))
        return Gfcc(brew_device_id, enabled, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["brewDeviceId"] = from_none(self.brew_device_id)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["items"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.items)
        return result


@dataclass
class Tilt:
    mode: Optional[str] = None
    temp: Optional[bool] = None
    items: Optional[List[Any]] = None
    enabled: Optional[bool] = None
    gravity: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tilt':
        assert isinstance(obj, dict)
        mode = from_union([from_str, from_none], obj.get("mode"))
        temp = from_union([from_bool, from_none], obj.get("temp"))
        items = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("items"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        gravity = from_union([from_bool, from_none], obj.get("gravity"))
        return Tilt(mode, temp, items, enabled, gravity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["temp"] = from_union([from_bool, from_none], self.temp)
        result["items"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.items)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["gravity"] = from_union([from_bool, from_none], self.gravity)
        return result


@dataclass
class Devices:
    gfcc: Optional[Gfcc] = None
    i_spindel: Optional[BrewPiLess] = None
    tilt: Optional[Tilt] = None
    brew_pi_less: Optional[BrewPiLess] = None
    float_hydrometer: Optional[BrewPiLess] = None
    plaato_keg: Optional[BrewPiLess] = None
    floaty_hydrometer: Optional[BrewPiLess] = None
    stream: Optional[BrewPiLess] = None
    plaato_airlock: Optional[BrewPiLess] = None
    my_brewbot: Optional[BrewPiLess] = None
    smart_pid: Optional[Gfcc] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Devices':
        assert isinstance(obj, dict)
        gfcc = from_union([Gfcc.from_dict, from_none], obj.get("gfcc"))
        i_spindel = from_union([BrewPiLess.from_dict, from_none], obj.get("iSpindel"))
        tilt = from_union([Tilt.from_dict, from_none], obj.get("tilt"))
        brew_pi_less = from_union([BrewPiLess.from_dict, from_none], obj.get("brewPiLess"))
        float_hydrometer = from_union([BrewPiLess.from_dict, from_none], obj.get("floatHydrometer"))
        plaato_keg = from_union([BrewPiLess.from_dict, from_none], obj.get("plaatoKeg"))
        floaty_hydrometer = from_union([BrewPiLess.from_dict, from_none], obj.get("floatyHydrometer"))
        stream = from_union([BrewPiLess.from_dict, from_none], obj.get("stream"))
        plaato_airlock = from_union([BrewPiLess.from_dict, from_none], obj.get("plaatoAirlock"))
        my_brewbot = from_union([BrewPiLess.from_dict, from_none], obj.get("myBrewbot"))
        smart_pid = from_union([Gfcc.from_dict, from_none], obj.get("smartPid"))
        return Devices(gfcc, i_spindel, tilt, brew_pi_less, float_hydrometer, plaato_keg, floaty_hydrometer, stream, plaato_airlock, my_brewbot, smart_pid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["gfcc"] = from_union([lambda x: to_class(Gfcc, x), from_none], self.gfcc)
        result["iSpindel"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.i_spindel)
        result["tilt"] = from_union([lambda x: to_class(Tilt, x), from_none], self.tilt)
        result["brewPiLess"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.brew_pi_less)
        result["floatHydrometer"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.float_hydrometer)
        result["plaatoKeg"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.plaato_keg)
        result["floatyHydrometer"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.floaty_hydrometer)
        result["stream"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.stream)
        result["plaatoAirlock"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.plaato_airlock)
        result["myBrewbot"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.my_brewbot)
        result["smartPid"] = from_union([lambda x: to_class(Gfcc, x), from_none], self.smart_pid)
        return result


@dataclass
class Event:
    day_event: Optional[bool] = None
    notify_time: Optional[int] = None
    description_html: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    time: Optional[int] = None
    event_text: Optional[str] = None
    event_type: Optional[str] = None
    active: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        day_event = from_union([from_bool, from_none], obj.get("dayEvent"))
        notify_time = from_union([from_int, from_none], obj.get("notifyTime"))
        description_html = from_union([from_str, from_none], obj.get("descriptionHTML"))
        description = from_union([from_str, from_none], obj.get("description"))
        title = from_union([from_str, from_none], obj.get("title"))
        time = from_union([from_int, from_none], obj.get("time"))
        event_text = from_union([from_none, from_str], obj.get("eventText"))
        event_type = from_union([from_str, from_none], obj.get("eventType"))
        active = from_union([from_bool, from_none], obj.get("active"))
        return Event(day_event, notify_time, description_html, description, title, time, event_text, event_type, active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dayEvent"] = from_union([from_bool, from_none], self.day_event)
        result["notifyTime"] = from_union([from_int, from_none], self.notify_time)
        result["descriptionHTML"] = from_union([from_str, from_none], self.description_html)
        result["description"] = from_union([from_str, from_none], self.description)
        result["title"] = from_union([from_str, from_none], self.title)
        result["time"] = from_union([from_int, from_none], self.time)
        result["eventText"] = from_union([from_none, from_str], self.event_text)
        result["eventType"] = from_union([from_str, from_none], self.event_type)
        result["active"] = from_union([from_bool, from_none], self.active)
        return result


@dataclass
class Note:
    timestamp: Optional[int] = None
    note: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Note':
        assert isinstance(obj, dict)
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        note = from_union([from_str, from_none], obj.get("note"))
        status = from_union([from_str, from_none], obj.get("status"))
        type = from_union([from_str, from_none], obj.get("type"))
        return Note(timestamp, note, status, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["note"] = from_union([from_str, from_none], self.note)
        result["status"] = from_union([from_str, from_none], self.status)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class CarbonationStyle:
    carb_min: Optional[float] = None
    name: Optional[str] = None
    id: Optional[str] = None
    carb_max: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CarbonationStyle':
        assert isinstance(obj, dict)
        carb_min = from_union([from_float, from_none], obj.get("carbMin"))
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("_id"))
        carb_max = from_union([from_float, from_none], obj.get("carbMax"))
        return CarbonationStyle(carb_min, name, id, carb_max)

    def to_dict(self) -> dict:
        result: dict = {}
        result["carbMin"] = from_union([to_float, from_none], self.carb_min)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["carbMax"] = from_union([to_float, from_none], self.carb_max)
        return result


@dataclass
class Data:
    batch_sparge_water_amount4: None
    batch_sparge_water_amount3: None
    batch_sparge_water_amount1: None
    strike_temp: None
    batch_sparge_water_amount2: None
    mash_volume_surplus: Optional[int] = None
    top_up_water: Optional[int] = None
    sparge_water_amount: Optional[float] = None
    mash_fermentables: Optional[List[Fermentable]] = None
    all_diastatic_power: Optional[bool] = None
    total_diastatic_power: Optional[int] = None
    hlt_water_amount: Optional[float] = None
    other_fermentables: Optional[List[Any]] = None
    mash_volume: Optional[float] = None
    mash_fermentables_amount: Optional[float] = None
    mash_water_amount: Optional[float] = None
    hops_amount: Optional[float] = None
    total_water_amount: Optional[float] = None
    other_fermentables_amount: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        batch_sparge_water_amount4 = from_none(obj.get("batchSpargeWaterAmount4"))
        batch_sparge_water_amount3 = from_none(obj.get("batchSpargeWaterAmount3"))
        batch_sparge_water_amount1 = from_none(obj.get("batchSpargeWaterAmount1"))
        strike_temp = from_none(obj.get("strikeTemp"))
        batch_sparge_water_amount2 = from_none(obj.get("batchSpargeWaterAmount2"))
        mash_volume_surplus = from_union([from_int, from_none], obj.get("mashVolumeSurplus"))
        top_up_water = from_union([from_int, from_none], obj.get("topUpWater"))
        sparge_water_amount = from_union([from_float, from_none], obj.get("spargeWaterAmount"))
        mash_fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("mashFermentables"))
        all_diastatic_power = from_union([from_bool, from_none], obj.get("allDiastaticPower"))
        total_diastatic_power = from_union([from_int, from_none], obj.get("totalDiastaticPower"))
        hlt_water_amount = from_union([from_float, from_none], obj.get("hltWaterAmount"))
        other_fermentables = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("otherFermentables"))
        mash_volume = from_union([from_float, from_none], obj.get("mashVolume"))
        mash_fermentables_amount = from_union([from_float, from_none], obj.get("mashFermentablesAmount"))
        mash_water_amount = from_union([from_float, from_none], obj.get("mashWaterAmount"))
        hops_amount = from_union([from_float, from_none], obj.get("hopsAmount"))
        total_water_amount = from_union([from_float, from_none], obj.get("totalWaterAmount"))
        other_fermentables_amount = from_union([from_int, from_none], obj.get("otherFermentablesAmount"))
        return Data(batch_sparge_water_amount4, batch_sparge_water_amount3, batch_sparge_water_amount1, strike_temp, batch_sparge_water_amount2, mash_volume_surplus, top_up_water, sparge_water_amount, mash_fermentables, all_diastatic_power, total_diastatic_power, hlt_water_amount, other_fermentables, mash_volume, mash_fermentables_amount, mash_water_amount, hops_amount, total_water_amount, other_fermentables_amount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["batchSpargeWaterAmount4"] = from_none(self.batch_sparge_water_amount4)
        result["batchSpargeWaterAmount3"] = from_none(self.batch_sparge_water_amount3)
        result["batchSpargeWaterAmount1"] = from_none(self.batch_sparge_water_amount1)
        result["strikeTemp"] = from_none(self.strike_temp)
        result["batchSpargeWaterAmount2"] = from_none(self.batch_sparge_water_amount2)
        result["mashVolumeSurplus"] = from_union([from_int, from_none], self.mash_volume_surplus)
        result["topUpWater"] = from_union([from_int, from_none], self.top_up_water)
        result["spargeWaterAmount"] = from_union([to_float, from_none], self.sparge_water_amount)
        result["mashFermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.mash_fermentables)
        result["allDiastaticPower"] = from_union([from_bool, from_none], self.all_diastatic_power)
        result["totalDiastaticPower"] = from_union([from_int, from_none], self.total_diastatic_power)
        result["hltWaterAmount"] = from_union([to_float, from_none], self.hlt_water_amount)
        result["otherFermentables"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.other_fermentables)
        result["mashVolume"] = from_union([to_float, from_none], self.mash_volume)
        result["mashFermentablesAmount"] = from_union([to_float, from_none], self.mash_fermentables_amount)
        result["mashWaterAmount"] = from_union([to_float, from_none], self.mash_water_amount)
        result["hopsAmount"] = from_union([to_float, from_none], self.hops_amount)
        result["totalWaterAmount"] = from_union([to_float, from_none], self.total_water_amount)
        result["otherFermentablesAmount"] = from_union([from_int, from_none], self.other_fermentables_amount)
        return result


@dataclass
class Defaults:
    gravity: Optional[str] = None
    grain_color: Optional[str] = None
    temp: Optional[str] = None
    pressure: Optional[str] = None
    color: Optional[str] = None
    weight: Optional[str] = None
    hop: Optional[str] = None
    altitude: Optional[str] = None
    volume: Optional[str] = None
    preferred: Optional[str] = None
    attenuation: Optional[str] = None
    abv: Optional[str] = None
    ibu: Optional[str] = None
    carbonation: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Defaults':
        assert isinstance(obj, dict)
        gravity = from_union([from_str, from_none], obj.get("gravity"))
        grain_color = from_union([from_str, from_none], obj.get("grainColor"))
        temp = from_union([from_str, from_none], obj.get("temp"))
        pressure = from_union([from_str, from_none], obj.get("pressure"))
        color = from_union([from_str, from_none], obj.get("color"))
        weight = from_union([from_str, from_none], obj.get("weight"))
        hop = from_union([from_str, from_none], obj.get("hop"))
        altitude = from_union([from_str, from_none], obj.get("altitude"))
        volume = from_union([from_str, from_none], obj.get("volume"))
        preferred = from_union([from_str, from_none], obj.get("preferred"))
        attenuation = from_union([from_str, from_none], obj.get("attenuation"))
        abv = from_union([from_str, from_none], obj.get("abv"))
        ibu = from_union([from_str, from_none], obj.get("ibu"))
        carbonation = from_union([from_str, from_none], obj.get("carbonation"))
        return Defaults(gravity, grain_color, temp, pressure, color, weight, hop, altitude, volume, preferred, attenuation, abv, ibu, carbonation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["gravity"] = from_union([from_str, from_none], self.gravity)
        result["grainColor"] = from_union([from_str, from_none], self.grain_color)
        result["temp"] = from_union([from_str, from_none], self.temp)
        result["pressure"] = from_union([from_str, from_none], self.pressure)
        result["color"] = from_union([from_str, from_none], self.color)
        result["weight"] = from_union([from_str, from_none], self.weight)
        result["hop"] = from_union([from_str, from_none], self.hop)
        result["altitude"] = from_union([from_str, from_none], self.altitude)
        result["volume"] = from_union([from_str, from_none], self.volume)
        result["preferred"] = from_union([from_str, from_none], self.preferred)
        result["attenuation"] = from_union([from_str, from_none], self.attenuation)
        result["abv"] = from_union([from_str, from_none], self.abv)
        result["ibu"] = from_union([from_str, from_none], self.ibu)
        result["carbonation"] = from_union([from_str, from_none], self.carbonation)
        return result


@dataclass
class Meta:
    mash_efficiency_is_calculated: Optional[bool] = None
    efficiency_is_calculated: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        mash_efficiency_is_calculated = from_union([from_bool, from_none], obj.get("mashEfficiencyIsCalculated"))
        efficiency_is_calculated = from_union([from_bool, from_none], obj.get("efficiencyIsCalculated"))
        return Meta(mash_efficiency_is_calculated, efficiency_is_calculated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mashEfficiencyIsCalculated"] = from_union([from_bool, from_none], self.mash_efficiency_is_calculated)
        result["efficiencyIsCalculated"] = from_union([from_bool, from_none], self.efficiency_is_calculated)
        return result


@dataclass
class Equipment:
    sparge_water_min: None
    ambient_temperature: None
    water_grain_ratio: None
    mash_water_volume_limit_enabled: Optional[bool] = None
    calc_aroma_hop_utilization: Optional[bool] = None
    grain_absorption_rate: Optional[float] = None
    id: Optional[str] = None
    sparge_temperature: Optional[int] = None
    mash_water_formula: Optional[str] = None
    name: Optional[str] = None
    brewhouse_efficiency: Optional[int] = None
    timestamp: Optional[Created] = None
    efficiency_type: Optional[str] = None
    sparge_water_overflow: Optional[str] = None
    sparge_water_formula: Optional[str] = None
    bottling_volume: Optional[int] = None
    created: Optional[Created] = None
    rev: Optional[str] = None
    trub_chiller_loss: Optional[float] = None
    boil_time: Optional[int] = None
    evaporation_rate: Optional[float] = None
    hopstand_temperature: Optional[int] = None
    calc_strike_water_temperature: Optional[bool] = None
    calc_mash_efficiency: Optional[bool] = None
    hop_utilization: Optional[int] = None
    fermenter_volume_before_top_up: Optional[int] = None
    mash_tun_dead_space: Optional[int] = None
    mash_efficiency: Optional[float] = None
    water_calculation: Optional[str] = None
    timestamp_ms: Optional[int] = None
    sparge_water_max: Optional[int] = None
    fermenter_loss: Optional[int] = None
    sparge_water_reminder_time: Optional[int] = None
    hidden: Optional[bool] = None
    post_boil_kettle_vol: Optional[float] = None
    batch_size: Optional[int] = None
    fermenter_volume: Optional[int] = None
    mash_water_max: Optional[int] = None
    aroma_hop_utilization: Optional[float] = None
    version: Optional[Version] = None
    boil_off_per_hr: Optional[float] = None
    notes: Optional[str] = None
    sparge_water_reminder_enabled: Optional[bool] = None
    calc_boil_volume: Optional[bool] = None
    efficiency: Optional[int] = None
    mash_water_min: Optional[int] = None
    fermenter_loss_estimate: Optional[int] = None
    meta: Optional[Meta] = None
    boil_size: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Equipment':
        assert isinstance(obj, dict)
        sparge_water_min = from_none(obj.get("spargeWaterMin"))
        ambient_temperature = from_none(obj.get("ambientTemperature"))
        water_grain_ratio = from_none(obj.get("waterGrainRatio"))
        mash_water_volume_limit_enabled = from_union([from_bool, from_none], obj.get("mashWaterVolumeLimitEnabled"))
        calc_aroma_hop_utilization = from_union([from_bool, from_none], obj.get("calcAromaHopUtilization"))
        grain_absorption_rate = from_union([from_float, from_none], obj.get("grainAbsorptionRate"))
        id = from_union([from_str, from_none], obj.get("_id"))
        sparge_temperature = from_union([from_int, from_none], obj.get("spargeTemperature"))
        mash_water_formula = from_union([from_str, from_none], obj.get("mashWaterFormula"))
        name = from_union([from_str, from_none], obj.get("name"))
        brewhouse_efficiency = from_union([from_int, from_none], obj.get("brewhouseEfficiency"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        efficiency_type = from_union([from_str, from_none], obj.get("efficiencyType"))
        sparge_water_overflow = from_union([from_str, from_none], obj.get("spargeWaterOverflow"))
        sparge_water_formula = from_union([from_str, from_none], obj.get("spargeWaterFormula"))
        bottling_volume = from_union([from_int, from_none], obj.get("bottlingVolume"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        trub_chiller_loss = from_union([from_float, from_none], obj.get("trubChillerLoss"))
        boil_time = from_union([from_int, from_none], obj.get("boilTime"))
        evaporation_rate = from_union([from_float, from_none], obj.get("evaporationRate"))
        hopstand_temperature = from_union([from_int, from_none], obj.get("hopstandTemperature"))
        calc_strike_water_temperature = from_union([from_bool, from_none], obj.get("calcStrikeWaterTemperature"))
        calc_mash_efficiency = from_union([from_bool, from_none], obj.get("calcMashEfficiency"))
        hop_utilization = from_union([from_int, from_none], obj.get("hopUtilization"))
        fermenter_volume_before_top_up = from_union([from_int, from_none], obj.get("fermenterVolumeBeforeTopUp"))
        mash_tun_dead_space = from_union([from_int, from_none], obj.get("mashTunDeadSpace"))
        mash_efficiency = from_union([from_float, from_none], obj.get("mashEfficiency"))
        water_calculation = from_union([from_str, from_none], obj.get("waterCalculation"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        sparge_water_max = from_union([from_int, from_none], obj.get("spargeWaterMax"))
        fermenter_loss = from_union([from_int, from_none], obj.get("fermenterLoss"))
        sparge_water_reminder_time = from_union([from_int, from_none], obj.get("spargeWaterReminderTime"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        post_boil_kettle_vol = from_union([from_float, from_none], obj.get("postBoilKettleVol"))
        batch_size = from_union([from_int, from_none], obj.get("batchSize"))
        fermenter_volume = from_union([from_int, from_none], obj.get("fermenterVolume"))
        mash_water_max = from_union([from_int, from_none], obj.get("mashWaterMax"))
        aroma_hop_utilization = from_union([from_float, from_none], obj.get("aromaHopUtilization"))
        version = from_union([Version, from_none], obj.get("_version"))
        boil_off_per_hr = from_union([from_float, from_none], obj.get("boilOffPerHr"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        sparge_water_reminder_enabled = from_union([from_bool, from_none], obj.get("spargeWaterReminderEnabled"))
        calc_boil_volume = from_union([from_bool, from_none], obj.get("calcBoilVolume"))
        efficiency = from_union([from_int, from_none], obj.get("efficiency"))
        mash_water_min = from_union([from_int, from_none], obj.get("mashWaterMin"))
        fermenter_loss_estimate = from_union([from_int, from_none], obj.get("fermenterLossEstimate"))
        meta = from_union([Meta.from_dict, from_none], obj.get("_meta"))
        boil_size = from_union([from_float, from_none], obj.get("boilSize"))
        return Equipment(sparge_water_min, ambient_temperature, water_grain_ratio, mash_water_volume_limit_enabled, calc_aroma_hop_utilization, grain_absorption_rate, id, sparge_temperature, mash_water_formula, name, brewhouse_efficiency, timestamp, efficiency_type, sparge_water_overflow, sparge_water_formula, bottling_volume, created, rev, trub_chiller_loss, boil_time, evaporation_rate, hopstand_temperature, calc_strike_water_temperature, calc_mash_efficiency, hop_utilization, fermenter_volume_before_top_up, mash_tun_dead_space, mash_efficiency, water_calculation, timestamp_ms, sparge_water_max, fermenter_loss, sparge_water_reminder_time, hidden, post_boil_kettle_vol, batch_size, fermenter_volume, mash_water_max, aroma_hop_utilization, version, boil_off_per_hr, notes, sparge_water_reminder_enabled, calc_boil_volume, efficiency, mash_water_min, fermenter_loss_estimate, meta, boil_size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["spargeWaterMin"] = from_none(self.sparge_water_min)
        result["ambientTemperature"] = from_none(self.ambient_temperature)
        result["waterGrainRatio"] = from_none(self.water_grain_ratio)
        result["mashWaterVolumeLimitEnabled"] = from_union([from_bool, from_none], self.mash_water_volume_limit_enabled)
        result["calcAromaHopUtilization"] = from_union([from_bool, from_none], self.calc_aroma_hop_utilization)
        result["grainAbsorptionRate"] = from_union([to_float, from_none], self.grain_absorption_rate)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["spargeTemperature"] = from_union([from_int, from_none], self.sparge_temperature)
        result["mashWaterFormula"] = from_union([from_str, from_none], self.mash_water_formula)
        result["name"] = from_union([from_str, from_none], self.name)
        result["brewhouseEfficiency"] = from_union([from_int, from_none], self.brewhouse_efficiency)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["efficiencyType"] = from_union([from_str, from_none], self.efficiency_type)
        result["spargeWaterOverflow"] = from_union([from_str, from_none], self.sparge_water_overflow)
        result["spargeWaterFormula"] = from_union([from_str, from_none], self.sparge_water_formula)
        result["bottlingVolume"] = from_union([from_int, from_none], self.bottling_volume)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["trubChillerLoss"] = from_union([to_float, from_none], self.trub_chiller_loss)
        result["boilTime"] = from_union([from_int, from_none], self.boil_time)
        result["evaporationRate"] = from_union([to_float, from_none], self.evaporation_rate)
        result["hopstandTemperature"] = from_union([from_int, from_none], self.hopstand_temperature)
        result["calcStrikeWaterTemperature"] = from_union([from_bool, from_none], self.calc_strike_water_temperature)
        result["calcMashEfficiency"] = from_union([from_bool, from_none], self.calc_mash_efficiency)
        result["hopUtilization"] = from_union([from_int, from_none], self.hop_utilization)
        result["fermenterVolumeBeforeTopUp"] = from_union([from_int, from_none], self.fermenter_volume_before_top_up)
        result["mashTunDeadSpace"] = from_union([from_int, from_none], self.mash_tun_dead_space)
        result["mashEfficiency"] = from_union([to_float, from_none], self.mash_efficiency)
        result["waterCalculation"] = from_union([from_str, from_none], self.water_calculation)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["spargeWaterMax"] = from_union([from_int, from_none], self.sparge_water_max)
        result["fermenterLoss"] = from_union([from_int, from_none], self.fermenter_loss)
        result["spargeWaterReminderTime"] = from_union([from_int, from_none], self.sparge_water_reminder_time)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["postBoilKettleVol"] = from_union([to_float, from_none], self.post_boil_kettle_vol)
        result["batchSize"] = from_union([from_int, from_none], self.batch_size)
        result["fermenterVolume"] = from_union([from_int, from_none], self.fermenter_volume)
        result["mashWaterMax"] = from_union([from_int, from_none], self.mash_water_max)
        result["aromaHopUtilization"] = from_union([to_float, from_none], self.aroma_hop_utilization)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["boilOffPerHr"] = from_union([to_float, from_none], self.boil_off_per_hr)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["spargeWaterReminderEnabled"] = from_union([from_bool, from_none], self.sparge_water_reminder_enabled)
        result["calcBoilVolume"] = from_union([from_bool, from_none], self.calc_boil_volume)
        result["efficiency"] = from_union([from_int, from_none], self.efficiency)
        result["mashWaterMin"] = from_union([from_int, from_none], self.mash_water_min)
        result["fermenterLossEstimate"] = from_union([from_int, from_none], self.fermenter_loss_estimate)
        result["_meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["boilSize"] = from_union([to_float, from_none], self.boil_size)
        return result


@dataclass
class FermentationStep:
    pressure: None
    display_pressure: None
    step_time: Optional[int] = None
    display_step_temp: Optional[float] = None
    type: Optional[str] = None
    actual_time: Optional[int] = None
    step_temp: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FermentationStep':
        assert isinstance(obj, dict)
        pressure = from_none(obj.get("pressure"))
        display_pressure = from_none(obj.get("displayPressure"))
        step_time = from_union([from_int, from_none], obj.get("stepTime"))
        display_step_temp = from_union([from_float, from_none], obj.get("displayStepTemp"))
        type = from_union([from_str, from_none], obj.get("type"))
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        step_temp = from_union([from_float, from_none], obj.get("stepTemp"))
        return FermentationStep(pressure, display_pressure, step_time, display_step_temp, type, actual_time, step_temp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pressure"] = from_none(self.pressure)
        result["displayPressure"] = from_none(self.display_pressure)
        result["stepTime"] = from_union([from_int, from_none], self.step_time)
        result["displayStepTemp"] = from_union([from_float, from_none], self.display_step_temp)
        result["type"] = from_union([from_str, from_none], self.type)
        result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        result["stepTemp"] = from_union([from_float, from_none], self.step_temp)
        return result


@dataclass
class Fermentation:
    created: Optional[Created] = None
    version: Optional[str] = None
    steps: Optional[List[FermentationStep]] = None
    name: Optional[str] = None
    timestamp: Optional[Created] = None
    rev: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentation':
        assert isinstance(obj, dict)
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        version = from_union([from_str, from_none], obj.get("_version"))
        steps = from_union([lambda x: from_list(FermentationStep.from_dict, x), from_none], obj.get("steps"))
        name = from_union([from_str, from_none], obj.get("name"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        id = from_union([from_str, from_none], obj.get("_id"))
        return Fermentation(created, version, steps, name, timestamp, rev, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(FermentationStep, x), x), from_none], self.steps)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class MashStep:
    display_step_temp: Optional[int] = None
    name: Optional[str] = None
    step_time: Optional[int] = None
    ramp_time: Optional[int] = None
    step_temp: Optional[int] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MashStep':
        assert isinstance(obj, dict)
        display_step_temp = from_union([from_int, from_none], obj.get("displayStepTemp"))
        name = from_union([from_str, from_none], obj.get("name"))
        step_time = from_union([from_int, from_none], obj.get("stepTime"))
        ramp_time = from_union([from_int, from_none], obj.get("rampTime"))
        step_temp = from_union([from_int, from_none], obj.get("stepTemp"))
        type = from_union([from_str, from_none], obj.get("type"))
        return MashStep(display_step_temp, name, step_time, ramp_time, step_temp, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["displayStepTemp"] = from_union([from_int, from_none], self.display_step_temp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["stepTime"] = from_union([from_int, from_none], self.step_time)
        result["rampTime"] = from_union([from_int, from_none], self.ramp_time)
        result["stepTemp"] = from_union([from_int, from_none], self.step_temp)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class RecipeMash:
    steps: Optional[List[MashStep]] = None
    timestamp: Optional[Created] = None
    name: Optional[str] = None
    version: Optional[str] = None
    rev: Optional[str] = None
    id: Optional[str] = None
    created: Optional[Created] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeMash':
        assert isinstance(obj, dict)
        steps = from_union([lambda x: from_list(MashStep.from_dict, x), from_none], obj.get("steps"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
        version = from_union([from_str, from_none], obj.get("_version"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        id = from_union([from_str, from_none], obj.get("_id"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        return RecipeMash(steps, timestamp, name, version, rev, id, created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(MashStep, x), x), from_none], self.steps)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        return result


@dataclass
class Misc:
    time: None
    type: Optional[str] = None
    id: Optional[str] = None
    use: Optional[str] = None
    hidden: Optional[bool] = None
    time_is_days: Optional[bool] = None
    amount: Optional[float] = None
    concentration: Optional[int] = None
    rev: Optional[str] = None
    version: Optional[Version] = None
    timestamp_ms: Optional[int] = None
    unit: Optional[str] = None
    name: Optional[str] = None
    timestamp: Optional[Created] = None
    inventory: Optional[float] = None
    water_adjustment: Optional[bool] = None
    created: Optional[Created] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Misc':
        assert isinstance(obj, dict)
        time = from_none(obj.get("time"))
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("_id"))
        use = from_union([from_str, from_none], obj.get("use"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        time_is_days = from_union([from_bool, from_none], obj.get("timeIsDays"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        concentration = from_union([from_int, from_none], obj.get("concentration"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        version = from_union([Version, from_none], obj.get("_version"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        unit = from_union([from_str, from_none], obj.get("unit"))
        name = from_union([from_str, from_none], obj.get("name"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        water_adjustment = from_union([from_bool, from_none], obj.get("waterAdjustment"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        return Misc(time, type, id, use, hidden, time_is_days, amount, concentration, rev, version, timestamp_ms, unit, name, timestamp, inventory, water_adjustment, created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = from_none(self.time)
        result["type"] = from_union([from_str, from_none], self.type)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["use"] = from_union([from_str, from_none], self.use)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["timeIsDays"] = from_union([from_bool, from_none], self.time_is_days)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["concentration"] = from_union([from_int, from_none], self.concentration)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["unit"] = from_union([from_str, from_none], self.unit)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["waterAdjustment"] = from_union([from_bool, from_none], self.water_adjustment)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        return result


@dataclass
class Calories:
    carbs: Optional[float] = None
    alcohol: Optional[float] = None
    k_j: Optional[float] = None
    total: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Calories':
        assert isinstance(obj, dict)
        carbs = from_union([from_float, from_none], obj.get("carbs"))
        alcohol = from_union([from_float, from_none], obj.get("alcohol"))
        k_j = from_union([from_float, from_none], obj.get("kJ"))
        total = from_union([from_float, from_none], obj.get("total"))
        return Calories(carbs, alcohol, k_j, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["carbs"] = from_union([to_float, from_none], self.carbs)
        result["alcohol"] = from_union([to_float, from_none], self.alcohol)
        result["kJ"] = from_union([to_float, from_none], self.k_j)
        result["total"] = from_union([to_float, from_none], self.total)
        return result


@dataclass
class Carbs:
    total: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Carbs':
        assert isinstance(obj, dict)
        total = from_union([from_float, from_none], obj.get("total"))
        return Carbs(total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total"] = from_union([to_float, from_none], self.total)
        return result


@dataclass
class Nutrition:
    calories: Optional[Calories] = None
    carbs: Optional[Carbs] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Nutrition':
        assert isinstance(obj, dict)
        calories = from_union([Calories.from_dict, from_none], obj.get("calories"))
        carbs = from_union([Carbs.from_dict, from_none], obj.get("carbs"))
        return Nutrition(calories, carbs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["calories"] = from_union([lambda x: to_class(Calories, x), from_none], self.calories)
        result["carbs"] = from_union([lambda x: to_class(Carbs, x), from_none], self.carbs)
        return result


@dataclass
class Style:
    carb_max: None
    carb_min: None
    category_number: Optional[int] = None
    style_letter: Optional[str] = None
    abv_max: Optional[int] = None
    ibu_max: Optional[int] = None
    bu_gu_max: Optional[float] = None
    carbonation_style: Optional[str] = None
    fg_max: Optional[float] = None
    abv_min: Optional[float] = None
    bu_gu_min: Optional[float] = None
    fg_min: Optional[float] = None
    ibu_min: Optional[int] = None
    color_min: Optional[int] = None
    id: Optional[str] = None
    category: Optional[str] = None
    name: Optional[str] = None
    lovibond_min: Optional[int] = None
    type: Optional[str] = None
    rbr_max: Optional[float] = None
    color_max: Optional[int] = None
    og_min: Optional[float] = None
    rbr_min: Optional[float] = None
    style_guide: Optional[str] = None
    og_max: Optional[float] = None
    lovibond_max: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Style':
        assert isinstance(obj, dict)
        carb_max = from_none(obj.get("carbMax"))
        carb_min = from_none(obj.get("carbMin"))
        category_number = from_union([from_none, lambda x: int(from_str(x))], obj.get("categoryNumber"))
        style_letter = from_union([from_str, from_none], obj.get("styleLetter"))
        abv_max = from_union([from_int, from_none], obj.get("abvMax"))
        ibu_max = from_union([from_int, from_none], obj.get("ibuMax"))
        bu_gu_max = from_union([from_float, from_none], obj.get("buGuMax"))
        carbonation_style = from_union([from_str, from_none], obj.get("carbonationStyle"))
        fg_max = from_union([from_float, from_none], obj.get("fgMax"))
        abv_min = from_union([from_float, from_none], obj.get("abvMin"))
        bu_gu_min = from_union([from_float, from_none], obj.get("buGuMin"))
        fg_min = from_union([from_float, from_none], obj.get("fgMin"))
        ibu_min = from_union([from_int, from_none], obj.get("ibuMin"))
        color_min = from_union([from_int, from_none], obj.get("colorMin"))
        id = from_union([from_str, from_none], obj.get("_id"))
        category = from_union([from_str, from_none], obj.get("category"))
        name = from_union([from_str, from_none], obj.get("name"))
        lovibond_min = from_union([from_int, from_none], obj.get("lovibondMin"))
        type = from_union([from_str, from_none], obj.get("type"))
        rbr_max = from_union([from_float, from_none], obj.get("rbrMax"))
        color_max = from_union([from_int, from_none], obj.get("colorMax"))
        og_min = from_union([from_float, from_none], obj.get("ogMin"))
        rbr_min = from_union([from_float, from_none], obj.get("rbrMin"))
        style_guide = from_union([from_str, from_none], obj.get("styleGuide"))
        og_max = from_union([from_float, from_none], obj.get("ogMax"))
        lovibond_max = from_union([from_int, from_none], obj.get("lovibondMax"))
        return Style(carb_max, carb_min, category_number, style_letter, abv_max, ibu_max, bu_gu_max, carbonation_style, fg_max, abv_min, bu_gu_min, fg_min, ibu_min, color_min, id, category, name, lovibond_min, type, rbr_max, color_max, og_min, rbr_min, style_guide, og_max, lovibond_max)

    def to_dict(self) -> dict:
        result: dict = {}
        result["carbMax"] = from_none(self.carb_max)
        result["carbMin"] = from_none(self.carb_min)
        result["categoryNumber"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.category_number)
        result["styleLetter"] = from_union([from_str, from_none], self.style_letter)
        result["abvMax"] = from_union([from_int, from_none], self.abv_max)
        result["ibuMax"] = from_union([from_int, from_none], self.ibu_max)
        result["buGuMax"] = from_union([to_float, from_none], self.bu_gu_max)
        result["carbonationStyle"] = from_union([from_str, from_none], self.carbonation_style)
        result["fgMax"] = from_union([to_float, from_none], self.fg_max)
        result["abvMin"] = from_union([to_float, from_none], self.abv_min)
        result["buGuMin"] = from_union([to_float, from_none], self.bu_gu_min)
        result["fgMin"] = from_union([to_float, from_none], self.fg_min)
        result["ibuMin"] = from_union([from_int, from_none], self.ibu_min)
        result["colorMin"] = from_union([from_int, from_none], self.color_min)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["category"] = from_union([from_str, from_none], self.category)
        result["name"] = from_union([from_str, from_none], self.name)
        result["lovibondMin"] = from_union([from_int, from_none], self.lovibond_min)
        result["type"] = from_union([from_str, from_none], self.type)
        result["rbrMax"] = from_union([to_float, from_none], self.rbr_max)
        result["colorMax"] = from_union([from_int, from_none], self.color_max)
        result["ogMin"] = from_union([to_float, from_none], self.og_min)
        result["rbrMin"] = from_union([to_float, from_none], self.rbr_min)
        result["styleGuide"] = from_union([from_str, from_none], self.style_guide)
        result["ogMax"] = from_union([to_float, from_none], self.og_max)
        result["lovibondMax"] = from_union([from_int, from_none], self.lovibond_max)
        return result


@dataclass
class SourceClass:
    id: Optional[str] = None
    timestamp: Optional[Created] = None
    calcium: Optional[float] = None
    residual_alkalinity: Optional[float] = None
    type: Optional[str] = None
    ion_balance_off: Optional[bool] = None
    bicarbonate_meq_l: Optional[float] = None
    anions: Optional[float] = None
    created: Optional[Created] = None
    hardness: Optional[int] = None
    sodium: Optional[float] = None
    cations: Optional[float] = None
    name: Optional[str] = None
    rev: Optional[str] = None
    ph: Optional[float] = None
    version: Optional[Version] = None
    ion_balance: Optional[int] = None
    bicarbonate: Optional[int] = None
    hidden: Optional[bool] = None
    residual_alkalinity_meq_l_calc: Optional[float] = None
    alkalinity: Optional[float] = None
    timestamp_ms: Optional[int] = None
    so_cl_ratio: Optional[float] = None
    chloride: Optional[float] = None
    sulfate: Optional[float] = None
    magnesium: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SourceClass':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("_id"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        residual_alkalinity = from_union([from_float, from_none], obj.get("residualAlkalinity"))
        type = from_union([from_str, from_none], obj.get("type"))
        ion_balance_off = from_union([from_bool, from_none], obj.get("ionBalanceOff"))
        bicarbonate_meq_l = from_union([from_float, from_none], obj.get("bicarbonateMeqL"))
        anions = from_union([from_float, from_none], obj.get("anions"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        hardness = from_union([from_int, from_none], obj.get("hardness"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        cations = from_union([from_float, from_none], obj.get("cations"))
        name = from_union([from_str, from_none], obj.get("name"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        ph = from_union([from_float, from_none], obj.get("ph"))
        version = from_union([Version, from_none], obj.get("_version"))
        ion_balance = from_union([from_int, from_none], obj.get("ionBalance"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        residual_alkalinity_meq_l_calc = from_union([from_float, from_none], obj.get("residualAlkalinityMeqLCalc"))
        alkalinity = from_union([from_float, from_none], obj.get("alkalinity"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        so_cl_ratio = from_union([from_float, from_none], obj.get("soClRatio"))
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        return SourceClass(id, timestamp, calcium, residual_alkalinity, type, ion_balance_off, bicarbonate_meq_l, anions, created, hardness, sodium, cations, name, rev, ph, version, ion_balance, bicarbonate, hidden, residual_alkalinity_meq_l_calc, alkalinity, timestamp_ms, so_cl_ratio, chloride, sulfate, magnesium)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_id"] = from_union([from_str, from_none], self.id)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["residualAlkalinity"] = from_union([to_float, from_none], self.residual_alkalinity)
        result["type"] = from_union([from_str, from_none], self.type)
        result["ionBalanceOff"] = from_union([from_bool, from_none], self.ion_balance_off)
        result["bicarbonateMeqL"] = from_union([to_float, from_none], self.bicarbonate_meq_l)
        result["anions"] = from_union([to_float, from_none], self.anions)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["hardness"] = from_union([from_int, from_none], self.hardness)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["cations"] = from_union([to_float, from_none], self.cations)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["ph"] = from_union([to_float, from_none], self.ph)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["ionBalance"] = from_union([from_int, from_none], self.ion_balance)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["residualAlkalinityMeqLCalc"] = from_union([to_float, from_none], self.residual_alkalinity_meq_l_calc)
        result["alkalinity"] = from_union([to_float, from_none], self.alkalinity)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["soClRatio"] = from_union([to_float, from_none], self.so_cl_ratio)
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        return result


@dataclass
class Acid:
    type: Optional[str] = None
    concentration: Optional[int] = None
    alkalinity_meq_l: Optional[float] = None
    amount: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Acid':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        concentration = from_union([from_int, from_none], obj.get("concentration"))
        alkalinity_meq_l = from_union([from_float, from_none], obj.get("alkalinityMeqL"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        return Acid(type, concentration, alkalinity_meq_l, amount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["concentration"] = from_union([from_int, from_none], self.concentration)
        result["alkalinityMeqL"] = from_union([to_float, from_none], self.alkalinity_meq_l)
        result["amount"] = from_union([to_float, from_none], self.amount)
        return result


@dataclass
class Adjustments:
    magnesium: Optional[float] = None
    bicarbonate: Optional[int] = None
    sodium_bicarbonate: Optional[int] = None
    calcium_carbonate: Optional[int] = None
    volume: Optional[float] = None
    calcium_chloride: Optional[int] = None
    lt_ams: Optional[int] = None
    lt_dwb: Optional[int] = None
    sodium_chloride: Optional[float] = None
    sodium: Optional[float] = None
    calcium_hydroxide: Optional[int] = None
    chloride: Optional[float] = None
    magnesium_chloride: Optional[int] = None
    sulfate: Optional[float] = None
    calcium_sulfate: Optional[float] = None
    sodium_metabisulfite: Optional[int] = None
    magnesium_sulfate: Optional[float] = None
    acids: Optional[List[Acid]] = None
    calcium: Optional[float] = None
    sodium_metabisulfite_ppm: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Adjustments':
        assert isinstance(obj, dict)
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        sodium_bicarbonate = from_union([from_int, from_none], obj.get("sodiumBicarbonate"))
        calcium_carbonate = from_union([from_int, from_none], obj.get("calciumCarbonate"))
        volume = from_union([from_float, from_none], obj.get("volume"))
        calcium_chloride = from_union([from_int, from_none], obj.get("calciumChloride"))
        lt_ams = from_union([from_int, from_none], obj.get("ltAMS"))
        lt_dwb = from_union([from_int, from_none], obj.get("ltDWB"))
        sodium_chloride = from_union([from_float, from_none], obj.get("sodiumChloride"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        calcium_hydroxide = from_union([from_int, from_none], obj.get("calciumHydroxide"))
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        magnesium_chloride = from_union([from_int, from_none], obj.get("magnesiumChloride"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        calcium_sulfate = from_union([from_float, from_none], obj.get("calciumSulfate"))
        sodium_metabisulfite = from_union([from_int, from_none], obj.get("sodiumMetabisulfite"))
        magnesium_sulfate = from_union([from_float, from_none], obj.get("magnesiumSulfate"))
        acids = from_union([lambda x: from_list(Acid.from_dict, x), from_none], obj.get("acids"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        sodium_metabisulfite_ppm = from_union([from_int, from_none], obj.get("sodiumMetabisulfitePPM"))
        return Adjustments(magnesium, bicarbonate, sodium_bicarbonate, calcium_carbonate, volume, calcium_chloride, lt_ams, lt_dwb, sodium_chloride, sodium, calcium_hydroxide, chloride, magnesium_chloride, sulfate, calcium_sulfate, sodium_metabisulfite, magnesium_sulfate, acids, calcium, sodium_metabisulfite_ppm)

    def to_dict(self) -> dict:
        result: dict = {}
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["sodiumBicarbonate"] = from_union([from_int, from_none], self.sodium_bicarbonate)
        result["calciumCarbonate"] = from_union([from_int, from_none], self.calcium_carbonate)
        result["volume"] = from_union([to_float, from_none], self.volume)
        result["calciumChloride"] = from_union([from_int, from_none], self.calcium_chloride)
        result["ltAMS"] = from_union([from_int, from_none], self.lt_ams)
        result["ltDWB"] = from_union([from_int, from_none], self.lt_dwb)
        result["sodiumChloride"] = from_union([to_float, from_none], self.sodium_chloride)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["calciumHydroxide"] = from_union([from_int, from_none], self.calcium_hydroxide)
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["magnesiumChloride"] = from_union([from_int, from_none], self.magnesium_chloride)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["calciumSulfate"] = from_union([to_float, from_none], self.calcium_sulfate)
        result["sodiumMetabisulfite"] = from_union([from_int, from_none], self.sodium_metabisulfite)
        result["magnesiumSulfate"] = from_union([to_float, from_none], self.magnesium_sulfate)
        result["acids"] = from_union([lambda x: from_list(lambda x: to_class(Acid, x), x), from_none], self.acids)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["sodiumMetabisulfitePPM"] = from_union([from_int, from_none], self.sodium_metabisulfite_ppm)
        return result


@dataclass
class MashTargetDiff:
    so_cl_ratio: Optional[float] = None
    cations: Optional[float] = None
    sulfate: Optional[float] = None
    anions: Optional[float] = None
    calcium: Optional[float] = None
    ion_balance: Optional[int] = None
    residual_alkalinity_meq_l_calc: Optional[float] = None
    magnesium: Optional[float] = None
    chloride: Optional[float] = None
    bicarbonate_meq_l: Optional[float] = None
    hardness: Optional[int] = None
    residual_alkalinity: Optional[float] = None
    ion_balance_off: Optional[bool] = None
    sodium: Optional[float] = None
    bicarbonate: Optional[int] = None
    alkalinity: Optional[float] = None
    description: Optional[str] = None
    type: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MashTargetDiff':
        assert isinstance(obj, dict)
        so_cl_ratio = from_union([from_float, from_none], obj.get("soClRatio"))
        cations = from_union([from_float, from_none], obj.get("cations"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        anions = from_union([from_float, from_none], obj.get("anions"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        ion_balance = from_union([from_int, from_none], obj.get("ionBalance"))
        residual_alkalinity_meq_l_calc = from_union([from_float, from_none], obj.get("residualAlkalinityMeqLCalc"))
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        bicarbonate_meq_l = from_union([from_float, from_none], obj.get("bicarbonateMeqL"))
        hardness = from_union([from_int, from_none], obj.get("hardness"))
        residual_alkalinity = from_union([from_float, from_none], obj.get("residualAlkalinity"))
        ion_balance_off = from_union([from_bool, from_none], obj.get("ionBalanceOff"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        alkalinity = from_union([from_float, from_none], obj.get("alkalinity"))
        description = from_union([from_str, from_none], obj.get("description"))
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return MashTargetDiff(so_cl_ratio, cations, sulfate, anions, calcium, ion_balance, residual_alkalinity_meq_l_calc, magnesium, chloride, bicarbonate_meq_l, hardness, residual_alkalinity, ion_balance_off, sodium, bicarbonate, alkalinity, description, type, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["soClRatio"] = from_union([to_float, from_none], self.so_cl_ratio)
        result["cations"] = from_union([to_float, from_none], self.cations)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["anions"] = from_union([to_float, from_none], self.anions)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["ionBalance"] = from_union([from_int, from_none], self.ion_balance)
        result["residualAlkalinityMeqLCalc"] = from_union([to_float, from_none], self.residual_alkalinity_meq_l_calc)
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["bicarbonateMeqL"] = from_union([to_float, from_none], self.bicarbonate_meq_l)
        result["hardness"] = from_union([from_int, from_none], self.hardness)
        result["residualAlkalinity"] = from_union([to_float, from_none], self.residual_alkalinity)
        result["ionBalanceOff"] = from_union([from_bool, from_none], self.ion_balance_off)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["alkalinity"] = from_union([to_float, from_none], self.alkalinity)
        result["description"] = from_union([from_str, from_none], self.description)
        result["type"] = from_union([from_str, from_none], self.type)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class MetaClass:
    equal_source_total: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MetaClass':
        assert isinstance(obj, dict)
        equal_source_total = from_union([from_bool, from_none], obj.get("equalSourceTotal"))
        return MetaClass(equal_source_total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["equalSourceTotal"] = from_union([from_bool, from_none], self.equal_source_total)
        return result


@dataclass
class CalciumChloride:
    auto: Optional[bool] = None
    mash: Optional[bool] = None
    form: Optional[str] = None
    sparge: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CalciumChloride':
        assert isinstance(obj, dict)
        auto = from_union([from_bool, from_none], obj.get("auto"))
        mash = from_union([from_bool, from_none], obj.get("mash"))
        form = from_union([from_str, from_none], obj.get("form"))
        sparge = from_union([from_bool, from_none], obj.get("sparge"))
        return CalciumChloride(auto, mash, form, sparge)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auto"] = from_union([from_bool, from_none], self.auto)
        result["mash"] = from_union([from_bool, from_none], self.mash)
        result["form"] = from_union([from_str, from_none], self.form)
        result["sparge"] = from_union([from_bool, from_none], self.sparge)
        return result


@dataclass
class WaterSettings:
    calcium_hydroxide: Optional[CalciumChloride] = None
    calcium_chloride: Optional[CalciumChloride] = None
    adjust_sparge: Optional[bool] = None
    magnesium_sulfate: Optional[CalciumChloride] = None
    sodium_chloride: Optional[CalciumChloride] = None
    calcium_sulfate: Optional[CalciumChloride] = None
    sodium_bicarbonate: Optional[CalciumChloride] = None
    magnesium_chloride: Optional[CalciumChloride] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WaterSettings':
        assert isinstance(obj, dict)
        calcium_hydroxide = from_union([CalciumChloride.from_dict, from_none], obj.get("calciumHydroxide"))
        calcium_chloride = from_union([CalciumChloride.from_dict, from_none], obj.get("calciumChloride"))
        adjust_sparge = from_union([from_bool, from_none], obj.get("adjustSparge"))
        magnesium_sulfate = from_union([CalciumChloride.from_dict, from_none], obj.get("magnesiumSulfate"))
        sodium_chloride = from_union([CalciumChloride.from_dict, from_none], obj.get("sodiumChloride"))
        calcium_sulfate = from_union([CalciumChloride.from_dict, from_none], obj.get("calciumSulfate"))
        sodium_bicarbonate = from_union([CalciumChloride.from_dict, from_none], obj.get("sodiumBicarbonate"))
        magnesium_chloride = from_union([CalciumChloride.from_dict, from_none], obj.get("magnesiumChloride"))
        return WaterSettings(calcium_hydroxide, calcium_chloride, adjust_sparge, magnesium_sulfate, sodium_chloride, calcium_sulfate, sodium_bicarbonate, magnesium_chloride)

    def to_dict(self) -> dict:
        result: dict = {}
        result["calciumHydroxide"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.calcium_hydroxide)
        result["calciumChloride"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.calcium_chloride)
        result["adjustSparge"] = from_union([from_bool, from_none], self.adjust_sparge)
        result["magnesiumSulfate"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.magnesium_sulfate)
        result["sodiumChloride"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.sodium_chloride)
        result["calciumSulfate"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.calcium_sulfate)
        result["sodiumBicarbonate"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.sodium_bicarbonate)
        result["magnesiumChloride"] = from_union([lambda x: to_class(CalciumChloride, x), from_none], self.magnesium_chloride)
        return result


@dataclass
class SpargeAdjustments:
    volume: Optional[float] = None
    sulfate: Optional[int] = None
    bicarbonate: Optional[int] = None
    sodium: Optional[int] = None
    acids: Optional[List[Acid]] = None
    chloride: Optional[int] = None
    calcium: Optional[int] = None
    magnesium: Optional[int] = None
    sodium_metabisulfite_ppm: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SpargeAdjustments':
        assert isinstance(obj, dict)
        volume = from_union([from_float, from_none], obj.get("volume"))
        sulfate = from_union([from_int, from_none], obj.get("sulfate"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        sodium = from_union([from_int, from_none], obj.get("sodium"))
        acids = from_union([lambda x: from_list(Acid.from_dict, x), from_none], obj.get("acids"))
        chloride = from_union([from_int, from_none], obj.get("chloride"))
        calcium = from_union([from_int, from_none], obj.get("calcium"))
        magnesium = from_union([from_int, from_none], obj.get("magnesium"))
        sodium_metabisulfite_ppm = from_union([from_int, from_none], obj.get("sodiumMetabisulfitePPM"))
        return SpargeAdjustments(volume, sulfate, bicarbonate, sodium, acids, chloride, calcium, magnesium, sodium_metabisulfite_ppm)

    def to_dict(self) -> dict:
        result: dict = {}
        result["volume"] = from_union([to_float, from_none], self.volume)
        result["sulfate"] = from_union([from_int, from_none], self.sulfate)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["sodium"] = from_union([from_int, from_none], self.sodium)
        result["acids"] = from_union([lambda x: from_list(lambda x: to_class(Acid, x), x), from_none], self.acids)
        result["chloride"] = from_union([from_int, from_none], self.chloride)
        result["calcium"] = from_union([from_int, from_none], self.calcium)
        result["magnesium"] = from_union([from_int, from_none], self.magnesium)
        result["sodiumMetabisulfitePPM"] = from_union([from_int, from_none], self.sodium_metabisulfite_ppm)
        return result


@dataclass
class Water:
    diluted: None
    mash_water_amount: None
    sparge_water_amount: None
    dilution_percentage: None
    acid_ph_adjustment: Optional[float] = None
    mash: Optional[SourceClass] = None
    enable_sparge_adjustments: Optional[bool] = None
    meta: Optional[MetaClass] = None
    source: Optional[SourceClass] = None
    mash_ph: Optional[float] = None
    mash_ph_distilled: Optional[float] = None
    mash_adjustments: Optional[Adjustments] = None
    enable_acid_adjustments: Optional[bool] = None
    sparge_target_diff: Optional[MashTargetDiff] = None
    source_target_diff: Optional[MashTargetDiff] = None
    total: Optional[SourceClass] = None
    total_target_diff: Optional[MashTargetDiff] = None
    sparge_acid_ph_adjustment: Optional[int] = None
    sparge_adjustments: Optional[SpargeAdjustments] = None
    sparge: Optional[SourceClass] = None
    target: Optional[MashTargetDiff] = None
    mash_target_diff: Optional[MashTargetDiff] = None
    style: Optional[str] = None
    total_adjustments: Optional[Adjustments] = None
    settings: Optional[WaterSettings] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Water':
        assert isinstance(obj, dict)
        diluted = from_none(obj.get("diluted"))
        mash_water_amount = from_none(obj.get("mashWaterAmount"))
        sparge_water_amount = from_none(obj.get("spargeWaterAmount"))
        dilution_percentage = from_none(obj.get("dilutionPercentage"))
        acid_ph_adjustment = from_union([from_float, from_none], obj.get("acidPhAdjustment"))
        mash = from_union([SourceClass.from_dict, from_none], obj.get("mash"))
        enable_sparge_adjustments = from_union([from_bool, from_none], obj.get("enableSpargeAdjustments"))
        meta = from_union([MetaClass.from_dict, from_none], obj.get("meta"))
        source = from_union([SourceClass.from_dict, from_none], obj.get("source"))
        mash_ph = from_union([from_float, from_none], obj.get("mashPh"))
        mash_ph_distilled = from_union([from_float, from_none], obj.get("mashPhDistilled"))
        mash_adjustments = from_union([Adjustments.from_dict, from_none], obj.get("mashAdjustments"))
        enable_acid_adjustments = from_union([from_bool, from_none], obj.get("enableAcidAdjustments"))
        sparge_target_diff = from_union([MashTargetDiff.from_dict, from_none], obj.get("spargeTargetDiff"))
        source_target_diff = from_union([MashTargetDiff.from_dict, from_none], obj.get("sourceTargetDiff"))
        total = from_union([SourceClass.from_dict, from_none], obj.get("total"))
        total_target_diff = from_union([MashTargetDiff.from_dict, from_none], obj.get("totalTargetDiff"))
        sparge_acid_ph_adjustment = from_union([from_int, from_none], obj.get("spargeAcidPhAdjustment"))
        sparge_adjustments = from_union([SpargeAdjustments.from_dict, from_none], obj.get("spargeAdjustments"))
        sparge = from_union([SourceClass.from_dict, from_none], obj.get("sparge"))
        target = from_union([MashTargetDiff.from_dict, from_none], obj.get("target"))
        mash_target_diff = from_union([MashTargetDiff.from_dict, from_none], obj.get("mashTargetDiff"))
        style = from_union([from_str, from_none], obj.get("style"))
        total_adjustments = from_union([Adjustments.from_dict, from_none], obj.get("totalAdjustments"))
        settings = from_union([WaterSettings.from_dict, from_none], obj.get("settings"))
        return Water(diluted, mash_water_amount, sparge_water_amount, dilution_percentage, acid_ph_adjustment, mash, enable_sparge_adjustments, meta, source, mash_ph, mash_ph_distilled, mash_adjustments, enable_acid_adjustments, sparge_target_diff, source_target_diff, total, total_target_diff, sparge_acid_ph_adjustment, sparge_adjustments, sparge, target, mash_target_diff, style, total_adjustments, settings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["diluted"] = from_none(self.diluted)
        result["mashWaterAmount"] = from_none(self.mash_water_amount)
        result["spargeWaterAmount"] = from_none(self.sparge_water_amount)
        result["dilutionPercentage"] = from_none(self.dilution_percentage)
        result["acidPhAdjustment"] = from_union([to_float, from_none], self.acid_ph_adjustment)
        result["mash"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.mash)
        result["enableSpargeAdjustments"] = from_union([from_bool, from_none], self.enable_sparge_adjustments)
        result["meta"] = from_union([lambda x: to_class(MetaClass, x), from_none], self.meta)
        result["source"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.source)
        result["mashPh"] = from_union([to_float, from_none], self.mash_ph)
        result["mashPhDistilled"] = from_union([to_float, from_none], self.mash_ph_distilled)
        result["mashAdjustments"] = from_union([lambda x: to_class(Adjustments, x), from_none], self.mash_adjustments)
        result["enableAcidAdjustments"] = from_union([from_bool, from_none], self.enable_acid_adjustments)
        result["spargeTargetDiff"] = from_union([lambda x: to_class(MashTargetDiff, x), from_none], self.sparge_target_diff)
        result["sourceTargetDiff"] = from_union([lambda x: to_class(MashTargetDiff, x), from_none], self.source_target_diff)
        result["total"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.total)
        result["totalTargetDiff"] = from_union([lambda x: to_class(MashTargetDiff, x), from_none], self.total_target_diff)
        result["spargeAcidPhAdjustment"] = from_union([from_int, from_none], self.sparge_acid_ph_adjustment)
        result["spargeAdjustments"] = from_union([lambda x: to_class(SpargeAdjustments, x), from_none], self.sparge_adjustments)
        result["sparge"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.sparge)
        result["target"] = from_union([lambda x: to_class(MashTargetDiff, x), from_none], self.target)
        result["mashTargetDiff"] = from_union([lambda x: to_class(MashTargetDiff, x), from_none], self.mash_target_diff)
        result["style"] = from_union([from_str, from_none], self.style)
        result["totalAdjustments"] = from_union([lambda x: to_class(Adjustments, x), from_none], self.total_adjustments)
        result["settings"] = from_union([lambda x: to_class(WaterSettings, x), from_none], self.settings)
        return result


@dataclass
class Yeast:
    starter_size: None
    starter: None
    id: Optional[str] = None
    name: Optional[str] = None
    ferments_all: Optional[bool] = None
    attenuation: Optional[int] = None
    amount: Optional[int] = None
    max_temp: Optional[int] = None
    min_temp: Optional[int] = None
    form: Optional[str] = None
    product_id: Optional[str] = None
    laboratory: Optional[str] = None
    unit: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    flocculation: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Yeast':
        assert isinstance(obj, dict)
        starter_size = from_none(obj.get("starterSize"))
        starter = from_none(obj.get("starter"))
        id = from_union([from_str, from_none], obj.get("_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        ferments_all = from_union([from_bool, from_none], obj.get("fermentsAll"))
        attenuation = from_union([from_int, from_none], obj.get("attenuation"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        max_temp = from_union([from_int, from_none], obj.get("maxTemp"))
        min_temp = from_union([from_int, from_none], obj.get("minTemp"))
        form = from_union([from_str, from_none], obj.get("form"))
        product_id = from_union([from_str, from_none], obj.get("productId"))
        laboratory = from_union([from_str, from_none], obj.get("laboratory"))
        unit = from_union([from_str, from_none], obj.get("unit"))
        type = from_union([from_str, from_none], obj.get("type"))
        description = from_union([from_str, from_none], obj.get("description"))
        flocculation = from_union([from_str, from_none], obj.get("flocculation"))
        return Yeast(starter_size, starter, id, name, ferments_all, attenuation, amount, max_temp, min_temp, form, product_id, laboratory, unit, type, description, flocculation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["starterSize"] = from_none(self.starter_size)
        result["starter"] = from_none(self.starter)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["fermentsAll"] = from_union([from_bool, from_none], self.ferments_all)
        result["attenuation"] = from_union([from_int, from_none], self.attenuation)
        result["amount"] = from_union([from_int, from_none], self.amount)
        result["maxTemp"] = from_union([from_int, from_none], self.max_temp)
        result["minTemp"] = from_union([from_int, from_none], self.min_temp)
        result["form"] = from_union([from_str, from_none], self.form)
        result["productId"] = from_union([from_str, from_none], self.product_id)
        result["laboratory"] = from_union([from_str, from_none], self.laboratory)
        result["unit"] = from_union([from_str, from_none], self.unit)
        result["type"] = from_union([from_str, from_none], self.type)
        result["description"] = from_union([from_str, from_none], self.description)
        result["flocculation"] = from_union([from_str, from_none], self.flocculation)
        return result


@dataclass
class Recipe:
    first_wort_gravity: None
    yeast_tolerance_exceeded_by: None
    recipe_origin: None
    tags: None
    share: None
    author: Optional[str] = None
    style_rbr: Optional[bool] = None
    og: Optional[float] = None
    init: Optional[bool] = None
    style_fg: Optional[bool] = None
    boil_size: Optional[float] = None
    created: Optional[Created] = None
    type: Optional[str] = None
    fermentable_ibu: Optional[int] = None
    hops_total_amount: Optional[float] = None
    public: Optional[bool] = None
    recipe_type: Optional[str] = None
    equipment: Optional[Equipment] = None
    primary_temp: Optional[int] = None
    style_og: Optional[bool] = None
    search_tags: Optional[List[str]] = None
    timestamp: Optional[Created] = None
    style_bu_gu: Optional[bool] = None
    path: Optional[str] = None
    total_gravity: Optional[float] = None
    water: Optional[Water] = None
    bu_gu_ratio: Optional[float] = None
    post_boil_gravity: Optional[float] = None
    hidden: Optional[bool] = None
    fermentables_total_amount: Optional[float] = None
    style_conformity: Optional[bool] = None
    version: Optional[Version] = None
    fg_estimated: Optional[float] = None
    data: Optional[Data] = None
    sum_dry_hop_per_liter: Optional[int] = None
    carbonation_style: Optional[CarbonationStyle] = None
    rb_ratio: Optional[float] = None
    fermentables: Optional[List[Fermentable]] = None
    defaults: Optional[Defaults] = None
    nutrition: Optional[Nutrition] = None
    img: Optional[str] = None
    carbonation: Optional[float] = None
    uid: Optional[str] = None
    style_carb: Optional[bool] = None
    style_abv: Optional[bool] = None
    teaser: Optional[str] = None
    ev: Optional[float] = None
    attenuation: Optional[float] = None
    rev: Optional[str] = None
    hops: Optional[List[Hop]] = None
    thumb: Optional[str] = None
    origin: Optional[str] = None
    miscs: Optional[List[Misc]] = None
    name: Optional[str] = None
    style_color: Optional[bool] = None
    og_plato: Optional[float] = None
    ibu: Optional[int] = None
    style_ibu: Optional[bool] = None
    batch_size: Optional[int] = None
    mash: Optional[RecipeMash] = None
    boil_time: Optional[int] = None
    timestamp_ms: Optional[int] = None
    efficiency: Optional[int] = None
    fg_formula: Optional[str] = None
    extra_gravity: Optional[int] = None
    yeasts: Optional[List[Yeast]] = None
    diastatic_power: Optional[float] = None
    recipe_public: Optional[bool] = None
    style: Optional[Style] = None
    avg_weighted_hopstand_temp: Optional[int] = None
    pre_boil_gravity: Optional[float] = None
    fg: Optional[float] = None
    id: Optional[str] = None
    hop_stand_minutes: Optional[int] = None
    notes: Optional[str] = None
    ibu_formula: Optional[str] = None
    color: Optional[float] = None
    mash_efficiency: Optional[float] = None
    abv: Optional[float] = None
    fermentation: Optional[Fermentation] = None
    img_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        first_wort_gravity = from_none(obj.get("firstWortGravity"))
        yeast_tolerance_exceeded_by = from_none(obj.get("yeastToleranceExceededBy"))
        recipe_origin = from_none(obj.get("origin"))
        tags = from_none(obj.get("tags"))
        share = from_none(obj.get("_share"))
        author = from_union([from_str, from_none], obj.get("author"))
        style_rbr = from_union([from_bool, from_none], obj.get("styleRbr"))
        og = from_union([from_float, from_none], obj.get("og"))
        init = from_union([from_bool, from_none], obj.get("_init"))
        style_fg = from_union([from_bool, from_none], obj.get("styleFg"))
        boil_size = from_union([from_float, from_none], obj.get("boilSize"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        type = from_union([from_str, from_none], obj.get("_type"))
        fermentable_ibu = from_union([from_int, from_none], obj.get("fermentableIbu"))
        hops_total_amount = from_union([from_float, from_none], obj.get("hopsTotalAmount"))
        public = from_union([from_bool, from_none], obj.get("_public"))
        recipe_type = from_union([from_str, from_none], obj.get("type"))
        equipment = from_union([Equipment.from_dict, from_none], obj.get("equipment"))
        primary_temp = from_union([from_int, from_none], obj.get("primaryTemp"))
        style_og = from_union([from_bool, from_none], obj.get("styleOg"))
        search_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("searchTags"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        style_bu_gu = from_union([from_bool, from_none], obj.get("styleBuGu"))
        path = from_union([from_str, from_none], obj.get("path"))
        total_gravity = from_union([from_float, from_none], obj.get("totalGravity"))
        water = from_union([Water.from_dict, from_none], obj.get("water"))
        bu_gu_ratio = from_union([from_float, from_none], obj.get("buGuRatio"))
        post_boil_gravity = from_union([from_float, from_none], obj.get("postBoilGravity"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        fermentables_total_amount = from_union([from_float, from_none], obj.get("fermentablesTotalAmount"))
        style_conformity = from_union([from_bool, from_none], obj.get("styleConformity"))
        version = from_union([Version, from_none], obj.get("_version"))
        fg_estimated = from_union([from_float, from_none], obj.get("fgEstimated"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        sum_dry_hop_per_liter = from_union([from_int, from_none], obj.get("sumDryHopPerLiter"))
        carbonation_style = from_union([CarbonationStyle.from_dict, from_none], obj.get("carbonationStyle"))
        rb_ratio = from_union([from_float, from_none], obj.get("rbRatio"))
        fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("fermentables"))
        defaults = from_union([Defaults.from_dict, from_none], obj.get("defaults"))
        nutrition = from_union([Nutrition.from_dict, from_none], obj.get("nutrition"))
        img = from_union([from_str, from_none], obj.get("img"))
        carbonation = from_union([from_float, from_none], obj.get("carbonation"))
        uid = from_union([from_str, from_none], obj.get("_uid"))
        style_carb = from_union([from_bool, from_none], obj.get("styleCarb"))
        style_abv = from_union([from_bool, from_none], obj.get("styleAbv"))
        teaser = from_union([from_str, from_none], obj.get("teaser"))
        ev = from_union([from_float, from_none], obj.get("_ev"))
        attenuation = from_union([from_float, from_none], obj.get("attenuation"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        hops = from_union([lambda x: from_list(Hop.from_dict, x), from_none], obj.get("hops"))
        thumb = from_union([from_str, from_none], obj.get("thumb"))
        origin = from_union([from_str, from_none], obj.get("_origin"))
        miscs = from_union([lambda x: from_list(Misc.from_dict, x), from_none], obj.get("miscs"))
        name = from_union([from_str, from_none], obj.get("name"))
        style_color = from_union([from_bool, from_none], obj.get("styleColor"))
        og_plato = from_union([from_float, from_none], obj.get("ogPlato"))
        ibu = from_union([from_int, from_none], obj.get("ibu"))
        style_ibu = from_union([from_bool, from_none], obj.get("styleIbu"))
        batch_size = from_union([from_int, from_none], obj.get("batchSize"))
        mash = from_union([RecipeMash.from_dict, from_none], obj.get("mash"))
        boil_time = from_union([from_int, from_none], obj.get("boilTime"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        efficiency = from_union([from_int, from_none], obj.get("efficiency"))
        fg_formula = from_union([from_str, from_none], obj.get("fgFormula"))
        extra_gravity = from_union([from_int, from_none], obj.get("extraGravity"))
        yeasts = from_union([lambda x: from_list(Yeast.from_dict, x), from_none], obj.get("yeasts"))
        diastatic_power = from_union([from_float, from_none], obj.get("diastaticPower"))
        recipe_public = from_union([from_bool, from_none], obj.get("public"))
        style = from_union([Style.from_dict, from_none], obj.get("style"))
        avg_weighted_hopstand_temp = from_union([from_int, from_none], obj.get("avgWeightedHopstandTemp"))
        pre_boil_gravity = from_union([from_float, from_none], obj.get("preBoilGravity"))
        fg = from_union([from_float, from_none], obj.get("fg"))
        id = from_union([from_str, from_none], obj.get("_id"))
        hop_stand_minutes = from_union([from_int, from_none], obj.get("hopStandMinutes"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        ibu_formula = from_union([from_str, from_none], obj.get("ibuFormula"))
        color = from_union([from_float, from_none], obj.get("color"))
        mash_efficiency = from_union([from_float, from_none], obj.get("mashEfficiency"))
        abv = from_union([from_float, from_none], obj.get("abv"))
        fermentation = from_union([Fermentation.from_dict, from_none], obj.get("fermentation"))
        img_url = from_union([from_str, from_none], obj.get("img_url"))
        return Recipe(first_wort_gravity, yeast_tolerance_exceeded_by, recipe_origin, tags, share, author, style_rbr, og, init, style_fg, boil_size, created, type, fermentable_ibu, hops_total_amount, public, recipe_type, equipment, primary_temp, style_og, search_tags, timestamp, style_bu_gu, path, total_gravity, water, bu_gu_ratio, post_boil_gravity, hidden, fermentables_total_amount, style_conformity, version, fg_estimated, data, sum_dry_hop_per_liter, carbonation_style, rb_ratio, fermentables, defaults, nutrition, img, carbonation, uid, style_carb, style_abv, teaser, ev, attenuation, rev, hops, thumb, origin, miscs, name, style_color, og_plato, ibu, style_ibu, batch_size, mash, boil_time, timestamp_ms, efficiency, fg_formula, extra_gravity, yeasts, diastatic_power, recipe_public, style, avg_weighted_hopstand_temp, pre_boil_gravity, fg, id, hop_stand_minutes, notes, ibu_formula, color, mash_efficiency, abv, fermentation, img_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["firstWortGravity"] = from_none(self.first_wort_gravity)
        result["yeastToleranceExceededBy"] = from_none(self.yeast_tolerance_exceeded_by)
        result["origin"] = from_none(self.recipe_origin)
        result["tags"] = from_none(self.tags)
        result["_share"] = from_none(self.share)
        result["author"] = from_union([from_str, from_none], self.author)
        result["styleRbr"] = from_union([from_bool, from_none], self.style_rbr)
        result["og"] = from_union([to_float, from_none], self.og)
        result["_init"] = from_union([from_bool, from_none], self.init)
        result["styleFg"] = from_union([from_bool, from_none], self.style_fg)
        result["boilSize"] = from_union([to_float, from_none], self.boil_size)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_type"] = from_union([from_str, from_none], self.type)
        result["fermentableIbu"] = from_union([from_int, from_none], self.fermentable_ibu)
        result["hopsTotalAmount"] = from_union([to_float, from_none], self.hops_total_amount)
        result["_public"] = from_union([from_bool, from_none], self.public)
        result["type"] = from_union([from_str, from_none], self.recipe_type)
        result["equipment"] = from_union([lambda x: to_class(Equipment, x), from_none], self.equipment)
        result["primaryTemp"] = from_union([from_int, from_none], self.primary_temp)
        result["styleOg"] = from_union([from_bool, from_none], self.style_og)
        result["searchTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.search_tags)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["styleBuGu"] = from_union([from_bool, from_none], self.style_bu_gu)
        result["path"] = from_union([from_str, from_none], self.path)
        result["totalGravity"] = from_union([to_float, from_none], self.total_gravity)
        result["water"] = from_union([lambda x: to_class(Water, x), from_none], self.water)
        result["buGuRatio"] = from_union([to_float, from_none], self.bu_gu_ratio)
        result["postBoilGravity"] = from_union([to_float, from_none], self.post_boil_gravity)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["fermentablesTotalAmount"] = from_union([to_float, from_none], self.fermentables_total_amount)
        result["styleConformity"] = from_union([from_bool, from_none], self.style_conformity)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["fgEstimated"] = from_union([to_float, from_none], self.fg_estimated)
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["sumDryHopPerLiter"] = from_union([from_int, from_none], self.sum_dry_hop_per_liter)
        result["carbonationStyle"] = from_union([lambda x: to_class(CarbonationStyle, x), from_none], self.carbonation_style)
        result["rbRatio"] = from_union([to_float, from_none], self.rb_ratio)
        result["fermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.fermentables)
        result["defaults"] = from_union([lambda x: to_class(Defaults, x), from_none], self.defaults)
        result["nutrition"] = from_union([lambda x: to_class(Nutrition, x), from_none], self.nutrition)
        result["img"] = from_union([from_str, from_none], self.img)
        result["carbonation"] = from_union([to_float, from_none], self.carbonation)
        result["_uid"] = from_union([from_str, from_none], self.uid)
        result["styleCarb"] = from_union([from_bool, from_none], self.style_carb)
        result["styleAbv"] = from_union([from_bool, from_none], self.style_abv)
        result["teaser"] = from_union([from_str, from_none], self.teaser)
        result["_ev"] = from_union([to_float, from_none], self.ev)
        result["attenuation"] = from_union([to_float, from_none], self.attenuation)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["hops"] = from_union([lambda x: from_list(lambda x: to_class(Hop, x), x), from_none], self.hops)
        result["thumb"] = from_union([from_str, from_none], self.thumb)
        result["_origin"] = from_union([from_str, from_none], self.origin)
        result["miscs"] = from_union([lambda x: from_list(lambda x: to_class(Misc, x), x), from_none], self.miscs)
        result["name"] = from_union([from_str, from_none], self.name)
        result["styleColor"] = from_union([from_bool, from_none], self.style_color)
        result["ogPlato"] = from_union([to_float, from_none], self.og_plato)
        result["ibu"] = from_union([from_int, from_none], self.ibu)
        result["styleIbu"] = from_union([from_bool, from_none], self.style_ibu)
        result["batchSize"] = from_union([from_int, from_none], self.batch_size)
        result["mash"] = from_union([lambda x: to_class(RecipeMash, x), from_none], self.mash)
        result["boilTime"] = from_union([from_int, from_none], self.boil_time)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["efficiency"] = from_union([from_int, from_none], self.efficiency)
        result["fgFormula"] = from_union([from_str, from_none], self.fg_formula)
        result["extraGravity"] = from_union([from_int, from_none], self.extra_gravity)
        result["yeasts"] = from_union([lambda x: from_list(lambda x: to_class(Yeast, x), x), from_none], self.yeasts)
        result["diastaticPower"] = from_union([to_float, from_none], self.diastatic_power)
        result["public"] = from_union([from_bool, from_none], self.recipe_public)
        result["style"] = from_union([lambda x: to_class(Style, x), from_none], self.style)
        result["avgWeightedHopstandTemp"] = from_union([from_int, from_none], self.avg_weighted_hopstand_temp)
        result["preBoilGravity"] = from_union([to_float, from_none], self.pre_boil_gravity)
        result["fg"] = from_union([to_float, from_none], self.fg)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["hopStandMinutes"] = from_union([from_int, from_none], self.hop_stand_minutes)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["ibuFormula"] = from_union([from_str, from_none], self.ibu_formula)
        result["color"] = from_union([to_float, from_none], self.color)
        result["mashEfficiency"] = from_union([to_float, from_none], self.mash_efficiency)
        result["abv"] = from_union([to_float, from_none], self.abv)
        result["fermentation"] = from_union([lambda x: to_class(Fermentation, x), from_none], self.fermentation)
        result["img_url"] = from_union([from_str, from_none], self.img_url)
        return result


@dataclass
class BatchItem:
    measured_conversion_efficiency: None
    brewer: None
    priming_sugar_equiv: None
    timestamp: Optional[Created] = None
    measured_abv: Optional[float] = None
    carbonation_type: Optional[str] = None
    measurements: Optional[List[Any]] = None
    hide_batch_events: Optional[bool] = None
    measured_og: Optional[float] = None
    fermentation_controller_enabled: Optional[bool] = None
    measured_boil_size: Optional[float] = None
    devices: Optional[Devices] = None
    batch_yeasts: Optional[List[BatchYeast]] = None
    measured_pre_boil_gravity: Optional[float] = None
    version: Optional[Version] = None
    boil_steps: Optional[List[BoilStep]] = None
    status: Optional[str] = None
    name: Optional[str] = None
    archived: Optional[bool] = None
    batch_hops: Optional[List[Hop]] = None
    id: Optional[str] = None
    events: Optional[List[Event]] = None
    batch_no: Optional[int] = None
    rev: Optional[str] = None
    measured_efficiency: Optional[float] = None
    measured_post_boil_gravity: Optional[float] = None
    boil_steps_count: Optional[int] = None
    batch_hops_local: Optional[List[Any]] = None
    notes: Optional[List[Note]] = None
    estimated_color: Optional[int] = None
    batch_miscs_local: Optional[List[Any]] = None
    created: Optional[Created] = None
    recipe: Optional[Recipe] = None
    estimated_total_gravity: Optional[float] = None
    mash_steps_count: Optional[int] = None
    brew_date: Optional[int] = None
    estimated_ibu: Optional[int] = None
    measured_attenuation: Optional[float] = None
    init: Optional[bool] = None
    estimated_rb_ratio: Optional[float] = None
    hidden: Optional[bool] = None
    measured_batch_size: Optional[int] = None
    brew_controller_enabled: Optional[bool] = None
    batch_fermentables: Optional[List[Fermentable]] = None
    batch_notes: Optional[str] = None
    batch_yeasts_local: Optional[List[Any]] = None
    batch_fermentables_local: Optional[List[Any]] = None
    estimated_og: Optional[float] = None
    measured_kettle_efficiency: Optional[float] = None
    type: Optional[str] = None
    measured_mash_efficiency: Optional[float] = None
    batch_miscs: Optional[List[BatchMisc]] = None
    estimated_fg: Optional[float] = None
    timestamp_ms: Optional[int] = None
    fermentation_start_date: Optional[int] = None
    carbonation_force: Optional[float] = None
    cost: Optional[Cost] = None
    estimated_bu_gu_ratio: Optional[float] = None
    bottling_date: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchItem':
        assert isinstance(obj, dict)
        measured_conversion_efficiency = from_none(obj.get("measuredConversionEfficiency"))
        brewer = from_none(obj.get("brewer"))
        priming_sugar_equiv = from_none(obj.get("primingSugarEquiv"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        measured_abv = from_union([from_float, from_none], obj.get("measuredAbv"))
        carbonation_type = from_union([from_str, from_none], obj.get("carbonationType"))
        measurements = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("measurements"))
        hide_batch_events = from_union([from_bool, from_none], obj.get("hideBatchEvents"))
        measured_og = from_union([from_float, from_none], obj.get("measuredOg"))
        fermentation_controller_enabled = from_union([from_bool, from_none], obj.get("fermentationControllerEnabled"))
        measured_boil_size = from_union([from_float, from_none], obj.get("measuredBoilSize"))
        devices = from_union([Devices.from_dict, from_none], obj.get("devices"))
        batch_yeasts = from_union([lambda x: from_list(BatchYeast.from_dict, x), from_none], obj.get("batchYeasts"))
        measured_pre_boil_gravity = from_union([from_float, from_none], obj.get("measuredPreBoilGravity"))
        version = from_union([Version, from_none], obj.get("_version"))
        boil_steps = from_union([lambda x: from_list(BoilStep.from_dict, x), from_none], obj.get("boilSteps"))
        status = from_union([from_str, from_none], obj.get("status"))
        name = from_union([from_str, from_none], obj.get("name"))
        archived = from_union([from_bool, from_none], obj.get("_archived"))
        batch_hops = from_union([lambda x: from_list(Hop.from_dict, x), from_none], obj.get("batchHops"))
        id = from_union([from_str, from_none], obj.get("_id"))
        events = from_union([lambda x: from_list(Event.from_dict, x), from_none], obj.get("events"))
        batch_no = from_union([from_int, from_none], obj.get("batchNo"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        measured_efficiency = from_union([from_float, from_none], obj.get("measuredEfficiency"))
        measured_post_boil_gravity = from_union([from_float, from_none], obj.get("measuredPostBoilGravity"))
        boil_steps_count = from_union([from_int, from_none], obj.get("boilStepsCount"))
        batch_hops_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchHopsLocal"))
        notes = from_union([lambda x: from_list(Note.from_dict, x), from_none], obj.get("notes"))
        estimated_color = from_union([from_int, from_none], obj.get("estimatedColor"))
        batch_miscs_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchMiscsLocal"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        estimated_total_gravity = from_union([from_float, from_none], obj.get("estimatedTotalGravity"))
        mash_steps_count = from_union([from_int, from_none], obj.get("mashStepsCount"))
        brew_date = from_union([from_int, from_none], obj.get("brewDate"))
        estimated_ibu = from_union([from_int, from_none], obj.get("estimatedIbu"))
        measured_attenuation = from_union([from_float, from_none], obj.get("measuredAttenuation"))
        init = from_union([from_bool, from_none], obj.get("_init"))
        estimated_rb_ratio = from_union([from_float, from_none], obj.get("estimatedRbRatio"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        measured_batch_size = from_union([from_int, from_none], obj.get("measuredBatchSize"))
        brew_controller_enabled = from_union([from_bool, from_none], obj.get("brewControllerEnabled"))
        batch_fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("batchFermentables"))
        batch_notes = from_union([from_str, from_none], obj.get("batchNotes"))
        batch_yeasts_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchYeastsLocal"))
        batch_fermentables_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchFermentablesLocal"))
        estimated_og = from_union([from_float, from_none], obj.get("estimatedOg"))
        measured_kettle_efficiency = from_union([from_float, from_none], obj.get("measuredKettleEfficiency"))
        type = from_union([from_str, from_none], obj.get("_type"))
        measured_mash_efficiency = from_union([from_float, from_none], obj.get("measuredMashEfficiency"))
        batch_miscs = from_union([lambda x: from_list(BatchMisc.from_dict, x), from_none], obj.get("batchMiscs"))
        estimated_fg = from_union([from_float, from_none], obj.get("estimatedFg"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        fermentation_start_date = from_union([from_int, from_none], obj.get("fermentationStartDate"))
        carbonation_force = from_union([from_float, from_none], obj.get("carbonationForce"))
        cost = from_union([Cost.from_dict, from_none], obj.get("cost"))
        estimated_bu_gu_ratio = from_union([from_float, from_none], obj.get("estimatedBuGuRatio"))
        bottling_date = from_union([from_int, from_none], obj.get("bottlingDate"))
        return BatchItem(measured_conversion_efficiency, brewer, priming_sugar_equiv, timestamp, measured_abv, carbonation_type, measurements, hide_batch_events, measured_og, fermentation_controller_enabled, measured_boil_size, devices, batch_yeasts, measured_pre_boil_gravity, version, boil_steps, status, name, archived, batch_hops, id, events, batch_no, rev, measured_efficiency, measured_post_boil_gravity, boil_steps_count, batch_hops_local, notes, estimated_color, batch_miscs_local, created, recipe, estimated_total_gravity, mash_steps_count, brew_date, estimated_ibu, measured_attenuation, init, estimated_rb_ratio, hidden, measured_batch_size, brew_controller_enabled, batch_fermentables, batch_notes, batch_yeasts_local, batch_fermentables_local, estimated_og, measured_kettle_efficiency, type, measured_mash_efficiency, batch_miscs, estimated_fg, timestamp_ms, fermentation_start_date, carbonation_force, cost, estimated_bu_gu_ratio, bottling_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["measuredConversionEfficiency"] = from_none(self.measured_conversion_efficiency)
        result["brewer"] = from_none(self.brewer)
        result["primingSugarEquiv"] = from_none(self.priming_sugar_equiv)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["measuredAbv"] = from_union([to_float, from_none], self.measured_abv)
        result["carbonationType"] = from_union([from_str, from_none], self.carbonation_type)
        result["measurements"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.measurements)
        result["hideBatchEvents"] = from_union([from_bool, from_none], self.hide_batch_events)
        result["measuredOg"] = from_union([to_float, from_none], self.measured_og)
        result["fermentationControllerEnabled"] = from_union([from_bool, from_none], self.fermentation_controller_enabled)
        result["measuredBoilSize"] = from_union([to_float, from_none], self.measured_boil_size)
        result["devices"] = from_union([lambda x: to_class(Devices, x), from_none], self.devices)
        result["batchYeasts"] = from_union([lambda x: from_list(lambda x: to_class(BatchYeast, x), x), from_none], self.batch_yeasts)
        result["measuredPreBoilGravity"] = from_union([to_float, from_none], self.measured_pre_boil_gravity)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["boilSteps"] = from_union([lambda x: from_list(lambda x: to_class(BoilStep, x), x), from_none], self.boil_steps)
        result["status"] = from_union([from_str, from_none], self.status)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_archived"] = from_union([from_bool, from_none], self.archived)
        result["batchHops"] = from_union([lambda x: from_list(lambda x: to_class(Hop, x), x), from_none], self.batch_hops)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["events"] = from_union([lambda x: from_list(lambda x: to_class(Event, x), x), from_none], self.events)
        result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["measuredEfficiency"] = from_union([to_float, from_none], self.measured_efficiency)
        result["measuredPostBoilGravity"] = from_union([to_float, from_none], self.measured_post_boil_gravity)
        result["boilStepsCount"] = from_union([from_int, from_none], self.boil_steps_count)
        result["batchHopsLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_hops_local)
        result["notes"] = from_union([lambda x: from_list(lambda x: to_class(Note, x), x), from_none], self.notes)
        result["estimatedColor"] = from_union([from_int, from_none], self.estimated_color)
        result["batchMiscsLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_miscs_local)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["recipe"] = from_union([lambda x: to_class(Recipe, x), from_none], self.recipe)
        result["estimatedTotalGravity"] = from_union([to_float, from_none], self.estimated_total_gravity)
        result["mashStepsCount"] = from_union([from_int, from_none], self.mash_steps_count)
        result["brewDate"] = from_union([from_int, from_none], self.brew_date)
        result["estimatedIbu"] = from_union([from_int, from_none], self.estimated_ibu)
        result["measuredAttenuation"] = from_union([to_float, from_none], self.measured_attenuation)
        result["_init"] = from_union([from_bool, from_none], self.init)
        result["estimatedRbRatio"] = from_union([to_float, from_none], self.estimated_rb_ratio)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["measuredBatchSize"] = from_union([from_int, from_none], self.measured_batch_size)
        result["brewControllerEnabled"] = from_union([from_bool, from_none], self.brew_controller_enabled)
        result["batchFermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.batch_fermentables)
        result["batchNotes"] = from_union([from_str, from_none], self.batch_notes)
        result["batchYeastsLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_yeasts_local)
        result["batchFermentablesLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_fermentables_local)
        result["estimatedOg"] = from_union([to_float, from_none], self.estimated_og)
        result["measuredKettleEfficiency"] = from_union([to_float, from_none], self.measured_kettle_efficiency)
        result["_type"] = from_union([from_str, from_none], self.type)
        result["measuredMashEfficiency"] = from_union([to_float, from_none], self.measured_mash_efficiency)
        result["batchMiscs"] = from_union([lambda x: from_list(lambda x: to_class(BatchMisc, x), x), from_none], self.batch_miscs)
        result["estimatedFg"] = from_union([to_float, from_none], self.estimated_fg)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["fermentationStartDate"] = from_union([from_int, from_none], self.fermentation_start_date)
        result["carbonationForce"] = from_union([to_float, from_none], self.carbonation_force)
        result["cost"] = from_union([lambda x: to_class(Cost, x), from_none], self.cost)
        result["estimatedBuGuRatio"] = from_union([to_float, from_none], self.estimated_bu_gu_ratio)
        result["bottlingDate"] = from_union([from_int, from_none], self.bottling_date)
        return result


def batch_item_from_dict(s: Any) -> BatchItem:
    return BatchItem.from_dict(s)


def batch_item_to_dict(x: BatchItem) -> Any:
    return to_class(BatchItem, x)
