from __future__ import annotations
from copy import deepcopy
import logging
from typing import Any, Dict, Optional
import voluptuous as vol  # type: ignore
from homeassistant import config_entries 
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv 
from .const import (
    DOMAIN,
    CONF_RAMP_TEMP_CORRECTION,
    VERSION_MAJOR,
    VERSION_MINOR,
)
from .connection import (
    Connection,
    CannotConnect,
    InvalidCredentials,
    InvalidScope
)
from homeassistant.const import ( 
    CONF_NAME,
    CONF_PASSWORD,
    CONF_USERNAME,
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_RAMP_TEMP_CORRECTION): cv.boolean,
    }
)

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_RAMP_TEMP_CORRECTION): cv.boolean,
    }
)


async def validate_auth(username:str, password:str) -> dict[str, any]:
    """Validate the user input allows us to connect."""

    connection = Connection(username, password)
    result = await connection.test_connection()
    return result
    
class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Brewfather."""
    VERSION = VERSION_MAJOR
    MINOR_VERSION = VERSION_MINOR
    
    # Pick one of the available connection classes in homeassistant/config_entries.py
    # This tells HA if it should be asking for updates, or it'll be notified of updates
    # automatically. This example uses PUSH, as the dummy hub will notify HA of
    # changes.
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Handle the user setup step."""
        errors: Dict[str, str] = {}
        validCredentials: bool = False
        if user_input is not None:     
            try:
                username = user_input.get(CONF_USERNAME, False)
                password = user_input.get(CONF_PASSWORD, False)
                
                validCredentials = await validate_auth(username, password)
            except InvalidCredentials:
                errors["base"] = "invalid_api_key"
            except InvalidScope:
                errors["base"] = "invalid_scope"
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception as ex:
                _LOGGER.error("Unexpected exception when testing connection: %s", str(ex))
                errors["base"] = "unknown"
                
        if not errors and validCredentials:
            # Input is valid, set data.
            name = user_input.get(CONF_NAME, False)
            await self.async_set_unique_id(name)
            self._abort_if_unique_id_configured()

            temp_correction = user_input.get(CONF_RAMP_TEMP_CORRECTION, False)
            self.data = ConfigFlow.get_config_entry(name, username, password, temp_correction)
            return self.async_create_entry(title=name, data=self.data)
        
        return self.async_show_form(
            step_id="user", data_schema=CONFIG_SCHEMA, errors=errors
        )   

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> OptionsFlowHandler:
        """Create the options flow."""
        return OptionsFlowHandler(config_entry)
    
    @staticmethod
    def get_config_entry(name:str, username: str, password: str, temp_correction: bool
    ) -> dict[str, Any]:
        """Create the config object."""
        config:dict[str, Any] = {
                CONF_NAME: name,
                CONF_USERNAME: username,
                CONF_PASSWORD: password,
                CONF_RAMP_TEMP_CORRECTION: temp_correction,
            }
        return config

class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Manage the options."""
        if user_input is not None:

            new_config = ConfigFlow.get_config_entry(
                self.config_entry.data.get(CONF_NAME),
                self.config_entry.data.get(CONF_USERNAME),
                self.config_entry.data.get(CONF_PASSWORD),
                user_input.get(CONF_RAMP_TEMP_CORRECTION)
            )

            # update config entry
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=new_config, options=self.config_entry.options
            )

            return self.async_create_entry(title="Brewfather", data=new_config)

        return self.async_show_form(
            step_id="init",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_SCHEMA, self.config_entry.data
            ),
        )
