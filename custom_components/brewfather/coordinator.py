from __future__ import annotations
import datetime
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional, List
import aiohttp
import json
from .connection import *

# from models.batches_item import BatchesItemElement
from .models.batches_item import BatchesItemElement, batches_item_from_dict
from .models.batch_item import FermentationStep
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import *

_LOGGER = logging.getLogger(__name__)
MS_IN_DAY = 86400000


def sort_by_actual_time(entity: FermentationStep):
    return entity.actual_time


class BrewfatherCoordinatorData:
    fermenting_name: Optional[str]
    fermenting_current_temperature: Optional[float]
    fermenting_next_date: Optional[datetime.datetime]
    fermenting_next_temperature: Optional[float]

    def __init__(self):
        # set defaults to None
        self.fermenting_name = None
        self.fermenting_current_temperature = None
        self.fermenting_next_date = None
        self.fermenting_next_temperature = None


class BrewfatherCoordinator(DataUpdateCoordinator[BrewfatherCoordinatorData]):
    """Class to manage fetching data from the API."""

    _connection: Connection

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

        fermentingBatchesItems = []
        for batch in allBatches:
            if batch.status == "Fermenting":
                fermentingBatchesItems.append(batch)

        fermentingBatches = []
        for batch in fermentingBatchesItems:
            fermentingBatches.append(await self.connection.get_batch(batch.id, DRY_RUN))

        # For now we only support a single fermenting batch
        if len(fermentingBatches) == 0:
            return None
        elif len(fermentingBatches) > 1:
            _LOGGER.warning(
                "Multiple fermenting batches found, at the moment only 1 is supported. Using the latest batch..."
            )
        currentBatch = fermentingBatches[0]

        currentTimeInMs = datetime.utcnow().timestamp() * 1000
        currentBatch.recipe.fermentation.steps.sort(key=sort_by_actual_time)

        currentStep: FermentationStep | None = None
        nextStep: FermentationStep | None = None

        for index, obj in enumerate(currentBatch.recipe.fermentation.steps):
            next_ = None
            # check if start date is in past, also check if end date (start date + step_time * MS_IN_DAY) is in future
            if (
                obj.actual_time < currentTimeInMs
                and obj.actual_time + obj.step_time * MS_IN_DAY > currentTimeInMs
            ):
                currentStep = obj
            # check if start date is in future
            elif obj.actual_time > currentTimeInMs:
                nextStep = obj
                break

        data = BrewfatherCoordinatorData()
        data.fermenting_name = currentBatch.recipe.name

        if currentStep is not None:
            data.fermenting_current_temperature = currentStep.display_step_temp
            _LOGGER.debug("Current step: %s", currentStep.display_step_temp)
        else:
            _LOGGER.debug("No current step")

        if nextStep is not None:
            data.fermenting_next_temperature = nextStep.display_step_temp
            fermentingStart: int | None = None
            for note in currentBatch.notes:
                if note.status == "Fermenting":
                    fermentingStart = note.timestamp
            _LOGGER.debug("fermentingStart: %s", fermentingStart)

            data.fermenting_next_date = datetime.fromtimestamp(
                nextStep.actual_time / 1000, timezone.utc
            )

            if fermentingStart is not None:
                fermentingStartDate = datetime.fromtimestamp(
                    fermentingStart / 1000, timezone.utc
                )
                _LOGGER.debug(
                    "fermenting_next_date before adding time: %s",
                    data.fermenting_next_date,
                )
                data.fermenting_next_date += timedelta(
                    hours=fermentingStartDate.hour,
                    minutes=fermentingStartDate.minute,
                    seconds=fermentingStartDate.second,
                )

            _LOGGER.debug("Next step: %s", nextStep.display_step_temp)
            _LOGGER.debug("fermenting_next_date: %s", data.fermenting_next_date)
        else:
            _LOGGER.debug("No next step")

        return data
