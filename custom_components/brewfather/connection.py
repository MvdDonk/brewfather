from __future__ import annotations
import logging
from typing import List
import aiohttp
import json
from homeassistant import exceptions
from .models.batches_item import BatchesItemElement, batches_item_from_dict
from .models.batch_item import BatchItem, batch_item_from_dict, readings_item_from_dict, Reading
from homeassistant.helpers.update_coordinator import UpdateFailed
from .const import *
from .testdata import *

_LOGGER = logging.getLogger(__name__)


class Connection:
    def __init__(self, username: str, apikey: str):
        # self.username = username
        # self.password = apikey
        self.auth = aiohttp.BasicAuth(username, apikey)

    async def test_connection(self) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(TEST_URI, auth=self.auth) as response:
                if response.status == 200:
                    return True
                elif response.status == 401:  # invalid credentials
                    raise InvalidCredentials()
                elif response.status == 403:  # scope issue
                    raise InvalidScope()
                else:
                    raise CannotConnect()

        return False

    async def get_batches(self, dryRun: bool) -> List[BatchesItemElement]:
        _LOGGER.debug("get_batches %s (%s)", BATCHES_URI, dryRun)
        if dryRun:
            return batches_item_from_dict(json.loads(TESTDATA_BATCHES))
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(BATCHES_URI, auth=self.auth) as response:
                    if response.status == 200:
                        jsonText = await response.text()
                        
                        try:
                            jsonData = json.loads(jsonText)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to parse json response")

                        try:
                            batches = batches_item_from_dict(jsonData)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to create batches from json")
                        else:
                            return batches
                        
                    else:
                        raise UpdateFailed(
                            f"Error communicating with API: {response.status}"
                        )

    async def get_batch(self, batchId: str, dryRun: bool, testData=TESTDATA_BATCH_1) -> BatchItem:
        url = BATCH_URI.format(batchId)
        _LOGGER.debug("get_batch %s (%s)", url, dryRun)

        if dryRun:
            return batch_item_from_dict(json.loads(testData))
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, auth=self.auth) as response:
                    if response.status == 200:
                        jsonText = await response.text()

                        try:
                            jsonData = json.loads(jsonText)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to parse json response")

                        try:
                            batch = batch_item_from_dict(jsonData)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to create batches from json")
                        else:
                            return batch
                        
                    else:
                        raise UpdateFailed(
                            f"Error communicating with API: {response.status}"
                        )

    async def get_readings(self, batchId: str, dryRun: bool) -> List[Reading]:
        url = READINGS_URI.format(batchId)
        _LOGGER.debug("get_readings %s (%s)", url, dryRun)

        if dryRun:
            return readings_item_from_dict(json.loads(TESTDATA_READINGS))
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, auth=self.auth) as response:
                    if response.status == 200:
                        jsonText = await response.text()

                        try:
                            jsonData = json.loads(jsonText)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to parse json response")

                        try:
                            reading = readings_item_from_dict(jsonData)
                        except Exception as e:
                            _LOGGER.debug("json response: %s", jsonText)
                            _LOGGER.error("Unable to create batches from json")
                        else:
                            return reading
                    else:
                        raise UpdateFailed(
                            f"Error communicating with API: {response.status}"
                        )


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidCredentials(exceptions.HomeAssistantError):
    """Error to indicate we do not have the correct credentials, 401."""


class InvalidScope(exceptions.HomeAssistantError):
    """Error to indicate api key doesn't have the correct scope, 403."""
