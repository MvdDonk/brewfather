"""The Candy integration."""
from __future__ import annotations
import datetime

# https://github.com/robinostlund/homeassistant-volkswagencarnet/blob/master/custom_components/volkswagencarnet/__init__.py
import logging
from datetime import datetime, timezone, timedelta
from typing import TypedDict, Optional

from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable

import aiohttp
import json


# from models.batches_item import BatchesItemElement
from .models.batches_item import BatchesItemElement, batches_item_from_dict
from .models.batch_item import BatchItem, batch_item_from_dict, FermentationStep

# ontwikkelogmvign: https://developers.home-assistant.io/docs/development_environment/

# voorbeeld https://github.com/black-roland/homeassistant-microsoft-todo/tree/master/custom_components/microsoft_todo
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryNotReady

from .coordinator import BrewfatherCoordinator
from .const import *
from .testdata import TESTDATA_BATCH

_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["sensor"]
REQUEST_TIMEOUT = 10
UPDATE_INTERVAL = 3600
MS_IN_DAY = 86400000
BATCHES_URI = "https://api.brewfather.app/v1/batches/"
BATCH_URI = "https://api.brewfather.app/v1/batches/{}"


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    # hass.states.async_set("brewfather.Hello_World", "Works!2")

    update_interval = timedelta(seconds=UPDATE_INTERVAL)
    coordinator = BrewfatherCoordinator(hass, config_entry, update_interval)

    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady
    hass.data.setdefault(DOMAIN, {})
    _LOGGER.debug("%s", config_entry.data[CONF_NAME])
    hass.data[DOMAIN][config_entry.entry_id] = {
        COORDINATOR: coordinator,
        CONNECTION_NAME: config_entry.data[CONF_NAME],
    }

    for component in PLATFORMS:
        _LOGGER.info("Setting up platform: %s", component)
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(config_entry, component)
        )

    # Return boolean to indicate that initialization was successfully.
    return True


def update_callback(hass, coordinator):
    _LOGGER.debug("CALLBACK!")
    hass.async_create_task(coordinator.async_request_refresh())
