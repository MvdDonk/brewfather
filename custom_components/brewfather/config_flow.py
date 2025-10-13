from __future__ import annotations
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
    CONF_MULTI_BATCH,
    CONF_ALL_BATCH_INFO_SENSOR,
    CONF_CUSTOM_STREAM_ENABLED,
    CONF_CUSTOM_STREAM_LOGGING_ID,
    CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME,
    CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE,
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
        vol.Required(CONF_MULTI_BATCH): cv.boolean,
    }
)

OPTIONS_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_RAMP_TEMP_CORRECTION): cv.boolean,
        vol.Required(CONF_MULTI_BATCH): cv.boolean,
        vol.Required(CONF_ALL_BATCH_INFO_SENSOR): cv.boolean,
        vol.Required(CONF_CUSTOM_STREAM_ENABLED): cv.boolean,
    }
)

OPTIONS_CUSTOM_STREAM_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_CUSTOM_STREAM_LOGGING_ID): cv.string,
        vol.Required(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME): cv.string,
        vol.Optional(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE): cv.string,
    }
)

async def validate_auth(username:str, password:str) -> bool:
    """Validate the user input allows us to connect."""

    connection = Connection(username, password)
    result = await connection.test_connection()
    return result

async def validate_custom_stream(username:str, password:str, logging_id:str) -> bool:
    """Validate the user input allows connect to custom stream."""

    connection = Connection(username, password)
    result = await connection.test_custom_stream(logging_id=logging_id)
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
            multi_batch = user_input.get(CONF_MULTI_BATCH, False)

            self.data = ConfigFlow.get_config_entry(name, username, password, temp_correction, multi_batch, False)
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
    def get_config_entry(name:str, username: str, password: str, temp_correction: bool, multi_batch: bool, all_batch_info_sensor: bool
    ) -> dict[str, Any]:
        """Create the config object."""
        config:dict[str, Any] = {
                CONF_NAME: name,
                CONF_USERNAME: username,
                CONF_PASSWORD: password,
                CONF_RAMP_TEMP_CORRECTION: temp_correction,
                CONF_MULTI_BATCH: multi_batch,
                CONF_ALL_BATCH_INFO_SENSOR: all_batch_info_sensor
            }
        return config

class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Manage the options."""

        errors: dict[str, str] = {}
        self.init_info: dict[str, Any] = {}

        if user_input is not None:

            new_config = ConfigFlow.get_config_entry(
                self.config_entry.data.get(CONF_NAME),
                self.config_entry.data.get(CONF_USERNAME),
                self.config_entry.data.get(CONF_PASSWORD),
                user_input.get(CONF_RAMP_TEMP_CORRECTION),
                user_input.get(CONF_MULTI_BATCH),
                user_input.get(CONF_ALL_BATCH_INFO_SENSOR)
            )

            custom_stream_enabled = user_input.get(CONF_CUSTOM_STREAM_ENABLED)
            new_config[CONF_CUSTOM_STREAM_ENABLED] = custom_stream_enabled

            if custom_stream_enabled:
                # Store info to use in next step
                self.init_info = new_config

                return self.async_show_form(
                    step_id="custom_stream",
                    data_schema=self.add_suggested_values_to_schema(
                        OPTIONS_CUSTOM_STREAM_SCHEMA, self.config_entry.data
                    ),
                    last_step=True
                )
            
            if errors is None or len(errors) == 0:
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
            errors=errors,
        )

    async def async_step_custom_stream(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Manage the options."""

        errors: dict[str, str] = {}

        if user_input is not None:
            entity_name = user_input.get(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME)
            if entity_name is None or entity_name == "":
                errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = "entity_required"
            else:
                entity = self.hass.states.get(entity_name)
                if entity is None:
                    errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = "entity_not_found"
                else:
                    entity_attribute = user_input.get(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE)
                    if entity_attribute is not None and entity_attribute != "" and entity.attributes.get(entity_attribute) is None:
                        errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE] = "attribute_not_found"
                    
                    # Validate that we can get a numeric temperature value
                    try:
                        if entity_attribute is None or entity_attribute == "":
                            temp_value = entity.state
                        else:
                            temp_value = entity.attributes.get(entity_attribute)
                        
                        if temp_value is None or temp_value in ("unknown", "unavailable", ""):
                            if entity_attribute:
                                errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE] = "attribute_not_found"
                            else:
                                errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = "entity_not_found"
                        else:
                            float(temp_value)  # Test if it's convertible to float
                    except (ValueError, TypeError):
                        if entity_attribute:
                            errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE] = "attribute_not_found" 
                        else:
                            errors[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = "entity_not_found"
            
            logging_id = user_input.get(CONF_CUSTOM_STREAM_LOGGING_ID)
            try:
                username = self.init_info[CONF_USERNAME]
                password = self.init_info[CONF_PASSWORD]
                valid_logging_id = await validate_custom_stream(username, password, logging_id)
                if valid_logging_id is False:
                    errors[CONF_CUSTOM_STREAM_LOGGING_ID] = "invalid_logging_id"

            except Exception as ex:
                _LOGGER.error("Unexpected exception when testing custom stream connection: %s", str(ex))
                errors["base"] = "unknown"
                
            if errors is None or len(errors) == 0:
                new_config = self.init_info
                new_config[CONF_CUSTOM_STREAM_LOGGING_ID] = logging_id
                new_config[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = entity_name
                new_config[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE] = entity_attribute

                # update config entry
                self.hass.config_entries.async_update_entry(
                    self.config_entry, data=new_config, options=self.config_entry.options
                )

                return self.async_create_entry(title="Brewfather", data=new_config)

        return self.async_show_form(
            step_id="custom_stream",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_CUSTOM_STREAM_SCHEMA, user_input 
            ),
            errors=errors,
            last_step=True
        )
    
