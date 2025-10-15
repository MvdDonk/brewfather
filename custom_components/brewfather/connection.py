from __future__ import annotations
import logging
from typing import List, TypeVar, Callable
import aiohttp # type: ignore
import json
from homeassistant import exceptions
from .models.batches_item import BatchesItemElement, batches_item_from_dict
from .models.batch_item import BatchItem, batch_item_from_dict
from .models.reading_item import Reading, readings_from_dict
from .models.custom_stream_data import custom_stream_data

from homeassistant.helpers.update_coordinator import UpdateFailed
from .const import (
    BATCHES_URI,
    TEST_URI,
    BATCH_URI,
    READINGS_URI,
    DRY_RUN,
    LAST_READING_URI,
    LOG_CUSTOM_STREAM
)
from .testdata import (
    TESTDATA_BATCHES,
    #TESTDATA_BATCH_1,
    #TESTDATA_BATCH_2,
    TESTDATA_BATCH_3,
    TESTDATA_READINGS,
    TESTDATA_LAST_READINGS_1
)

_LOGGER = logging.getLogger(__name__)

T = TypeVar("T")

class Connection:
    def __init__(self, username: str, apikey: str):
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
    
    async def test_custom_stream(self, logging_id:str) -> bool:
        url = LOG_CUSTOM_STREAM.format(logging_id)
        stream_data = custom_stream_data(name = "HomeAssistant")
        stream_data.temp_unit = "C"
        stream_data.temp = 1.2
        data = self.to_dict(stream_data)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, auth=self.auth) as response:
                if response.status == 200:
                    response_text = await response.text()
                    _LOGGER.debug("POST request response: %s", response_text)
                    try:
                        response_json = json.loads(response_text)
                        result_value = response_json.get("result", "").lower()
                        return result_value in ["ok", "success"]
                    except json.JSONDecodeError as ex:
                        _LOGGER.error("Unable to parse JSON response: %s", str(ex))
                        raise Exception("Failed to parse JSON response")
        return False
    
    async def get_batches(self) -> List[BatchesItemElement]:
        url = BATCHES_URI
        if DRY_RUN:
            return batches_item_from_dict(json.loads(TESTDATA_BATCHES))
        else:
            batch = await self.get_api_response(url, batches_item_from_dict)
            return batch

    async def get_batch(self, batchId: str, testData=TESTDATA_BATCH_3) -> BatchItem:
        url = BATCH_URI.format(batchId)
        if DRY_RUN:
            return batch_item_from_dict(json.loads(testData))
        else:
            batch = await self.get_api_response(url, batch_item_from_dict)
            return batch    

    async def get_readings(self, batchId: str) -> List[Reading]:
        url = READINGS_URI.format(batchId)
        if DRY_RUN:
            return readings_from_dict(json.loads(TESTDATA_READINGS))
        else:
            reading = await self.get_api_response(url, readings_from_dict)
            return reading
        
    async def get_last_reading(self, batchId: str) -> Reading:
        url = LAST_READING_URI.format(batchId)
        if DRY_RUN:
            return Reading.from_dict(json.loads(TESTDATA_LAST_READINGS_1))
            #raise Exception("Not implemented")
        else:
            reading = await self.get_api_response(url, Reading.from_dict, accept_404 = True)
            return reading
        
    async def post_custom_stream(self, logging_id: str, data:custom_stream_data) -> bool:
        url = LOG_CUSTOM_STREAM.format(logging_id)
        if DRY_RUN:
            raise Exception("Not implemented")
        else:
            success, response_text = await self.post(url, self.to_dict(data))
            
            if success == False:
                return False
            try:
                response_json = json.loads(response_text)
                result_value = response_json.get("result", "").lower()
                return result_value in ["ok", "success"]
            except json.JSONDecodeError as ex:
                _LOGGER.error("Unable to parse JSON response: %s", str(ex))
                raise UpdateFailed(
                    f"Failed to parse JSON response, URL: {url}"
                )
        
    def to_dict(self, obj):
        """
        Convert an object to a dictionary.
        Handles objects with __dict__, lists, tuples, and other types.
        """
        if isinstance(obj, dict):
            return {k: self.to_dict(v) for k, v in obj.items()}
        elif hasattr(obj, "__dict__"):
            return {k: self.to_dict(v) for k, v in obj.__dict__.items()}
        elif isinstance(obj, list):
            return [self.to_dict(i) for i in obj]
        elif isinstance(obj, tuple):
            return tuple(self.to_dict(i) for i in obj)
        else:
            return obj
        
    async def get_api_response(self, url: str, parseJson:Callable[[str], T], accept_404: bool = False) -> T:
        _LOGGER.debug("Making api call to: %s", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, auth=self.auth) as response:
                if response.status == 200:
                    jsonText = await response.text()
                    _LOGGER.debug("Api call response: %s", jsonText)

                    try:
                        jsonData = json.loads(jsonText)
                        return parseJson(jsonData)
                    except Exception as ex:
                        _LOGGER.error("Unable read or parse json response: %s", str(ex))
                        exit(1)
                    
                else:
                    if accept_404 and response.status == 404:
                        return None

                    _LOGGER.debug("Failed getting correct api call result, got status: %s", response.status)
                    raise UpdateFailed(
                        f"Error communicating with API: {response.status}, URL: {url}"
                    )

    async def post(self, url: str, data: dict) -> (bool, str):
        _LOGGER.debug("Making api call to: %s, with body: %s", url, data)
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, auth=self.auth) as response:
                if response.status == 200:
                    response_text = await response.text()
                    _LOGGER.debug("POST request response: %s", response_text)
                    return (True, response_text)
                else:
                    _LOGGER.debug("Failed posting to api, got status: %s", response.status)
                    raise UpdateFailed(
                        f"Error communicating with API: {response.status}, URL: {url}"
                    )

class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""

class InvalidCredentials(exceptions.HomeAssistantError):
    """Error to indicate we do not have the correct credentials, 401."""

class InvalidScope(exceptions.HomeAssistantError):
    """Error to indicate api key doesn't have the correct scope, 403."""