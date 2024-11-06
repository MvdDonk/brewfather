"""The Brewfather integration."""
from __future__ import annotations
import logging
from homeassistant import config_entries, core
from datetime import timedelta
from homeassistant.const import CONF_NAME
from homeassistant.exceptions import ConfigEntryNotReady 
from homeassistant.const import Platform 

from .coordinator import BrewfatherCoordinator
from .const import (
    DOMAIN,
    COORDINATOR,
    CONNECTION_NAME,
    UPDATE_INTERVAL,
    CONF_SINGLEBATCHMODE,
    VERSION_MAJOR,
    VERSION_MINOR
)

_LOGGER = logging.getLogger(__name__)
PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    # """Setup our skeleton component."""

    update_interval = timedelta(seconds=UPDATE_INTERVAL)
    coordinator = BrewfatherCoordinator(hass, config_entry, update_interval)

    ## On Home Assistant startup we want to grab data so all sensors are running and up to date 
    #await coordinator.async_refresh()

    # if not coordinator.last_update_success:
    #     raise ConfigEntryNotReady

    """Set up platform from a ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = {
        COORDINATOR: coordinator,
        CONNECTION_NAME: config_entry.data[CONF_NAME],
    }

    # This creates each HA object for each platform your device requires.
    # It's done by calling the `async_setup_entry` function in each platform module.
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True

def update_callback(hass, coordinator):
    hass.async_create_task(coordinator.async_request_refresh())

async def async_migrate_entry(hass, config_entry: config_entries.ConfigEntry):
    """Migrate old entry."""
    _LOGGER.debug("Migrating configuration from version %s.%s", config_entry.version, config_entry.minor_version)

    if config_entry.version > 1:
        # This means the user has downgraded from a future version
        return False

    if config_entry.version == 1:

        new_data = {**config_entry.data}
        if config_entry.minor_version < 5:
            new_data[CONF_SINGLEBATCHMODE] = True
            pass

        hass.config_entries.async_update_entry(config_entry, data=new_data, minor_version=VERSION_MINOR, version=VERSION_MAJOR)

    _LOGGER.debug("Migration to configuration version %s.%s successful", config_entry.version, config_entry.minor_version)

    return True
