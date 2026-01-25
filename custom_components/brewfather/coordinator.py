from __future__ import annotations
import logging
from logging import DEBUG
from copy import copy
from datetime import datetime, timezone, timedelta
import math
from typing import Optional
from .connection import Connection
from .models.batch_item import (
    Fermentation,
    BatchItem,
    Step,
    Reading,
    Event
)
from .models.custom_stream_data import custom_stream_data
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, UnitOfTemperature, STATE_UNKNOWN, STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import (
    DOMAIN,
    MS_IN_DAY,
    CONF_RAMP_TEMP_CORRECTION,
    CONF_MULTI_BATCH,
    CONF_ALL_BATCH_INFO_SENSOR,
    CONF_CUSTOM_STREAM_ENABLED,
    CONF_CUSTOM_STREAM_LOGGING_ID,
    CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME
)

_LOGGER = logging.getLogger(__name__)

def sort_by_actual_time(entity: Fermentation):
    return entity.actual_time

class BrewfatherCoordinatorData:
    batch_id: Optional[str]
    brew_name: Optional[str]
    current_step_temperature: Optional[float]
    next_step_date: Optional[datetime.datetime]
    next_step_temperature: Optional[float]
    last_reading: Optional[Reading]
    other_batches: list[BrewfatherCoordinatorData]
    all_batches_data: Optional[list[BatchItem]]
    start_date: Optional[datetime.datetime]
    batch_notes: Optional[str]
    events: Optional[list[Event]]

    def __init__(self):
        # set defaults to None
        self.batch_id = None
        self.brew_name = None
        self.current_step_temperature = None
        self.next_step_date = None
        self.next_step_temperature = None
        self.last_reading = None
        self.other_batches = []
        self.all_batches_data = None
        self.start_date = None
        self.batch_notes = None
        self.events = None


class BatchInfo:
    batch: BatchItem
    #readings: list[Reading]
    last_reading: Reading
    
    #def __init__(self, batch: BatchItem, readings: list[Reading]):
    def __init__(self, batch: BatchItem, last_reading: Reading):
        self.batch = batch
        self.last_reading = last_reading

