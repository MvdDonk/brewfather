"""Platform for sensor integration."""
from __future__ import annotations
from datetime import datetime, timezone
import enum
import logging
from typing import Mapping, cast, Any
from custom_components.brewfather.models.reading_item import Reading
from homeassistant.core import callback
from homeassistant.config_entries import ConfigEntry
from .const import (
    DOMAIN,
    COORDINATOR
)
from homeassistant.const import UnitOfTemperature
from .coordinator import BrewfatherCoordinator, BrewfatherCoordinatorData
from homeassistant.components.sensor import SensorEntity, SensorStateClass, SensorEntityDescription, SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

_LOGGER = logging.getLogger(__name__)
SENSOR_PREFIX = "Brewfather"
async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    """Set up the sensor platforms."""
    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    sensors = []


    sensors.append(
        BrewfatherSensor(
            coordinator,
            SensorKinds.fermenting_name,
            SensorEntityDescription(
                key="batch_recipe_name",
                name="Batch recipe name",
                icon="mdi:glass-mug",
            )
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            SensorKinds.fermenting_current_temperature,
            SensorEntityDescription(
                key="batch_target_temperature",
                name="Batch target temperature",
                icon="mdi:thermometer",
                #native_unit_of_measurement=UnitOfTemperature.CELSIUS, #Should we support fahrenheit?
                device_class=SensorDeviceClass.TEMPERATURE,
                state_class=SensorStateClass.MEASUREMENT,
            )
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            SensorKinds.fermenting_next_temperature,
            SensorEntityDescription(
                key="batch_upcoming_target_temperature",
                name="Batch upcoming target temperature",
                icon="mdi:thermometer-chevron-up",
                native_unit_of_measurement=UnitOfTemperature.CELSIUS, #Should we support fahrenheit?
                device_class=SensorDeviceClass.TEMPERATURE,
            )
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            SensorKinds.fermenting_next_date,
            SensorEntityDescription(
                key="batch_upcoming_target_temperature_change",
                name="Batch upcoming target temperature change",
                icon="mdi:clock",
                device_class=SensorDeviceClass.TIMESTAMP,
            )
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            SensorKinds.fermenting_last_reading,
            SensorEntityDescription(
                key="batch_last_reading",
                name="Batch last reading",
                icon="mdi:chart-line",
                state_class=SensorStateClass.MEASUREMENT,
            )
        )
    )

    # sensors.append(
    #     BrewfatherSensor(
    #         coordinator,
    #         "Fermenting batches",
    #         SensorKinds.fermenting_batches,
    #         "mdi:glass-mug",
    #         connectionName,
    #     )
    # )
    # async_add_entities(
    #     BrewfatherSensor(coordinator, idx, ent) for idx, ent in enumerate(sensors)
    # )
    #coordinator.async_add_listener
    async_add_entities(sensors, update_before_add=False)


