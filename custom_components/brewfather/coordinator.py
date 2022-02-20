from __future__ import annotations
import datetime
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, List

import pytz
from .connection import *

from .models.batch_item import FermentationStep
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from .const import *

_LOGGER = logging.getLogger(__name__)
MS_IN_DAY = 86400000


def sort_by_actual_time(entity: FermentationStep):
    return entity.actual_time


class BrewfatherCoordinatorData:
    brew_name: Optional[str]
    current_step_temperature: Optional[float]
    next_step_date: Optional[datetime.datetime]
    next_step_temperature: Optional[float]

    def __init__(self):
        # set defaults to None
        self.brew_name = None
        self.current_step_temperature = None
        self.next_step_date = None
        self.next_step_temperature = None


class BrewfatherCoordinator(DataUpdateCoordinator[BrewfatherCoordinatorData]):
    """Class to manage fetching data from the API."""

    def __init__(self, hass: HomeAssistant, entry, update_interval: timedelta):
        self.entry = entry
        self.connection = Connection(
            hass, entry.data[CONF_USERNAME], entry.data[CONF_PASSWORD]
        )

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=update_interval)

    async def _async_update_data(self) -> BrewfatherCoordinatorData:
        """Update data via library."""
        _LOGGER.debug("BrewfatherCoordinator._async_update_data!")
        # https://github.com/djtimca/HASpaceX/blob/master/custom_components/spacex/__init__.py
        data = await self.update()
        return data

    async def update(self) -> BrewfatherCoordinatorData:
        _LOGGER.debug("BrewfatherCoordinator.update!")

        allBatches = await self.connection.get_batches(DRY_RUN)

        fermentingBatches = []
        for batch in allBatches:
            if batch.status == "Fermenting":  # redundant because of query
                fermentingBatches.append(
                    await self.connection.get_batch(batch.id, DRY_RUN)
                )

        # For now we only support a single fermenting batch
        if len(fermentingBatches) == 0:
            return None
        elif len(fermentingBatches) > 1:
            _LOGGER.warning(
                "Multiple fermenting batches found, at the moment only 1 is supported. Using the latest batch..."
            )
        currentBatch = fermentingBatches[0]

        currentTime = pytz.utc.localize(datetime.utcnow())
        currentBatch.recipe.fermentation.steps.sort(key=sort_by_actual_time)

        currentStep: FermentationStep | None = None
        nextStep: FermentationStep | None = None

        fermenting_start: int | None = None
        for note in currentBatch.notes:
            if note.status == "Fermenting":
                fermenting_start = note.timestamp

        for (index, step) in enumerate[FermentationStep](
            currentBatch.recipe.fermentation.steps
        ):
            step_start_datetime = self.datetime_fromtimestamp_with_fermentingstart(
                step.actual_time, fermenting_start
            )
            step_end_datetime = self.datetime_fromtimestamp_with_fermentingstart(
                step.actual_time + step.step_time * MS_IN_DAY, fermenting_start
            )

            # check if start date is in past, also check if end date (start date + step_time * MS_IN_DAY) is in future
            if step_start_datetime < currentTime and step_end_datetime > currentTime:
                currentStep = step
            # check if start date is in future
            elif step_start_datetime > currentTime:
                nextStep = step
                break

        data = BrewfatherCoordinatorData()
        data.brew_name = currentBatch.recipe.name

        if currentStep is not None:
            data.current_step_temperature = currentStep.display_step_temp
            _LOGGER.debug("Current step: %s", currentStep.display_step_temp)
        else:
            _LOGGER.debug("No current step")

        if nextStep is not None:
            data.next_step_temperature = nextStep.display_step_temp

            data.next_step_date = self.datetime_fromtimestamp_with_fermentingstart(
                nextStep.actual_time, fermenting_start
            )

            _LOGGER.debug(
                "Next step: %s - %s",
                nextStep.display_step_temp,
                data.next_step_date,
            )
        else:
            _LOGGER.debug("No next step")

        return data

    def datetime_fromtimestamp_with_fermentingstart(
        self, epoch: int | None, fermenting_start: int | None
    ) -> datetime.datetime:
        datetime_value = datetime.fromtimestamp(epoch / 1000, timezone.utc)

        if fermenting_start is not None:
            fermenting_start_date = datetime.fromtimestamp(fermenting_start / 1000)

            datetime_value += timedelta(
                hours=fermenting_start_date.hour,
                minutes=fermenting_start_date.minute,
                seconds=fermenting_start_date.second,
            )

        return datetime_value
