# Tests

Automated tests for the Brewfather Home Assistant integration.

## Setup

Install test dependencies:
```bash
pip install -r requirements-dev.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_batch_item.py
```

Run specific test:
```bash
pytest tests/test_batch_item.py::TestBatchItemParsing::test_parse_valid_batch
```

Run with verbose output:
```bash
pytest -v
```

Run with coverage:
```bash
pytest --cov=custom_components.brewfather.models --cov-report=html
```

## Test Structure

- `conftest.py` - pytest configuration and dependency mocking
- `test_batch_item.py` - Tests for batch JSON parsing (13 tests, 87% coverage)
  - `TestBatchItemParsing` - Valid parsing scenarios
  - `TestErrorHandling` - Error handling and validation

## GitHub Actions

Tests run automatically on:
- Pull requests
- Pushes to main branch
- Manual workflow dispatch

See [`.github/workflows/tests.yml`](../.github/workflows/tests.yml) for CI configuration.

## Test Coverage

Current coverage for `batch_item.py`: **87%**

The tests verify:
- ✅ Parsing of valid batch data with all fields
- ✅ Parsing with the problematic array-formatted fields
- ✅ Handling of missing/null optional fields
- ✅ Removed unused properties don't exist
- ✅ Error handling logs and raises detailed errors
- ✅ Round-trip serialization (to_dict/from_dict)

