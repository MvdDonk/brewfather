"""pytest configuration for Brewfather tests."""
import sys
from unittest.mock import MagicMock

# Mock all external dependencies for data model tests that don't need full runtime
# This allows us to test just the parsing logic without installing all dependencies
def mock_dependencies():
    """Mock external dependencies."""
    # Home Assistant
    mock_ha = MagicMock()
    mock_ha.const = MagicMock()
    mock_ha.config_entries = MagicMock()
    mock_ha.core = MagicMock()
    mock_ha.exceptions = MagicMock()
    mock_ha.helpers = MagicMock()
    mock_ha.helpers.update_coordinator = MagicMock()
    
    sys.modules['homeassistant'] = mock_ha
    sys.modules['homeassistant.const'] = mock_ha.const
    sys.modules['homeassistant.config_entries'] = mock_ha.config_entries
    sys.modules['homeassistant.core'] = mock_ha.core
    sys.modules['homeassistant.exceptions'] = mock_ha.exceptions
    sys.modules['homeassistant.helpers'] = mock_ha.helpers
    sys.modules['homeassistant.helpers.update_coordinator'] = mock_ha.helpers.update_coordinator
    
    # External libraries used by the integration
    sys.modules['aiohttp'] = MagicMock()

# Mock dependencies before any imports happen
mock_dependencies()

