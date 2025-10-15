from __future__ import annotations
import logging
from typing import Any, Dict, Optional
from urllib.parse import urlparse, parse_qs
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
    UnitOfTemperature,
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

def extract_logging_id_from_url(input_value: str) -> str:
    """Extract logging_id from Brewfather stream URL if input starts with http."""
    if not input_value.startswith("http"):
        return input_value
    
    try:
        parsed_url = urlparse(input_value)
        query_params = parse_qs(parsed_url.query)
        if "id" in query_params:
            return query_params["id"][0]
        else:
            _LOGGER.warning("No 'id' parameter found in URL: %s", input_value)
            return input_value
    except Exception as ex:
        _LOGGER.warning("Failed to parse URL %s: %s", input_value, str(ex))
        return input_value

def validate_temperature_unit(entity, entity_attribute: str = None) -> bool:
    """Validate that the entity reports temperature in a supported unit."""
    # Supported temperature units for Brewfather custom stream
    supported_units = [UnitOfTemperature.CELSIUS, UnitOfTemperature.FAHRENHEIT, UnitOfTemperature.KELVIN]
    
    # Get the unit of measurement from the entity
    unit_of_measurement = entity.attributes.get("unit_of_measurement")
    
    if unit_of_measurement is None:
        _LOGGER.warning("Entity %s has no unit_of_measurement attribute", entity.entity_id)
        return False
    
    if unit_of_measurement not in supported_units:
        _LOGGER.warning("Entity %s has unsupported temperature unit: %s. Supported units: %s", 
                       entity.entity_id, unit_of_measurement, supported_units)
        return False
    
    return True

def get_brewfather_temp_unit(ha_unit: str) -> str:
    """Convert Home Assistant temperature unit to Brewfather custom stream unit."""
    if ha_unit == UnitOfTemperature.CELSIUS:
        return "C"
    elif ha_unit == UnitOfTemperature.FAHRENHEIT:
        return "F"
    elif ha_unit == UnitOfTemperature.KELVIN:
        return "K"
    else:
        return "C"  # Default to Celsius
    
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

    def _validate_entity_name(self, entity_name: str) -> tuple[str | None, bool, dict]:
        """Validate entity name and return entity state, success flag, and errors."""
        if not entity_name:
            return None, False, {CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME: "entity_required"}
        
        entity = self.hass.states.get(entity_name)
        if entity is None:
            return None, False, {CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME: "entity_not_found"}
        
        return entity, True, {}

    def _validate_entity_attribute(self, entity, entity_attribute: str) -> tuple[bool, dict]:
        """Validate entity attribute exists if specified."""
        if entity_attribute and entity.attributes.get(entity_attribute) is None:
            return False, {CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE: "attribute_not_found"}
        return True, {}

    def _validate_temperature_value(self, entity, entity_attribute: str) -> tuple[bool, dict]:
        """Validate that temperature value is numeric and available."""
        try:
            temp_value = entity.state if not entity_attribute else entity.attributes.get(entity_attribute)
            
            if temp_value is None or temp_value in ("unknown", "unavailable", ""):
                field = CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE if entity_attribute else CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME
                return False, {field: "attribute_not_found" if entity_attribute else "entity_not_found"}
            
            float(temp_value)  # Test if it's convertible to float
            return True, {}
            
        except (ValueError, TypeError):
            field = CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE if entity_attribute else CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME
            return False, {field: "attribute_not_found" if entity_attribute else "entity_not_found"}

    def _validate_temperature_unit(self, entity) -> tuple[bool, dict]:
        """Validate that entity uses supported temperature unit."""
        if not validate_temperature_unit(entity):
            return False, {CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME: "unsupported_temperature_unit"}
        return True, {}

    async def _validate_logging_id(self, logging_id: str) -> tuple[str, bool, dict]:
        """Validate and extract logging ID."""
        extracted_logging_id = extract_logging_id_from_url(logging_id)
        
        try:
            username = self.init_info[CONF_USERNAME]
            password = self.init_info[CONF_PASSWORD]
            valid_logging_id = await validate_custom_stream(username, password, extracted_logging_id)
            
            if not valid_logging_id:
                return extracted_logging_id, False, {CONF_CUSTOM_STREAM_LOGGING_ID: "invalid_logging_id"}
            
            return extracted_logging_id, True, {}
            
        except Exception as ex:
            _LOGGER.error("Unexpected exception when testing custom stream connection: %s", str(ex))
            return extracted_logging_id, False, {"base": "unknown"}

    def _show_custom_stream_form(self, user_input: dict[str, Any] | None, errors: dict[str, str]) -> config_entries.FlowResult:
        """Show the custom stream configuration form."""
        return self.async_show_form(
            step_id="custom_stream",
            data_schema=self.add_suggested_values_to_schema(
                OPTIONS_CUSTOM_STREAM_SCHEMA, user_input 
            ),
            errors=errors,
            last_step=True
        )

    async def async_step_custom_stream(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Manage the custom stream configuration options."""
        errors: dict[str, str] = {}

        if user_input is None:
            return self._show_custom_stream_form(user_input, errors)

        # Validate entity name and get entity
        entity_name = user_input.get(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME)
        entity, entity_valid, entity_errors = self._validate_entity_name(entity_name)
        errors.update(entity_errors)

        if not entity_valid:
            return self._show_custom_stream_form(user_input, errors)

        # Clean up entity_attribute - treat empty string as None
        entity_attribute = user_input.get(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE)
        if entity_attribute == "":
            entity_attribute = None

        # Validate entity attribute
        attribute_valid, attribute_errors = self._validate_entity_attribute(entity, entity_attribute)
        errors.update(attribute_errors)

        if not attribute_valid:
            return self._show_custom_stream_form(user_input, errors)

        # Validate temperature value
        temp_value_valid, temp_value_errors = self._validate_temperature_value(entity, entity_attribute)
        errors.update(temp_value_errors)

        if not temp_value_valid:
            return self._show_custom_stream_form(user_input, errors)

        # Validate temperature unit
        temp_unit_valid, temp_unit_errors = self._validate_temperature_unit(entity)
        errors.update(temp_unit_errors)

        if not temp_unit_valid:
            return self._show_custom_stream_form(user_input, errors)

        # Validate logging ID
        logging_id = user_input.get(CONF_CUSTOM_STREAM_LOGGING_ID)
        extracted_logging_id, logging_valid, logging_errors = await self._validate_logging_id(logging_id)
        errors.update(logging_errors)

        if not logging_valid:
            return self._show_custom_stream_form(user_input, errors)

        # All validations passed - save configuration
        new_config = self.init_info.copy()
        new_config[CONF_CUSTOM_STREAM_LOGGING_ID] = extracted_logging_id
        new_config[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME] = entity_name
        new_config[CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_ATTRIBUTE] = entity_attribute

        self.hass.config_entries.async_update_entry(
            self.config_entry, data=new_config, options=self.config_entry.options
        )

        return self.async_create_entry(title="Brewfather", data=new_config)
    
