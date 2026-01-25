"""Tests for batch_item parsing.

Unit tests for JSON parsing of batch data models.
"""
import pytest
import json

from custom_components.brewfather.models.batch_item import (
    batch_item_from_dict,
    BatchItem,
    Step,
    Fermentation,
    Recipe,
    Note,
    Event
)


class TestBatchItemParsing:
    """Test BatchItem JSON parsing with various scenarios."""

    @pytest.fixture
    def valid_batch_json(self):
        """Batch JSON with array-formatted fermentation fields (the problematic case)."""
        return {
            "_id": "hju83jUgqEgUQT4VIUMoFUbED7Kp8a",
            "name": "Batch",
            "batchNo": 59,
            "status": "Fermenting",
            "brewer": None,
            "brewDate": 1769209200000,
            "recipe": {
                "name": "Tropical White Wine",
                "fermentation": {
                    "steps": [
                        {
                            "displayStepTemp": 20,
                            "ramp": None,
                            "type": "Primary",
                            "stepTime": 8,
                            "pressure": None,
                            "actualTime": 1769209200000,
                            "displayPressure": None,
                            "stepTemp": 20
                        },
                        {
                            "pressure": None,
                            "stepTime": 4,
                            "displayPressure": None,
                            "displayStepTemp": 22,
                            "stepTemp": 22,
                            "actualTime": 1769900400000,
                            "type": "Primary",
                            "ramp": None
                        }
                    ],
                    "name": ["Ale"],  # Array format that was causing issues
                    "_id": ["default"]  # Array format that was causing issues
                }
            },
            "notes": [
                {
                    "timestamp": 1769253593918,
                    "note": "",
                    "type": "statusChanged",
                    "status": "Fermenting"
                }
            ],
            "measuredOg": 1.07
        }

    def test_parse_valid_batch(self, valid_batch_json):
        """Test parsing a valid batch with all required fields."""
        batch = batch_item_from_dict(valid_batch_json)
        
        assert isinstance(batch, BatchItem)
        assert batch.id == "hju83jUgqEgUQT4VIUMoFUbED7Kp8a"
        assert batch.name == "Batch"
        assert batch.batch_no == 59
        assert batch.status == "Fermenting"
        assert batch.brew_date == 1769209200000
        assert batch.measured_og == 1.07

    def test_parse_recipe(self, valid_batch_json):
        """Test recipe parsing."""
        batch = batch_item_from_dict(valid_batch_json)
        
        assert batch.recipe is not None
        assert isinstance(batch.recipe, Recipe)
        assert batch.recipe.name == "Tropical White Wine"

    def test_parse_fermentation_steps(self, valid_batch_json):
        """Test fermentation steps parsing."""
        batch = batch_item_from_dict(valid_batch_json)
        
        assert batch.recipe.fermentation is not None
        assert isinstance(batch.recipe.fermentation, Fermentation)
        assert batch.recipe.fermentation.steps is not None
        assert len(batch.recipe.fermentation.steps) == 2
        
        # Check first step
        step1 = batch.recipe.fermentation.steps[0]
        assert isinstance(step1, Step)
        assert step1.actual_time == 1769209200000
        assert step1.step_temp == 20
        assert step1.step_time == 8
        assert step1.ramp is None

    def test_parse_notes(self, valid_batch_json):
        """Test notes parsing."""
        batch = batch_item_from_dict(valid_batch_json)
        
        assert batch.notes is not None
        assert len(batch.notes) == 1
        assert isinstance(batch.notes[0], Note)
        assert batch.notes[0].type == "statusChanged"
        assert batch.notes[0].status == "Fermenting"
        assert batch.notes[0].timestamp == 1769253593918

    def test_parse_with_missing_optional_fields(self):
        """Test parsing with minimal required fields."""
        minimal_json = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": 1,
            "status": "Planning"
        }
        
        batch = batch_item_from_dict(minimal_json)
        
        assert batch.id == "test123"
        assert batch.name == "Test Batch"
        assert batch.batch_no == 1
        assert batch.status == "Planning"
        assert batch.brew_date is None
        assert batch.recipe is None
        assert batch.notes is None
        assert batch.measured_og is None

    def test_parse_with_null_values(self):
        """Test parsing with explicit null values."""
        null_json = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": 1,
            "status": "Planning",
            "brewDate": None,
            "recipe": None,
            "notes": None,
            "measuredOg": None
        }
        
        batch = batch_item_from_dict(null_json)
        
        assert batch.id == "test123"
        assert batch.brew_date is None
        assert batch.recipe is None

    def test_removed_brewer_field_ignored(self, valid_batch_json):
        """Test that brewer field is ignored (removed property)."""
        batch = batch_item_from_dict(valid_batch_json)
        
        # brewer should not be an attribute anymore
        assert not hasattr(batch, 'brewer')

    def test_step_only_has_used_properties(self, valid_batch_json):
        """Test that Step only has properties that are actually used."""
        batch = batch_item_from_dict(valid_batch_json)
        step = batch.recipe.fermentation.steps[0]
        
        # Should have these
        assert hasattr(step, 'actual_time')
        assert hasattr(step, 'step_temp')
        assert hasattr(step, 'step_time')
        assert hasattr(step, 'ramp')
        
        # Should NOT have these (removed unused properties)
        assert not hasattr(step, 'name')
        assert not hasattr(step, 'pressure')
        assert not hasattr(step, 'display_pressure')
        assert not hasattr(step, 'display_step_temp')
        assert not hasattr(step, 'type')

    def test_fermentation_only_has_steps(self, valid_batch_json):
        """Test that Fermentation only has steps property."""
        batch = batch_item_from_dict(valid_batch_json)
        fermentation = batch.recipe.fermentation
        
        # Should have this
        assert hasattr(fermentation, 'steps')
        
        # Should NOT have these (removed unused properties)
        assert not hasattr(fermentation, 'hidden')
        assert not hasattr(fermentation, 'created')
        assert not hasattr(fermentation, 'rev')
        assert not hasattr(fermentation, 'timestamp_ms')
        assert not hasattr(fermentation, 'timestamp')
        assert not hasattr(fermentation, 'version')
        assert not hasattr(fermentation, 'name')
        assert not hasattr(fermentation, 'id')

    def test_parse_invalid_field_type_raises_error(self):
        """Test that invalid field types raise ValueError with details."""
        invalid_json = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": "not_a_number",  # Should be int
            "status": "Planning"
        }
        
        with pytest.raises(ValueError) as exc_info:
            batch_item_from_dict(invalid_json)
        
        # Should mention which field failed
        assert "batchNo" in str(exc_info.value)

    def test_to_dict_roundtrip(self, valid_batch_json):
        """Test that to_dict creates valid JSON that can be parsed again."""
        batch1 = batch_item_from_dict(valid_batch_json)
        batch_dict = batch1.to_dict()
        batch2 = batch_item_from_dict(batch_dict)
        
        assert batch1.id == batch2.id
        assert batch1.name == batch2.name
        assert batch1.batch_no == batch2.batch_no
        assert batch1.status == batch2.status
        assert batch1.measured_og == batch2.measured_og


