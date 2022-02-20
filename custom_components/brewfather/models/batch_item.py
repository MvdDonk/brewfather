# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = batch_item_from_dict(json.loads(json_string))

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


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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


class GrainCategory(Enum):
    BASE = "Base"
    BASE_MARIS_OTTER = "Base (Maris Otter)"
    BASE_MUNICH = "Base (Munich)"
    BASE_PILSNER = "Base (Pilsner)"
    BASE_WHEAT = "Base (Wheat)"
    CRYSTAL_CARAMEL = "Crystal/Caramel"
    ROASTED = "Roasted"


class BatchFermentableOrigin(Enum):
    BELGIUM = "Belgium"
    GERMANY = "Germany"
    NETHERLANDS = "Netherlands"
    POLAND = "Poland"
    UK = "UK"
    US = "US"


class Substitutes(Enum):
    EMPTY = ""
    PALE_LIQUID_EXTRACT = "Pale Liquid Extract"
    WHEAT_LIQUID_EXTRACT = "Wheat Liquid Extract"


class Supplier(Enum):
    BEST_MALZ = "BestMalz"
    BRIESS = "Briess"
    DINGEMANS = "Dingemans"
    EMPTY = ""
    THE_SWAEN = "The Swaen"
    THOMAS_FAWCETT = "Thomas Fawcett"
    VIKING_MALT = "Viking Malt"
    WEYERMANN = "Weyermann"


class BatchFermentableType(Enum):
    ADJUNCT = "Adjunct"
    GRAIN = "Grain"


class Version(Enum):
    THE_213 = "2.1.3"
    THE_248 = "2.4.8"
    THE_260 = "2.6.0"
    THE_272 = "2.7.2"
    THE_276 = "2.7.6"
    THE_280 = "2.8.0"
    THE_281 = "2.8.1"


