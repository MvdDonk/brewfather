from __future__ import annotations
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional
from .connection import Connection
from .models.batch_item import (
    Fermentation,
    BatchItem,
    Step
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
    batches: Optional[list[BatchItem]]

    def __init__(self):
        # set defaults to None
        self.brew_name = None
        self.current_step_temperature = None
        self.next_step_date = None
        self.next_step_temperature = None


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

        fermentingBatches:list[BatchItem] = []
        for batch in allBatches:
            fermentingBatch = await self.connection.get_batch(batch.id)
            readings = await self.connection.get_readings(batch.id)
            fermentingBatch.readings = readings
            
            fermentingBatches.append(
                fermentingBatch
            )
            if self.single_batch_mode:
                break

        if len(fermentingBatches) == 0:
            return None
        
        currentTimeUtc = datetime.now().astimezone()

        currentStep: Fermentation | None = None
        nextStep: Fermentation | None = None

        if not self.single_batch_mode:
            raise Exception("Multibatch is not implemented")
        
        currentBatch = fermentingBatches[0]

        fermenting_start: int | None = None
        for note in currentBatch.notes:
            if note.status == "Fermenting":
                fermenting_start = note.timestamp

        _LOGGER.debug("currentTimeUtc: %s", currentTimeUtc.strftime("%m/%d/%Y, %H:%M:%S"))

        if currentBatch.recipe is not None and currentBatch.recipe.fermentation is not None and currentBatch.recipe.fermentation.steps is not None:
            for (index, step) in enumerate[Step](
                currentBatch.recipe.fermentation.steps
            ):
                step_start_datetime_utc = self.datetime_fromtimestamp_with_fermentingstart(
                    step.actual_time, fermenting_start
                )
                step_end_datetime_utc = self.datetime_fromtimestamp_with_fermentingstart(
                    step.actual_time + step.step_time * MS_IN_DAY, fermenting_start
                )
                
                #TODO implement ramp times, calculate a increase of temperature for each hour
                
                _LOGGER.debug("step_start_datetime_utc (%s C): %s", step.step_temp, step_start_datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))
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
        data.brew_name = currentBatch.recipe.name

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
                "Next step: %s - %s",
                nextStep.step_temp,
                data.next_step_date,
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
