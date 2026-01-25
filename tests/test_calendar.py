"""Tests for calendar platform."""
import pytest
from datetime import datetime, timedelta
from unittest.mock import Mock, AsyncMock

from custom_components.brewfather.calendar import BrewfatherCalendar
from custom_components.brewfather.coordinator import BrewfatherCoordinatorData
from custom_components.brewfather.models.batch_item import Event
from homeassistant.util import dt as dt_util


class TestBrewfatherCalendar:
    """Test Brewfather Calendar entity."""

    @pytest.fixture
    def mock_coordinator(self):
        """Create a mock coordinator."""
        coordinator = Mock()
        coordinator.data = BrewfatherCoordinatorData()
        return coordinator

    @pytest.fixture
    def mock_entry(self):
        """Create a mock config entry."""
        entry = Mock()
        entry.entry_id = "test_entry"
        return entry

    @pytest.fixture
    def calendar(self, mock_coordinator, mock_entry):
        """Create a calendar instance."""
        return BrewfatherCalendar(mock_coordinator, mock_entry)

    @pytest.fixture
    def sample_events(self):
        """Create sample events."""
        now = datetime.now(dt_util.UTC)
        
        return [
            Event(
                event_text="Fermentation @ 20°C",
                description="Primary fermentation step",
                time=int((now + timedelta(days=1)).timestamp() * 1000),
                description_html="<b>Primary fermentation</b>",
                active=True,
                event_type="event-batch-ferm-step",
                title="Fermentation Step - Batch #1",
                day_event=False,
                notify_time=None
            ),
            Event(
                event_text="Bottling Day",
                description="Bottle the beer",
                time=int((now + timedelta(days=7)).timestamp() * 1000),
                description_html="<b>Bottling Day</b>",
                active=True,
                event_type="event-batch-bottling-day",
                title="Bottling Day - Batch #1",
                day_event=True,
                notify_time=None
            ),
            Event(
                event_text="Past event",
                description="Should not show",
                time=int((now - timedelta(days=1)).timestamp() * 1000),
                description_html="<b>Past</b>",
                active=True,
                event_type="event-batch-brew-day",
                title="Brew Day",
                day_event=True,
                notify_time=None
            ),
            Event(
                event_text="Inactive event",
                description="Should not show",
                time=int((now + timedelta(days=2)).timestamp() * 1000),
                description_html="<b>Inactive</b>",
                active=False,
                event_type="event-batch-dry-hop",
                title="Dry Hop",
                day_event=False,
                notify_time=None
            )
        ]

    def test_calendar_initialization(self, calendar, mock_entry):
        """Test calendar entity initialization."""
        assert calendar._attr_unique_id == f"{mock_entry.entry_id}_calendar"
        assert calendar._attr_name == "Brewfather Events"
        assert calendar._attr_icon == "mdi:calendar-clock"

    def test_get_events_filters_inactive(self, calendar, sample_events):
        """Test that _get_events filters out inactive events."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        events = calendar._get_events(start, end)
        
        # Should only have 2 active future events
        assert len(events) == 2
        assert all(event.summary != "Dry Hop" for event in events)

    def test_get_events_filters_past(self, calendar, sample_events):
        """Test that _get_events filters out past events."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        events = calendar._get_events(start, end)
        
        # Should not include brew day (past event)
        assert all(event.summary != "Brew Day" for event in events)

    def test_get_events_respects_date_range(self, calendar, sample_events):
        """Test that _get_events respects the date range."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now + timedelta(days=1)
        end = now + timedelta(days=3)
        
        events = calendar._get_events(start, end)
        
        # Should only have the fermentation event (tomorrow)
        assert len(events) == 1
        assert events[0].summary == "Fermentation Step - Batch #1"

    def test_get_events_sorts_by_time(self, calendar, sample_events):
        """Test that events are sorted by start time."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        events = calendar._get_events(start, end)
        
        # First event should be tomorrow's fermentation (earliest)
        assert events[0].summary == "Fermentation Step - Batch #1"
        # Second should be bottling day (later)
        assert events[1].summary == "Bottling Day - Batch #1"

    def test_day_event_has_date_only(self, calendar, sample_events):
        """Test that day events use date instead of datetime."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now + timedelta(days=6)
        end = now + timedelta(days=8)
        
        events = calendar._get_events(start, end)
        
        # Find the bottling day event (day_event=True)
        bottling = next(e for e in events if "Bottling" in e.summary)
        
        # Should have date objects, not datetime
        assert not isinstance(bottling.start, datetime)
        assert not isinstance(bottling.end, datetime)

    def test_timed_event_has_datetime(self, calendar, sample_events):
        """Test that timed events use datetime."""
        calendar.coordinator.data.events = sample_events
        
        now = datetime.now(dt_util.UTC)
        start = now
        end = now + timedelta(days=2)
        
        events = calendar._get_events(start, end)
        
        # Find the fermentation event (day_event=False)
        ferm = next(e for e in events if "Fermentation" in e.summary)
        
        # Should have datetime objects
        assert isinstance(ferm.start, datetime)
        assert isinstance(ferm.end, datetime)
        # Should be 1 hour duration
        assert (ferm.end - ferm.start) == timedelta(hours=1)

    def test_get_events_with_no_data(self, calendar):
        """Test _get_events when coordinator has no data."""
        calendar.coordinator.data = None
        
        now = datetime.now(dt_util.UTC)
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        events = calendar._get_events(start, end)
        
        assert events == []

    def test_get_events_with_no_events(self, calendar):
        """Test _get_events when coordinator data has no events."""
        calendar.coordinator.data.events = None
        
        now = datetime.now(dt_util.UTC)
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        events = calendar._get_events(start, end)
        
        assert events == []

    def test_event_property(self, calendar, sample_events):
        """Test that event property returns next upcoming event."""
        calendar.coordinator.data.events = sample_events
        
        next_event = calendar.event
        
        # Should be the fermentation event (soonest)
        assert next_event is not None
        assert "Fermentation" in next_event.summary

    def test_event_property_with_no_events(self, calendar):
        """Test event property when no events exist."""
        calendar.coordinator.data.events = []
        
        next_event = calendar.event
        
        assert next_event is None

    def test_timezone_aware_dates(self, calendar, sample_events):
        """Test that dates are handled as timezone-aware."""
        calendar.coordinator.data.events = sample_events
        
        # Create timezone-naive dates (should be converted)
        now = datetime.now()  # No timezone
        start = now - timedelta(days=10)
        end = now + timedelta(days=30)
        
        # Should not raise TypeError about naive vs aware datetimes
        events = calendar._get_events(start, end)
        
        assert isinstance(events, list)
