"""Platform for sensor integration."""
from __future__ import annotations

import json
from datetime import datetime, timezone
import enum
import logging
from typing import cast


from homeassistant.config_entries import ConfigEntry
from .const import *
from .coordinator import BrewfatherCoordinator

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.const import (
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_TIMESTAMP,
    TEMP_CELSIUS, UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
):
    """Set up the sensor platforms."""
    _LOGGER.debug("async_setup_entry")
    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    connectionName = hass.data[DOMAIN][entry.entry_id][CONNECTION_NAME]
    sensors = []

    sensors.append(
        BrewfatherSensor(
            coordinator,
            "Recipe name",
            SensorKinds.fermenting_name,
            "mdi:glass-mug",
            connectionName,
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            "Current temperature",
            SensorKinds.fermenting_current_temperature,
            "mdi:thermometer",
            connectionName,
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            "Upcoming temperature",
            SensorKinds.fermenting_next_temperature,
            "mdi:thermometer-chevron-up",
            connectionName,
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            "Upcoming temperature change",
            SensorKinds.fermenting_next_date,
            "mdi:clock",
            connectionName,
        )
    )

    sensors.append(
        BrewfatherSensor(
            coordinator,
            "Fermenting batches",
            SensorKinds.fermenting_batches,
            "mdi:glass-mug",
            connectionName,
        )
    )
    async_add_entities(sensors)


class BrewfatherSensor(CoordinatorEntity[SensorEntity]):
    """Defines a sensor."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        name: str,
        sensorKind: SensorKinds,
        icon: str,
        connectionName: str,
    ):
        """Initialize Entities."""

        super().__init__(coordinator=coordinator)

        # https://developers.home-assistant.io/docs/entity_registry_index/
        self.batches = None
        self._attr_name = f"{name}"
        self._attr_unique_id = f"{DOMAIN}_{connectionName}_{sensorKind}"
        self._state = None
        self._icon = icon
        self._kind = sensorKind
        self._unit_of_measure = None
        self.attrs = {}
        if self._kind == SensorKinds.fermenting_current_temperature:
            self._attr_state_class = SensorStateClass.MEASUREMENT

        if "temperature" in str(self._kind):
            self._unit_of_measure = TEMP_CELSIUS
            self._attr_device_class = DEVICE_CLASS_TEMPERATURE
        elif "date" in str(self._kind):
            self._attr_device_class = DEVICE_CLASS_TIMESTAMP

    @property
    def icon(self):
        """Return the icon for this entity."""
        return self._icon

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement for this entity."""
        return self._unit_of_measure

    # @property
    # def device_info(self):
    #     """Define the device based on device_identifier."""

    #     device_name = "SpaceX Launches"
    #     device_model = "Launch"

    #     if self._device_identifier != "spacexlaunch":
    #         device_name = "SpaceX Starman"
    #         device_model = "Starman"

    #     return {
    #         ATTR_IDENTIFIERS: {(DOMAIN, self._device_identifier)},
    #         ATTR_NAME: device_name,
    #         ATTR_MANUFACTURER: "SpaceX",
    #         ATTR_MODEL: device_model,
    #     }

    @property
    def state(self) -> StateType:
        """Return the state."""
        brewfatherCoordinator: BrewfatherCoordinator = self.coordinator

        if brewfatherCoordinator.data is None:
            self._state = None
        else:
            if self._kind == SensorKinds.fermenting_name:
                self._state = brewfatherCoordinator.data.brew_name
            elif self._kind == SensorKinds.fermenting_current_temperature:
                self._state = brewfatherCoordinator.data.current_step_temperature
            elif self._kind == SensorKinds.fermenting_next_date:
                self._state = brewfatherCoordinator.data.next_step_date
            elif self._kind == SensorKinds.fermenting_next_temperature:
                self._state = brewfatherCoordinator.data.next_step_temperature
            elif self._kind == SensorKinds.fermenting_batches:
                self._state = len(brewfatherCoordinator.data.batches)
                self.batches = brewfatherCoordinator.data.batches

        # Received a datetime
        if self._state is not None and self.device_class == DEVICE_CLASS_TIMESTAMP:
            try:
                # We cast the value, to avoid using isinstance, but satisfy
                # typechecking. The errors are guarded in this try.
                value = cast(datetime, self._state)
                if value.tzinfo is None:
                    raise ValueError(
                        f"Invalid datetime: {self.entity_id} provides state '{value}', "
                        "which is missing timezone information"
                    )

                if value.tzinfo != timezone.utc:
                    value = value.astimezone(timezone.utc)

                _LOGGER.debug("value %s, %s", value, value.tzinfo)

                return value.isoformat(timespec="seconds")
            except (AttributeError, TypeError) as err:
                raise ValueError(
                    f"Invalid datetime: {self.entity_id} has a timestamp device class"
                    f"but does not provide a datetime state but {type(value)}"
                ) from err

        return self._state

    @property
    def extra_state_attributes(self):
        if self.batches is None:
            return None
        attributes = {}
        attributes["data"] = []
        for batch in self.batches:
            attributes["data"].append(batch.to_attribute_entry_hassio())
        return attributes

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        brewfatherCoordinator: BrewfatherCoordinator = self.coordinator
        self._attr_available = brewfatherCoordinator.data is not None
        return self._attr_available

    async def async_update(self):
        """Update Sensor Entity."""
        await self.coordinator.async_request_refresh()
        _LOGGER.debug("Updating state of the sensors.")

    async def async_added_to_hass(self):
        """Subscribe to updates."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )


class SensorKinds(enum.Enum):
    fermenting_name = 1
    fermenting_current_temperature = 2
    fermenting_next_temperature = 3
    fermenting_next_date = 4
    fermenting_batches = 5