@dataclass
class Fermentable:
    fan: None
    cgdb: None
    manufacturing_date: None
    type: Optional[BatchFermentableType] = None
    potential: Optional[float] = None
    origin: Optional[BatchFermentableOrigin] = None
    cost_per_amount: Optional[float] = None
    not_in_recipe: Optional[bool] = None
    fgdb: Optional[int] = None
    checked: Optional[bool] = None
    amount: Optional[float] = None
    timestamp: Optional[Created] = None
    grain_category: Optional[GrainCategory] = None
    removed_from_inventory: Optional[bool] = None
    supplier: Optional[Supplier] = None
    coarse_fine_diff: Optional[float] = None
    moisture: Optional[float] = None
    version: Optional[Version] = None
    potential_percentage: Optional[float] = None
    timestamp_ms: Optional[int] = None
    total_cost: Optional[float] = None
    ibu_per_amount: Optional[int] = None
    removed_amount: Optional[float] = None
    color: Optional[float] = None
    inventory: Optional[float] = None
    not_fermentable: Optional[bool] = None
    user_notes: Optional[str] = None
    max_in_batch: Optional[int] = None
    used_in: Optional[str] = None
    attenuation: Optional[float] = None
    rev: Optional[str] = None
    created: Optional[Created] = None
    acid: Optional[int] = None
    friability: Optional[int] = None
    id: Optional[str] = None
    hidden: Optional[bool] = None
    substitutes: Optional[Substitutes] = None
    notes: Optional[str] = None
    diastatic_power: Optional[int] = None
    best_before_date: Optional[int] = None
    protein: Optional[float] = None
    name: Optional[str] = None
    display_amount: Optional[int] = None
    lovibond: Optional[float] = None
    percentage: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentable':
        assert isinstance(obj, dict)
        fan = from_none(obj.get("fan"))
        cgdb = from_none(obj.get("cgdb"))
        manufacturing_date = from_none(obj.get("manufacturingDate"))
        type = from_union([BatchFermentableType, from_none], obj.get("type"))
        potential = from_union([from_float, from_none], obj.get("potential"))
        origin = from_union([BatchFermentableOrigin, from_none], obj.get("origin"))
        cost_per_amount = from_union([from_float, from_none], obj.get("costPerAmount"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        fgdb = from_union([from_int, from_none], obj.get("fgdb"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        grain_category = from_union([from_none, GrainCategory], obj.get("grainCategory"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        supplier = from_union([Supplier, from_none], obj.get("supplier"))
        coarse_fine_diff = from_union([from_float, from_none], obj.get("coarseFineDiff"))
        moisture = from_union([from_float, from_none], obj.get("moisture"))
        version = from_union([Version, from_none], obj.get("_version"))
        potential_percentage = from_union([from_float, from_none], obj.get("potentialPercentage"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        total_cost = from_union([from_float, from_none], obj.get("totalCost"))
        ibu_per_amount = from_union([from_int, from_none], obj.get("ibuPerAmount"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        color = from_union([from_float, from_none], obj.get("color"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        not_fermentable = from_union([from_bool, from_none], obj.get("notFermentable"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        max_in_batch = from_union([from_int, from_none], obj.get("maxInBatch"))
        used_in = from_union([from_str, from_none], obj.get("usedIn"))
        attenuation = from_union([from_float, from_none], obj.get("attenuation"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        acid = from_union([from_int, from_none], obj.get("acid"))
        friability = from_union([from_int, from_none], obj.get("friability"))
        id = from_union([from_str, from_none], obj.get("_id"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        substitutes = from_union([Substitutes, from_none], obj.get("substitutes"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        diastatic_power = from_union([from_int, from_none], obj.get("diastaticPower"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        protein = from_union([from_float, from_none], obj.get("protein"))
        name = from_union([from_str, from_none], obj.get("name"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        lovibond = from_union([from_float, from_none], obj.get("lovibond"))
        percentage = from_union([from_float, from_none], obj.get("percentage"))
        return Fermentable(fan, cgdb, manufacturing_date, type, potential, origin, cost_per_amount, not_in_recipe, fgdb, checked, amount, timestamp, grain_category, removed_from_inventory, supplier, coarse_fine_diff, moisture, version, potential_percentage, timestamp_ms, total_cost, ibu_per_amount, removed_amount, color, inventory, not_fermentable, user_notes, max_in_batch, used_in, attenuation, rev, created, acid, friability, id, hidden, substitutes, notes, diastatic_power, best_before_date, protein, name, display_amount, lovibond, percentage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fan"] = from_none(self.fan)
        result["cgdb"] = from_none(self.cgdb)
        result["manufacturingDate"] = from_none(self.manufacturing_date)
        result["type"] = from_union([lambda x: to_enum(BatchFermentableType, x), from_none], self.type)
        result["potential"] = from_union([to_float, from_none], self.potential)
        result["origin"] = from_union([lambda x: to_enum(BatchFermentableOrigin, x), from_none], self.origin)
        result["costPerAmount"] = from_union([to_float, from_none], self.cost_per_amount)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["fgdb"] = from_union([from_int, from_none], self.fgdb)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["grainCategory"] = from_union([from_none, lambda x: to_enum(GrainCategory, x)], self.grain_category)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["supplier"] = from_union([lambda x: to_enum(Supplier, x), from_none], self.supplier)
        result["coarseFineDiff"] = from_union([to_float, from_none], self.coarse_fine_diff)
        result["moisture"] = from_union([to_float, from_none], self.moisture)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["potentialPercentage"] = from_union([to_float, from_none], self.potential_percentage)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["totalCost"] = from_union([to_float, from_none], self.total_cost)
        result["ibuPerAmount"] = from_union([from_int, from_none], self.ibu_per_amount)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["color"] = from_union([to_float, from_none], self.color)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["notFermentable"] = from_union([from_bool, from_none], self.not_fermentable)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["maxInBatch"] = from_union([from_int, from_none], self.max_in_batch)
        result["usedIn"] = from_union([from_str, from_none], self.used_in)
        result["attenuation"] = from_union([to_float, from_none], self.attenuation)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["acid"] = from_union([from_int, from_none], self.acid)
        result["friability"] = from_union([from_int, from_none], self.friability)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["substitutes"] = from_union([lambda x: to_enum(Substitutes, x), from_none], self.substitutes)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["diastaticPower"] = from_union([from_int, from_none], self.diastatic_power)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["protein"] = from_union([to_float, from_none], self.protein)
        result["name"] = from_union([from_str, from_none], self.name)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["lovibond"] = from_union([to_float, from_none], self.lovibond)
        result["percentage"] = from_union([to_float, from_none], self.percentage)
        return result


class BatchHopOrigin(Enum):
    AUSTRALIA = "Australia"
    GERMANY = "Germany"
    UNITED_KINGDOM = "United Kingdom"
    US = "US"
    U_S = "U.S."


class BatchHopType(Enum):
    PELLET = "Pellet"


class Usage(Enum):
    AROMA = "Aroma"
    BITTERING = "Bittering"
    BOTH = "Both"


class BatchHopUse(Enum):
    AROMA = "Aroma"
    BOIL = "Boil"
    DRY_HOP = "Dry Hop"
    FIRST_WORT = "First Wort"


@dataclass
class Hop:
    caryophyllene: None
    cohumulone: None
    humulene: None
    farnesene: None
    oil: None
    year: None
    myrcene: None
    hsi: None
    beta: None
    edit_flag: Optional[bool] = None
    inventory: Optional[float] = None
    actual_time: Optional[int] = None
    day: Optional[int] = None
    user_notes: Optional[str] = None
    origin: Optional[BatchHopOrigin] = None
    substitutes: Optional[str] = None
    removed_from_inventory: Optional[bool] = None
    alpha: Optional[float] = None
    type: Optional[BatchHopType] = None
    best_before_date: Optional[int] = None
    notes: Optional[str] = None
    ibu: Optional[float] = None
    used_in: Optional[str] = None
    manufacturing_date: Optional[int] = None
    removed_amount: Optional[float] = None
    time: Optional[int] = None
    checked: Optional[bool] = None
    total_cost: Optional[float] = None
    cost_per_amount: Optional[float] = None
    not_in_recipe: Optional[bool] = None
    hidden: Optional[bool] = None
    name: Optional[str] = None
    display_amount: Optional[int] = None
    use: Optional[BatchHopUse] = None
    timestamp_ms: Optional[int] = None
    timestamp: Optional[Created] = None
    amount: Optional[float] = None
    usage: Optional[Usage] = None
    temp: Optional[int] = None
    id: Optional[str] = None
    version: Optional[Version] = None
    rev: Optional[str] = None
    created: Optional[Created] = None
    time_unit: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Hop':
        assert isinstance(obj, dict)
        caryophyllene = from_none(obj.get("caryophyllene"))
        cohumulone = from_none(obj.get("cohumulone"))
        humulene = from_none(obj.get("humulene"))
        farnesene = from_none(obj.get("farnesene"))
        oil = from_none(obj.get("oil"))
        year = from_none(obj.get("year"))
        myrcene = from_none(obj.get("myrcene"))
        hsi = from_none(obj.get("hsi"))
        beta = from_none(obj.get("beta"))
        edit_flag = from_union([from_bool, from_none], obj.get("_editFlag"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        day = from_union([from_int, from_none], obj.get("day"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        origin = from_union([BatchHopOrigin, from_none], obj.get("origin"))
        substitutes = from_union([from_str, from_none], obj.get("substitutes"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        alpha = from_union([from_float, from_none], obj.get("alpha"))
        type = from_union([BatchHopType, from_none], obj.get("type"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        ibu = from_union([from_float, from_none], obj.get("ibu"))
        used_in = from_union([from_str, from_none], obj.get("usedIn"))
        manufacturing_date = from_union([from_int, from_none], obj.get("manufacturingDate"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        time = from_union([from_int, from_none], obj.get("time"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        total_cost = from_union([from_float, from_none], obj.get("totalCost"))
        cost_per_amount = from_union([from_float, from_none], obj.get("costPerAmount"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        name = from_union([from_str, from_none], obj.get("name"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        use = from_union([BatchHopUse, from_none], obj.get("use"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        usage = from_union([Usage, from_none], obj.get("usage"))
        temp = from_union([from_int, from_none], obj.get("temp"))
        id = from_union([from_str, from_none], obj.get("_id"))
        version = from_union([Version, from_none], obj.get("_version"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        time_unit = from_union([from_none, from_str], obj.get("timeUnit"))
        return Hop(caryophyllene, cohumulone, humulene, farnesene, oil, year, myrcene, hsi, beta, edit_flag, inventory, actual_time, day, user_notes, origin, substitutes, removed_from_inventory, alpha, type, best_before_date, notes, ibu, used_in, manufacturing_date, removed_amount, time, checked, total_cost, cost_per_amount, not_in_recipe, hidden, name, display_amount, use, timestamp_ms, timestamp, amount, usage, temp, id, version, rev, created, time_unit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["caryophyllene"] = from_none(self.caryophyllene)
        result["cohumulone"] = from_none(self.cohumulone)
        result["humulene"] = from_none(self.humulene)
        result["farnesene"] = from_none(self.farnesene)
        result["oil"] = from_none(self.oil)
        result["year"] = from_none(self.year)
        result["myrcene"] = from_none(self.myrcene)
        result["hsi"] = from_none(self.hsi)
        result["beta"] = from_none(self.beta)
        result["_editFlag"] = from_union([from_bool, from_none], self.edit_flag)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        result["day"] = from_union([from_int, from_none], self.day)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["origin"] = from_union([lambda x: to_enum(BatchHopOrigin, x), from_none], self.origin)
        result["substitutes"] = from_union([from_str, from_none], self.substitutes)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["alpha"] = from_union([to_float, from_none], self.alpha)
        result["type"] = from_union([lambda x: to_enum(BatchHopType, x), from_none], self.type)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["ibu"] = from_union([to_float, from_none], self.ibu)
        result["usedIn"] = from_union([from_str, from_none], self.used_in)
        result["manufacturingDate"] = from_union([from_int, from_none], self.manufacturing_date)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["time"] = from_union([from_int, from_none], self.time)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["totalCost"] = from_union([to_float, from_none], self.total_cost)
        result["costPerAmount"] = from_union([to_float, from_none], self.cost_per_amount)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["name"] = from_union([from_str, from_none], self.name)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["use"] = from_union([lambda x: to_enum(BatchHopUse, x), from_none], self.use)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["usage"] = from_union([lambda x: to_enum(Usage, x), from_none], self.usage)
        result["temp"] = from_union([from_int, from_none], self.temp)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["timeUnit"] = from_union([from_none, from_str], self.time_unit)
        return result


@dataclass
class BatchHopsLocal:
    temp: None
    not_in_recipe: Optional[bool] = None
    origin: Optional[BatchHopOrigin] = None
    ibu: Optional[float] = None
    id: Optional[str] = None
    display_amount: Optional[float] = None
    amount: Optional[float] = None
    use: Optional[BatchHopUse] = None
    name: Optional[str] = None
    alpha: Optional[float] = None
    time: Optional[int] = None
    inventory: Optional[int] = None
    cost_per_amount: Optional[int] = None
    notes: Optional[str] = None
    type: Optional[BatchHopType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchHopsLocal':
        assert isinstance(obj, dict)
        temp = from_none(obj.get("temp"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        origin = from_union([BatchHopOrigin, from_none], obj.get("origin"))
        ibu = from_union([from_float, from_none], obj.get("ibu"))
        id = from_union([from_str, from_none], obj.get("_id"))
        display_amount = from_union([from_float, from_none], obj.get("displayAmount"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        use = from_union([BatchHopUse, from_none], obj.get("use"))
        name = from_union([from_str, from_none], obj.get("name"))
        alpha = from_union([from_float, from_none], obj.get("alpha"))
        time = from_union([from_int, from_none], obj.get("time"))
        inventory = from_union([from_int, from_none], obj.get("inventory"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        type = from_union([BatchHopType, from_none], obj.get("type"))
        return BatchHopsLocal(temp, not_in_recipe, origin, ibu, id, display_amount, amount, use, name, alpha, time, inventory, cost_per_amount, notes, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["temp"] = from_none(self.temp)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["origin"] = from_union([lambda x: to_enum(BatchHopOrigin, x), from_none], self.origin)
        result["ibu"] = from_union([to_float, from_none], self.ibu)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["displayAmount"] = from_union([to_float, from_none], self.display_amount)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["use"] = from_union([lambda x: to_enum(BatchHopUse, x), from_none], self.use)
        result["name"] = from_union([from_str, from_none], self.name)
        result["alpha"] = from_union([to_float, from_none], self.alpha)
        result["time"] = from_union([from_int, from_none], self.time)
        result["inventory"] = from_union([from_int, from_none], self.inventory)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["type"] = from_union([lambda x: to_enum(BatchHopType, x), from_none], self.type)
        return result


class BatchMiscID(Enum):
    DEFAULT_07_ADB1 = "default-07adb1"
    DEFAULT_1_F88_DF = "default-1f88df"
    DEFAULT_3_B1827 = "default-3b1827"
    DEFAULT_4_E9_D62 = "default-4e9d62"
    DEFAULT_BK9_J78 = "default-bk9j78"
    DEFAULT_YN1_J28_SF = "default-yn1j28sf"


class InventoryUnit(Enum):
    G = "g"
    ML = "ml"


class BatchMiscName(Enum):
    CALCIUM_CHLORIDE_CA_CL2 = "Calcium Chloride (CaCl2)"
    CANNING_SALT_NA_CL = "Canning Salt (NaCl)"
    EPSOM_SALT_MG_SO4 = "Epsom Salt (MgSO4)"
    GYPSUM_CA_SO4 = "Gypsum (CaSO4)"
    LACTIC_ACID = "Lactic Acid"
    YEAST_NUTRIENTS = "Yeast Nutrients"


class BatchMiscType(Enum):
    OTHER = "Other"
    WATER_AGENT = "Water Agent"


class SpargeWaterOverflowEnum(Enum):
    BOIL = "Boil"
    MASH = "Mash"


@dataclass
class Misc:
    best_before_date: None
    amount_per_l: None
    display_amount: Optional[float] = None
    created: Optional[Created] = None
    total_cost: Optional[float] = None
    cost_per_amount: Optional[float] = None
    time_is_days: Optional[bool] = None
    version: Optional[Version] = None
    removed_unit: Optional[InventoryUnit] = None
    rev: Optional[str] = None
    inventory_unit: Optional[InventoryUnit] = None
    timestamp: Optional[Created] = None
    removed_amount: Optional[float] = None
    removed_from_inventory: Optional[bool] = None
    amount: Optional[float] = None
    name: Optional[BatchMiscName] = None
    water_adjustment: Optional[bool] = None
    use: Optional[SpargeWaterOverflowEnum] = None
    type: Optional[BatchMiscType] = None
    inventory: Optional[float] = None
    checked: Optional[bool] = None
    unit: Optional[InventoryUnit] = None
    not_in_recipe: Optional[bool] = None
    id: Optional[BatchMiscID] = None
    time: Optional[int] = None
    hidden: Optional[bool] = None
    timestamp_ms: Optional[int] = None
    user_notes: Optional[str] = None
    notes: Optional[str] = None
    substitutes: Optional[str] = None
    manufacturing_date: Optional[int] = None
    use_for: Optional[str] = None
    concentration: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Misc':
        assert isinstance(obj, dict)
        best_before_date = from_none(obj.get("bestBeforeDate"))
        amount_per_l = from_none(obj.get("amountPerL"))
        display_amount = from_union([from_float, from_none], obj.get("displayAmount"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        total_cost = from_union([from_float, from_none], obj.get("totalCost"))
        cost_per_amount = from_union([from_float, from_none], obj.get("costPerAmount"))
        time_is_days = from_union([from_bool, from_none], obj.get("timeIsDays"))
        version = from_union([Version, from_none], obj.get("_version"))
        removed_unit = from_union([InventoryUnit, from_none], obj.get("removedUnit"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        inventory_unit = from_union([InventoryUnit, from_none], obj.get("inventoryUnit"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        removed_amount = from_union([from_float, from_none], obj.get("removedAmount"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        name = from_union([BatchMiscName, from_none], obj.get("name"))
        water_adjustment = from_union([from_bool, from_none], obj.get("waterAdjustment"))
        use = from_union([SpargeWaterOverflowEnum, from_none], obj.get("use"))
        type = from_union([BatchMiscType, from_none], obj.get("type"))
        inventory = from_union([from_float, from_none], obj.get("inventory"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        unit = from_union([InventoryUnit, from_none], obj.get("unit"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        id = from_union([BatchMiscID, from_none], obj.get("_id"))
        time = from_union([from_int, from_none], obj.get("time"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        substitutes = from_union([from_str, from_none], obj.get("substitutes"))
        manufacturing_date = from_union([from_int, from_none], obj.get("manufacturingDate"))
        use_for = from_union([from_str, from_none], obj.get("useFor"))
        concentration = from_union([from_int, from_none], obj.get("concentration"))
        return Misc(best_before_date, amount_per_l, display_amount, created, total_cost, cost_per_amount, time_is_days, version, removed_unit, rev, inventory_unit, timestamp, removed_amount, removed_from_inventory, amount, name, water_adjustment, use, type, inventory, checked, unit, not_in_recipe, id, time, hidden, timestamp_ms, user_notes, notes, substitutes, manufacturing_date, use_for, concentration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bestBeforeDate"] = from_none(self.best_before_date)
        result["amountPerL"] = from_none(self.amount_per_l)
        result["displayAmount"] = from_union([to_float, from_none], self.display_amount)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["totalCost"] = from_union([to_float, from_none], self.total_cost)
        result["costPerAmount"] = from_union([to_float, from_none], self.cost_per_amount)
        result["timeIsDays"] = from_union([from_bool, from_none], self.time_is_days)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["removedUnit"] = from_union([lambda x: to_enum(InventoryUnit, x), from_none], self.removed_unit)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["inventoryUnit"] = from_union([lambda x: to_enum(InventoryUnit, x), from_none], self.inventory_unit)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["removedAmount"] = from_union([to_float, from_none], self.removed_amount)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["amount"] = from_union([to_float, from_none], self.amount)
        result["name"] = from_union([lambda x: to_enum(BatchMiscName, x), from_none], self.name)
        result["waterAdjustment"] = from_union([from_bool, from_none], self.water_adjustment)
        result["use"] = from_union([lambda x: to_enum(SpargeWaterOverflowEnum, x), from_none], self.use)
        result["type"] = from_union([lambda x: to_enum(BatchMiscType, x), from_none], self.type)
        result["inventory"] = from_union([to_float, from_none], self.inventory)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["unit"] = from_union([lambda x: to_enum(InventoryUnit, x), from_none], self.unit)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["_id"] = from_union([lambda x: to_enum(BatchMiscID, x), from_none], self.id)
        result["time"] = from_union([from_int, from_none], self.time)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["substitutes"] = from_union([from_str, from_none], self.substitutes)
        result["manufacturingDate"] = from_union([from_int, from_none], self.manufacturing_date)
        result["useFor"] = from_union([from_str, from_none], self.use_for)
        result["concentration"] = from_union([from_int, from_none], self.concentration)
        return result


class Form(Enum):
    DRY = "Dry"
    LIQUID = "Liquid"


class Unit(Enum):
    ML = "ml"
    PKG = "pkg"


class BatchYeastType(Enum):
    ALE = "Ale"
    WHEAT = "Wheat"


@dataclass
class Yeast:
    min_attenuation: None
    max_attenuation: None
    manufacturing_date: None
    inventory_unit: Optional[Unit] = None
    total_cost: Optional[int] = None
    ferments_all: Optional[bool] = None
    checked: Optional[bool] = None
    form: Optional[Form] = None
    removed_from_inventory: Optional[bool] = None
    not_in_recipe: Optional[bool] = None
    user_notes: Optional[str] = None
    product_id: Optional[str] = None
    type: Optional[BatchYeastType] = None
    rev: Optional[str] = None
    unit: Optional[Unit] = None
    removed_amount: Optional[int] = None
    timestamp: Optional[Created] = None
    laboratory: Optional[str] = None
    inventory: Optional[int] = None
    cost_per_amount: Optional[int] = None
    attenuation: Optional[int] = None
    removed_unit: Optional[Unit] = None
    description: Optional[str] = None
    best_before_date: Optional[int] = None
    name: Optional[str] = None
    max_abv: Optional[int] = None
    id: Optional[str] = None
    version: Optional[str] = None
    display_amount: Optional[int] = None
    min_temp: Optional[float] = None
    created: Optional[Created] = None
    hidden: Optional[bool] = None
    timestamp_ms: Optional[int] = None
    max_temp: Optional[float] = None
    flocculation: Optional[str] = None
    amount: Optional[int] = None
    starter: Optional[bool] = None
    starter_size: Optional[int] = None
    starter_gram_extract: Optional[int] = None
    notes: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Yeast':
        assert isinstance(obj, dict)
        min_attenuation = from_none(obj.get("minAttenuation"))
        max_attenuation = from_none(obj.get("maxAttenuation"))
        manufacturing_date = from_none(obj.get("manufacturingDate"))
        inventory_unit = from_union([Unit, from_none], obj.get("inventoryUnit"))
        total_cost = from_union([from_int, from_none], obj.get("totalCost"))
        ferments_all = from_union([from_bool, from_none], obj.get("fermentsAll"))
        checked = from_union([from_bool, from_none], obj.get("checked"))
        form = from_union([Form, from_none], obj.get("form"))
        removed_from_inventory = from_union([from_bool, from_none], obj.get("removedFromInventory"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        product_id = from_union([from_str, from_none], obj.get("productId"))
        type = from_union([BatchYeastType, from_none], obj.get("type"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        unit = from_union([Unit, from_none], obj.get("unit"))
        removed_amount = from_union([from_int, from_none], obj.get("removedAmount"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        laboratory = from_union([from_str, from_none], obj.get("laboratory"))
        inventory = from_union([from_int, from_none], obj.get("inventory"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        attenuation = from_union([from_int, from_none], obj.get("attenuation"))
        removed_unit = from_union([Unit, from_none], obj.get("removedUnit"))
        description = from_union([from_str, from_none], obj.get("description"))
        best_before_date = from_union([from_int, from_none], obj.get("bestBeforeDate"))
        name = from_union([from_str, from_none], obj.get("name"))
        max_abv = from_union([from_int, from_none], obj.get("maxAbv"))
        id = from_union([from_str, from_none], obj.get("_id"))
        version = from_union([from_str, from_none], obj.get("_version"))
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        min_temp = from_union([from_float, from_none], obj.get("minTemp"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        max_temp = from_union([from_float, from_none], obj.get("maxTemp"))
        flocculation = from_union([from_str, from_none], obj.get("flocculation"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        starter = from_union([from_bool, from_none], obj.get("starter"))
        starter_size = from_union([from_int, from_none], obj.get("starterSize"))
        starter_gram_extract = from_union([from_int, from_none], obj.get("starterGramExtract"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        return Yeast(min_attenuation, max_attenuation, manufacturing_date, inventory_unit, total_cost, ferments_all, checked, form, removed_from_inventory, not_in_recipe, user_notes, product_id, type, rev, unit, removed_amount, timestamp, laboratory, inventory, cost_per_amount, attenuation, removed_unit, description, best_before_date, name, max_abv, id, version, display_amount, min_temp, created, hidden, timestamp_ms, max_temp, flocculation, amount, starter, starter_size, starter_gram_extract, notes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["minAttenuation"] = from_none(self.min_attenuation)
        result["maxAttenuation"] = from_none(self.max_attenuation)
        result["manufacturingDate"] = from_none(self.manufacturing_date)
        result["inventoryUnit"] = from_union([lambda x: to_enum(Unit, x), from_none], self.inventory_unit)
        result["totalCost"] = from_union([from_int, from_none], self.total_cost)
        result["fermentsAll"] = from_union([from_bool, from_none], self.ferments_all)
        result["checked"] = from_union([from_bool, from_none], self.checked)
        result["form"] = from_union([lambda x: to_enum(Form, x), from_none], self.form)
        result["removedFromInventory"] = from_union([from_bool, from_none], self.removed_from_inventory)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["productId"] = from_union([from_str, from_none], self.product_id)
        result["type"] = from_union([lambda x: to_enum(BatchYeastType, x), from_none], self.type)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["unit"] = from_union([lambda x: to_enum(Unit, x), from_none], self.unit)
        result["removedAmount"] = from_union([from_int, from_none], self.removed_amount)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["laboratory"] = from_union([from_str, from_none], self.laboratory)
        result["inventory"] = from_union([from_int, from_none], self.inventory)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["attenuation"] = from_union([from_int, from_none], self.attenuation)
        result["removedUnit"] = from_union([lambda x: to_enum(Unit, x), from_none], self.removed_unit)
        result["description"] = from_union([from_str, from_none], self.description)
        result["bestBeforeDate"] = from_union([from_int, from_none], self.best_before_date)
        result["name"] = from_union([from_str, from_none], self.name)
        result["maxAbv"] = from_union([from_int, from_none], self.max_abv)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["minTemp"] = from_union([to_float, from_none], self.min_temp)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["maxTemp"] = from_union([to_float, from_none], self.max_temp)
        result["flocculation"] = from_union([from_str, from_none], self.flocculation)
        result["amount"] = from_union([from_int, from_none], self.amount)
        result["starter"] = from_union([from_bool, from_none], self.starter)
        result["starterSize"] = from_union([from_int, from_none], self.starter_size)
        result["starterGramExtract"] = from_union([from_int, from_none], self.starter_gram_extract)
        result["notes"] = from_union([from_str, from_none], self.notes)
        return result


@dataclass
class BatchYeastsLocal:
    display_amount: Optional[int] = None
    ferments_all: Optional[bool] = None
    form: Optional[Form] = None
    inventory: Optional[int] = None
    attenuation: Optional[int] = None
    inventory_unit: Optional[Unit] = None
    name: Optional[str] = None
    amount: Optional[int] = None
    cost_per_amount: Optional[int] = None
    id: Optional[str] = None
    user_notes: Optional[str] = None
    unit: Optional[Unit] = None
    not_in_recipe: Optional[bool] = None
    product_id: Optional[str] = None
    laboratory: Optional[str] = None
    type: Optional[BatchYeastType] = None
    notes: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchYeastsLocal':
        assert isinstance(obj, dict)
        display_amount = from_union([from_int, from_none], obj.get("displayAmount"))
        ferments_all = from_union([from_bool, from_none], obj.get("fermentsAll"))
        form = from_union([Form, from_none], obj.get("form"))
        inventory = from_union([from_int, from_none], obj.get("inventory"))
        attenuation = from_union([from_int, from_none], obj.get("attenuation"))
        inventory_unit = from_union([Unit, from_none], obj.get("inventoryUnit"))
        name = from_union([from_str, from_none], obj.get("name"))
        amount = from_union([from_int, from_none], obj.get("amount"))
        cost_per_amount = from_union([from_int, from_none], obj.get("costPerAmount"))
        id = from_union([from_str, from_none], obj.get("_id"))
        user_notes = from_union([from_str, from_none], obj.get("userNotes"))
        unit = from_union([Unit, from_none], obj.get("unit"))
        not_in_recipe = from_union([from_bool, from_none], obj.get("notInRecipe"))
        product_id = from_union([from_str, from_none], obj.get("productId"))
        laboratory = from_union([from_str, from_none], obj.get("laboratory"))
        type = from_union([BatchYeastType, from_none], obj.get("type"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        return BatchYeastsLocal(display_amount, ferments_all, form, inventory, attenuation, inventory_unit, name, amount, cost_per_amount, id, user_notes, unit, not_in_recipe, product_id, laboratory, type, notes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["displayAmount"] = from_union([from_int, from_none], self.display_amount)
        result["fermentsAll"] = from_union([from_bool, from_none], self.ferments_all)
        result["form"] = from_union([lambda x: to_enum(Form, x), from_none], self.form)
        result["inventory"] = from_union([from_int, from_none], self.inventory)
        result["attenuation"] = from_union([from_int, from_none], self.attenuation)
        result["inventoryUnit"] = from_union([lambda x: to_enum(Unit, x), from_none], self.inventory_unit)
        result["name"] = from_union([from_str, from_none], self.name)
        result["amount"] = from_union([from_int, from_none], self.amount)
        result["costPerAmount"] = from_union([from_int, from_none], self.cost_per_amount)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["userNotes"] = from_union([from_str, from_none], self.user_notes)
        result["unit"] = from_union([lambda x: to_enum(Unit, x), from_none], self.unit)
        result["notInRecipe"] = from_union([from_bool, from_none], self.not_in_recipe)
        result["productId"] = from_union([from_str, from_none], self.product_id)
        result["laboratory"] = from_union([from_str, from_none], self.laboratory)
        result["type"] = from_union([lambda x: to_enum(BatchYeastType, x), from_none], self.type)
        result["notes"] = from_union([from_str, from_none], self.notes)
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
    fermentables: Optional[float] = None
    total: Optional[float] = None
    hops: Optional[float] = None
    yeasts: Optional[int] = None
    yeasts_share: Optional[int] = None
    fermentables_share: Optional[float] = None
    hops_share: Optional[float] = None
    miscs_share: Optional[float] = None
    miscs: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Cost':
        assert isinstance(obj, dict)
        per_bottling_liter = from_union([from_float, from_none], obj.get("perBottlingLiter"))
        fermentables = from_union([from_float, from_none], obj.get("fermentables"))
        total = from_union([from_float, from_none], obj.get("total"))
        hops = from_union([from_float, from_none], obj.get("hops"))
        yeasts = from_union([from_int, from_none], obj.get("yeasts"))
        yeasts_share = from_union([from_int, from_none], obj.get("yeastsShare"))
        fermentables_share = from_union([from_float, from_none], obj.get("fermentablesShare"))
        hops_share = from_union([from_float, from_none], obj.get("hopsShare"))
        miscs_share = from_union([from_float, from_none], obj.get("miscsShare"))
        miscs = from_union([from_float, from_none], obj.get("miscs"))
        return Cost(per_bottling_liter, fermentables, total, hops, yeasts, yeasts_share, fermentables_share, hops_share, miscs_share, miscs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["perBottlingLiter"] = from_union([to_float, from_none], self.per_bottling_liter)
        result["fermentables"] = from_union([to_float, from_none], self.fermentables)
        result["total"] = from_union([to_float, from_none], self.total)
        result["hops"] = from_union([to_float, from_none], self.hops)
        result["yeasts"] = from_union([from_int, from_none], self.yeasts)
        result["yeastsShare"] = from_union([from_int, from_none], self.yeasts_share)
        result["fermentablesShare"] = from_union([to_float, from_none], self.fermentables_share)
        result["hopsShare"] = from_union([to_float, from_none], self.hops_share)
        result["miscsShare"] = from_union([to_float, from_none], self.miscs_share)
        result["miscs"] = from_union([to_float, from_none], self.miscs)
        return result


@dataclass
class LastData:
    id: Optional[str] = None
    status: Optional[str] = None
    time: Optional[int] = None
    angle: Optional[float] = None
    rssi: Optional[int] = None
    battery: Optional[float] = None
    temp: Optional[float] = None
    type: Optional[str] = None
    sg: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LastData':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        status = from_union([from_str, from_none], obj.get("status"))
        time = from_union([from_int, from_none], obj.get("time"))
        angle = from_union([from_float, from_none], obj.get("angle"))
        rssi = from_union([from_int, from_none], obj.get("rssi"))
        battery = from_union([from_float, from_none], obj.get("battery"))
        temp = from_union([from_float, from_none], obj.get("temp"))
        type = from_union([from_str, from_none], obj.get("type"))
        sg = from_union([from_float, from_none], obj.get("sg"))
        return LastData(id, status, time, angle, rssi, battery, temp, type, sg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["status"] = from_union([from_str, from_none], self.status)
        result["time"] = from_union([from_int, from_none], self.time)
        result["angle"] = from_union([to_float, from_none], self.angle)
        result["rssi"] = from_union([from_int, from_none], self.rssi)
        result["battery"] = from_union([to_float, from_none], self.battery)
        result["temp"] = from_union([to_float, from_none], self.temp)
        result["type"] = from_union([from_str, from_none], self.type)
        result["sg"] = from_union([to_float, from_none], self.sg)
        return result


class Series(Enum):
    GRAVITY = "gravity"
    TEMP = "temp"


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
    settings: Optional[ItemSettings] = None
    hidden: Optional[bool] = None
    name: Optional[str] = None
    series: Optional[List[Series]] = None
    enabled: Optional[bool] = None
    last_log: Optional[int] = None
    last_data: Optional[LastData] = None
    batch_id: Optional[str] = None
    type: Optional[str] = None
    key: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        settings = from_union([ItemSettings.from_dict, from_none], obj.get("settings"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        name = from_union([from_str, from_none], obj.get("name"))
        series = from_union([lambda x: from_list(Series, x), from_none], obj.get("series"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        last_log = from_union([from_int, from_none], obj.get("lastLog"))
        last_data = from_union([LastData.from_dict, from_none], obj.get("lastData"))
        batch_id = from_union([from_none, from_str], obj.get("batchId"))
        type = from_union([from_str, from_none], obj.get("type"))
        key = from_union([from_str, from_none], obj.get("key"))
        return Item(settings, hidden, name, series, enabled, last_log, last_data, batch_id, type, key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["settings"] = from_union([lambda x: to_class(ItemSettings, x), from_none], self.settings)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["name"] = from_union([from_str, from_none], self.name)
        result["series"] = from_union([lambda x: from_list(lambda x: to_enum(Series, x), x), from_none], self.series)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["lastLog"] = from_union([from_int, from_none], self.last_log)
        result["lastData"] = from_union([lambda x: to_class(LastData, x), from_none], self.last_data)
        result["batchId"] = from_union([from_none, from_str], self.batch_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["key"] = from_union([from_str, from_none], self.key)
        return result


@dataclass
class BrewPiLess:
    items: Optional[List[Item]] = None
    enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BrewPiLess':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(Item.from_dict, x), from_none], obj.get("items"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        return BrewPiLess(items, enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_union([lambda x: from_list(lambda x: to_class(Item, x), x), from_none], self.items)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
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
    items: Optional[List[Any]] = None
    mode: Optional[str] = None
    gravity: Optional[bool] = None
    enabled: Optional[bool] = None
    temp: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Tilt':
        assert isinstance(obj, dict)
        items = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("items"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        gravity = from_union([from_bool, from_none], obj.get("gravity"))
        enabled = from_union([from_bool, from_none], obj.get("enabled"))
        temp = from_union([from_bool, from_none], obj.get("temp"))
        return Tilt(items, mode, gravity, enabled, temp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.items)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["gravity"] = from_union([from_bool, from_none], self.gravity)
        result["enabled"] = from_union([from_bool, from_none], self.enabled)
        result["temp"] = from_union([from_bool, from_none], self.temp)
        return result


@dataclass
class Devices:
    plaato_airlock: Optional[BrewPiLess] = None
    brew_pi_less: Optional[BrewPiLess] = None
    my_brewbot: Optional[BrewPiLess] = None
    float_hydrometer: Optional[BrewPiLess] = None
    floaty_hydrometer: Optional[BrewPiLess] = None
    i_spindel: Optional[BrewPiLess] = None
    plaato_keg: Optional[BrewPiLess] = None
    gfcc: Optional[Gfcc] = None
    stream: Optional[BrewPiLess] = None
    tilt: Optional[Tilt] = None
    smart_pid: Optional[Gfcc] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Devices':
        assert isinstance(obj, dict)
        plaato_airlock = from_union([BrewPiLess.from_dict, from_none], obj.get("plaatoAirlock"))
        brew_pi_less = from_union([BrewPiLess.from_dict, from_none], obj.get("brewPiLess"))
        my_brewbot = from_union([BrewPiLess.from_dict, from_none], obj.get("myBrewbot"))
        float_hydrometer = from_union([BrewPiLess.from_dict, from_none], obj.get("floatHydrometer"))
        floaty_hydrometer = from_union([BrewPiLess.from_dict, from_none], obj.get("floatyHydrometer"))
        i_spindel = from_union([BrewPiLess.from_dict, from_none], obj.get("iSpindel"))
        plaato_keg = from_union([BrewPiLess.from_dict, from_none], obj.get("plaatoKeg"))
        gfcc = from_union([Gfcc.from_dict, from_none], obj.get("gfcc"))
        stream = from_union([BrewPiLess.from_dict, from_none], obj.get("stream"))
        tilt = from_union([Tilt.from_dict, from_none], obj.get("tilt"))
        smart_pid = from_union([Gfcc.from_dict, from_none], obj.get("smartPid"))
        return Devices(plaato_airlock, brew_pi_less, my_brewbot, float_hydrometer, floaty_hydrometer, i_spindel, plaato_keg, gfcc, stream, tilt, smart_pid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["plaatoAirlock"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.plaato_airlock)
        result["brewPiLess"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.brew_pi_less)
        result["myBrewbot"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.my_brewbot)
        result["floatHydrometer"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.float_hydrometer)
        result["floatyHydrometer"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.floaty_hydrometer)
        result["iSpindel"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.i_spindel)
        result["plaatoKeg"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.plaato_keg)
        result["gfcc"] = from_union([lambda x: to_class(Gfcc, x), from_none], self.gfcc)
        result["stream"] = from_union([lambda x: to_class(BrewPiLess, x), from_none], self.stream)
        result["tilt"] = from_union([lambda x: to_class(Tilt, x), from_none], self.tilt)
        result["smartPid"] = from_union([lambda x: to_class(Gfcc, x), from_none], self.smart_pid)
        return result


@dataclass
class Event:
    event_type: Optional[str] = None
    time: Optional[int] = None
    event_text: Optional[str] = None
    description_html: Optional[str] = None
    notify_time: Optional[int] = None
    active: Optional[bool] = None
    title: Optional[str] = None
    description: Optional[str] = None
    day_event: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        event_type = from_union([from_str, from_none], obj.get("eventType"))
        time = from_union([from_int, from_none], obj.get("time"))
        event_text = from_union([from_none, from_str], obj.get("eventText"))
        description_html = from_union([from_str, from_none], obj.get("descriptionHTML"))
        notify_time = from_union([from_int, from_none], obj.get("notifyTime"))
        active = from_union([from_bool, from_none], obj.get("active"))
        title = from_union([from_str, from_none], obj.get("title"))
        description = from_union([from_str, from_none], obj.get("description"))
        day_event = from_union([from_bool, from_none], obj.get("dayEvent"))
        return Event(event_type, time, event_text, description_html, notify_time, active, title, description, day_event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["eventType"] = from_union([from_str, from_none], self.event_type)
        result["time"] = from_union([from_int, from_none], self.time)
        result["eventText"] = from_union([from_none, from_str], self.event_text)
        result["descriptionHTML"] = from_union([from_str, from_none], self.description_html)
        result["notifyTime"] = from_union([from_int, from_none], self.notify_time)
        result["active"] = from_union([from_bool, from_none], self.active)
        result["title"] = from_union([from_str, from_none], self.title)
        result["description"] = from_union([from_str, from_none], self.description)
        result["dayEvent"] = from_union([from_bool, from_none], self.day_event)
        return result


class NoteType(Enum):
    STATUS_CHANGED = "statusChanged"


@dataclass
class Note:
    note: Optional[str] = None
    type: Optional[NoteType] = None
    status: Optional[str] = None
    timestamp: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Note':
        assert isinstance(obj, dict)
        note = from_union([from_str, from_none], obj.get("note"))
        type = from_union([NoteType, from_none], obj.get("type"))
        status = from_union([from_str, from_none], obj.get("status"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        return Note(note, type, status, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["note"] = from_union([from_str, from_none], self.note)
        result["type"] = from_union([lambda x: to_enum(NoteType, x), from_none], self.type)
        result["status"] = from_union([from_str, from_none], self.status)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        return result


@dataclass
class CarbonationStyle:
    carb_min: Optional[float] = None
    carb_max: Optional[float] = None
    name: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CarbonationStyle':
        assert isinstance(obj, dict)
        carb_min = from_union([from_float, from_none], obj.get("carbMin"))
        carb_max = from_union([from_float, from_none], obj.get("carbMax"))
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("_id"))
        return CarbonationStyle(carb_min, carb_max, name, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["carbMin"] = from_union([to_float, from_none], self.carb_min)
        result["carbMax"] = from_union([to_float, from_none], self.carb_max)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class Data:
    batch_sparge_water_amount1: None
    batch_sparge_water_amount2: None
    batch_sparge_water_amount3: None
    batch_sparge_water_amount4: None
    mash_volume: Optional[float] = None
    strike_temp: Optional[float] = None
    mash_fermentables_amount: Optional[float] = None
    other_fermentables: Optional[List[Fermentable]] = None
    other_fermentables_amount: Optional[float] = None
    all_diastatic_power: Optional[bool] = None
    mash_water_amount: Optional[float] = None
    sparge_water_amount: Optional[float] = None
    total_water_amount: Optional[float] = None
    hlt_water_amount: Optional[float] = None
    hops_amount: Optional[float] = None
    top_up_water: Optional[int] = None
    mash_fermentables: Optional[List[Fermentable]] = None
    total_diastatic_power: Optional[float] = None
    mash_volume_surplus: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        batch_sparge_water_amount1 = from_none(obj.get("batchSpargeWaterAmount1"))
        batch_sparge_water_amount2 = from_none(obj.get("batchSpargeWaterAmount2"))
        batch_sparge_water_amount3 = from_none(obj.get("batchSpargeWaterAmount3"))
        batch_sparge_water_amount4 = from_none(obj.get("batchSpargeWaterAmount4"))
        mash_volume = from_union([from_float, from_none], obj.get("mashVolume"))
        strike_temp = from_union([from_float, from_none], obj.get("strikeTemp"))
        mash_fermentables_amount = from_union([from_float, from_none], obj.get("mashFermentablesAmount"))
        other_fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("otherFermentables"))
        other_fermentables_amount = from_union([from_float, from_none], obj.get("otherFermentablesAmount"))
        all_diastatic_power = from_union([from_bool, from_none], obj.get("allDiastaticPower"))
        mash_water_amount = from_union([from_float, from_none], obj.get("mashWaterAmount"))
        sparge_water_amount = from_union([from_float, from_none], obj.get("spargeWaterAmount"))
        total_water_amount = from_union([from_float, from_none], obj.get("totalWaterAmount"))
        hlt_water_amount = from_union([from_float, from_none], obj.get("hltWaterAmount"))
        hops_amount = from_union([from_float, from_none], obj.get("hopsAmount"))
        top_up_water = from_union([from_int, from_none], obj.get("topUpWater"))
        mash_fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("mashFermentables"))
        total_diastatic_power = from_union([from_float, from_none], obj.get("totalDiastaticPower"))
        mash_volume_surplus = from_union([from_int, from_none], obj.get("mashVolumeSurplus"))
        return Data(batch_sparge_water_amount1, batch_sparge_water_amount2, batch_sparge_water_amount3, batch_sparge_water_amount4, mash_volume, strike_temp, mash_fermentables_amount, other_fermentables, other_fermentables_amount, all_diastatic_power, mash_water_amount, sparge_water_amount, total_water_amount, hlt_water_amount, hops_amount, top_up_water, mash_fermentables, total_diastatic_power, mash_volume_surplus)

    def to_dict(self) -> dict:
        result: dict = {}
        result["batchSpargeWaterAmount1"] = from_none(self.batch_sparge_water_amount1)
        result["batchSpargeWaterAmount2"] = from_none(self.batch_sparge_water_amount2)
        result["batchSpargeWaterAmount3"] = from_none(self.batch_sparge_water_amount3)
        result["batchSpargeWaterAmount4"] = from_none(self.batch_sparge_water_amount4)
        result["mashVolume"] = from_union([to_float, from_none], self.mash_volume)
        result["strikeTemp"] = from_union([to_float, from_none], self.strike_temp)
        result["mashFermentablesAmount"] = from_union([to_float, from_none], self.mash_fermentables_amount)
        result["otherFermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.other_fermentables)
        result["otherFermentablesAmount"] = from_union([to_float, from_none], self.other_fermentables_amount)
        result["allDiastaticPower"] = from_union([from_bool, from_none], self.all_diastatic_power)
        result["mashWaterAmount"] = from_union([to_float, from_none], self.mash_water_amount)
        result["spargeWaterAmount"] = from_union([to_float, from_none], self.sparge_water_amount)
        result["totalWaterAmount"] = from_union([to_float, from_none], self.total_water_amount)
        result["hltWaterAmount"] = from_union([to_float, from_none], self.hlt_water_amount)
        result["hopsAmount"] = from_union([to_float, from_none], self.hops_amount)
        result["topUpWater"] = from_union([from_int, from_none], self.top_up_water)
        result["mashFermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.mash_fermentables)
        result["totalDiastaticPower"] = from_union([to_float, from_none], self.total_diastatic_power)
        result["mashVolumeSurplus"] = from_union([from_int, from_none], self.mash_volume_surplus)
        return result


@dataclass
class Defaults:
    ibu: Optional[str] = None
    altitude: Optional[str] = None
    carbonation: Optional[str] = None
    abv: Optional[str] = None
    color: Optional[str] = None
    temp: Optional[str] = None
    gravity: Optional[str] = None
    hop: Optional[InventoryUnit] = None
    pressure: Optional[str] = None
    weight: Optional[str] = None
    attenuation: Optional[str] = None
    preferred: Optional[str] = None
    grain_color: Optional[str] = None
    volume: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Defaults':
        assert isinstance(obj, dict)
        ibu = from_union([from_str, from_none], obj.get("ibu"))
        altitude = from_union([from_str, from_none], obj.get("altitude"))
        carbonation = from_union([from_str, from_none], obj.get("carbonation"))
        abv = from_union([from_str, from_none], obj.get("abv"))
        color = from_union([from_str, from_none], obj.get("color"))
        temp = from_union([from_str, from_none], obj.get("temp"))
        gravity = from_union([from_str, from_none], obj.get("gravity"))
        hop = from_union([InventoryUnit, from_none], obj.get("hop"))
        pressure = from_union([from_str, from_none], obj.get("pressure"))
        weight = from_union([from_str, from_none], obj.get("weight"))
        attenuation = from_union([from_str, from_none], obj.get("attenuation"))
        preferred = from_union([from_str, from_none], obj.get("preferred"))
        grain_color = from_union([from_str, from_none], obj.get("grainColor"))
        volume = from_union([from_str, from_none], obj.get("volume"))
        return Defaults(ibu, altitude, carbonation, abv, color, temp, gravity, hop, pressure, weight, attenuation, preferred, grain_color, volume)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ibu"] = from_union([from_str, from_none], self.ibu)
        result["altitude"] = from_union([from_str, from_none], self.altitude)
        result["carbonation"] = from_union([from_str, from_none], self.carbonation)
        result["abv"] = from_union([from_str, from_none], self.abv)
        result["color"] = from_union([from_str, from_none], self.color)
        result["temp"] = from_union([from_str, from_none], self.temp)
        result["gravity"] = from_union([from_str, from_none], self.gravity)
        result["hop"] = from_union([lambda x: to_enum(InventoryUnit, x), from_none], self.hop)
        result["pressure"] = from_union([from_str, from_none], self.pressure)
        result["weight"] = from_union([from_str, from_none], self.weight)
        result["attenuation"] = from_union([from_str, from_none], self.attenuation)
        result["preferred"] = from_union([from_str, from_none], self.preferred)
        result["grainColor"] = from_union([from_str, from_none], self.grain_color)
        result["volume"] = from_union([from_str, from_none], self.volume)
        return result


@dataclass
class Meta:
    efficiency_is_calculated: Optional[bool] = None
    mash_efficiency_is_calculated: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        efficiency_is_calculated = from_union([from_bool, from_none], obj.get("efficiencyIsCalculated"))
        mash_efficiency_is_calculated = from_union([from_bool, from_none], obj.get("mashEfficiencyIsCalculated"))
        return Meta(efficiency_is_calculated, mash_efficiency_is_calculated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["efficiencyIsCalculated"] = from_union([from_bool, from_none], self.efficiency_is_calculated)
        result["mashEfficiencyIsCalculated"] = from_union([from_bool, from_none], self.mash_efficiency_is_calculated)
        return result


@dataclass
class Equipment:
    ambient_temperature: None
    water_grain_ratio: None
    sparge_water_min: None
    timestamp: Optional[Created] = None
    sparge_water_formula: Optional[str] = None
    evaporation_rate: Optional[float] = None
    efficiency: Optional[int] = None
    trub_chiller_loss: Optional[float] = None
    fermenter_loss: Optional[int] = None
    sparge_water_reminder_time: Optional[int] = None
    boil_off_per_hr: Optional[float] = None
    version: Optional[Version] = None
    sparge_temperature: Optional[int] = None
    grain_absorption_rate: Optional[float] = None
    boil_time: Optional[int] = None
    created: Optional[Created] = None
    boil_size: Optional[float] = None
    sparge_water_max: Optional[int] = None
    calc_boil_volume: Optional[bool] = None
    water_calculation: Optional[str] = None
    calc_aroma_hop_utilization: Optional[bool] = None
    fermenter_loss_estimate: Optional[int] = None
    mash_water_volume_limit_enabled: Optional[bool] = None
    batch_size: Optional[int] = None
    fermenter_volume: Optional[int] = None
    hidden: Optional[bool] = None
    hopstand_temperature: Optional[int] = None
    notes: Optional[str] = None
    sparge_water_reminder_enabled: Optional[bool] = None
    brewhouse_efficiency: Optional[int] = None
    efficiency_type: Optional[str] = None
    hop_utilization: Optional[int] = None
    meta: Optional[Meta] = None
    calc_mash_efficiency: Optional[bool] = None
    calc_strike_water_temperature: Optional[bool] = None
    rev: Optional[str] = None
    mash_water_min: Optional[int] = None
    id: Optional[str] = None
    mash_efficiency: Optional[float] = None
    post_boil_kettle_vol: Optional[float] = None
    mash_water_max: Optional[int] = None
    mash_tun_dead_space: Optional[int] = None
    fermenter_volume_before_top_up: Optional[int] = None
    mash_water_formula: Optional[str] = None
    bottling_volume: Optional[int] = None
    name: Optional[str] = None
    aroma_hop_utilization: Optional[float] = None
    sparge_water_overflow: Optional[SpargeWaterOverflowEnum] = None
    timestamp_ms: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Equipment':
        assert isinstance(obj, dict)
        ambient_temperature = from_none(obj.get("ambientTemperature"))
        water_grain_ratio = from_none(obj.get("waterGrainRatio"))
        sparge_water_min = from_none(obj.get("spargeWaterMin"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        sparge_water_formula = from_union([from_str, from_none], obj.get("spargeWaterFormula"))
        evaporation_rate = from_union([from_float, from_none], obj.get("evaporationRate"))
        efficiency = from_union([from_int, from_none], obj.get("efficiency"))
        trub_chiller_loss = from_union([from_float, from_none], obj.get("trubChillerLoss"))
        fermenter_loss = from_union([from_int, from_none], obj.get("fermenterLoss"))
        sparge_water_reminder_time = from_union([from_int, from_none], obj.get("spargeWaterReminderTime"))
        boil_off_per_hr = from_union([from_float, from_none], obj.get("boilOffPerHr"))
        version = from_union([Version, from_none], obj.get("_version"))
        sparge_temperature = from_union([from_int, from_none], obj.get("spargeTemperature"))
        grain_absorption_rate = from_union([from_float, from_none], obj.get("grainAbsorptionRate"))
        boil_time = from_union([from_int, from_none], obj.get("boilTime"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        boil_size = from_union([from_float, from_none], obj.get("boilSize"))
        sparge_water_max = from_union([from_int, from_none], obj.get("spargeWaterMax"))
        calc_boil_volume = from_union([from_bool, from_none], obj.get("calcBoilVolume"))
        water_calculation = from_union([from_str, from_none], obj.get("waterCalculation"))
        calc_aroma_hop_utilization = from_union([from_bool, from_none], obj.get("calcAromaHopUtilization"))
        fermenter_loss_estimate = from_union([from_int, from_none], obj.get("fermenterLossEstimate"))
        mash_water_volume_limit_enabled = from_union([from_bool, from_none], obj.get("mashWaterVolumeLimitEnabled"))
        batch_size = from_union([from_int, from_none], obj.get("batchSize"))
        fermenter_volume = from_union([from_int, from_none], obj.get("fermenterVolume"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        hopstand_temperature = from_union([from_int, from_none], obj.get("hopstandTemperature"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        sparge_water_reminder_enabled = from_union([from_bool, from_none], obj.get("spargeWaterReminderEnabled"))
        brewhouse_efficiency = from_union([from_int, from_none], obj.get("brewhouseEfficiency"))
        efficiency_type = from_union([from_str, from_none], obj.get("efficiencyType"))
        hop_utilization = from_union([from_int, from_none], obj.get("hopUtilization"))
        meta = from_union([Meta.from_dict, from_none], obj.get("_meta"))
        calc_mash_efficiency = from_union([from_bool, from_none], obj.get("calcMashEfficiency"))
        calc_strike_water_temperature = from_union([from_bool, from_none], obj.get("calcStrikeWaterTemperature"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        mash_water_min = from_union([from_int, from_none], obj.get("mashWaterMin"))
        id = from_union([from_str, from_none], obj.get("_id"))
        mash_efficiency = from_union([from_float, from_none], obj.get("mashEfficiency"))
        post_boil_kettle_vol = from_union([from_float, from_none], obj.get("postBoilKettleVol"))
        mash_water_max = from_union([from_int, from_none], obj.get("mashWaterMax"))
        mash_tun_dead_space = from_union([from_int, from_none], obj.get("mashTunDeadSpace"))
        fermenter_volume_before_top_up = from_union([from_int, from_none], obj.get("fermenterVolumeBeforeTopUp"))
        mash_water_formula = from_union([from_str, from_none], obj.get("mashWaterFormula"))
        bottling_volume = from_union([from_int, from_none], obj.get("bottlingVolume"))
        name = from_union([from_str, from_none], obj.get("name"))
        aroma_hop_utilization = from_union([from_float, from_none], obj.get("aromaHopUtilization"))
        sparge_water_overflow = from_union([SpargeWaterOverflowEnum, from_none], obj.get("spargeWaterOverflow"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        return Equipment(ambient_temperature, water_grain_ratio, sparge_water_min, timestamp, sparge_water_formula, evaporation_rate, efficiency, trub_chiller_loss, fermenter_loss, sparge_water_reminder_time, boil_off_per_hr, version, sparge_temperature, grain_absorption_rate, boil_time, created, boil_size, sparge_water_max, calc_boil_volume, water_calculation, calc_aroma_hop_utilization, fermenter_loss_estimate, mash_water_volume_limit_enabled, batch_size, fermenter_volume, hidden, hopstand_temperature, notes, sparge_water_reminder_enabled, brewhouse_efficiency, efficiency_type, hop_utilization, meta, calc_mash_efficiency, calc_strike_water_temperature, rev, mash_water_min, id, mash_efficiency, post_boil_kettle_vol, mash_water_max, mash_tun_dead_space, fermenter_volume_before_top_up, mash_water_formula, bottling_volume, name, aroma_hop_utilization, sparge_water_overflow, timestamp_ms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ambientTemperature"] = from_none(self.ambient_temperature)
        result["waterGrainRatio"] = from_none(self.water_grain_ratio)
        result["spargeWaterMin"] = from_none(self.sparge_water_min)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["spargeWaterFormula"] = from_union([from_str, from_none], self.sparge_water_formula)
        result["evaporationRate"] = from_union([to_float, from_none], self.evaporation_rate)
        result["efficiency"] = from_union([from_int, from_none], self.efficiency)
        result["trubChillerLoss"] = from_union([to_float, from_none], self.trub_chiller_loss)
        result["fermenterLoss"] = from_union([from_int, from_none], self.fermenter_loss)
        result["spargeWaterReminderTime"] = from_union([from_int, from_none], self.sparge_water_reminder_time)
        result["boilOffPerHr"] = from_union([to_float, from_none], self.boil_off_per_hr)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["spargeTemperature"] = from_union([from_int, from_none], self.sparge_temperature)
        result["grainAbsorptionRate"] = from_union([to_float, from_none], self.grain_absorption_rate)
        result["boilTime"] = from_union([from_int, from_none], self.boil_time)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["boilSize"] = from_union([to_float, from_none], self.boil_size)
        result["spargeWaterMax"] = from_union([from_int, from_none], self.sparge_water_max)
        result["calcBoilVolume"] = from_union([from_bool, from_none], self.calc_boil_volume)
        result["waterCalculation"] = from_union([from_str, from_none], self.water_calculation)
        result["calcAromaHopUtilization"] = from_union([from_bool, from_none], self.calc_aroma_hop_utilization)
        result["fermenterLossEstimate"] = from_union([from_int, from_none], self.fermenter_loss_estimate)
        result["mashWaterVolumeLimitEnabled"] = from_union([from_bool, from_none], self.mash_water_volume_limit_enabled)
        result["batchSize"] = from_union([from_int, from_none], self.batch_size)
        result["fermenterVolume"] = from_union([from_int, from_none], self.fermenter_volume)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["hopstandTemperature"] = from_union([from_int, from_none], self.hopstand_temperature)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["spargeWaterReminderEnabled"] = from_union([from_bool, from_none], self.sparge_water_reminder_enabled)
        result["brewhouseEfficiency"] = from_union([from_int, from_none], self.brewhouse_efficiency)
        result["efficiencyType"] = from_union([from_str, from_none], self.efficiency_type)
        result["hopUtilization"] = from_union([from_int, from_none], self.hop_utilization)
        result["_meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["calcMashEfficiency"] = from_union([from_bool, from_none], self.calc_mash_efficiency)
        result["calcStrikeWaterTemperature"] = from_union([from_bool, from_none], self.calc_strike_water_temperature)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["mashWaterMin"] = from_union([from_int, from_none], self.mash_water_min)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["mashEfficiency"] = from_union([to_float, from_none], self.mash_efficiency)
        result["postBoilKettleVol"] = from_union([to_float, from_none], self.post_boil_kettle_vol)
        result["mashWaterMax"] = from_union([from_int, from_none], self.mash_water_max)
        result["mashTunDeadSpace"] = from_union([from_int, from_none], self.mash_tun_dead_space)
        result["fermenterVolumeBeforeTopUp"] = from_union([from_int, from_none], self.fermenter_volume_before_top_up)
        result["mashWaterFormula"] = from_union([from_str, from_none], self.mash_water_formula)
        result["bottlingVolume"] = from_union([from_int, from_none], self.bottling_volume)
        result["name"] = from_union([from_str, from_none], self.name)
        result["aromaHopUtilization"] = from_union([to_float, from_none], self.aroma_hop_utilization)
        result["spargeWaterOverflow"] = from_union([lambda x: to_enum(SpargeWaterOverflowEnum, x), from_none], self.sparge_water_overflow)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        return result


@dataclass
class FermentationStep:
    display_pressure: None
    ramp: None
    pressure: None
    name: Optional[str] = None
    step_time: Optional[int] = None
    actual_time: Optional[int] = None
    step_temp: Optional[float] = None
    display_step_temp: Optional[int] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FermentationStep':
        assert isinstance(obj, dict)
        display_pressure = from_none(obj.get("displayPressure"))
        ramp = from_none(obj.get("ramp"))
        pressure = from_none(obj.get("pressure"))
        name = from_union([from_str, from_none], obj.get("name"))
        step_time = from_union([from_int, from_none], obj.get("stepTime"))
        actual_time = from_union([from_int, from_none], obj.get("actualTime"))
        step_temp = from_union([from_float, from_none], obj.get("stepTemp"))
        display_step_temp = from_union([from_int, from_none], obj.get("displayStepTemp"))
        type = from_union([from_str, from_none], obj.get("type"))
        return FermentationStep(display_pressure, ramp, pressure, name, step_time, actual_time, step_temp, display_step_temp, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["displayPressure"] = from_none(self.display_pressure)
        result["ramp"] = from_none(self.ramp)
        result["pressure"] = from_none(self.pressure)
        result["name"] = from_union([from_str, from_none], self.name)
        result["stepTime"] = from_union([from_int, from_none], self.step_time)
        result["actualTime"] = from_union([from_int, from_none], self.actual_time)
        result["stepTemp"] = from_union([to_float, from_none], self.step_temp)
        result["displayStepTemp"] = from_union([from_int, from_none], self.display_step_temp)
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Fermentation:
    timestamp: Optional[Created] = None
    created: Optional[Created] = None
    version: Optional[str] = None
    steps: Optional[List[FermentationStep]] = None
    name: Optional[str] = None
    rev: Optional[str] = None
    id: Optional[str] = None
    timestamp_ms: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Fermentation':
        assert isinstance(obj, dict)
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        version = from_union([from_str, from_none], obj.get("_version"))
        steps = from_union([lambda x: from_list(FermentationStep.from_dict, x), from_none], obj.get("steps"))
        name = from_union([from_str, from_none], obj.get("name"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        id = from_union([from_none, from_str], obj.get("_id"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        return Fermentation(timestamp, created, version, steps, name, rev, id, timestamp_ms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(FermentationStep, x), x), from_none], self.steps)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_id"] = from_union([from_none, from_str], self.id)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        return result


class StepType(Enum):
    INFUSION = "Infusion"
    TEMPERATURE = "Temperature"


@dataclass
class MashStep:
    name: Optional[str] = None
    display_step_temp: Optional[int] = None
    step_temp: Optional[float] = None
    ramp_time: Optional[int] = None
    type: Optional[StepType] = None
    step_time: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MashStep':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        display_step_temp = from_union([from_int, from_none], obj.get("displayStepTemp"))
        step_temp = from_union([from_float, from_none], obj.get("stepTemp"))
        ramp_time = from_union([from_int, from_none], obj.get("rampTime"))
        type = from_union([StepType, from_none], obj.get("type"))
        step_time = from_union([from_int, from_none], obj.get("stepTime"))
        return MashStep(name, display_step_temp, step_temp, ramp_time, type, step_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["displayStepTemp"] = from_union([from_int, from_none], self.display_step_temp)
        result["stepTemp"] = from_union([to_float, from_none], self.step_temp)
        result["rampTime"] = from_union([from_int, from_none], self.ramp_time)
        result["type"] = from_union([lambda x: to_enum(StepType, x), from_none], self.type)
        result["stepTime"] = from_union([from_int, from_none], self.step_time)
        return result


@dataclass
class RecipeMash:
    timestamp: Optional[Created] = None
    created: Optional[Created] = None
    name: Optional[str] = None
    id: Optional[str] = None
    rev: Optional[str] = None
    version: Optional[str] = None
    steps: Optional[List[MashStep]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecipeMash':
        assert isinstance(obj, dict)
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_none, from_str], obj.get("_id"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        version = from_union([from_str, from_none], obj.get("_version"))
        steps = from_union([lambda x: from_list(MashStep.from_dict, x), from_none], obj.get("steps"))
        return RecipeMash(timestamp, created, name, id, rev, version, steps)

    def to_dict(self) -> dict:
        result: dict = {}
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["name"] = from_union([from_str, from_none], self.name)
        result["_id"] = from_union([from_none, from_str], self.id)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["steps"] = from_union([lambda x: from_list(lambda x: to_class(MashStep, x), x), from_none], self.steps)
        return result


@dataclass
class Calories:
    total: Optional[float] = None
    carbs: Optional[float] = None
    alcohol: Optional[float] = None
    k_j: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Calories':
        assert isinstance(obj, dict)
        total = from_union([from_float, from_none], obj.get("total"))
        carbs = from_union([from_float, from_none], obj.get("carbs"))
        alcohol = from_union([from_float, from_none], obj.get("alcohol"))
        k_j = from_union([from_float, from_none], obj.get("kJ"))
        return Calories(total, carbs, alcohol, k_j)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total"] = from_union([to_float, from_none], self.total)
        result["carbs"] = from_union([to_float, from_none], self.carbs)
        result["alcohol"] = from_union([to_float, from_none], self.alcohol)
        result["kJ"] = from_union([to_float, from_none], self.k_j)
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
    ibu_max: Optional[int] = None
    category: Optional[str] = None
    fg_min: Optional[float] = None
    fg_max: Optional[float] = None
    og_max: Optional[float] = None
    id: Optional[str] = None
    ibu_min: Optional[int] = None
    lovibond_max: Optional[int] = None
    og_min: Optional[float] = None
    rbr_max: Optional[float] = None
    abv_max: Optional[float] = None
    bu_gu_max: Optional[float] = None
    name: Optional[str] = None
    color_min: Optional[int] = None
    abv_min: Optional[float] = None
    category_number: Optional[str] = None
    rbr_min: Optional[float] = None
    color_max: Optional[int] = None
    type: Optional[str] = None
    bu_gu_min: Optional[float] = None
    style_letter: Optional[str] = None
    lovibond_min: Optional[int] = None
    style_guide: Optional[str] = None
    carbonation_style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Style':
        assert isinstance(obj, dict)
        carb_max = from_none(obj.get("carbMax"))
        carb_min = from_none(obj.get("carbMin"))
        ibu_max = from_union([from_int, from_none], obj.get("ibuMax"))
        category = from_union([from_str, from_none], obj.get("category"))
        fg_min = from_union([from_float, from_none], obj.get("fgMin"))
        fg_max = from_union([from_float, from_none], obj.get("fgMax"))
        og_max = from_union([from_float, from_none], obj.get("ogMax"))
        id = from_union([from_str, from_none], obj.get("_id"))
        ibu_min = from_union([from_int, from_none], obj.get("ibuMin"))
        lovibond_max = from_union([from_int, from_none], obj.get("lovibondMax"))
        og_min = from_union([from_float, from_none], obj.get("ogMin"))
        rbr_max = from_union([from_float, from_none], obj.get("rbrMax"))
        abv_max = from_union([from_float, from_none], obj.get("abvMax"))
        bu_gu_max = from_union([from_float, from_none], obj.get("buGuMax"))
        name = from_union([from_str, from_none], obj.get("name"))
        color_min = from_union([from_int, from_none], obj.get("colorMin"))
        abv_min = from_union([from_float, from_none], obj.get("abvMin"))
        category_number = from_union([from_str, from_none], obj.get("categoryNumber"))
        rbr_min = from_union([from_float, from_none], obj.get("rbrMin"))
        color_max = from_union([from_int, from_none], obj.get("colorMax"))
        type = from_union([from_none, from_str], obj.get("type"))
        bu_gu_min = from_union([from_float, from_none], obj.get("buGuMin"))
        style_letter = from_union([from_str, from_none], obj.get("styleLetter"))
        lovibond_min = from_union([from_int, from_none], obj.get("lovibondMin"))
        style_guide = from_union([from_str, from_none], obj.get("styleGuide"))
        carbonation_style = from_union([from_str, from_none], obj.get("carbonationStyle"))
        return Style(carb_max, carb_min, ibu_max, category, fg_min, fg_max, og_max, id, ibu_min, lovibond_max, og_min, rbr_max, abv_max, bu_gu_max, name, color_min, abv_min, category_number, rbr_min, color_max, type, bu_gu_min, style_letter, lovibond_min, style_guide, carbonation_style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["carbMax"] = from_none(self.carb_max)
        result["carbMin"] = from_none(self.carb_min)
        result["ibuMax"] = from_union([from_int, from_none], self.ibu_max)
        result["category"] = from_union([from_str, from_none], self.category)
        result["fgMin"] = from_union([to_float, from_none], self.fg_min)
        result["fgMax"] = from_union([to_float, from_none], self.fg_max)
        result["ogMax"] = from_union([to_float, from_none], self.og_max)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["ibuMin"] = from_union([from_int, from_none], self.ibu_min)
        result["lovibondMax"] = from_union([from_int, from_none], self.lovibond_max)
        result["ogMin"] = from_union([to_float, from_none], self.og_min)
        result["rbrMax"] = from_union([to_float, from_none], self.rbr_max)
        result["abvMax"] = from_union([to_float, from_none], self.abv_max)
        result["buGuMax"] = from_union([to_float, from_none], self.bu_gu_max)
        result["name"] = from_union([from_str, from_none], self.name)
        result["colorMin"] = from_union([from_int, from_none], self.color_min)
        result["abvMin"] = from_union([to_float, from_none], self.abv_min)
        result["categoryNumber"] = from_union([from_str, from_none], self.category_number)
        result["rbrMin"] = from_union([to_float, from_none], self.rbr_min)
        result["colorMax"] = from_union([from_int, from_none], self.color_max)
        result["type"] = from_union([from_none, from_str], self.type)
        result["buGuMin"] = from_union([to_float, from_none], self.bu_gu_min)
        result["styleLetter"] = from_union([from_str, from_none], self.style_letter)
        result["lovibondMin"] = from_union([from_int, from_none], self.lovibond_min)
        result["styleGuide"] = from_union([from_str, from_none], self.style_guide)
        result["carbonationStyle"] = from_union([from_str, from_none], self.carbonation_style)
        return result


class MashID(Enum):
    TJF_TI_HX89_DOTR_V_FW_JE3_JOT5_V9_WCR_QN = "tjfTIHx89DotrVFwJe3Jot5v9wcrQn"
    UYSW1_B_GV3_W_VG_Y_LQSO_J_YCG_H1_A_PX_KH_VD = "UYSW1BGv3wVgYLqsoJYcgH1aPXKhVD"


class MashName(Enum):
    AMERSFOORT_2020 = "Amersfoort 2020"
    UTRECHT = "Utrecht"


class Rev(Enum):
    GM9_K_XGYJ_NJDT_HS_UMM_WEP_CE_TB_DILM_ZT = "Gm9kXGYJNjdtHsUMMWepCeTbDilmZT"
    THE_0_RU_DM8_DEROLEI_E_AY_ZD0_EE_D9_U7_M_THJ6 = "0ruDm8deroleiEAyZD0EeD9U7MThj6"
    W3_B4_V_S7_JPPE_T4_PJL_CT_FC33_CN_FM_FP_UN = "W3B4vS7JppeT4PJLCtFc33CnFmFpUN"
    WO61_IW_ND0_PCLIEHV5_V9_PHKI8_O_SC_U9_A = "Wo61IwNd0PCLIEHV5v9Phki8OScU9a"


class MashType(Enum):
    SOURCE = "source"


@dataclass
class SourceClass:
    hidden: Optional[bool] = None
    chloride: Optional[float] = None
    type: Optional[MashType] = None
    residual_alkalinity_meq_l_calc: Optional[float] = None
    timestamp_ms: Optional[int] = None
    calcium: Optional[float] = None
    created: Optional[Created] = None
    id: Optional[MashID] = None
    so_cl_ratio: Optional[float] = None
    rev: Optional[Rev] = None
    ion_balance: Optional[int] = None
    magnesium: Optional[float] = None
    alkalinity: Optional[float] = None
    anions: Optional[float] = None
    version: Optional[Version] = None
    ion_balance_off: Optional[bool] = None
    bicarbonate_meq_l: Optional[float] = None
    sodium: Optional[float] = None
    timestamp: Optional[Created] = None
    bicarbonate: Optional[int] = None
    hardness: Optional[int] = None
    sulfate: Optional[float] = None
    ph: Optional[float] = None
    residual_alkalinity: Optional[float] = None
    cations: Optional[float] = None
    name: Optional[MashName] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SourceClass':
        assert isinstance(obj, dict)
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        type = from_union([MashType, from_none], obj.get("type"))
        residual_alkalinity_meq_l_calc = from_union([from_float, from_none], obj.get("residualAlkalinityMeqLCalc"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        id = from_union([MashID, from_none], obj.get("_id"))
        so_cl_ratio = from_union([from_float, from_none], obj.get("soClRatio"))
        rev = from_union([Rev, from_none], obj.get("_rev"))
        ion_balance = from_union([from_int, from_none], obj.get("ionBalance"))
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        alkalinity = from_union([from_float, from_none], obj.get("alkalinity"))
        anions = from_union([from_float, from_none], obj.get("anions"))
        version = from_union([Version, from_none], obj.get("_version"))
        ion_balance_off = from_union([from_bool, from_none], obj.get("ionBalanceOff"))
        bicarbonate_meq_l = from_union([from_float, from_none], obj.get("bicarbonateMeqL"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        hardness = from_union([from_int, from_none], obj.get("hardness"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        ph = from_union([from_float, from_none], obj.get("ph"))
        residual_alkalinity = from_union([from_float, from_none], obj.get("residualAlkalinity"))
        cations = from_union([from_float, from_none], obj.get("cations"))
        name = from_union([MashName, from_none], obj.get("name"))
        return SourceClass(hidden, chloride, type, residual_alkalinity_meq_l_calc, timestamp_ms, calcium, created, id, so_cl_ratio, rev, ion_balance, magnesium, alkalinity, anions, version, ion_balance_off, bicarbonate_meq_l, sodium, timestamp, bicarbonate, hardness, sulfate, ph, residual_alkalinity, cations, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["type"] = from_union([lambda x: to_enum(MashType, x), from_none], self.type)
        result["residualAlkalinityMeqLCalc"] = from_union([to_float, from_none], self.residual_alkalinity_meq_l_calc)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_id"] = from_union([lambda x: to_enum(MashID, x), from_none], self.id)
        result["soClRatio"] = from_union([to_float, from_none], self.so_cl_ratio)
        result["_rev"] = from_union([lambda x: to_enum(Rev, x), from_none], self.rev)
        result["ionBalance"] = from_union([from_int, from_none], self.ion_balance)
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        result["alkalinity"] = from_union([to_float, from_none], self.alkalinity)
        result["anions"] = from_union([to_float, from_none], self.anions)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["ionBalanceOff"] = from_union([from_bool, from_none], self.ion_balance_off)
        result["bicarbonateMeqL"] = from_union([to_float, from_none], self.bicarbonate_meq_l)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["hardness"] = from_union([from_int, from_none], self.hardness)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["ph"] = from_union([to_float, from_none], self.ph)
        result["residualAlkalinity"] = from_union([to_float, from_none], self.residual_alkalinity)
        result["cations"] = from_union([to_float, from_none], self.cations)
        result["name"] = from_union([lambda x: to_enum(MashName, x), from_none], self.name)
        return result


class AcidType(Enum):
    LACTIC = "lactic"


@dataclass
class Acid:
    alkalinity_meq_l: Optional[float] = None
    type: Optional[AcidType] = None
    concentration: Optional[int] = None
    amount: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Acid':
        assert isinstance(obj, dict)
        alkalinity_meq_l = from_union([from_float, from_none], obj.get("alkalinityMeqL"))
        type = from_union([AcidType, from_none], obj.get("type"))
        concentration = from_union([from_int, from_none], obj.get("concentration"))
        amount = from_union([from_float, from_none], obj.get("amount"))
        return Acid(alkalinity_meq_l, type, concentration, amount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["alkalinityMeqL"] = from_union([to_float, from_none], self.alkalinity_meq_l)
        result["type"] = from_union([lambda x: to_enum(AcidType, x), from_none], self.type)
        result["concentration"] = from_union([from_int, from_none], self.concentration)
        result["amount"] = from_union([to_float, from_none], self.amount)
        return result


@dataclass
class Adjustments:
    calcium_hydroxide: Optional[int] = None
    lt_dwb: Optional[int] = None
    sodium_bicarbonate: Optional[int] = None
    sulfate: Optional[float] = None
    chloride: Optional[float] = None
    calcium_sulfate: Optional[float] = None
    calcium: Optional[float] = None
    bicarbonate: Optional[int] = None
    magnesium_chloride: Optional[int] = None
    calcium_carbonate: Optional[int] = None
    magnesium_sulfate: Optional[float] = None
    calcium_chloride: Optional[float] = None
    lt_ams: Optional[int] = None
    sodium: Optional[float] = None
    sodium_metabisulfite: Optional[int] = None
    acids: Optional[List[Acid]] = None
    magnesium: Optional[float] = None
    sodium_metabisulfite_ppm: Optional[int] = None
    volume: Optional[float] = None
    sodium_chloride: Optional[float] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Adjustments':
        assert isinstance(obj, dict)
        calcium_hydroxide = from_union([from_int, from_none], obj.get("calciumHydroxide"))
        lt_dwb = from_union([from_int, from_none], obj.get("ltDWB"))
        sodium_bicarbonate = from_union([from_int, from_none], obj.get("sodiumBicarbonate"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        calcium_sulfate = from_union([from_float, from_none], obj.get("calciumSulfate"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        magnesium_chloride = from_union([from_int, from_none], obj.get("magnesiumChloride"))
        calcium_carbonate = from_union([from_int, from_none], obj.get("calciumCarbonate"))
        magnesium_sulfate = from_union([from_float, from_none], obj.get("magnesiumSulfate"))
        calcium_chloride = from_union([from_float, from_none], obj.get("calciumChloride"))
        lt_ams = from_union([from_int, from_none], obj.get("ltAMS"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        sodium_metabisulfite = from_union([from_int, from_none], obj.get("sodiumMetabisulfite"))
        acids = from_union([lambda x: from_list(Acid.from_dict, x), from_none], obj.get("acids"))
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        sodium_metabisulfite_ppm = from_union([from_int, from_none], obj.get("sodiumMetabisulfitePPM"))
        volume = from_union([from_float, from_none], obj.get("volume"))
        sodium_chloride = from_union([from_float, from_none], obj.get("sodiumChloride"))
        return Adjustments(calcium_hydroxide, lt_dwb, sodium_bicarbonate, sulfate, chloride, calcium_sulfate, calcium, bicarbonate, magnesium_chloride, calcium_carbonate, magnesium_sulfate, calcium_chloride, lt_ams, sodium, sodium_metabisulfite, acids, magnesium, sodium_metabisulfite_ppm, volume, sodium_chloride)

    def to_dict(self) -> dict:
        result: dict = {}
        result["calciumHydroxide"] = from_union([from_int, from_none], self.calcium_hydroxide)
        result["ltDWB"] = from_union([from_int, from_none], self.lt_dwb)
        result["sodiumBicarbonate"] = from_union([from_int, from_none], self.sodium_bicarbonate)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["calciumSulfate"] = from_union([to_float, from_none], self.calcium_sulfate)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["magnesiumChloride"] = from_union([from_int, from_none], self.magnesium_chloride)
        result["calciumCarbonate"] = from_union([from_int, from_none], self.calcium_carbonate)
        result["magnesiumSulfate"] = from_union([to_float, from_none], self.magnesium_sulfate)
        result["calciumChloride"] = from_union([to_float, from_none], self.calcium_chloride)
        result["ltAMS"] = from_union([from_int, from_none], self.lt_ams)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["sodiumMetabisulfite"] = from_union([from_int, from_none], self.sodium_metabisulfite)
        result["acids"] = from_union([lambda x: from_list(lambda x: to_class(Acid, x), x), from_none], self.acids)
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        result["sodiumMetabisulfitePPM"] = from_union([from_int, from_none], self.sodium_metabisulfite_ppm)
        result["volume"] = from_union([to_float, from_none], self.volume)
        result["sodiumChloride"] = from_union([to_float, from_none], self.sodium_chloride)
        return result


@dataclass
class TargetDiff:
    chloride: Optional[float] = None
    ion_balance_off: Optional[bool] = None
    cations: Optional[float] = None
    magnesium: Optional[float] = None
    bicarbonate_meq_l: Optional[float] = None
    hardness: Optional[int] = None
    so_cl_ratio: Optional[float] = None
    sulfate: Optional[float] = None
    residual_alkalinity: Optional[float] = None
    sodium: Optional[float] = None
    residual_alkalinity_meq_l_calc: Optional[float] = None
    alkalinity: Optional[float] = None
    ion_balance: Optional[int] = None
    calcium: Optional[float] = None
    anions: Optional[float] = None
    bicarbonate: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TargetDiff':
        assert isinstance(obj, dict)
        chloride = from_union([from_float, from_none], obj.get("chloride"))
        ion_balance_off = from_union([from_bool, from_none], obj.get("ionBalanceOff"))
        cations = from_union([from_float, from_none], obj.get("cations"))
        magnesium = from_union([from_float, from_none], obj.get("magnesium"))
        bicarbonate_meq_l = from_union([from_float, from_none], obj.get("bicarbonateMeqL"))
        hardness = from_union([from_int, from_none], obj.get("hardness"))
        so_cl_ratio = from_union([from_float, from_none], obj.get("soClRatio"))
        sulfate = from_union([from_float, from_none], obj.get("sulfate"))
        residual_alkalinity = from_union([from_float, from_none], obj.get("residualAlkalinity"))
        sodium = from_union([from_float, from_none], obj.get("sodium"))
        residual_alkalinity_meq_l_calc = from_union([from_float, from_none], obj.get("residualAlkalinityMeqLCalc"))
        alkalinity = from_union([from_float, from_none], obj.get("alkalinity"))
        ion_balance = from_union([from_int, from_none], obj.get("ionBalance"))
        calcium = from_union([from_float, from_none], obj.get("calcium"))
        anions = from_union([from_float, from_none], obj.get("anions"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        return TargetDiff(chloride, ion_balance_off, cations, magnesium, bicarbonate_meq_l, hardness, so_cl_ratio, sulfate, residual_alkalinity, sodium, residual_alkalinity_meq_l_calc, alkalinity, ion_balance, calcium, anions, bicarbonate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chloride"] = from_union([to_float, from_none], self.chloride)
        result["ionBalanceOff"] = from_union([from_bool, from_none], self.ion_balance_off)
        result["cations"] = from_union([to_float, from_none], self.cations)
        result["magnesium"] = from_union([to_float, from_none], self.magnesium)
        result["bicarbonateMeqL"] = from_union([to_float, from_none], self.bicarbonate_meq_l)
        result["hardness"] = from_union([from_int, from_none], self.hardness)
        result["soClRatio"] = from_union([to_float, from_none], self.so_cl_ratio)
        result["sulfate"] = from_union([to_float, from_none], self.sulfate)
        result["residualAlkalinity"] = from_union([to_float, from_none], self.residual_alkalinity)
        result["sodium"] = from_union([to_float, from_none], self.sodium)
        result["residualAlkalinityMeqLCalc"] = from_union([to_float, from_none], self.residual_alkalinity_meq_l_calc)
        result["alkalinity"] = from_union([to_float, from_none], self.alkalinity)
        result["ionBalance"] = from_union([from_int, from_none], self.ion_balance)
        result["calcium"] = from_union([to_float, from_none], self.calcium)
        result["anions"] = from_union([to_float, from_none], self.anions)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
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
class CalciumCarbonate:
    sparge: Optional[bool] = None
    mash: Optional[bool] = None
    auto: Optional[bool] = None
    form: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CalciumCarbonate':
        assert isinstance(obj, dict)
        sparge = from_union([from_bool, from_none], obj.get("sparge"))
        mash = from_union([from_bool, from_none], obj.get("mash"))
        auto = from_union([from_bool, from_none], obj.get("auto"))
        form = from_union([from_str, from_none], obj.get("form"))
        return CalciumCarbonate(sparge, mash, auto, form)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sparge"] = from_union([from_bool, from_none], self.sparge)
        result["mash"] = from_union([from_bool, from_none], self.mash)
        result["auto"] = from_union([from_bool, from_none], self.auto)
        result["form"] = from_union([from_str, from_none], self.form)
        return result


@dataclass
class WaterSettings:
    calcium_sulfate: Optional[CalciumCarbonate] = None
    magnesium_sulfate: Optional[CalciumCarbonate] = None
    adjust_sparge: Optional[bool] = None
    calcium_hydroxide: Optional[CalciumCarbonate] = None
    sodium_bicarbonate: Optional[CalciumCarbonate] = None
    magnesium_chloride: Optional[CalciumCarbonate] = None
    sodium_chloride: Optional[CalciumCarbonate] = None
    calcium_chloride: Optional[CalciumCarbonate] = None
    calcium_carbonate: Optional[CalciumCarbonate] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WaterSettings':
        assert isinstance(obj, dict)
        calcium_sulfate = from_union([CalciumCarbonate.from_dict, from_none], obj.get("calciumSulfate"))
        magnesium_sulfate = from_union([CalciumCarbonate.from_dict, from_none], obj.get("magnesiumSulfate"))
        adjust_sparge = from_union([from_bool, from_none], obj.get("adjustSparge"))
        calcium_hydroxide = from_union([CalciumCarbonate.from_dict, from_none], obj.get("calciumHydroxide"))
        sodium_bicarbonate = from_union([CalciumCarbonate.from_dict, from_none], obj.get("sodiumBicarbonate"))
        magnesium_chloride = from_union([CalciumCarbonate.from_dict, from_none], obj.get("magnesiumChloride"))
        sodium_chloride = from_union([CalciumCarbonate.from_dict, from_none], obj.get("sodiumChloride"))
        calcium_chloride = from_union([CalciumCarbonate.from_dict, from_none], obj.get("calciumChloride"))
        calcium_carbonate = from_union([CalciumCarbonate.from_dict, from_none], obj.get("calciumCarbonate"))
        return WaterSettings(calcium_sulfate, magnesium_sulfate, adjust_sparge, calcium_hydroxide, sodium_bicarbonate, magnesium_chloride, sodium_chloride, calcium_chloride, calcium_carbonate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["calciumSulfate"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.calcium_sulfate)
        result["magnesiumSulfate"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.magnesium_sulfate)
        result["adjustSparge"] = from_union([from_bool, from_none], self.adjust_sparge)
        result["calciumHydroxide"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.calcium_hydroxide)
        result["sodiumBicarbonate"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.sodium_bicarbonate)
        result["magnesiumChloride"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.magnesium_chloride)
        result["sodiumChloride"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.sodium_chloride)
        result["calciumChloride"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.calcium_chloride)
        result["calciumCarbonate"] = from_union([lambda x: to_class(CalciumCarbonate, x), from_none], self.calcium_carbonate)
        return result


@dataclass
class SpargeAdjustments:
    sodium: Optional[int] = None
    calcium: Optional[int] = None
    chloride: Optional[int] = None
    volume: Optional[float] = None
    sodium_metabisulfite_ppm: Optional[int] = None
    bicarbonate: Optional[int] = None
    sulfate: Optional[int] = None
    magnesium: Optional[int] = None
    acids: Optional[List[Acid]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SpargeAdjustments':
        assert isinstance(obj, dict)
        sodium = from_union([from_int, from_none], obj.get("sodium"))
        calcium = from_union([from_int, from_none], obj.get("calcium"))
        chloride = from_union([from_int, from_none], obj.get("chloride"))
        volume = from_union([from_float, from_none], obj.get("volume"))
        sodium_metabisulfite_ppm = from_union([from_int, from_none], obj.get("sodiumMetabisulfitePPM"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        sulfate = from_union([from_int, from_none], obj.get("sulfate"))
        magnesium = from_union([from_int, from_none], obj.get("magnesium"))
        acids = from_union([lambda x: from_list(Acid.from_dict, x), from_none], obj.get("acids"))
        return SpargeAdjustments(sodium, calcium, chloride, volume, sodium_metabisulfite_ppm, bicarbonate, sulfate, magnesium, acids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sodium"] = from_union([from_int, from_none], self.sodium)
        result["calcium"] = from_union([from_int, from_none], self.calcium)
        result["chloride"] = from_union([from_int, from_none], self.chloride)
        result["volume"] = from_union([to_float, from_none], self.volume)
        result["sodiumMetabisulfitePPM"] = from_union([from_int, from_none], self.sodium_metabisulfite_ppm)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["sulfate"] = from_union([from_int, from_none], self.sulfate)
        result["magnesium"] = from_union([from_int, from_none], self.magnesium)
        result["acids"] = from_union([lambda x: from_list(lambda x: to_class(Acid, x), x), from_none], self.acids)
        return result


@dataclass
class Target:
    sulfate: Optional[int] = None
    chloride: Optional[int] = None
    residual_alkalinity: Optional[float] = None
    bicarbonate_meq_l: Optional[float] = None
    alkalinity: Optional[float] = None
    id: Optional[str] = None
    calcium: Optional[int] = None
    hardness: Optional[int] = None
    anions: Optional[float] = None
    ion_balance_off: Optional[bool] = None
    residual_alkalinity_meq_l_calc: Optional[float] = None
    bicarbonate: Optional[int] = None
    ion_balance: Optional[int] = None
    so_cl_ratio: Optional[float] = None
    type: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    sodium: Optional[int] = None
    magnesium: Optional[int] = None
    cations: Optional[float] = None
    rev: Optional[str] = None
    timestamp_ms: Optional[int] = None
    created: Optional[Created] = None
    version: Optional[str] = None
    timestamp: Optional[Created] = None
    hidden: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Target':
        assert isinstance(obj, dict)
        sulfate = from_union([from_none, from_int, lambda x: int(from_str(x))], obj.get("sulfate"))
        chloride = from_union([from_none, from_int, lambda x: int(from_str(x))], obj.get("chloride"))
        residual_alkalinity = from_union([from_float, from_none], obj.get("residualAlkalinity"))
        bicarbonate_meq_l = from_union([from_float, from_none], obj.get("bicarbonateMeqL"))
        alkalinity = from_union([from_float, from_none], obj.get("alkalinity"))
        id = from_union([from_str, from_none], obj.get("_id"))
        calcium = from_union([from_int, from_none], obj.get("calcium"))
        hardness = from_union([from_int, from_none], obj.get("hardness"))
        anions = from_union([from_float, from_none], obj.get("anions"))
        ion_balance_off = from_union([from_bool, from_none], obj.get("ionBalanceOff"))
        residual_alkalinity_meq_l_calc = from_union([from_float, from_none], obj.get("residualAlkalinityMeqLCalc"))
        bicarbonate = from_union([from_int, from_none], obj.get("bicarbonate"))
        ion_balance = from_union([from_int, from_none], obj.get("ionBalance"))
        so_cl_ratio = from_union([from_float, from_none], obj.get("soClRatio"))
        type = from_union([from_str, from_none], obj.get("type"))
        description = from_union([from_str, from_none], obj.get("description"))
        name = from_union([from_str, from_none], obj.get("name"))
        sodium = from_union([from_int, from_none], obj.get("sodium"))
        magnesium = from_union([from_int, from_none], obj.get("magnesium"))
        cations = from_union([from_float, from_none], obj.get("cations"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        version = from_union([from_str, from_none], obj.get("_version"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        return Target(sulfate, chloride, residual_alkalinity, bicarbonate_meq_l, alkalinity, id, calcium, hardness, anions, ion_balance_off, residual_alkalinity_meq_l_calc, bicarbonate, ion_balance, so_cl_ratio, type, description, name, sodium, magnesium, cations, rev, timestamp_ms, created, version, timestamp, hidden)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sulfate"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_int((lambda x: is_type(int, x))(x))], self.sulfate)
        result["chloride"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_int((lambda x: is_type(int, x))(x))], self.chloride)
        result["residualAlkalinity"] = from_union([to_float, from_none], self.residual_alkalinity)
        result["bicarbonateMeqL"] = from_union([to_float, from_none], self.bicarbonate_meq_l)
        result["alkalinity"] = from_union([to_float, from_none], self.alkalinity)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["calcium"] = from_union([from_int, from_none], self.calcium)
        result["hardness"] = from_union([from_int, from_none], self.hardness)
        result["anions"] = from_union([to_float, from_none], self.anions)
        result["ionBalanceOff"] = from_union([from_bool, from_none], self.ion_balance_off)
        result["residualAlkalinityMeqLCalc"] = from_union([to_float, from_none], self.residual_alkalinity_meq_l_calc)
        result["bicarbonate"] = from_union([from_int, from_none], self.bicarbonate)
        result["ionBalance"] = from_union([from_int, from_none], self.ion_balance)
        result["soClRatio"] = from_union([to_float, from_none], self.so_cl_ratio)
        result["type"] = from_union([from_str, from_none], self.type)
        result["description"] = from_union([from_str, from_none], self.description)
        result["name"] = from_union([from_str, from_none], self.name)
        result["sodium"] = from_union([from_int, from_none], self.sodium)
        result["magnesium"] = from_union([from_int, from_none], self.magnesium)
        result["cations"] = from_union([to_float, from_none], self.cations)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_version"] = from_union([from_str, from_none], self.version)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        return result


@dataclass
class Water:
    sparge_water_amount: None
    dilution_percentage: None
    diluted: None
    mash_water_amount: None
    total: Optional[SourceClass] = None
    target: Optional[Target] = None
    total_adjustments: Optional[Adjustments] = None
    acid_ph_adjustment: Optional[float] = None
    mash: Optional[SourceClass] = None
    enable_sparge_adjustments: Optional[bool] = None
    sparge_adjustments: Optional[SpargeAdjustments] = None
    source_target_diff: Optional[TargetDiff] = None
    source: Optional[SourceClass] = None
    mash_ph_distilled: Optional[float] = None
    mash_adjustments: Optional[Adjustments] = None
    sparge_acid_ph_adjustment: Optional[int] = None
    total_target_diff: Optional[TargetDiff] = None
    sparge_target_diff: Optional[TargetDiff] = None
    mash_target_diff: Optional[TargetDiff] = None
    mash_ph: Optional[float] = None
    sparge: Optional[SourceClass] = None
    style: Optional[str] = None
    meta: Optional[MetaClass] = None
    enable_acid_adjustments: Optional[bool] = None
    settings: Optional[WaterSettings] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Water':
        assert isinstance(obj, dict)
        sparge_water_amount = from_none(obj.get("spargeWaterAmount"))
        dilution_percentage = from_none(obj.get("dilutionPercentage"))
        diluted = from_none(obj.get("diluted"))
        mash_water_amount = from_none(obj.get("mashWaterAmount"))
        total = from_union([SourceClass.from_dict, from_none], obj.get("total"))
        target = from_union([Target.from_dict, from_none], obj.get("target"))
        total_adjustments = from_union([Adjustments.from_dict, from_none], obj.get("totalAdjustments"))
        acid_ph_adjustment = from_union([from_float, from_none], obj.get("acidPhAdjustment"))
        mash = from_union([SourceClass.from_dict, from_none], obj.get("mash"))
        enable_sparge_adjustments = from_union([from_bool, from_none], obj.get("enableSpargeAdjustments"))
        sparge_adjustments = from_union([SpargeAdjustments.from_dict, from_none], obj.get("spargeAdjustments"))
        source_target_diff = from_union([TargetDiff.from_dict, from_none], obj.get("sourceTargetDiff"))
        source = from_union([SourceClass.from_dict, from_none], obj.get("source"))
        mash_ph_distilled = from_union([from_float, from_none], obj.get("mashPhDistilled"))
        mash_adjustments = from_union([Adjustments.from_dict, from_none], obj.get("mashAdjustments"))
        sparge_acid_ph_adjustment = from_union([from_int, from_none], obj.get("spargeAcidPhAdjustment"))
        total_target_diff = from_union([TargetDiff.from_dict, from_none], obj.get("totalTargetDiff"))
        sparge_target_diff = from_union([TargetDiff.from_dict, from_none], obj.get("spargeTargetDiff"))
        mash_target_diff = from_union([TargetDiff.from_dict, from_none], obj.get("mashTargetDiff"))
        mash_ph = from_union([from_float, from_none], obj.get("mashPh"))
        sparge = from_union([SourceClass.from_dict, from_none], obj.get("sparge"))
        style = from_union([from_str, from_none], obj.get("style"))
        meta = from_union([MetaClass.from_dict, from_none], obj.get("meta"))
        enable_acid_adjustments = from_union([from_bool, from_none], obj.get("enableAcidAdjustments"))
        settings = from_union([WaterSettings.from_dict, from_none], obj.get("settings"))
        return Water(sparge_water_amount, dilution_percentage, diluted, mash_water_amount, total, target, total_adjustments, acid_ph_adjustment, mash, enable_sparge_adjustments, sparge_adjustments, source_target_diff, source, mash_ph_distilled, mash_adjustments, sparge_acid_ph_adjustment, total_target_diff, sparge_target_diff, mash_target_diff, mash_ph, sparge, style, meta, enable_acid_adjustments, settings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["spargeWaterAmount"] = from_none(self.sparge_water_amount)
        result["dilutionPercentage"] = from_none(self.dilution_percentage)
        result["diluted"] = from_none(self.diluted)
        result["mashWaterAmount"] = from_none(self.mash_water_amount)
        result["total"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.total)
        result["target"] = from_union([lambda x: to_class(Target, x), from_none], self.target)
        result["totalAdjustments"] = from_union([lambda x: to_class(Adjustments, x), from_none], self.total_adjustments)
        result["acidPhAdjustment"] = from_union([to_float, from_none], self.acid_ph_adjustment)
        result["mash"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.mash)
        result["enableSpargeAdjustments"] = from_union([from_bool, from_none], self.enable_sparge_adjustments)
        result["spargeAdjustments"] = from_union([lambda x: to_class(SpargeAdjustments, x), from_none], self.sparge_adjustments)
        result["sourceTargetDiff"] = from_union([lambda x: to_class(TargetDiff, x), from_none], self.source_target_diff)
        result["source"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.source)
        result["mashPhDistilled"] = from_union([to_float, from_none], self.mash_ph_distilled)
        result["mashAdjustments"] = from_union([lambda x: to_class(Adjustments, x), from_none], self.mash_adjustments)
        result["spargeAcidPhAdjustment"] = from_union([from_int, from_none], self.sparge_acid_ph_adjustment)
        result["totalTargetDiff"] = from_union([lambda x: to_class(TargetDiff, x), from_none], self.total_target_diff)
        result["spargeTargetDiff"] = from_union([lambda x: to_class(TargetDiff, x), from_none], self.sparge_target_diff)
        result["mashTargetDiff"] = from_union([lambda x: to_class(TargetDiff, x), from_none], self.mash_target_diff)
        result["mashPh"] = from_union([to_float, from_none], self.mash_ph)
        result["sparge"] = from_union([lambda x: to_class(SourceClass, x), from_none], self.sparge)
        result["style"] = from_union([from_str, from_none], self.style)
        result["meta"] = from_union([lambda x: to_class(MetaClass, x), from_none], self.meta)
        result["enableAcidAdjustments"] = from_union([from_bool, from_none], self.enable_acid_adjustments)
        result["settings"] = from_union([lambda x: to_class(WaterSettings, x), from_none], self.settings)
        return result


@dataclass
class Recipe:
    tags: None
    recipe_origin: None
    first_wort_gravity: None
    yeast_tolerance_exceeded_by: None
    uid: Optional[str] = None
    style_ibu: Optional[bool] = None
    hops: Optional[List[Hop]] = None
    origin: Optional[str] = None
    timestamp_ms: Optional[int] = None
    recipe_type: Optional[str] = None
    og: Optional[float] = None
    style_bu_gu: Optional[bool] = None
    fermentation: Optional[Fermentation] = None
    hidden: Optional[bool] = None
    nutrition: Optional[Nutrition] = None
    hop_stand_minutes: Optional[int] = None
    fermentables_total_amount: Optional[float] = None
    yeasts: Optional[List[Yeast]] = None
    style_abv: Optional[bool] = None
    public: Optional[bool] = None
    type: Optional[str] = None
    search_tags: Optional[List[str]] = None
    timestamp: Optional[Created] = None
    fg_estimated: Optional[float] = None
    style_color: Optional[bool] = None
    miscs: Optional[List[Misc]] = None
    path: Optional[str] = None
    recipe_public: Optional[bool] = None
    boil_size: Optional[float] = None
    img: Optional[str] = None
    teaser: Optional[str] = None
    style: Optional[Style] = None
    fg: Optional[float] = None
    author: Optional[str] = None
    init: Optional[bool] = None
    carbonation: Optional[float] = None
    style_conformity: Optional[bool] = None
    avg_weighted_hopstand_temp: Optional[int] = None
    boil_time: Optional[int] = None
    post_boil_gravity: Optional[float] = None
    ev: Optional[float] = None
    primary_temp: Optional[float] = None
    thumb: Optional[str] = None
    rb_ratio: Optional[float] = None
    abv: Optional[float] = None
    share: Optional[str] = None
    mash: Optional[RecipeMash] = None
    color: Optional[float] = None
    style_carb: Optional[bool] = None
    ibu_formula: Optional[str] = None
    attenuation: Optional[float] = None
    carbonation_style: Optional[CarbonationStyle] = None
    fermentable_ibu: Optional[int] = None
    created: Optional[Created] = None
    version: Optional[Version] = None
    rev: Optional[str] = None
    notes: Optional[str] = None
    og_plato: Optional[float] = None
    style_og: Optional[bool] = None
    pre_boil_gravity: Optional[float] = None
    extra_gravity: Optional[int] = None
    id: Optional[str] = None
    mash_efficiency: Optional[float] = None
    fermentables: Optional[List[Fermentable]] = None
    fg_formula: Optional[str] = None
    equipment: Optional[Equipment] = None
    batch_size: Optional[int] = None
    efficiency: Optional[int] = None
    diastatic_power: Optional[float] = None
    total_gravity: Optional[float] = None
    style_fg: Optional[bool] = None
    water: Optional[Water] = None
    sum_dry_hop_per_liter: Optional[float] = None
    style_rbr: Optional[bool] = None
    name: Optional[str] = None
    defaults: Optional[Defaults] = None
    hops_total_amount: Optional[float] = None
    ibu: Optional[float] = None
    bu_gu_ratio: Optional[float] = None
    data: Optional[Data] = None
    img_url: Optional[str] = None
    manual_fg: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        tags = from_none(obj.get("tags"))
        recipe_origin = from_none(obj.get("origin"))
        first_wort_gravity = from_none(obj.get("firstWortGravity"))
        yeast_tolerance_exceeded_by = from_none(obj.get("yeastToleranceExceededBy"))
        uid = from_union([from_str, from_none], obj.get("_uid"))
        style_ibu = from_union([from_bool, from_none], obj.get("styleIbu"))
        hops = from_union([lambda x: from_list(Hop.from_dict, x), from_none], obj.get("hops"))
        origin = from_union([from_none, from_str], obj.get("_origin"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        recipe_type = from_union([from_str, from_none], obj.get("type"))
        og = from_union([from_float, from_none], obj.get("og"))
        style_bu_gu = from_union([from_bool, from_none], obj.get("styleBuGu"))
        fermentation = from_union([Fermentation.from_dict, from_none], obj.get("fermentation"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        nutrition = from_union([Nutrition.from_dict, from_none], obj.get("nutrition"))
        hop_stand_minutes = from_union([from_int, from_none], obj.get("hopStandMinutes"))
        fermentables_total_amount = from_union([from_float, from_none], obj.get("fermentablesTotalAmount"))
        yeasts = from_union([lambda x: from_list(Yeast.from_dict, x), from_none], obj.get("yeasts"))
        style_abv = from_union([from_bool, from_none], obj.get("styleAbv"))
        public = from_union([from_bool, from_none], obj.get("_public"))
        type = from_union([from_str, from_none], obj.get("_type"))
        search_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("searchTags"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        fg_estimated = from_union([from_float, from_none], obj.get("fgEstimated"))
        style_color = from_union([from_bool, from_none], obj.get("styleColor"))
        miscs = from_union([lambda x: from_list(Misc.from_dict, x), from_none], obj.get("miscs"))
        path = from_union([from_str, from_none], obj.get("path"))
        recipe_public = from_union([from_bool, from_none], obj.get("public"))
        boil_size = from_union([from_float, from_none], obj.get("boilSize"))
        img = from_union([from_none, from_str], obj.get("img"))
        teaser = from_union([from_str, from_none], obj.get("teaser"))
        style = from_union([Style.from_dict, from_none], obj.get("style"))
        fg = from_union([from_float, from_none], obj.get("fg"))
        author = from_union([from_str, from_none], obj.get("author"))
        init = from_union([from_bool, from_none], obj.get("_init"))
        carbonation = from_union([from_float, from_none], obj.get("carbonation"))
        style_conformity = from_union([from_bool, from_none], obj.get("styleConformity"))
        avg_weighted_hopstand_temp = from_union([from_int, from_none], obj.get("avgWeightedHopstandTemp"))
        boil_time = from_union([from_int, from_none], obj.get("boilTime"))
        post_boil_gravity = from_union([from_float, from_none], obj.get("postBoilGravity"))
        ev = from_union([from_float, from_none], obj.get("_ev"))
        primary_temp = from_union([from_float, from_none], obj.get("primaryTemp"))
        thumb = from_union([from_none, from_str], obj.get("thumb"))
        rb_ratio = from_union([from_float, from_none], obj.get("rbRatio"))
        abv = from_union([from_float, from_none], obj.get("abv"))
        share = from_union([from_none, from_str], obj.get("_share"))
        mash = from_union([RecipeMash.from_dict, from_none], obj.get("mash"))
        color = from_union([from_float, from_none], obj.get("color"))
        style_carb = from_union([from_bool, from_none], obj.get("styleCarb"))
        ibu_formula = from_union([from_str, from_none], obj.get("ibuFormula"))
        attenuation = from_union([from_float, from_none], obj.get("attenuation"))
        carbonation_style = from_union([CarbonationStyle.from_dict, from_none], obj.get("carbonationStyle"))
        fermentable_ibu = from_union([from_int, from_none], obj.get("fermentableIbu"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        version = from_union([Version, from_none], obj.get("_version"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        og_plato = from_union([from_float, from_none], obj.get("ogPlato"))
        style_og = from_union([from_bool, from_none], obj.get("styleOg"))
        pre_boil_gravity = from_union([from_float, from_none], obj.get("preBoilGravity"))
        extra_gravity = from_union([from_int, from_none], obj.get("extraGravity"))
        id = from_union([from_str, from_none], obj.get("_id"))
        mash_efficiency = from_union([from_float, from_none], obj.get("mashEfficiency"))
        fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("fermentables"))
        fg_formula = from_union([from_str, from_none], obj.get("fgFormula"))
        equipment = from_union([Equipment.from_dict, from_none], obj.get("equipment"))
        batch_size = from_union([from_int, from_none], obj.get("batchSize"))
        efficiency = from_union([from_int, from_none], obj.get("efficiency"))
        diastatic_power = from_union([from_float, from_none], obj.get("diastaticPower"))
        total_gravity = from_union([from_float, from_none], obj.get("totalGravity"))
        style_fg = from_union([from_bool, from_none], obj.get("styleFg"))
        water = from_union([Water.from_dict, from_none], obj.get("water"))
        sum_dry_hop_per_liter = from_union([from_float, from_none], obj.get("sumDryHopPerLiter"))
        style_rbr = from_union([from_bool, from_none], obj.get("styleRbr"))
        name = from_union([from_str, from_none], obj.get("name"))
        defaults = from_union([Defaults.from_dict, from_none], obj.get("defaults"))
        hops_total_amount = from_union([from_float, from_none], obj.get("hopsTotalAmount"))
        ibu = from_union([from_float, from_none], obj.get("ibu"))
        bu_gu_ratio = from_union([from_float, from_none], obj.get("buGuRatio"))
        data = from_union([Data.from_dict, from_none], obj.get("data"))
        img_url = from_union([from_str, from_none], obj.get("img_url"))
        manual_fg = from_union([from_bool, from_none], obj.get("manualFg"))
        return Recipe(tags, recipe_origin, first_wort_gravity, yeast_tolerance_exceeded_by, uid, style_ibu, hops, origin, timestamp_ms, recipe_type, og, style_bu_gu, fermentation, hidden, nutrition, hop_stand_minutes, fermentables_total_amount, yeasts, style_abv, public, type, search_tags, timestamp, fg_estimated, style_color, miscs, path, recipe_public, boil_size, img, teaser, style, fg, author, init, carbonation, style_conformity, avg_weighted_hopstand_temp, boil_time, post_boil_gravity, ev, primary_temp, thumb, rb_ratio, abv, share, mash, color, style_carb, ibu_formula, attenuation, carbonation_style, fermentable_ibu, created, version, rev, notes, og_plato, style_og, pre_boil_gravity, extra_gravity, id, mash_efficiency, fermentables, fg_formula, equipment, batch_size, efficiency, diastatic_power, total_gravity, style_fg, water, sum_dry_hop_per_liter, style_rbr, name, defaults, hops_total_amount, ibu, bu_gu_ratio, data, img_url, manual_fg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["tags"] = from_none(self.tags)
        result["origin"] = from_none(self.recipe_origin)
        result["firstWortGravity"] = from_none(self.first_wort_gravity)
        result["yeastToleranceExceededBy"] = from_none(self.yeast_tolerance_exceeded_by)
        result["_uid"] = from_union([from_str, from_none], self.uid)
        result["styleIbu"] = from_union([from_bool, from_none], self.style_ibu)
        result["hops"] = from_union([lambda x: from_list(lambda x: to_class(Hop, x), x), from_none], self.hops)
        result["_origin"] = from_union([from_none, from_str], self.origin)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["type"] = from_union([from_str, from_none], self.recipe_type)
        result["og"] = from_union([to_float, from_none], self.og)
        result["styleBuGu"] = from_union([from_bool, from_none], self.style_bu_gu)
        result["fermentation"] = from_union([lambda x: to_class(Fermentation, x), from_none], self.fermentation)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["nutrition"] = from_union([lambda x: to_class(Nutrition, x), from_none], self.nutrition)
        result["hopStandMinutes"] = from_union([from_int, from_none], self.hop_stand_minutes)
        result["fermentablesTotalAmount"] = from_union([to_float, from_none], self.fermentables_total_amount)
        result["yeasts"] = from_union([lambda x: from_list(lambda x: to_class(Yeast, x), x), from_none], self.yeasts)
        result["styleAbv"] = from_union([from_bool, from_none], self.style_abv)
        result["_public"] = from_union([from_bool, from_none], self.public)
        result["_type"] = from_union([from_str, from_none], self.type)
        result["searchTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.search_tags)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["fgEstimated"] = from_union([to_float, from_none], self.fg_estimated)
        result["styleColor"] = from_union([from_bool, from_none], self.style_color)
        result["miscs"] = from_union([lambda x: from_list(lambda x: to_class(Misc, x), x), from_none], self.miscs)
        result["path"] = from_union([from_str, from_none], self.path)
        result["public"] = from_union([from_bool, from_none], self.recipe_public)
        result["boilSize"] = from_union([to_float, from_none], self.boil_size)
        result["img"] = from_union([from_none, from_str], self.img)
        result["teaser"] = from_union([from_str, from_none], self.teaser)
        result["style"] = from_union([lambda x: to_class(Style, x), from_none], self.style)
        result["fg"] = from_union([to_float, from_none], self.fg)
        result["author"] = from_union([from_str, from_none], self.author)
        result["_init"] = from_union([from_bool, from_none], self.init)
        result["carbonation"] = from_union([to_float, from_none], self.carbonation)
        result["styleConformity"] = from_union([from_bool, from_none], self.style_conformity)
        result["avgWeightedHopstandTemp"] = from_union([from_int, from_none], self.avg_weighted_hopstand_temp)
        result["boilTime"] = from_union([from_int, from_none], self.boil_time)
        result["postBoilGravity"] = from_union([to_float, from_none], self.post_boil_gravity)
        result["_ev"] = from_union([to_float, from_none], self.ev)
        result["primaryTemp"] = from_union([to_float, from_none], self.primary_temp)
        result["thumb"] = from_union([from_none, from_str], self.thumb)
        result["rbRatio"] = from_union([to_float, from_none], self.rb_ratio)
        result["abv"] = from_union([to_float, from_none], self.abv)
        result["_share"] = from_union([from_none, from_str], self.share)
        result["mash"] = from_union([lambda x: to_class(RecipeMash, x), from_none], self.mash)
        result["color"] = from_union([to_float, from_none], self.color)
        result["styleCarb"] = from_union([from_bool, from_none], self.style_carb)
        result["ibuFormula"] = from_union([from_str, from_none], self.ibu_formula)
        result["attenuation"] = from_union([to_float, from_none], self.attenuation)
        result["carbonationStyle"] = from_union([lambda x: to_class(CarbonationStyle, x), from_none], self.carbonation_style)
        result["fermentableIbu"] = from_union([from_int, from_none], self.fermentable_ibu)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["notes"] = from_union([from_str, from_none], self.notes)
        result["ogPlato"] = from_union([to_float, from_none], self.og_plato)
        result["styleOg"] = from_union([from_bool, from_none], self.style_og)
        result["preBoilGravity"] = from_union([to_float, from_none], self.pre_boil_gravity)
        result["extraGravity"] = from_union([from_int, from_none], self.extra_gravity)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["mashEfficiency"] = from_union([to_float, from_none], self.mash_efficiency)
        result["fermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.fermentables)
        result["fgFormula"] = from_union([from_str, from_none], self.fg_formula)
        result["equipment"] = from_union([lambda x: to_class(Equipment, x), from_none], self.equipment)
        result["batchSize"] = from_union([from_int, from_none], self.batch_size)
        result["efficiency"] = from_union([from_int, from_none], self.efficiency)
        result["diastaticPower"] = from_union([to_float, from_none], self.diastatic_power)
        result["totalGravity"] = from_union([to_float, from_none], self.total_gravity)
        result["styleFg"] = from_union([from_bool, from_none], self.style_fg)
        result["water"] = from_union([lambda x: to_class(Water, x), from_none], self.water)
        result["sumDryHopPerLiter"] = from_union([to_float, from_none], self.sum_dry_hop_per_liter)
        result["styleRbr"] = from_union([from_bool, from_none], self.style_rbr)
        result["name"] = from_union([from_str, from_none], self.name)
        result["defaults"] = from_union([lambda x: to_class(Defaults, x), from_none], self.defaults)
        result["hopsTotalAmount"] = from_union([to_float, from_none], self.hops_total_amount)
        result["ibu"] = from_union([to_float, from_none], self.ibu)
        result["buGuRatio"] = from_union([to_float, from_none], self.bu_gu_ratio)
        result["data"] = from_union([lambda x: to_class(Data, x), from_none], self.data)
        result["img_url"] = from_union([from_str, from_none], self.img_url)
        result["manualFg"] = from_union([from_bool, from_none], self.manual_fg)
        return result


@dataclass
class BatchItem:
    measured_conversion_efficiency: None
    priming_sugar_equiv: None
    cost: Optional[Cost] = None
    batch_no: Optional[int] = None
    timestamp_ms: Optional[int] = None
    estimated_bu_gu_ratio: Optional[float] = None
    measured_abv: Optional[float] = None
    version: Optional[Version] = None
    measured_fg: Optional[float] = None
    measured_mash_efficiency: Optional[float] = None
    type: Optional[str] = None
    rev: Optional[str] = None
    estimated_og: Optional[float] = None
    mash_steps_count: Optional[int] = None
    measurements: Optional[List[Any]] = None
    measured_og: Optional[float] = None
    hidden: Optional[bool] = None
    timestamp: Optional[Created] = None
    events: Optional[List[Event]] = None
    boil_steps: Optional[List[BoilStep]] = None
    notes: Optional[List[Note]] = None
    batch_miscs_local: Optional[List[Any]] = None
    batch_yeasts_local: Optional[List[BatchYeastsLocal]] = None
    estimated_total_gravity: Optional[float] = None
    estimated_fg: Optional[float] = None
    fermentation_start_date_set: Optional[bool] = None
    brewer: Optional[str] = None
    carbonation_force: Optional[float] = None
    created: Optional[Created] = None
    brew_date: Optional[int] = None
    carbonation_type: Optional[str] = None
    measured_kettle_efficiency: Optional[float] = None
    brew_controller_enabled: Optional[bool] = None
    measured_post_boil_gravity: Optional[float] = None
    archived: Optional[bool] = None
    recipe: Optional[Recipe] = None
    bottling_date_set: Optional[bool] = None
    init: Optional[bool] = None
    estimated_color: Optional[float] = None
    batch_hops_local: Optional[List[BatchHopsLocal]] = None
    boil_steps_count: Optional[int] = None
    measured_attenuation: Optional[float] = None
    estimated_rb_ratio: Optional[float] = None
    fermentation_start_date: Optional[int] = None
    bottling_date: Optional[int] = None
    fermentation_controller_enabled: Optional[bool] = None
    measured_pre_boil_gravity: Optional[float] = None
    devices: Optional[Devices] = None
    measured_boil_size: Optional[float] = None
    batch_yeasts: Optional[List[Yeast]] = None
    batch_notes: Optional[str] = None
    estimated_ibu: Optional[int] = None
    measured_batch_size: Optional[float] = None
    name: Optional[str] = None
    batch_fermentables: Optional[List[Fermentable]] = None
    batch_hops: Optional[List[Hop]] = None
    hide_batch_events: Optional[bool] = None
    id: Optional[str] = None
    batch_fermentables_local: Optional[List[Any]] = None
    batch_miscs: Optional[List[Misc]] = None
    status: Optional[str] = None
    measured_efficiency: Optional[float] = None
    taste_notes: Optional[str] = None
    taste_rating: Optional[int] = None
    shared: Optional[bool] = None
    share: Optional[str] = None
    measured_bottling_size: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BatchItem':
        assert isinstance(obj, dict)
        measured_conversion_efficiency = from_none(obj.get("measuredConversionEfficiency"))
        priming_sugar_equiv = from_none(obj.get("primingSugarEquiv"))
        cost = from_union([Cost.from_dict, from_none], obj.get("cost"))
        batch_no = from_union([from_int, from_none], obj.get("batchNo"))
        timestamp_ms = from_union([from_int, from_none], obj.get("_timestamp_ms"))
        estimated_bu_gu_ratio = from_union([from_float, from_none], obj.get("estimatedBuGuRatio"))
        measured_abv = from_union([from_float, from_none], obj.get("measuredAbv"))
        version = from_union([Version, from_none], obj.get("_version"))
        measured_fg = from_union([from_float, from_none], obj.get("measuredFg"))
        measured_mash_efficiency = from_union([from_float, from_none], obj.get("measuredMashEfficiency"))
        type = from_union([from_str, from_none], obj.get("_type"))
        rev = from_union([from_str, from_none], obj.get("_rev"))
        estimated_og = from_union([from_float, from_none], obj.get("estimatedOg"))
        mash_steps_count = from_union([from_int, from_none], obj.get("mashStepsCount"))
        measurements = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("measurements"))
        measured_og = from_union([from_float, from_none], obj.get("measuredOg"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        timestamp = from_union([Created.from_dict, from_none], obj.get("_timestamp"))
        events = from_union([lambda x: from_list(Event.from_dict, x), from_none], obj.get("events"))
        boil_steps = from_union([lambda x: from_list(BoilStep.from_dict, x), from_none], obj.get("boilSteps"))
        notes = from_union([lambda x: from_list(Note.from_dict, x), from_none], obj.get("notes"))
        batch_miscs_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchMiscsLocal"))
        batch_yeasts_local = from_union([lambda x: from_list(BatchYeastsLocal.from_dict, x), from_none], obj.get("batchYeastsLocal"))
        estimated_total_gravity = from_union([from_float, from_none], obj.get("estimatedTotalGravity"))
        estimated_fg = from_union([from_float, from_none], obj.get("estimatedFg"))
        fermentation_start_date_set = from_union([from_bool, from_none], obj.get("fermentationStartDateSet"))
        brewer = from_union([from_none, from_str], obj.get("brewer"))
        carbonation_force = from_union([from_float, from_none], obj.get("carbonationForce"))
        created = from_union([Created.from_dict, from_none], obj.get("_created"))
        brew_date = from_union([from_int, from_none], obj.get("brewDate"))
        carbonation_type = from_union([from_str, from_none], obj.get("carbonationType"))
        measured_kettle_efficiency = from_union([from_float, from_none], obj.get("measuredKettleEfficiency"))
        brew_controller_enabled = from_union([from_bool, from_none], obj.get("brewControllerEnabled"))
        measured_post_boil_gravity = from_union([from_float, from_none], obj.get("measuredPostBoilGravity"))
        archived = from_union([from_bool, from_none], obj.get("_archived"))
        recipe = from_union([Recipe.from_dict, from_none], obj.get("recipe"))
        bottling_date_set = from_union([from_bool, from_none], obj.get("bottlingDateSet"))
        init = from_union([from_bool, from_none], obj.get("_init"))
        estimated_color = from_union([from_float, from_none], obj.get("estimatedColor"))
        batch_hops_local = from_union([lambda x: from_list(BatchHopsLocal.from_dict, x), from_none], obj.get("batchHopsLocal"))
        boil_steps_count = from_union([from_int, from_none], obj.get("boilStepsCount"))
        measured_attenuation = from_union([from_float, from_none], obj.get("measuredAttenuation"))
        estimated_rb_ratio = from_union([from_float, from_none], obj.get("estimatedRbRatio"))
        fermentation_start_date = from_union([from_int, from_none], obj.get("fermentationStartDate"))
        bottling_date = from_union([from_int, from_none], obj.get("bottlingDate"))
        fermentation_controller_enabled = from_union([from_bool, from_none], obj.get("fermentationControllerEnabled"))
        measured_pre_boil_gravity = from_union([from_float, from_none], obj.get("measuredPreBoilGravity"))
        devices = from_union([Devices.from_dict, from_none], obj.get("devices"))
        measured_boil_size = from_union([from_float, from_none], obj.get("measuredBoilSize"))
        batch_yeasts = from_union([lambda x: from_list(Yeast.from_dict, x), from_none], obj.get("batchYeasts"))
        batch_notes = from_union([from_str, from_none], obj.get("batchNotes"))
        estimated_ibu = from_union([from_int, from_none], obj.get("estimatedIbu"))
        measured_batch_size = from_union([from_float, from_none], obj.get("measuredBatchSize"))
        name = from_union([from_str, from_none], obj.get("name"))
        batch_fermentables = from_union([lambda x: from_list(Fermentable.from_dict, x), from_none], obj.get("batchFermentables"))
        batch_hops = from_union([lambda x: from_list(Hop.from_dict, x), from_none], obj.get("batchHops"))
        hide_batch_events = from_union([from_bool, from_none], obj.get("hideBatchEvents"))
        id = from_union([from_str, from_none], obj.get("_id"))
        batch_fermentables_local = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("batchFermentablesLocal"))
        batch_miscs = from_union([lambda x: from_list(Misc.from_dict, x), from_none], obj.get("batchMiscs"))
        status = from_union([from_str, from_none], obj.get("status"))
        measured_efficiency = from_union([from_float, from_none], obj.get("measuredEfficiency"))
        taste_notes = from_union([from_str, from_none], obj.get("tasteNotes"))
        taste_rating = from_union([from_int, from_none], obj.get("tasteRating"))
        shared = from_union([from_bool, from_none], obj.get("_shared"))
        share = from_union([from_str, from_none], obj.get("_share"))
        measured_bottling_size = from_union([from_int, from_none], obj.get("measuredBottlingSize"))
        return BatchItem(measured_conversion_efficiency, priming_sugar_equiv, cost, batch_no, timestamp_ms, estimated_bu_gu_ratio, measured_abv, version, measured_fg, measured_mash_efficiency, type, rev, estimated_og, mash_steps_count, measurements, measured_og, hidden, timestamp, events, boil_steps, notes, batch_miscs_local, batch_yeasts_local, estimated_total_gravity, estimated_fg, fermentation_start_date_set, brewer, carbonation_force, created, brew_date, carbonation_type, measured_kettle_efficiency, brew_controller_enabled, measured_post_boil_gravity, archived, recipe, bottling_date_set, init, estimated_color, batch_hops_local, boil_steps_count, measured_attenuation, estimated_rb_ratio, fermentation_start_date, bottling_date, fermentation_controller_enabled, measured_pre_boil_gravity, devices, measured_boil_size, batch_yeasts, batch_notes, estimated_ibu, measured_batch_size, name, batch_fermentables, batch_hops, hide_batch_events, id, batch_fermentables_local, batch_miscs, status, measured_efficiency, taste_notes, taste_rating, shared, share, measured_bottling_size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["measuredConversionEfficiency"] = from_none(self.measured_conversion_efficiency)
        result["primingSugarEquiv"] = from_none(self.priming_sugar_equiv)
        result["cost"] = from_union([lambda x: to_class(Cost, x), from_none], self.cost)
        result["batchNo"] = from_union([from_int, from_none], self.batch_no)
        result["_timestamp_ms"] = from_union([from_int, from_none], self.timestamp_ms)
        result["estimatedBuGuRatio"] = from_union([to_float, from_none], self.estimated_bu_gu_ratio)
        result["measuredAbv"] = from_union([to_float, from_none], self.measured_abv)
        result["_version"] = from_union([lambda x: to_enum(Version, x), from_none], self.version)
        result["measuredFg"] = from_union([to_float, from_none], self.measured_fg)
        result["measuredMashEfficiency"] = from_union([to_float, from_none], self.measured_mash_efficiency)
        result["_type"] = from_union([from_str, from_none], self.type)
        result["_rev"] = from_union([from_str, from_none], self.rev)
        result["estimatedOg"] = from_union([to_float, from_none], self.estimated_og)
        result["mashStepsCount"] = from_union([from_int, from_none], self.mash_steps_count)
        result["measurements"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.measurements)
        result["measuredOg"] = from_union([to_float, from_none], self.measured_og)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["_timestamp"] = from_union([lambda x: to_class(Created, x), from_none], self.timestamp)
        result["events"] = from_union([lambda x: from_list(lambda x: to_class(Event, x), x), from_none], self.events)
        result["boilSteps"] = from_union([lambda x: from_list(lambda x: to_class(BoilStep, x), x), from_none], self.boil_steps)
        result["notes"] = from_union([lambda x: from_list(lambda x: to_class(Note, x), x), from_none], self.notes)
        result["batchMiscsLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_miscs_local)
        result["batchYeastsLocal"] = from_union([lambda x: from_list(lambda x: to_class(BatchYeastsLocal, x), x), from_none], self.batch_yeasts_local)
        result["estimatedTotalGravity"] = from_union([to_float, from_none], self.estimated_total_gravity)
        result["estimatedFg"] = from_union([to_float, from_none], self.estimated_fg)
        result["fermentationStartDateSet"] = from_union([from_bool, from_none], self.fermentation_start_date_set)
        result["brewer"] = from_union([from_none, from_str], self.brewer)
        result["carbonationForce"] = from_union([to_float, from_none], self.carbonation_force)
        result["_created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["brewDate"] = from_union([from_int, from_none], self.brew_date)
        result["carbonationType"] = from_union([from_str, from_none], self.carbonation_type)
        result["measuredKettleEfficiency"] = from_union([to_float, from_none], self.measured_kettle_efficiency)
        result["brewControllerEnabled"] = from_union([from_bool, from_none], self.brew_controller_enabled)
        result["measuredPostBoilGravity"] = from_union([to_float, from_none], self.measured_post_boil_gravity)
        result["_archived"] = from_union([from_bool, from_none], self.archived)
        result["recipe"] = from_union([lambda x: to_class(Recipe, x), from_none], self.recipe)
        result["bottlingDateSet"] = from_union([from_bool, from_none], self.bottling_date_set)
        result["_init"] = from_union([from_bool, from_none], self.init)
        result["estimatedColor"] = from_union([to_float, from_none], self.estimated_color)
        result["batchHopsLocal"] = from_union([lambda x: from_list(lambda x: to_class(BatchHopsLocal, x), x), from_none], self.batch_hops_local)
        result["boilStepsCount"] = from_union([from_int, from_none], self.boil_steps_count)
        result["measuredAttenuation"] = from_union([to_float, from_none], self.measured_attenuation)
        result["estimatedRbRatio"] = from_union([to_float, from_none], self.estimated_rb_ratio)
        result["fermentationStartDate"] = from_union([from_int, from_none], self.fermentation_start_date)
        result["bottlingDate"] = from_union([from_int, from_none], self.bottling_date)
        result["fermentationControllerEnabled"] = from_union([from_bool, from_none], self.fermentation_controller_enabled)
        result["measuredPreBoilGravity"] = from_union([to_float, from_none], self.measured_pre_boil_gravity)
        result["devices"] = from_union([lambda x: to_class(Devices, x), from_none], self.devices)
        result["measuredBoilSize"] = from_union([to_float, from_none], self.measured_boil_size)
        result["batchYeasts"] = from_union([lambda x: from_list(lambda x: to_class(Yeast, x), x), from_none], self.batch_yeasts)
        result["batchNotes"] = from_union([from_str, from_none], self.batch_notes)
        result["estimatedIbu"] = from_union([from_int, from_none], self.estimated_ibu)
        result["measuredBatchSize"] = from_union([to_float, from_none], self.measured_batch_size)
        result["name"] = from_union([from_str, from_none], self.name)
        result["batchFermentables"] = from_union([lambda x: from_list(lambda x: to_class(Fermentable, x), x), from_none], self.batch_fermentables)
        result["batchHops"] = from_union([lambda x: from_list(lambda x: to_class(Hop, x), x), from_none], self.batch_hops)
        result["hideBatchEvents"] = from_union([from_bool, from_none], self.hide_batch_events)
        result["_id"] = from_union([from_str, from_none], self.id)
        result["batchFermentablesLocal"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.batch_fermentables_local)
        result["batchMiscs"] = from_union([lambda x: from_list(lambda x: to_class(Misc, x), x), from_none], self.batch_miscs)
        result["status"] = from_union([from_str, from_none], self.status)
        result["measuredEfficiency"] = from_union([to_float, from_none], self.measured_efficiency)
        result["tasteNotes"] = from_union([from_str, from_none], self.taste_notes)
        result["tasteRating"] = from_union([from_int, from_none], self.taste_rating)
        result["_shared"] = from_union([from_bool, from_none], self.shared)
        result["_share"] = from_union([from_str, from_none], self.share)
        result["measuredBottlingSize"] = from_union([from_int, from_none], self.measured_bottling_size)
        return result


def batch_item_from_dict(s: Any) -> BatchItem:
    return BatchItem.from_dict(s)


# def batch_item_to_dict(x: List[BatchItemElement]) -> Any:
#     return from_list(lambda x: to_class(BatchItemElement, x), x)