class TestErrorHandling:
    """Test error handling and logging."""

    def test_partial_parsing_with_invalid_step(self):
        """Test that one invalid step doesn't prevent parsing other steps."""
        json_data = {
            "_id": "test123",
            "name": "Test",
            "batchNo": 1,
            "status": "Fermenting",
            "recipe": {
                "name": "Test Recipe",
                "fermentation": {
                    "steps": [
                        {
                            "actualTime": "invalid",  # Invalid type
                            "stepTemp": 20,
                            "stepTime": 8
                        }
                    ]
                }
            }
        }
        
        # Should raise error - the error bubbles up through Recipe -> BatchItem
        with pytest.raises(ValueError) as exc_info:
            batch_item_from_dict(json_data)
        
        # Error message should mention the problem originated from recipe
        assert "recipe" in str(exc_info.value).lower()

    def test_error_message_includes_all_failures(self):
        """Test that error message includes all field failures, not just first."""
        json_data = {
            "_id": "test123",
            "name": 123,  # Should be string
            "batchNo": "abc",  # Should be int
            "status": ["array"],  # Should be string
        }
        
        with pytest.raises(ValueError) as exc_info:
            batch_item_from_dict(json_data)
        
        error_msg = str(exc_info.value)
        # Should mention multiple fields
        assert "name" in error_msg
        assert "batchNo" in error_msg
        assert "status" in error_msg


