# Custom Stream Documentation

This document provides detailed information about setting up and using the Custom Stream feature in the Brewfather Home Assistant integration.

## Overview

The Custom Stream feature allows you to automatically send temperature data from Home Assistant sensors to Brewfather's logging system. This enables you to use external temperature sensors (like IoT devices, smart thermometers, etc.) to monitor your fermentation process directly in the Brewfather app.

## Prerequisites

1. **Brewfather Account**: You need an active Brewfather account with a batch configured for fermentation
2. **Home Assistant**: A working Home Assistant installation with temperature sensor entities
3. **API Access**: Valid Brewfather API credentials (User ID and API Key)

## Setup Guide

### Step 1: Get Custom Stream Logging ID

1. Open the Brewfather mobile app
2. Navigate to your active batch
3. Go to batch settings → "Logging"
4. Select "Custom Stream"
5. You'll see a URL like: `http://log.brewfather.net/stream?id=YOUR_LOGGING_ID`
6. Copy the `YOUR_LOGGING_ID` portion (everything after `id=`)

### Step 2: Identify Temperature Sensor

Identify the Home Assistant entity that provides your fermentation temperature:

- **Entity ID**: Full entity name (e.g., `sensor.fermentation_temperature`)
- **Entity State**: The main value should be numeric temperature
- **Entity Attribute**: (Optional) If temperature is stored in an attribute instead of the main state

Example entities:
```
sensor.fermentation_chamber_temperature
sensor.fermzilla_temp
sensor.tilt_hydrometer  (if using attribute like 'temperature')
```

### Step 3: Configure in Home Assistant

1. Go to Settings → Devices & Services
2. Find your Brewfather integration
3. Click "Configure"
4. Enable "Custom Stream"
5. Click Submit to proceed to custom stream configuration
6. Fill in the form:
   - **BrewFathers logging-id**: Enter your logging ID from Step 1
   - **Full entity name for temperature**: Enter complete entity ID from Step 2  
   - **Attribute name** (optional): Leave blank unless using an attribute

### Step 4: Validation

The integration will validate your configuration:
- Tests connection to Brewfather Custom Stream endpoint
- Verifies the entity exists and has a valid numeric temperature value
- Confirms attribute exists (if specified) and contains numeric data

## Configuration Examples

### Example 1: Basic Temperature Sensor
```
Entity: sensor.fermentation_temperature
Entity value: 20.5
Attribute: (leave empty)
```

### Example 2: Multi-sensor Device
```
Entity: sensor.tilt_hydrometer
Entity attributes: { temperature: 19.8, specific_gravity: 1.020 }
Attribute: temperature
```

### Example 3: Smart Thermometer
```
Entity: sensor.inkbird_308_temperature  
Entity value: 21.2
Attribute: (leave empty)
```

## Data Flow

1. **Collection**: Home Assistant reads temperature from your specified entity every 15 minutes (default update interval)
2. **Conversion**: Temperature value is converted to Celsius and prepared for transmission
3. **Transmission**: Data is posted to Brewfather's Custom Stream endpoint
4. **Display**: Temperature appears in your Brewfather batch monitoring

## Troubleshooting

### Common Errors and Solutions

#### "Logging-id seems invalid"
- **Problem**: The logging ID is incorrect or the Custom Stream endpoint is unreachable
- **Solution**: 
  - Verify you copied only the ID portion (not the full URL)
  - Check your Brewfather app settings to ensure Custom Stream is enabled
  - Ensure your Brewfather API credentials have proper permissions

#### "Entity not found" or "Entity does not have a valid numeric value"
- **Problem**: The specified entity doesn't exist or doesn't provide numeric temperature data
- **Solution**:
  - Check the entity ID spelling and ensure it exists in Home Assistant
  - Verify the entity's current state contains a number (not "unknown" or "unavailable")
  - Use Developer Tools → States to inspect your entity

#### "Attribute not found" or "Attribute does not have a valid numeric value"  
- **Problem**: The specified attribute doesn't exist or isn't numeric
- **Solution**:
  - Use Developer Tools → States to inspect entity attributes
  - Verify attribute name spelling
  - Ensure the attribute contains a numeric temperature value

#### "Failed to post custom stream data"
- **Problem**: Data transmission to Brewfather failed
- **Solution**:
  - Check Home Assistant logs for detailed error messages
  - Verify internet connectivity 
  - Confirm Brewfather API credentials are correct

### Debug Steps

1. **Check Entity State**:
   ```
   Go to Developer Tools → States
   Search for your temperature entity
   Verify current state is numeric
   ```

2. **Review Integration Logs**:
   ```
   Go to Settings → System → Logs
   Filter for "brewfather" 
   Look for custom stream related messages
   ```

3. **Test API Credentials**:
   - Remove and re-add the integration with fresh API credentials
   - Ensure API key has "Read Batches" scope minimum

## Limitations

- Temperature data is sent every 15 minutes (matches integration update interval)
- Only temperature data is currently supported (not gravity, pH, etc.)
- Requires active internet connection for data transmission
- Entity must provide numeric temperature values (strings like "20.5" are converted automatically)

## Advanced Configuration

### Custom Update Intervals

The integration updates every 15 minutes by default. This cannot be changed through the UI but can be modified in the integration code if needed.

### Multiple Temperature Sensors

Currently, only one temperature sensor per integration instance is supported. For multiple sensors, you would need multiple Brewfather batch configurations with different logging IDs.

### Temperature Unit Conversion

All temperatures are sent to Brewfather in Celsius. The integration automatically handles this conversion, so your Home Assistant sensors can be in any unit.

## Support

If you encounter issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/MvdDonk/brewfather/issues)
2. Review Home Assistant logs for detailed error messages  
3. Create a new issue with:
   - Your configuration details (without sensitive data)
   - Relevant log entries
   - Steps to reproduce the problem