from __future__ import annotations
import logging
from logging import DEBUG
from datetime import datetime, timezone, timedelta
import math
from typing import Optional
from .connection import Connection
from .models.batch_item import (
    Fermentation,
    BatchItem,
    Step,
    Reading
)
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import (
    DOMAIN,
    MS_IN_DAY,
    CONF_RAMP_TEMP_CORRECTION
)

_LOGGER = logging.getLogger(__name__)

def sort_by_actual_time(entity: Fermentation):
    return entity.actual_time

class BrewfatherCoordinatorData:
    brew_name: Optional[str]
    current_step_temperature: Optional[float]
    next_step_date: Optional[datetime.datetime]
    next_step_temperature: Optional[float]
    last_reading: Optional[Reading]
    batches: Optional[list[BatchItem]]

    def __init__(self):
        # set defaults to None
        self.brew_name = None
        self.current_step_temperature = None
        self.next_step_date = None
        self.next_step_temperature = None
        self.last_reading = None


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
        self.single_batch_mode = True
        self.temperature_correction_enabled = entry.data[CONF_RAMP_TEMP_CORRECTION]
        self.connection = Connection(
            entry.data[CONF_USERNAME], entry.data[CONF_PASSWORD]
        )

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self) -> BrewfatherCoordinatorData:
        """Update data via library."""
        _LOGGER.debug("Updating data via library")
        data = await self.update()
        return data

    async def update(self) -> BrewfatherCoordinatorData:
        _LOGGER.debug("Updating data...")
        allBatches = await self.connection.get_batches()

        fermentingBatches:list[BatchInfo] = []

        for batch in allBatches:
            batchData = await self.connection.get_batch(batch.id)
            #readings = await self.connection.get_readings(batch.id)
            last_reading = await self.connection.get_last_reading(batch.id)

            #fermentingBatches.append(BatchInfo(batchData, readings))
            fermentingBatches.append(BatchInfo(batchData, last_reading))

            if self.single_batch_mode:
                break

        if len(fermentingBatches) == 0:
            return None
        
        currentTimeUtc = datetime.now().astimezone()

        currentStep: Step | None = None
        nextStep: Step | None = None
        prevStep: Step | None = None
        curren_step_is_ramping = False
        current_step_actual_start_time_utc: datetime|None

        if not self.single_batch_mode:
            raise Exception("Multibatch is not implemented")
        
        currentBatch = fermentingBatches[0]
        
        fermenting_start: int | None = None
        for note in currentBatch.batch.notes:
            if note.status == "Fermenting":
                fermenting_start = note.timestamp


        _LOGGER.debug("CurrentTimeUtc: %s", currentTimeUtc.strftime("%m/%d/%Y, %H:%M:%S"))
        _LOGGER.debug("---------------------------------------------------- Fermentation steps -----------------------------------------------------")
        if currentBatch.batch.recipe is not None and currentBatch.batch.recipe.fermentation is not None and currentBatch.batch.recipe.fermentation.steps is not None:
            for (index, step) in enumerate[Step](
                currentBatch.batch.recipe.fermentation.steps
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

                if self.temperature_correction_enabled:
                    _LOGGER.debug("| %s\tstarts: %s\tends: %s\tramp: %s\tactualstart: %s |", step.step_temp, step_start_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step_end_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step.ramp, actual_start_time_utc.strftime("%m/%d/%Y, %H:%M:%S"))
                else:
                    _LOGGER.debug("| %s\tstarts: %s\tends: %s\tramp: %s\t\t\t|", step.step_temp, step_start_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step_end_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step.ramp)

                # check if start date is in past, also check if end date (start date + step_time * MS_IN_DAY) is in future
                if actual_start_time_utc <= currentTimeUtc and step_end_datetime_utc > currentTimeUtc:
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
        data.batches = fermentingBatches
        data.brew_name = currentBatch.batch.recipe.name
        data.last_reading = currentBatch.last_reading
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

    def datetime_fromtimestamp_with_fermentingstart(
        self, epoch: int | None, fermenting_start: int | None
    ) -> datetime:
        datetime_value = datetime.fromtimestamp(epoch / 1000, timezone.utc)

        if fermenting_start is not None:
            fermenting_start_date = datetime.fromtimestamp(fermenting_start / 1000)

            datetime_value += timedelta(
                hours=fermenting_start_date.hour,
                minutes=fermenting_start_date.minute,
                seconds=fermenting_start_date.second,
            )

        return datetime_value

