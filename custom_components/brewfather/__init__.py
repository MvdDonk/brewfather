"""The Brewfather integration."""
from __future__ import annotations
import logging
from homeassistant import config_entries, core
from datetime import timedelta
from homeassistant.exceptions import ConfigEntryNotReady 
from homeassistant.const import Platform 

from .coordinator import BrewfatherCoordinator
from .const import (
    DOMAIN,
    COORDINATOR,
    UPDATE_INTERVAL,
    CONF_RAMP_TEMP_CORRECTION,
    VERSION_MAJOR,
    VERSION_MINOR
)

_LOGGER = logging.getLogger(__name__)
PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    # """Setup our skeleton component."""

    update_interval = timedelta(seconds=UPDATE_INTERVAL)
    coordinator = BrewfatherCoordinator(hass, config_entry, update_interval)

    #Signal updates from options flow
    config_entry.async_on_unload(config_entry.add_update_listener(options_update_listener))

    # On Home Assistant startup we want to grab data so all sensors are running and up to date 
    #await coordinator.async_refresh()
    await coordinator.async_config_entry_first_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    """Set up platform from a ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = {
        COORDINATOR: coordinator,
    }

    # This creates each HA object for each platform your device requires.
    # It's done by calling the `async_setup_entry` function in each platform module.
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True

async def options_update_listener(hass: core.HomeAssistant, config_entry: config_entries.ConfigEntry):
    """Handle options update."""
    _LOGGER.debug("options changed")
    await hass.config_entries.async_reload(config_entry.entry_id)

def update_callback(hass, coordinator):
    hass.async_create_task(coordinator.async_request_refresh())

async def async_unload_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    # Pop add-on data
    hass.data[DOMAIN].pop(entry.entry_id)
    #hass.data.pop(ADDONS_COORDINATOR, None)

    return unload_ok

async def async_migrate_entry(hass, config_entry: config_entries.ConfigEntry):
    """Migrate old entry."""
    _LOGGER.debug("Migrating configuration from version %s.%s", config_entry.version, config_entry.minor_version)

    if config_entry.version > 1:
        # This means the user has downgraded from a future version
        return False

    if config_entry.version == 1:

        new_data = {**config_entry.data}
        if config_entry.minor_version < 8:
            new_data[CONF_RAMP_TEMP_CORRECTION] = False
            pass

        hass.config_entries.async_update_entry(config_entry, data=new_data, minor_version=VERSION_MINOR, version=VERSION_MAJOR)

    _LOGGER.debug("Migration to configuration version %s.%s successful", config_entry.version, config_entry.minor_version)

    return True
