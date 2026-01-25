"""Tests for batch_notes and events sensors."""
import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import Mock

from custom_components.brewfather.sensor import BrewfatherSensor, SensorKinds
from custom_components.brewfather.coordinator import BrewfatherCoordinatorData
from custom_components.brewfather.models.batch_item import Event
from homeassistant.components.sensor import SensorEntityDescription


class TestBatchNotesSensor:
    """Test batch_notes sensor functionality."""

    @pytest.fixture
    def coordinator_data_with_notes(self):
        """Create coordinator data with batch notes."""
        data = BrewfatherCoordinatorData()
        data.batch_id = "test123"
        data.batch_notes = "This is a test batch note\nWith multiple lines\nAnd important info"
        return data

    def test_batch_notes_sensor_state(self, coordinator_data_with_notes):
        """Test that batch_notes sensor returns notes as state."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_notes,
            SensorKinds.batch_notes,
            None,
            "test_entity"
        )
        
        assert sensor_data.state == "This is a test batch note\nWith multiple lines\nAnd important info"
        assert sensor_data.attr_available is True
        assert "batch_id" in sensor_data.extra_state_attributes
        assert sensor_data.extra_state_attributes["batch_id"] == "test123"

    def test_batch_notes_sensor_without_notes(self):
        """Test batch_notes sensor when notes are None."""
        data = BrewfatherCoordinatorData()
        data.batch_id = "test123"
        data.batch_notes = None
        
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            data,
            SensorKinds.batch_notes,
            None,
            "test_entity"
        )
        
        assert sensor_data.state is None
        assert sensor_data.attr_available is True


class TestEventsSensor:
    """Test events sensor functionality."""

    @pytest.fixture
    def future_events(self):
        """Create future events for testing."""
        current_time = datetime.now(timezone.utc).timestamp() * 1000
        
        events = [
            Event(
                event_text="Fermentation @ 20°C",
                description="Fermentation step",
                time=int(current_time + 86400000),  # Tomorrow
                description_html="<b>Fermentation step</b>",
                active=True,
                event_type="event-batch-ferm-step",
                title="Fermentation Step",
                day_event=False,
                notify_time=None
            ),
            Event(
                event_text="Bottling Day",
                description="Bottle the beer",
                time=int(current_time + 604800000),  # Next week
                description_html="<b>Bottling Day</b>",
                active=True,
                event_type="event-batch-bottling-day",
                title="Bottling Day - Batch #1",
                day_event=True,
                notify_time=None
            ),
            Event(
                event_text="Old event",
                description="Past event",
                time=int(current_time - 86400000),  # Yesterday
                description_html="<b>Past event</b>",
                active=True,
                event_type="event-batch-brew-day",
                title="Brew Day",
                day_event=True,
                notify_time=None
            ),
            Event(
                event_text="Inactive future event",
                description="Should be filtered",
                time=int(current_time + 172800000),  # 2 days from now
                description_html="<b>Inactive</b>",
                active=False,
                event_type="event-batch-dry-hop",
                title="Dry Hop",
                day_event=False,
                notify_time=None
            )
        ]
        return events

    @pytest.fixture
    def coordinator_data_with_events(self, future_events):
        """Create coordinator data with events."""
        data = BrewfatherCoordinatorData()
        data.batch_id = "test123"
        data.events = future_events
        return data

    def test_events_sensor_filters_future_and_active(self, coordinator_data_with_events):
        """Test that events sensor only shows future active events."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_events,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        # Should have 2 events: tomorrow's fermentation and next week's bottling
        assert sensor_data.state == 2
        assert sensor_data.attr_available is True
        assert "events" in sensor_data.extra_state_attributes
        assert len(sensor_data.extra_state_attributes["events"]) == 2

    def test_events_sensor_sorts_by_time(self, coordinator_data_with_events):
        """Test that events are sorted by time."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_events,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        events = sensor_data.extra_state_attributes["events"]
        # First event should be tomorrow (earliest)
        assert events[0]["title"] == "Fermentation Step"
        # Second event should be next week
        assert events[1]["title"] == "Bottling Day - Batch #1"

    def test_events_sensor_includes_required_fields(self, coordinator_data_with_events):
        """Test that event attributes include all required fields."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_events,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        event = sensor_data.extra_state_attributes["events"][0]
        
        assert "title" in event
        assert "description" in event
        assert "time" in event
        assert "time_ms" in event
        assert "event_type" in event
        assert "day_event" in event
        assert "active" in event
        assert isinstance(event["time"], datetime)

    def test_events_sensor_without_events(self):
        """Test events sensor when no events exist."""
        data = BrewfatherCoordinatorData()
        data.batch_id = "test123"
        data.events = None
        
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            data,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        assert sensor_data.state is None

    def test_events_sensor_with_empty_list(self):
        """Test events sensor with empty events list."""
        data = BrewfatherCoordinatorData()
        data.batch_id = "test123"
        data.events = []
        
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            data,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        # Should still process but have 0 events
        assert sensor_data.attr_available is True

    def test_events_filters_inactive_events(self, coordinator_data_with_events):
        """Test that inactive events are filtered out."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_events,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        events = sensor_data.extra_state_attributes["events"]
        # Should not include the inactive event
        assert all(event["active"] is True for event in events)
        assert not any(event["title"] == "Dry Hop" for event in events)

    def test_events_filters_past_events(self, coordinator_data_with_events):
        """Test that past events are filtered out."""
        sensor_data = BrewfatherSensor._refresh_sensor_data(
            coordinator_data_with_events,
            SensorKinds.events,
            None,
            "test_entity"
        )
        
        events = sensor_data.extra_state_attributes["events"]
        # Should not include yesterday's brew day
        assert not any(event["title"] == "Brew Day" for event in events)
