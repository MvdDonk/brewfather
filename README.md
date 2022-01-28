# Brewfather integration for Home Assistant
A Home Assistant custom Integration for getting Brewfather batch information in Home Assistant for all homebrewers!

The following sensors will be added after setup:
- **Recipe name**

  Name of the beer you are fermenting
- **Current temperature**

  Temperature the fermentation should have following the recipe
- **Upcoming temperature**

  The temperature of the next step in the fermentation profile from the recipe
- **Upcoming temperature change**

  The date and time when the upcoming temperature will be activated


# Installation:

Copy the brewfather folder and all of its contents into your Home Assistant's custom_components folder. This folder is usually inside your `/config` folder. If you are running Hass.io, use SAMBA to copy the folder over. If you are running Home Assistant Supervised, the custom_components folder might be located at `/usr/share/hassio/homeassistant`. You may need to create the `custom_components` folder and then copy the brewfather folder and all of its contents into it

Alternatively, you can install brewfather through [HACS](https://hacs.xyz/) by adding this repository.


# Setup

After installation is completed you must create a new integration in Home Assistant by clicking on the "ADD INTEGRATION" button and search for "Brewfather". A dialog will popup containing the following fields:
- **Connection name**

  A unique name for your Brewfather connection that will be used in Home Assistant
- **User ID**

  User ID used for API-access. You can get this in the Brewfather app under Settings -> Api -> Generate API-Key.
- **API-Key**

  API-Key with the correct scopes. This is also located in Settings -> Api -> Generate API-Key. For more info on how to create a correct key see the section "Creating a Brewfather API-key" below.

## Creating a Brewfather API-Key

To create a Brewfather API-key follow the documentation on [Brewfather - docs](https://docs.brewfather.app/api#generate-api-key). Make sure to give the API-key at least the "Read Batches" [scope](https://docs.brewfather.app/api#scopes).


# Known issues

- At the moment only a single fermenting batch is supported