class BrewfatherSensor(CoordinatorEntity[BrewfatherCoordinator], SensorEntity):
    """An entity using CoordinatorEntity.

    The CoordinatorEntity class provides:
      should_poll
      async_update
      async_added_to_hass
      available

    """
    """Defines a sensor."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        sensorKind: SensorKinds,
        description: SensorEntityDescription,
    ):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator)

        self._entity_description = description
        self._sensor_type = sensorKind
        self.device_type = self._entity_description.key

        self._attr_name = f"{SENSOR_PREFIX} {self._entity_description.name}"
        self._attr_unique_id = f"{SENSOR_PREFIX}_{self._entity_description.name}"

        self._attr_icon = self._entity_description.icon
        self._attr_state_class = self._entity_description.state_class
        self._attr_native_unit_of_measurement = self._entity_description.native_unit_of_measurement
        self._attr_device_class = self._entity_description.device_class
        #self._state = None
        self._discovery = False
        self._dev_id = {}

        brewfatherCoordinator: BrewfatherCoordinator = coordinator
        sensor_data = self._refresh_sensor_data(brewfatherCoordinator.data, self._sensor_type, self.device_class, self.entity_id)
        self._state = sensor_data.state
        self._attr_available = sensor_data.attr_available
        self._attr_extra_state_attributes = sensor_data.extra_state_attributes
        
    @property
    def state(self) -> StateType:
        """Return the state."""
        return self._state

    # @property
    # def extra_state_attributes(self):
    #     if self.batches is None:
    #         return None
    #     attributes = {}
    #     attributes["data"] = []
    #     for batch in self.batches:
    #         attributes["data"].append(batch.to_attribute_entry_hassio())
    #     return attributes

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._attr_available

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        """Update Sensor Entity."""
        _LOGGER.debug(" _handle_coordinator_update Updating state of the sensors.")
        #await self.coordinator.async_request_refresh()
        brewfatherCoordinator: BrewfatherCoordinator = self.coordinator
        sensor_data = self._refresh_sensor_data(brewfatherCoordinator.data, self._sensor_type, self.device_class, self.entity_id)
        self._state = sensor_data.state
        self._attr_available = sensor_data.attr_available
        self.async_write_ha_state()

    @staticmethod
    def _refresh_sensor_data(
        data: BrewfatherCoordinatorData,
        sensor_type: str,
        device_class: SensorDeviceClass,
        entity_id: str
    ) -> SensorUpdateData:
        """Get sensor data."""
        sensor_data = SensorUpdateData()
        if data is None:
            return sensor_data
        
        sensor_data.attr_available = True
        custom_attributes:dict[str, Any] = dict()

        if sensor_type == SensorKinds.fermenting_name:
            sensor_data.state = data.brew_name
        elif sensor_type == SensorKinds.fermenting_current_temperature:
            sensor_data.state = data.current_step_temperature
        elif sensor_type == SensorKinds.fermenting_next_date:
            sensor_data.state = data.next_step_date
        elif sensor_type == SensorKinds.fermenting_next_temperature:
            sensor_data.state = data.next_step_temperature
        elif sensor_type == SensorKinds.fermenting_last_reading:
            sensor_data.state = data.last_reading.sg

            custom_attributes["angle"] = data.last_reading.angle
            custom_attributes["temp"] = data.last_reading.temp
            custom_attributes["time_ms"] = data.last_reading.time
            custom_attributes["time"] = datetime.fromtimestamp(data.last_reading.time / 1000, timezone.utc)

        elif sensor_type == SensorKinds.fermenting_batches:
            sensor_data.state = len(data.batches)
            #batches = data.batches

        sensor_data.extra_state_attributes = custom_attributes

        # Received a datetime
        if sensor_data.state is not None and device_class == SensorDeviceClass.TIMESTAMP:
            try:
                # We cast the value, to avoid using isinstance, but satisfy
                # typechecking. The errors are guarded in this try.
                value = cast(datetime, sensor_data.state)
                if value.tzinfo is None:
                    raise ValueError(
                        f"Invalid datetime: {entity_id} provides state '{value}', "
                        "which is missing timezone information"
                    )

                if value.tzinfo != timezone.utc:
                    value = value.astimezone(timezone.utc)

                _LOGGER.debug("value %s, %s", value, value.tzinfo)

                #return value.isoformat(timespec="seconds")
                sensor_data.state =value.isoformat(timespec="seconds")
            except (AttributeError, TypeError) as err:
                raise ValueError(
                    f"Invalid datetime: {entity_id} has a timestamp device class"
                    f"but does not provide a datetime state but {type(value)}"
                ) from err
            
        return sensor_data
            

    # async def async_added_to_hass(self):
    #     """Subscribe to updates."""
    #     self.async_on_remove(
    #         self.coordinator.async_add_listener(self.async_write_ha_state)
    #     )

class SensorUpdateData:
    state: Any
    attr_available: bool
    extra_state_attributes: dict[str, Any]
    
    def __init__(self):
        self.state = None
        self.attr_available = False
        self.extra_state_attributes = dict()

class SensorKinds(enum.Enum):
    fermenting_name = 1
    fermenting_current_temperature = 2
    fermenting_next_temperature = 3
    fermenting_next_date = 4
    fermenting_batches = 5
    fermenting_last_reading = 6