"""Calendar platform for Brewfather."""
from __future__ import annotations

from datetime import datetime, timedelta
import logging

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN, COORDINATOR
from .coordinator import BrewfatherCoordinator

_LOGGER = logging.getLogger(__name__)
SENSOR_PREFIX = "Brewfather"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Brewfather calendar based on a config entry."""
    coordinator: BrewfatherCoordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    async_add_entities([BrewfatherCalendar(coordinator, entry)])


class BrewfatherCalendar(CoordinatorEntity[BrewfatherCoordinator], CalendarEntity):
    """Representation of a Brewfather Calendar."""

    def __init__(
        self,
        coordinator: BrewfatherCoordinator,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the Brewfather calendar."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_calendar"
        self._attr_name = f"{SENSOR_PREFIX} Events"
        self._attr_icon = "mdi:calendar-clock"
        self._event: CalendarEvent | None = None

    @property
    def event(self) -> CalendarEvent | None:
        """Return the next upcoming event."""
        events = self._get_events(datetime.now(), datetime.now() + timedelta(days=365))
        return events[0] if events else None

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime,
        end_date: datetime,
    ) -> list[CalendarEvent]:
        """Return calendar events within a datetime range."""
        return self._get_events(start_date, end_date)

    def _get_events(
        self,
        start_date: datetime,
        end_date: datetime,
    ) -> list[CalendarEvent]:
        """Get events within a datetime range."""
        if not self.coordinator.data or not self.coordinator.data.events:
            return []

        events = []
        # Ensure start_date and end_date are timezone-aware
        if start_date.tzinfo is None:
            start_date = dt_util.as_utc(start_date)
        if end_date.tzinfo is None:
            end_date = dt_util.as_utc(end_date)
            
        start_timestamp = int(start_date.timestamp() * 1000)
        end_timestamp = int(end_date.timestamp() * 1000)

        for event_data in self.coordinator.data.events:
            if not event_data.time or not event_data.active:
                continue

            # Filter events within the date range
            if start_timestamp <= event_data.time <= end_timestamp:
                event_datetime = dt_util.utc_from_timestamp(event_data.time / 1000)
                
                # All-day event if day_event is True
                if event_data.day_event:
                    # For all-day events, use date only (no time)
                    start = event_datetime.date()
                    end = start
                else:
                    # For timed events, default 1 hour duration
                    start = event_datetime
                    end = event_datetime + timedelta(hours=1)

                events.append(
                    CalendarEvent(
                        start=start,
                        end=end,
                        summary=event_data.title or "Brewfather Event",
                        description=event_data.description,
                    )
                )

        # Sort by start time - handle both date and datetime objects
        def get_sortable_datetime(event):
            if isinstance(event.start, datetime):
                return event.start
            else:  # date object
                return dt_util.start_of_local_day(datetime.combine(event.start, datetime.min.time()))
        
        events.sort(key=get_sortable_datetime)
        return events

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._event = self.event
        self.async_write_ha_state()
