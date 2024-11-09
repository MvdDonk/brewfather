from __future__ import annotations
import logging
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
    CONF_SINGLEBATCHMODE
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
        self.single_batch_mode = entry.data[CONF_SINGLEBATCHMODE]
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

        if not self.single_batch_mode:
            raise Exception("Multibatch is not implemented")
        
        currentBatch = fermentingBatches[0]
        
        fermenting_start: int | None = None
        for note in currentBatch.batch.notes:
            if note.status == "Fermenting":
                fermenting_start = note.timestamp

        _LOGGER.debug("currentTimeUtc: %s", currentTimeUtc.strftime("%m/%d/%Y, %H:%M:%S"))

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

                _LOGGER.debug("step_start_datetime_utc (%s C): %s [%s]", step.step_temp, step_start_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"), step.ramp)
                _LOGGER.debug("step_end_datetime_utc (%s C): %s", step.step_temp, step_end_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))
                
                # check if start date is in past, also check if end date (start date + step_time * MS_IN_DAY) is in future
                if step_start_datetime_utc < currentTimeUtc and step_end_datetime_utc > currentTimeUtc:
                    currentStep = step
                # check if start date is in future
                elif step_start_datetime_utc > currentTimeUtc:
                    nextStep = step
                    break

        data = BrewfatherCoordinatorData()
        data.batches = fermentingBatches
        data.brew_name = currentBatch.batch.recipe.name
        data.last_reading = currentBatch.last_reading
        # if currentBatch.readings is not None and len(currentBatch.readings) > 0:
        #     data.last_reading = sorted(currentBatch.readings, key=lambda r: r.time, reverse=True)[0]

        if currentStep is not None:
            data.current_step_temperature = currentStep.step_temp
            _LOGGER.debug("Current step: %s", currentStep.step_temp)
        else:
            _LOGGER.debug("No current step")

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
            if(currentStep is not None and nextStep.ramp is not None and nextStep.ramp > 0):

                #instead of calculating what the temperature increase should be every hour, we will calculate how often we have to increase of decrease 1 whole degree C
                _LOGGER.debug("Next temperature has a ramp value of %s days", nextStep.ramp)
                ramp_hours = nextStep.ramp * 24


                #from 20 to 25 in 24 hours
                #5 degree in 24 hour
                #24 / 5  = 4.8 hour 
                #each 4.8 hour 1 degree increase


                #from 25 to 20 in 24 hours
                #-5 degree in 24 hour
                #24 / 5  = 4.8 hour 
                #each 4.8 hour -1 degree increase

                temperature_difference = nextStep.step_temp - currentStep.step_temp
                one_degree_each_hours = ramp_hours / abs(temperature_difference)
                _LOGGER.debug("We have to go from %sC to %sC in %s hours", currentStep.step_temp, nextStep.step_temp, ramp_hours)
                _LOGGER.debug("1 degree each: %s / %s = %s hours", ramp_hours, abs(temperature_difference), one_degree_each_hours)


                #seconds_left_for_ramp:timedelta = (data.next_step_date - self.datetime_fromtimestamp_with_fermentingstart(currentStep.actual_time, fermenting_start))
                #temperature_steps = data.next_step_date


                #_LOGGER.debug("Time between current step and next: %s, number of hours to ramp: %s", time_between_steps, ramp_hours)
                #temperature_increase_each_hour = (nextStep.step_temp - currentStep.step_temp) / ramp_hours

                seconds_left_for_ramp:timedelta = (data.next_step_date - currentTimeUtc)
                hours_left = (seconds_left_for_ramp.days * 24) + (seconds_left_for_ramp.seconds / 3600)
                _LOGGER.debug("We have %s hours left to reach %sC", hours_left, nextStep.step_temp)

                # subtract 1 because the last degree change we want to skip (since we are getting very close to the nextStep target)
                number_of_degrees_to_change = math.floor(hours_left / one_degree_each_hours) - 1

                if temperature_difference < 0:
                    number_of_degrees_to_change = number_of_degrees_to_change * -1

                new_temp = round(nextStep.step_temp - number_of_degrees_to_change, ndigits=1)
                if new_temp != data.current_step_temperature:
                    _LOGGER.debug("Overwrite current step temperature because of ramp to next temperature, setting temp from %s to: %sC", data.current_step_temperature, new_temp)

                    #new_temp = round(nextStep.step_temp - (hours_left * temperature_increase_each_hour), ndigits=1)
                    #_LOGGER.debug("Overwrite current step temperature because of ramp to next temperature, setting temp to: %s C", new_temp)
                    data.current_step_temperature = new_temp
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