class TestBatchNotesAndEvents:
    """Test new batch_notes and events functionality."""

    @pytest.fixture
    def batch_with_notes_and_events(self):
        """Batch JSON with batchNotes and events."""
        return {
            "_id": "hju83jUgqEgUQT4VIUMoFUbED7Kp8a",
            "name": "Batch",
            "batchNo": 59,
            "status": "Fermenting",
            "brewDate": 1769209200000,
            "recipe": {
                "name": "Chardonnay Cloud",
                "fermentation": {
                    "steps": [
                        {
                            "type": "Primary",
                            "actualTime": 1769209200000,
                            "stepTime": 8,
                            "stepTemp": 20,
                            "ramp": None
                        }
                    ]
                }
            },
            "notes": [
                {
                    "timestamp": 1769253593918,
                    "note": "",
                    "type": "statusChanged",
                    "status": "Fermenting"
                }
            ],
            "batchNotes": "Dubbel crush, stuck mash wel\npH veel te laag: 5 (teveel zuur gebruikt, te laat gemeten)\n30min mash: 1.062\n60 min: 1.067\n80: 1.068\nMashout toegepast",
            "events": [
                {
                    "eventText": "Primary (Fermentation) @ 12 °C",
                    "description": "Fermentation Profile Step: Primary (Fermentation) @ 12 °C",
                    "time": 1770282000000,
                    "descriptionHTML": "Fermentation Profile Step:<br>Primary (Fermentation) @ 12 °C",
                    "active": True,
                    "eventType": "event-batch-ferm-step",
                    "title": "Fermentation Step - Batch #59 (Chardonnay Cloud)",
                    "dayEvent": False
                },
                {
                    "eventType": "event-batch-brew-day",
                    "time": 1769245200000,
                    "dayEvent": True,
                    "active": False,
                    "eventText": "Brew Day",
                    "notifyTime": 1769245200000,
                    "title": "Brew Day - Batch #59 (Chardonnay Cloud)",
                    "descriptionHTML": "Brew Day (Chardonnay Cloud)",
                    "description": "Brew Day (Chardonnay Cloud)"
                },
                {
                    "title": "Bottling Day - Batch #59 (Chardonnay Cloud)",
                    "dayEvent": True,
                    "eventType": "event-batch-bottling-day",
                    "time": 1770454800000,
                    "description": "Bottling Day (Chardonnay Cloud)",
                    "descriptionHTML": "Bottling Day (Chardonnay Cloud)",
                    "eventText": "Bottling Day",
                    "active": True
                }
            ],
            "measuredOg": 1.07
        }

    def test_parse_batch_notes(self, batch_with_notes_and_events):
        """Test parsing batch notes."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        
        assert batch.batch_notes is not None
        assert isinstance(batch.batch_notes, str)
        assert "Dubbel crush" in batch.batch_notes
        assert "pH veel te laag" in batch.batch_notes
        assert "\n" in batch.batch_notes  # Should preserve line breaks

    def test_parse_events(self, batch_with_notes_and_events):
        """Test parsing events."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        
        assert batch.events is not None
        assert len(batch.events) == 3
        assert all(isinstance(event, Event) for event in batch.events)

    def test_event_fields(self, batch_with_notes_and_events):
        """Test individual event fields."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        event = batch.events[0]
        
        assert event.event_text == "Primary (Fermentation) @ 12 °C"
        assert event.description == "Fermentation Profile Step: Primary (Fermentation) @ 12 °C"
        assert event.time == 1770282000000
        assert event.description_html == "Fermentation Profile Step:<br>Primary (Fermentation) @ 12 °C"
        assert event.active is True
        assert event.event_type == "event-batch-ferm-step"
        assert event.title == "Fermentation Step - Batch #59 (Chardonnay Cloud)"
        assert event.day_event is False

    def test_event_with_notify_time(self, batch_with_notes_and_events):
        """Test event with optional notifyTime field."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        event = batch.events[1]
        
        assert event.notify_time == 1769245200000
        assert event.day_event is True
        assert event.active is False

    def test_batch_without_notes_and_events(self):
        """Test batch without batchNotes and events."""
        minimal_json = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": 1,
            "status": "Planning"
        }
        
        batch = batch_item_from_dict(minimal_json)
        
        assert batch.batch_notes is None
        assert batch.events is None

    def test_batch_with_null_notes_and_events(self):
        """Test batch with explicit null values for batchNotes and events."""
        json_data = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": 1,
            "status": "Planning",
            "batchNotes": None,
            "events": None
        }
        
        batch = batch_item_from_dict(json_data)
        
        assert batch.batch_notes is None
        assert batch.events is None

    def test_batch_with_empty_events_list(self):
        """Test batch with empty events list."""
        json_data = {
            "_id": "test123",
            "name": "Test Batch",
            "batchNo": 1,
            "status": "Planning",
            "events": []
        }
        
        batch = batch_item_from_dict(json_data)
        
        assert batch.events is not None
        assert len(batch.events) == 0

    def test_to_dict_includes_notes_and_events(self, batch_with_notes_and_events):
        """Test that to_dict includes batchNotes and events."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        batch_dict = batch.to_dict()
        
        assert "batchNotes" in batch_dict
        assert batch_dict["batchNotes"] == batch.batch_notes
        assert "events" in batch_dict
        assert len(batch_dict["events"]) == 3

    def test_event_to_dict_roundtrip(self, batch_with_notes_and_events):
        """Test Event to_dict and from_dict roundtrip."""
        batch1 = batch_item_from_dict(batch_with_notes_and_events)
        event1 = batch1.events[0]
        
        event_dict = event1.to_dict()
        event2 = Event.from_dict(event_dict)
        
        assert event1.event_text == event2.event_text
        assert event1.description == event2.description
        assert event1.time == event2.time
        assert event1.active == event2.active
        assert event1.event_type == event2.event_type
        assert event1.title == event2.title
        assert event1.day_event == event2.day_event

    def test_to_attribute_entry_hassio_includes_notes_and_events(self, batch_with_notes_and_events):
        """Test that to_attribute_entry_hassio includes batchNotes and events."""
        batch = batch_item_from_dict(batch_with_notes_and_events)
        batch.readings = []  # Set empty readings to avoid None errors
        
        result = batch.to_attribute_entry_hassio()
        
        assert "batchNotes" in result
        assert result["batchNotes"] == batch.batch_notes
        assert "events" in result
        assert len(result["events"]) == 3