class BrewfatherCoordinator(DataUpdateCoordinator[BrewfatherCoordinatorData]):
    """Class to manage fetching data from the API."""

    def __init__(self, hass: HomeAssistant, entry, update_interval: timedelta):
        self.multi_batch_mode = entry.data.get(CONF_MULTI_BATCH, False)
        self.all_batch_info_sensor = entry.data.get(CONF_ALL_BATCH_INFO_SENSOR, False)
        self.temperature_correction_enabled = entry.data.get(CONF_RAMP_TEMP_CORRECTION, False)
        self.connection = Connection(
            entry.data.get(CONF_USERNAME), 
            entry.data.get(CONF_PASSWORD)
        )
        self.custom_stream_enabled = entry.data.get(CONF_CUSTOM_STREAM_ENABLED, False)
        self.last_update_success_time: Optional[datetime] = None
        if self.custom_stream_enabled:
            self.custom_stream_logging_id = entry.data.get(CONF_CUSTOM_STREAM_LOGGING_ID, None)

            self.custom_stream_temperature_entity_name = entry.data.get(CONF_CUSTOM_STREAM_TEMPERATURE_ENTITY_NAME, None)

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self) -> BrewfatherCoordinatorData:
        """Update data via library."""
        try:
            _LOGGER.debug("Updating data via library")
            data = await self.update()
            # Update the last successful update time
            self.last_update_success_time = datetime.now(timezone.utc)
            return data
        except Exception as ex:
            _LOGGER.error("Error updating Brewfather data: %s", str(ex))
            raise UpdateFailed(f"Error communicating with Brewfather API: {ex}") from ex

    async def update(self) -> BrewfatherCoordinatorData:
        _LOGGER.debug("Updating data...")
        allBatches = await self.connection.get_batches()

        fermentingBatches:list[BatchInfo] = []
        all_batches_data:list[BatchInfo] = []

        #if custom stream enabled
        if self.custom_stream_enabled:
            stream_data = self.create_custom_stream_data()
            if stream_data is None:
                _LOGGER.debug("No data was found to post to custom stream")
            else:
                _LOGGER.debug("Posting custom stream data")
                success = await self.connection.post_custom_stream(self.custom_stream_logging_id, stream_data)
                if not success:
                    _LOGGER.error("Failed to post custom stream data")

        for batch in allBatches:
            batchData = await self.connection.get_batch(batch.id)
            last_reading = await self.connection.get_last_reading(batch.id)
            fermentingBatches.append(BatchInfo(batchData, last_reading))

            if self.all_batch_info_sensor:
                readings = await self.connection.get_readings(batch.id)
                all_batch_data = copy(batchData)
                all_batch_data.readings = readings

                all_batches_data.append(all_batch_data)
            elif not self.multi_batch_mode:
                break

        if len(fermentingBatches) == 0:
            return None
        
        currentTimeUtc = datetime.now().astimezone()
        main_batch_data: BrewfatherCoordinatorData = None
        #batch_data:list[BrewfatherCoordinatorData] = []
        for fermenting_batch in fermentingBatches:
            batch_data = self.get_batch_data(fermenting_batch, currentTimeUtc)
            
            if main_batch_data is None:
                main_batch_data = batch_data
            else:
                if self.multi_batch_mode:
                    main_batch_data.other_batches.append(batch_data)
                else:
                    break
        
        if self.all_batch_info_sensor:
            main_batch_data.all_batches_data = all_batches_data
            
        return main_batch_data
    
    def get_batch_data(self, currentBatch: BatchInfo, currentTimeUtc: datetime) -> BrewfatherCoordinatorData | None:
        fermenting_start: int | None = None
        for note in currentBatch.batch.notes:
            if note.status == "Fermenting":
                fermenting_start = note.timestamp
        
        if fermenting_start is None:
            return None
        
        currentStep: Step | None = None
        nextStep: Step | None = None
        prevStep: Step | None = None
        curren_step_is_ramping = False
        current_step_actual_start_time_utc: datetime|None

        if currentBatch.batch.recipe is not None and currentBatch.batch.recipe.fermentation is not None and currentBatch.batch.recipe.fermentation.steps is not None:
            _LOGGER.debug("%s (%s) | CurrentTimeUtc: %s", currentBatch.batch.recipe.name, currentBatch.batch.id, currentTimeUtc.strftime("%m/%d/%Y, %H:%M:%S"))
            _LOGGER.debug("-------------------------------------- Fermentation steps -------- (tce:\t%s)---------------------------------------------", self.temperature_correction_enabled)
            for (index, step) in enumerate[Step](
                sorted(currentBatch.batch.recipe.fermentation.steps, key=lambda x: x.actual_time)
            ):
                step_start_datetime_utc = self.datetime_fromtimestamp_with_fermentingstart(
                    step.actual_time, fermenting_start
                )
                step_end_datetime_utc = self.datetime_fromtimestamp_with_fermentingstart(
                    step.actual_time + step.step_time * MS_IN_DAY, fermenting_start
                )

                actual_start_time_utc = step_start_datetime_utc
                if self.temperature_correction_enabled and step.ramp is not None and step.ramp > 0:
                    actual_start_time_utc = step_start_datetime_utc + timedelta(days = -1 * step.ramp)

                _LOGGER.debug("| %s\tstarts: %s\tends: %s\tramp: %s\tactualstart: %s |", step.step_temp, step_start_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step_end_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step.ramp, actual_start_time_utc.strftime("%m/%d/%Y, %H:%M:%S"))

                # check if start date is in past, we will keep looping so the latest step that matches will be current step.
                # this way it will also work for steps with ramping even if we have temperature_correction_enabled is disabled
                if actual_start_time_utc <= currentTimeUtc:
                    currentStep = step
                    current_step_actual_start_time_utc = actual_start_time_utc
                    if step_start_datetime_utc > currentTimeUtc:
                        curren_step_is_ramping = True
                    if index > 0:
                        prevStep = currentBatch.batch.recipe.fermentation.steps[index - 1]
                # check if start date is in future
                elif actual_start_time_utc > currentTimeUtc:
                    nextStep = step
                    break

        _LOGGER.debug("-----------------------------------------------------------------------------------------------------------------------------")

        data = BrewfatherCoordinatorData()
        data.batch_id = currentBatch.batch.id
        data.brew_name = currentBatch.batch.recipe.name
        data.last_reading = currentBatch.last_reading
        data.start_date = self.datetime_fromtimestamp(fermenting_start)
        data.batch_notes = currentBatch.batch.batch_notes
        data.events = currentBatch.batch.events

        # if currentBatch.readings is not None and len(currentBatch.readings) > 0:
        #     data.last_reading = sorted(currentBatch.readings, key=lambda r: r.time, reverse=True)[0]

        if currentStep is not None:
            data.current_step_temperature = currentStep.step_temp
            _LOGGER.debug("Current step: %s, ramp days: %s", currentStep.step_temp, currentStep.ramp)

            rampingStep = currentStep
            stepBeforeRamp = prevStep
            if self.temperature_correction_enabled and curren_step_is_ramping and stepBeforeRamp is not None and rampingStep.ramp is not None and rampingStep.ramp > 0:
                #instead of calculating what the temperature increase should be every hour, we will calculate how often we have to increase of decrease 1 whole degree C
                _LOGGER.debug("Next temperature has a ramp value of %s days", rampingStep.ramp)
                
                #from 20 to 25 in 24 hours
                #5 steps in 24 hour
                #24 / 5  = 4.8 hour 
                #each step will last 4.8 hours
                #step       temp        increase    new temp    start time, hours
                #0          20          0           20          0
                #1          20          1           21          4.8
                #2          20          2           22          9.6
                #3          20          3           23          14.4
                #4          20          4           24          19.2
                #end        25          0           0           24 (or 0 since the new step has started)

                number_of_steps = math.floor(rampingStep.step_temp - stepBeforeRamp.step_temp)
                if number_of_steps > 0:
                    ramp_hours = rampingStep.ramp * 24
                    hours_per_ramp = ramp_hours / number_of_steps

                    if _LOGGER.isEnabledFor(DEBUG):
                        _LOGGER.debug("------------------------------ Ramping schedule ----------------------------")
                        _LOGGER.debug("| Step\tTemp\tIncrease\tNew temp\tStart time (hours delta) |")
                        for x in range(number_of_steps):
                            ramp_step_temp = stepBeforeRamp.step_temp
                            ramp_step_increase = round(x, ndigits=1)
                            ramp_step_new_temp = round(stepBeforeRamp.step_temp + ramp_step_increase, ndigits=1)
                            ramp_step_time = round(x * hours_per_ramp, ndigits=1)
                            _LOGGER.debug("| #%s\t%s\t%s\t\t%s\t\t%s\t\t\t |", x, ramp_step_temp, ramp_step_increase, ramp_step_new_temp, ramp_step_time )

                        _LOGGER.debug("----------------------------------------------------------------------------")

                    time_already_ramping:timedelta = (current_step_actual_start_time_utc - currentTimeUtc)
                    hours_already_ramping  = abs((time_already_ramping.days * 24) + (time_already_ramping.seconds / 3600))
                    current_ramp_step = math.floor(hours_already_ramping / hours_per_ramp)
                    current_ramp_step_exact = hours_already_ramping / hours_per_ramp
                    temp_increase = current_ramp_step
                    _LOGGER.debug("We have been ramping %s hours, we are in ramp step: %s (%s)", round(hours_already_ramping, ndigits=2), current_ramp_step, current_ramp_step_exact)

                    if current_ramp_step > number_of_steps:
                        _LOGGER.error("Invalid temperature ramping step found!")
                        _LOGGER.debug("Somehow we have found a ramp step that is too high, ignoring any temp changes to prevent weird temperatures. Ramp step found: %s, max steps: %s", current_ramp_step, number_of_steps)

                    elif temp_increase > 0:
                        new_temp = round(stepBeforeRamp.step_temp + temp_increase, ndigits=1)
                        _LOGGER.debug("Overwrite current step temperature because of ramp to next temperature, setting temp from %s to: %s (%s)", data.current_step_temperature, new_temp, hours_per_ramp)
                        data.current_step_temperature = new_temp
        else:
            _LOGGER.error("Unable to determing current fermenting step!")

        if nextStep is not None:
            data.next_step_temperature = nextStep.step_temp

            data.next_step_date = self.datetime_fromtimestamp_with_fermentingstart(
                nextStep.actual_time, fermenting_start
            )

            _LOGGER.debug(
                "Next step: %s - %s [%s]",
                nextStep.step_temp,
                data.next_step_date,
                nextStep.ramp
            )            
        else:
            _LOGGER.debug("No next step")

        return data
        
    def datetime_fromtimestamp(self, epoch: int) -> datetime:
        return datetime.fromtimestamp(epoch / 1000, timezone.utc)

    def datetime_fromtimestamp_with_fermentingstart(
        self, epoch: int | None, fermenting_start: int | None
    ) -> datetime:
        datetime_value = self.datetime_fromtimestamp(epoch)

        if fermenting_start is not None:
            fermenting_start_date = datetime.fromtimestamp(fermenting_start / 1000)

            datetime_value += timedelta(
                hours=fermenting_start_date.hour,
                minutes=fermenting_start_date.minute,
                seconds=fermenting_start_date.second,
            )

        return datetime_value

    def get_brewfather_temp_unit(self, ha_unit: str) -> str:
        """Convert Home Assistant temperature unit to Brewfather custom stream unit."""
        if ha_unit == UnitOfTemperature.CELSIUS:
            return "C"
        elif ha_unit == UnitOfTemperature.FAHRENHEIT:
            return "F"
        elif ha_unit == UnitOfTemperature.KELVIN:
            return "K"
        else:
            _LOGGER.warning("Unsupported temperature unit '%s', defaulting to Celsius", ha_unit)
            return "C"  # Default to Celsius

    def create_custom_stream_data(self) -> Optional[custom_stream_data]:
        stream_data = custom_stream_data(name = "HomeAssistant")

        entity = self.hass.states.get(self.custom_stream_temperature_entity_name)
        if entity is None:
            return None
        
        # Get temperature unit from entity
        entity_unit = entity.attributes.get("unit_of_measurement")
        if entity_unit:
            stream_data.temp_unit = self.get_brewfather_temp_unit(entity_unit)
        else:
            stream_data.temp_unit = "C"  # Default to Celsius if no unit specified
        
        try:
            temp_value = entity.state
            
            # Convert to float if possible
            if temp_value is not None and temp_value != STATE_UNKNOWN and temp_value != STATE_UNAVAILABLE:
                stream_data.temp = float(temp_value)
            else:
                return None
        except (ValueError, TypeError) as ex:
            _LOGGER.warning("Unable to convert temperature value '%s' to float: %s", temp_value, str(ex))
            return None

        return stream_data
