"""Config flow for Hello World integration."""
from __future__ import annotations

import logging
from typing import Any
from sqlalchemy import true

import voluptuous as vol

from homeassistant import config_entries, exceptions
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN  # pylint:disable=unused-import
from .connection import *

# from .hub import Hub

from homeassistant.const import (
    CONF_NAME,
    CONF_PASSWORD,
    CONF_USERNAME,
)

_LOGGER = logging.getLogger(__name__)


# This is the schema that used to display the UI to the user. This simple
# schema has a single required host field, but it could include a number of fields
# such as username, password etc. See other components in the HA core code for
# further examples.
# Note the input displayed to the user will be translated. See the
# translations/<lang>.json file and strings.json. See here for further information:
# https://developers.home-assistant.io/docs/config_entries_config_flow_handler/#translations
# At the time of writing I found the translations created by the scaffold didn't
# quite work as documented and always gave me the "Lokalise key references" string
# (in square brackets), rather than the actual translated value. I did not attempt to
# figure this out or look further into it.
# DATA_SCHEMA = vol.Schema({("host"): str})
DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_USERNAME, msg="cxzcxzcxzcxz"): cv.string,
        vol.Required(CONF_PASSWORD, description="dasdsadsadsa"): cv.string,
    }
)


# https://github.com/robinostlund/homeassistant-volkswagencarnet/blob/master/custom_components/volkswagencarnet/config_flow.py
# globale coordinator? https://github.com/robinostlund/homeassistant-volkswagencarnet/blob/master/custom_components/volkswagencarnet/__init__.py


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Hello World."""

    VERSION = 1
    # Pick one of the available connection classes in homeassistant/config_entries.py
    # This tells HA if it should be asking for updates, or it'll be notified of updates
    # automatically. This example uses PUSH, as the dummy hub will notify HA of
    # changes.
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def validate_input(self, data: dict) -> dict[str, any]:
        """Validate the user input allows us to connect.
        Data has the keys from DATA_SCHEMA with values provided by the user.
        """
        # Validate the data can be used to set up a connection.
        name = data.get(CONF_NAME, False)

        connection = Connection(data.get(CONF_USERNAME, False), data.get(CONF_PASSWORD, False))

        result = await connection.test_connection()
        return {"status": result, "name": name}

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        # This goes through the steps to take the user through the setup process.
        # Using this it is possible to update the UI and prompt for additional
        # information. This example provides a single form (built from `DATA_SCHEMA`),
        # and when that has some validated input, it calls `async_create_entry` to
        # actually create the HA config entry. Note the "title" value is returned by
        # `validate_input` above.
        errors = {}
        if user_input is not None:

            # uniek stuff:
            # await self.async_set_unique_id(device_unique_id)
            # self._abort_if_unique_id_configured()

            # https://developers.home-assistant.io/docs/config_entries_config_flow_handler/

            try:
                validationResult = await self.validate_input(user_input)
            except InvalidCredentials:
                errors["base"] = "invalid_api_key"
            except InvalidScope:
                errors["base"] = "invalid_scope"
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

            if validationResult["status"] == True:
                name = validationResult["name"]
                existing_entry = await self.async_set_unique_id(name)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(title=name, data=user_input)

        return await self._show_config_form(user_input, errors)

    async def _show_config_form(self, user_input, errors):
        """Show the configuration form to edit location data."""
        if not user_input:
            user_input = {}

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default=user_input.get(CONF_NAME, False)
                    ): str,
                    vol.Required(
                        CONF_USERNAME, default=user_input.get(CONF_USERNAME, False)
                    ): str,
                    vol.Required(
                        CONF_PASSWORD, default=user_input.get(CONF_PASSWORD, False)
                    ): str,
                }
            ),
            errors=errors,
        )


# class CannotConnect(exceptions.HomeAssistantError):
#     """Error to indicate we cannot connect."""


# class InvalidHost(exceptions.HomeAssistantError):
#     """Error to indicate there is an invalid hostname."""
