Dev notes

1. Open repo with Home assistant forked
1. Update to correct version
2. Modify devcontainer (mount + git fix, see commit: 74259f4c0ae0f7d17415834807b7754c4d69ee51)
3. Open in Visual studio code, rebuild and run devcontainer
4. Run HA with debugging mode: ctrl shift d, play button "Home Assistant"


Install hacs via docker script/guide: https://www.hacs.xyz/docs/use/download/download/
run in ./ha-forked/



https://www.awesome-ha.com/#third-party-add-ons
https://github.com/hacs/default?tab=readme-ov-file


https://my.home-assistant.io/redirect/config_flow_start/?domain=brewfather

https://my.home-assistant.io/redirect/hacs_repository/?owner=MvdDonk&repository=Brewfather



github flows/ versioning?


1. Install hacs
2. Add custom repo
3. Download/install brewfather via hacs (url or interface)



Version 0 sensors data
------
sensor.upcoming_temperature
state: unknown

unit_of_measurement: °C
device_class: temperature
icon: mdi:thermometer-chevron-up
friendly_name: Upcoming temperature
------
sensor.upcoming_temperature_change
state: unknown

device_class: timestamp
icon: mdi:clock
friendly_name: Upcoming temperature change
------
sensor.recipe_name
state: Collab stout - lactose

icon: mdi:glass-mug
friendly_name: Recipe name
------
sensor.current_temperature
state: 44.0

unit_of_measurement: °C
device_class: temperature
icon: mdi:thermometer
friendly_name: Current temperature
------
sensor.fermenting_batches
sate: 2

data:
  - name: Collab stout - lactose
    brewDate: "2024-10-25T22:00:00"
    batchNo: 50
    fermentingStart: "2024-10-25T22:00:00"
    current_temperature: null
    target_temperature: 44
    fermentingEnd: "2024-12-10T22:00:00"
    fermentingLeft: 17.38793947233646
    status: Fermenting
    measuredOg: 1.083
    recipe:
      name: Collab stout - lactose
      fermentation:
        name: Ale
        _id: default
        steps:
          - actualTime: 1729893600000
            stepTemp: 19
            displayStepTemp: 19
            stepTime: 7
            type: Primary
          - actualTime: 1730502000000
            stepTemp: 20
            displayStepTemp: 20
            stepTime: 2
            type: Primary
          - actualTime: 1730674800000
            stepTemp: 21
            displayStepTemp: 21
            stepTime: 3
            type: Primary
          - actualTime: 1730934000000
            stepTemp: 22
            displayStepTemp: 22
            stepTime: 2
            type: Primary
          - actualTime: 1731193200000
            stepTemp: 40
            ramp: 1
            displayStepTemp: 40
            stepTime: 2
            type: Primary
          - actualTime: 1731625200000
            stepTemp: 44
            ramp: 3
            displayStepTemp: 44
            stepTime: 30
            type: Primary
    notes:
      - note: ""
        type: statusChanged
        timestamp: 1729964646344
        status: Fermenting
    readings:
      - sg: 1.037
        time: 1730628183536
        id: manual
        type: manual
        comment: ""
      - sg: 1.052
        time: 1730475900000
        id: manual
        type: manual
        comment: ""
      - sg: 1.037
        time: 1730651460000
        id: manual
        type: manual
        comment: ""
      - temp: 20
        time: 1730910707898
        id: manual
        type: manual
        comment: ""
      - temp: 21
        time: 1730911604149
        id: manual
        type: manual
        comment: ""
      - sg: 1.031
        time: 1731236447317
        id: manual
        type: manual
        comment: ""
  - name: Hoppy weizen
    brewDate: "2024-09-21T22:00:00"
    batchNo: 49
    fermentingStart: "2024-09-21T22:00:00"
    current_temperature: null
    target_temperature: 21
    fermentingEnd: "2024-12-10T22:00:00"
    fermentingLeft: 17.38793947002402
    status: Fermenting
    measuredOg: 1.041
    recipe:
      name: Hoppy weizen
      fermentation:
        name: Ale
        _id: default
        steps:
          - actualTime: 1726956000000
            stepTemp: 20
            displayStepTemp: 20
            stepTime: 50
            type: Primary
          - actualTime: 1731279600000
            stepTemp: 21
            displayStepTemp: 21
            stepTime: 30
            type: Primary
    notes:
      - note: ""
        type: statusChanged
        timestamp: 1731535178926
        status: Fermenting
      - note: ""
        type: statusChanged
        timestamp: 1728211540067
        status: Conditioning
      - note: ""
        type: statusChanged
        timestamp: 1727008897151
        status: Fermenting
    readings:
      - sg: 1.01
        time: 1727865131185
        id: manual
        type: manual
        comment: ""
      - sg: 1.01
        time: 1728216708402
        id: manual
        type: manual
        comment: ""
icon: mdi:glass-mug
friendly_name: Fermenting batches
