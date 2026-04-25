# Custom Stream Documentation

This document provides detailed information about setting up and using the Custom Stream feature in the Brewfather Home Assistant integration.

## Overview

The Custom Stream feature allows you to automatically send temperature and gravity data from Home Assistant sensors to Brewfather's logging system. This enables you to use external sensors (like IoT devices, smart thermometers, hydrometers, etc.) to monitor your fermentation process directly in the Brewfather app.

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

### Step 2b: Identify Specific Gravity Sensor (Optional)

If you have a hydrometer or gravity sensor, you can optionally configure it to send specific gravity readings:

- **Entity ID**: Full entity name (e.g., `sensor.rapt_orangeboy_specific_gravity`)
- **Entity State**: The main value should be numeric specific gravity (e.g., 1.050)

Example entities:
```
sensor.rapt_orangeboy_specific_gravity
sensor.tilt_hydrometer_gravity
sensor.ispindel_gravity
```

### Step 3: Configure in Home Assistant

1. Go to Settings → Devices & Services
2. Find your Brewfather integration
3. Click "Configure"
4. Enable "Custom Stream"
5. Click Submit to proceed to custom stream configuration
6. Fill in the form:
   - **BrewFathers logging-id**: Enter your logging ID from Step 1
   - **Temperature Sensor**: Select your temperature sensor entity from Step 2  
   - **Specific Gravity Sensor (Optional)**: Select your gravity sensor entity from Step 2b (leave empty if not using)

### Step 4: Validation

The integration will validate your configuration:
- Tests connection to Brewfather Custom Stream endpoint
- Verifies the temperature entity exists and has a valid numeric temperature value
- Verifies the gravity entity exists and has a valid numeric value (if specified)

## Configuration Examples

### Example 1: Basic Temperature Sensor
```
Temperature Entity: sensor.fermentation_temperature
Entity value: 20.5
Gravity Entity: (leave empty)
```

### Example 2: Temperature + Hydrometer
```
Temperature Entity: sensor.fermentation_chamber_temperature
Entity value: 19.8
Gravity Entity: sensor.rapt_orangeboy_specific_gravity
Entity value: 1.045
```

### Example 3: Tilt Hydrometer (Combined sensor)
```
Temperature Entity: sensor.tilt_orange_temperature  
Entity value: 21.2
Gravity Entity: sensor.tilt_orange_specific_gravity
Entity value: 1.020
```

## Data Flow

1. **Collection**: Home Assistant reads temperature and gravity (if configured) from your specified entities every 15 minutes (default update interval)
2. **Conversion**: Temperature value is converted to appropriate unit and prepared for transmission
3. **Transmission**: Data is posted to Brewfather's Custom Stream endpoint
4. **Display**: Temperature and gravity appear in your Brewfather batch monitoring

## Troubleshooting

### Common Errors and Solutions

#### "Logging-id seems invalid"
- **Problem**: The logging ID is incorrect or the Custom Stream endpoint is unreachable
- **Solution**: 
  - Verify you copied only the ID portion (not the full URL)
  - Check your Brewfather app settings to ensure Custom Stream is enabled
  - Ensure your Brewfather API credentials have proper permissions

#### "Entity not found" or "Entity does not have a valid numeric value"
- **Problem**: The specified entity doesn't exist or doesn't provide numeric data
- **Solution**:
  - Check the entity ID spelling and ensure it exists in Home Assistant
  - Verify the entity's current state contains a number (not "unknown" or "unavailable")
  - Use Developer Tools → States to inspect your entity

#### "Gravity sensor unavailable"
- **Problem**: The gravity sensor entity is unavailable or returning invalid data
- **Solution**:
  - Verify your hydrometer/gravity sensor is online and functioning
  - Check that the entity state is a valid numeric gravity value (e.g., 1.050)
  - If not using a gravity sensor, leave the field empty during configuration

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

- Temperature and gravity data are sent every 15 minutes (matches integration update interval)
- Temperature is required; gravity is optional
- Requires active internet connection for data transmission
- Entity must provide numeric values (strings like "20.5" or "1.045" are converted automatically)

## Advanced Configuration

### Custom Update Intervals

The integration updates every 15 minutes by default. This cannot be changed through the UI but can be modified in the integration code if needed.

### Multiple Temperature Sensors

Currently, only one temperature sensor and one gravity sensor per integration instance are supported. For multiple sensors, you would need multiple Brewfather batch configurations with different logging IDs.

### Temperature Unit Conversion

All temperatures are sent to Brewfather with appropriate unit labels. The integration automatically handles temperature units (Celsius, Fahrenheit, Kelvin), so your Home Assistant sensors can use any supported temperature unit.

## Support

If you encounter issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/MvdDonk/brewfather/issues)
2. Review Home Assistant logs for detailed error messages  
3. Create a new issue with:
   - Your configuration details (without sensitive data)
   - Relevant log entries
   - Steps to reproduce the problem