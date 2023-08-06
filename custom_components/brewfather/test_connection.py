import os

import pytest as pytest

from custom_components.brewfather.connection import Connection
from custom_components.brewfather.testdata import TESTDATA_BATCH_2


@pytest.mark.asyncio
async def test_test_connection():
    connection = Connection(
        os.environ['USER_ID'], os.environ['API_KEY']
    )
    await connection.test_connection()

@pytest.mark.asyncio
async def test_get_batches():
    connection = Connection(
        os.environ['USER_ID'], os.environ['API_KEY']
    )
    await connection.get_batches(True)

@pytest.mark.asyncio
async def test_get_batch_1():
    connection = Connection(
        os.environ['USER_ID'], os.environ['API_KEY']
    )
    await connection.get_batch("MdygaYwzcjEGmDTwQXJ4Wfhjbm0O8s", True)

@pytest.mark.asyncio
async def test_get_batch_2():
    connection = Connection(
        os.environ['USER_ID'], os.environ['API_KEY']
    )
    await connection.get_batch("BZFF1swDJnQWmkyzSEog28O2aIsZ12", True, TESTDATA_BATCH_2)
