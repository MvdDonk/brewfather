TESTDATA_BATCHES = r"""
[
    {
        "_id": "MdygaYwzcjEGmDTwQXJ4Wfhjbm0O8s",
        "name": "Batch",
        "batchNo": 30,
        "status": "Fermenting",
        "brewer": null,
        "brewDate": 1642806000000,
        "recipe": {
            "name": "Ryerish Red Ale"
        }
    },
    {
        "_id": "aIJH9A6NeUApZcrN93oXoZm4HcanrB",
        "name": "Batch",
        "batchNo": 29,
        "status": "Completed",
        "brewer": null,
        "brewDate": 1638486000000,
        "recipe": {
            "name": "Even Sharks Need Water - Donky"
        }
    },
    {
        "_id": "PqADx67L8peat5TbjXI4L6Lh56iyNz",
        "name": "Batch",
        "batchNo": 28,
        "status": "Completed",
        "brewer": null,
        "brewDate": 1631867216513,
        "recipe": {
            "name": "MG - American Amber Ale - Short"
        }
    },
    {
        "_id": "2KDjsjUr3iGksIBk9vFgeet1ZBh9lw",
        "name": "Batch",
        "batchNo": 27,
        "status": "Conditioning",
        "brewer": "Maarten",
        "brewDate": 1630133999772,
        "recipe": {
            "name": "Donk'el Weizen"
        }
    },
    {
        "_id": "wKBJXsJmMES0VesusqKg2uZpbnuBpi",
        "name": "Batch",
        "batchNo": 26,
        "status": "Completed",
        "brewer": null,
        "brewDate": 1621838995222,
        "recipe": {
            "name": "CAS NEIPA"
        }
    },
    {
        "_id": "YjD1G1pi8mC5miGX6bqoynRVsx2BYZ",
        "name": "Batch",
        "batchNo": 25,
        "status": "Archived",
        "brewer": null,
        "brewDate": 1615636120457,
        "recipe": {
            "name": "Saison Greeg en Donk"
        }
    },
    {
        "_id": "yCtZiqTaQL07UldKx0CtVVa8fwq4ki",
        "name": "Batch",
        "batchNo": 24,
        "status": "Archived",
        "brewer": null,
        "brewDate": 1611906119965,
        "recipe": {
            "name": "NEIPA Milkshake"
        }
    },
    {
        "_id": "NRZfJRMl8zsQEelk4dzhexbMPlZz7a",
        "name": "Batch",
        "batchNo": 23,
        "status": "Archived",
        "brewer": null,
        "brewDate": 1608455980274,
        "recipe": {
            "name": "Homebrew Challenge - Belgian IPA"
        }
    },
    {
        "_id": "5pcAXwZDsmxh25XSSffZ81UFpraJgP",
        "name": "Batch",
        "batchNo": 22,
        "status": "Archived",
        "brewer": null,
        "brewDate": 1605250827018,
        "recipe": {
            "name": "Gingerbread christmas"
        }
    },
    {
        "_id": "dh7ulzII0WICzBlFuYtpYGu2so57De",
        "name": "Batch",
        "batchNo": 21,
        "status": "Archived",
        "brewer": null,
        "brewDate": 1603443822289,
        "recipe": {
            "name": "Restjes stout"
        }
    }
]
"""

TESTDATA_BATCH_1 = r"""
{
    "_timestamp": {
        "_seconds": 1642957959,
        "_nanoseconds": 166000000
    },
    "measuredAbv": 5.3,
    "carbonationType": "Keg (Force)",
    "measurements": [],
    "hideBatchEvents": true,
    "measuredOg": 1.053,
    "fermentationControllerEnabled": false,
    "measuredBoilSize": 23.2,
    "devices": {
        "gfcc": {
            "enabled": false,
            "items": [],
            "brewDeviceId": null
        },
        "iSpindel": {
            "items": [
                {
                    "lastData": {
                        "angle": 46.44819,
                        "type": "iSpindel",
                        "status": "success",
                        "id": "ISPINDEL000",
                        "battery": 3.800834,
                        "time": 1642865742908,
                        "temp": 20.1,
                        "rssi": -67,
                        "sg": 1.054
                    },
                    "settings": {
                        "gravityOffset": -6,
                        "tempOffset": null
                    },
                    "hidden": false,
                    "type": "iSpindel",
                    "series": [
                        "gravity",
                        "temp"
                    ],
                    "lastLog": 1642865742755,
                    "name": "Ispindel000",
                    "key": "ISPINDEL000",
                    "enabled": true,
                    "batchId": "MdygaYwzcjEGmDTwQXJ4Wfhjbm0O8s"
                }
            ],
            "enabled": true
        },
        "tilt": {
            "mode": "default",
            "temp": true,
            "items": [],
            "enabled": true,
            "gravity": true
        },
        "brewPiLess": {
            "enabled": true,
            "items": []
        },
        "floatHydrometer": {
            "items": [],
            "enabled": true
        },
        "plaatoKeg": {
            "enabled": true,
            "items": []
        },
        "floatyHydrometer": {
            "enabled": true,
            "items": []
        },
        "stream": {
            "items": [],
            "enabled": true
        },
        "plaatoAirlock": {
            "enabled": true,
            "items": []
        },
        "myBrewbot": {
            "items": [],
            "enabled": true
        },
        "smartPid": {
            "brewDeviceId": null,
            "items": [],
            "enabled": true
        }
    },
    "batchYeasts": [
        {
            "removedFromInventory": true,
            "bestBeforeDate": 1706742000000,
            "inventory": 0,
            "removedUnit": "pkg",
            "minTemp": 15,
            "costPerAmount": 0,
            "removedAmount": 1,
            "fermentsAll": false,
            "userNotes": "",
            "productId": "S-04",
            "maxAttenuation": null,
            "manufacturingDate": null,
            "type": "Ale",
            "maxTemp": 20,
            "name": "SafAle English Ale",
            "_rev": "AMmpH4FJBJzmAphie6o1Hlz7boHPpp",
            "checked": true,
            "form": "Dry",
            "_timestamp": {
                "_seconds": 1642600849,
                "_nanoseconds": 922000000
            },
            "_version": "2.8.0",
            "laboratory": "Fermentis",
            "inventoryUnit": "pkg",
            "amount": 1,
            "maxAbv": null,
            "minAttenuation": null,
            "unit": "pkg",
            "totalCost": 0,
            "_timestamp_ms": 1642600849922,
            "_created": {
                "_seconds": 1589637599,
                "_nanoseconds": 658000000
            },
            "_id": "default-e294c5",
            "hidden": false,
            "attenuation": 75,
            "notInRecipe": false,
            "flocculation": "Medium",
            "description": "English ale yeast selected for its fast fermentation character and its ability to form a compact sediment at the end of fermentation, helping to improve beer clarity. Recommended for the production of a large range of ales and specially adapted to cask-conditioned ones and fermentation in cylindo-conical tanks.",
            "displayAmount": 0
        }
    ],
    "measuredPreBoilGravity": 1.05,
    "_version": "2.8.0",
    "boilSteps": [
        {
            "name": "25.7g Fuggles",
            "time": 60
        },
        {
            "time": 30,
            "name": "12.6g East Kent Goldings (EKG)"
        },
        {
            "time": 15,
            "name": "12.6g East Kent Goldings (EKG)"
        }
    ],
    "status": "Fermenting",
    "name": "Batch",
    "_archived": false,
    "batchHops": [
        {
            "inventory": -0.8,
            "usage": "Both",
            "substitutes": "",
            "type": "Pellet",
            "humulene": null,
            "actualTime": 1590789600000,
            "removedAmount": 42,
            "checked": true,
            "cohumulone": null,
            "bestBeforeDate": null,
            "beta": null,
            "hidden": false,
            "name": "Citra",
            "time": 60,
            "manufacturingDate": null,
            "notInRecipe": false,
            "_id": "default-8e9450d5",
            "year": null,
            "_version": "2.8.0",
            "totalCost": 2.3856,
            "use": "Boil",
            "oil": null,
            "_created": {
                "_seconds": 1589637652,
                "_nanoseconds": 932000000
            },
            "myrcene": null,
            "_editFlag": true,
            "farnesene": null,
            "costPerAmount": 0.0568,
            "hsi": null,
            "_timestamp_ms": 1642345389592,
            "usedIn": "",
            "origin": "US",
            "ibu": 0,
            "_rev": "fA27bw9duibFZwmGwFg5cFp9jIMMCu",
            "removedFromInventory": true,
            "userNotes": "",
            "notes": "",
            "temp": null,
            "displayAmount": 0,
            "amount": 42,
            "caryophyllene": null,
            "day": 6,
            "alpha": 12,
            "_timestamp": {
                "_seconds": 1642345389,
                "_nanoseconds": 592000000
            }
        },
        {
            "oil": null,
            "name": "East Kent Goldings (EKG)",
            "notInRecipe": false,
            "removedAmount": 25.2,
            "beta": null,
            "alpha": 5.61,
            "farnesene": null,
            "substitutes": "",
            "displayAmount": 0,
            "ibu": 0,
            "manufacturingDate": null,
            "_created": {
                "_seconds": 1584258247,
                "_nanoseconds": 820000000
            },
            "temp": null,
            "_timestamp_ms": 1642600935503,
            "costPerAmount": 0,
            "amount": 25.2,
            "cohumulone": null,
            "caryophyllene": null,
            "time": 60,
            "type": "Pellet",
            "removedFromInventory": true,
            "_id": "default-7f820fa1",
            "notes": "",
            "humulene": null,
            "hsi": null,
            "_version": "2.8.0",
            "_timestamp": {
                "_seconds": 1642600935,
                "_nanoseconds": 503000000
            },
            "usage": "Both",
            "myrcene": null,
            "inventory": 74.8,
            "_rev": "2oG7dlZYcYucgsOXQxshOj4jnZPo3a",
            "year": null,
            "checked": true,
            "hidden": false,
            "totalCost": 0,
            "bestBeforeDate": 1690754400000,
            "origin": "United Kingdom",
            "use": "Boil",
            "usedIn": "",
            "userNotes": ""
        },
        {
            "use": "Boil",
            "usedIn": "",
            "origin": "United Kingdom",
            "manufacturingDate": 1546297200000,
            "_rev": "OYS9Yzfb0bBrwfSh9FCJAOaoHcD54n",
            "_timestamp": {
                "_seconds": 1615831047,
                "_nanoseconds": 483000000
            },
            "_timestamp_ms": 1615831047483,
            "costPerAmount": 0,
            "hidden": false,
            "removedAmount": 25.7,
            "totalCost": 0,
            "usage": "Aroma",
            "alpha": 4.5,
            "bestBeforeDate": 1667430000000,
            "temp": null,
            "ibu": 0,
            "_created": {
                "_seconds": 1604951227,
                "_nanoseconds": 953000000
            },
            "substitutes": "",
            "year": null,
            "userNotes": "",
            "displayAmount": 0,
            "name": "Fuggles",
            "amount": 25.7,
            "type": "Pellet",
            "time": 60,
            "removedFromInventory": true,
            "notes": "",
            "inventory": 17,
            "_id": "default-f80149bd",
            "notInRecipe": false,
            "_version": "2.7.2",
            "checked": true
        }
    ],
    "_id": "MdygaYwzcjEGmDTwQXJ4Wfhjbm0O8s",
    "measuredConversionEfficiency": null,
    "events": [
        {
            "dayEvent": true,
            "notifyTime": 1642842000000,
            "descriptionHTML": "Brew Day (Ryerish Red Ale)",
            "description": "Brew Day (Ryerish Red Ale)",
            "title": "Brew Day - Batch #30",
            "time": 1642842000000,
            "eventText": "Brew Day",
            "eventType": "event-batch-brew-day",
            "active": false
        },
        {
            "eventType": "event-batch-brew-day-reminder",
            "time": 1642755600000,
            "eventText": "Brew Day &mdash; Reminder",
            "dayEvent": true,
            "descriptionHTML": "You have a planned batch upcoming (Ryerish Red Ale)",
            "active": false,
            "description": "You have a planned batch upcoming (Ryerish Red Ale)",
            "title": "Brew Day - Reminder - Batch #30",
            "notifyTime": 1642755600000
        },
        {
            "descriptionHTML": "Bottling Day (Ryerish Red Ale)",
            "title": "Bottling Day - Batch #30",
            "eventType": "event-batch-bottling-day",
            "active": true,
            "time": 1643878800000,
            "dayEvent": true,
            "eventText": "Bottling Day",
            "description": "Bottling Day (Ryerish Red Ale)"
        },
        {
            "eventType": "event-batch-dry-hop",
            "time": 1643274000000,
            "description": "Citra (42 g)",
            "title": "Dry Hop - Batch #30",
            "dayEvent": true,
            "descriptionHTML": "Citra (<b>42 g</b>)",
            "eventText": null,
            "active": true
        },
        {
            "active": true,
            "description": "Fermentation Profile Step: Primary (Fermentation) @ 20 °C",
            "eventText": "Primary (Fermentation) @ 20 °C",
            "time": 1643187600000,
            "eventType": "event-batch-ferm-step",
            "descriptionHTML": "Fermentation Profile Step:<br>Primary (Fermentation) @ 20 °C",
            "dayEvent": false,
            "title": "Fermentation Step - Batch #30"
        },
        {
            "dayEvent": false,
            "title": "Fermentation Step - Batch #30",
            "active": true,
            "eventText": "Primary (Fermentation) @ 22 °C",
            "eventType": "event-batch-ferm-step",
            "descriptionHTML": "Fermentation Profile Step:<br>Primary (Fermentation) @ 22 °C",
            "time": 1643360400000,
            "description": "Fermentation Profile Step: Primary (Fermentation) @ 22 °C"
        },
        {
            "title": "Fermentation Step - Batch #30",
            "descriptionHTML": "Fermentation Profile Step:<br>Cold Crash (Fermentation) @ 2 °C",
            "description": "Fermentation Profile Step: Cold Crash (Fermentation) @ 2 °C",
            "dayEvent": false,
            "active": true,
            "eventType": "event-batch-ferm-step",
            "time": 1643533200000,
            "eventText": "Cold Crash (Fermentation) @ 2 °C"
        }
    ],
    "batchNo": 30,
    "_rev": "LMO1KK60yiU8jUMx1Dssn0eIC5Ljxa",
    "measuredEfficiency": 73.22,
    "measuredPostBoilGravity": 1.053,
    "boilStepsCount": 0,
    "batchHopsLocal": [],
    "brewer": null,
    "notes": [
        {
            "timestamp": 1642875493365,
            "note": "",
            "status": "Fermenting",
            "type": "statusChanged"
        },
        {
            "type": "statusChanged",
            "timestamp": 1642863430881,
            "status": "Brewing",
            "note": ""
        }
    ],
    "estimatedColor": 15,
    "primingSugarEquiv": null,
    "batchMiscsLocal": [],
    "_created": {
        "_seconds": 1642841654,
        "_nanoseconds": 378000000
    },
    "recipe": {
        "author": "Matthew",
        "styleRbr": true,
        "og": 1.047049076,
        "_init": true,
        "styleFg": true,
        "boilSize": 24.51,
        "_created": {
            "_seconds": 1543795351,
            "_nanoseconds": 196000000
        },
        "_type": "recipe",
        "fermentableIbu": 0,
        "hopsTotalAmount": 92.9,
        "_public": false,
        "firstWortGravity": null,
        "type": "All Grain",
        "equipment": {
            "mashWaterVolumeLimitEnabled": true,
            "calcAromaHopUtilization": true,
            "grainAbsorptionRate": 1.15,
            "spargeWaterMin": null,
            "_id": "IyTWpqjuSfeAgMf74dwZnrFbbgFraG",
            "spargeTemperature": 80,
            "mashWaterFormula": "(GrainAmountKg * WaterGrainRatio) + MashTunDeadSpaceL",
            "name": "Maarten - Brew Monk - 21L - aug 2021",
            "brewhouseEfficiency": 65,
            "_timestamp": {
                "_seconds": 1642345843,
                "_nanoseconds": 0
            },
            "efficiencyType": "Fermenter",
            "spargeWaterOverflow": "Mash",
            "spargeWaterFormula": "BoilVolumeColdL - MashWaterL + (GrainAmountKg * GrainAbsorptionRate) + MashTunLossL",
            "bottlingVolume": 19,
            "_created": {
                "_seconds": 1563431175,
                "_nanoseconds": 376000000
            },
            "_rev": "d4aQvTxHxdt1Z7jVA19TSDzpmqhliT",
            "trubChillerLoss": 0.9,
            "boilTime": 60,
            "evaporationRate": 0.06935944512443899,
            "hopstandTemperature": 80,
            "calcStrikeWaterTemperature": false,
            "calcMashEfficiency": true,
            "hopUtilization": 1,
            "fermenterVolumeBeforeTopUp": 21,
            "mashTunDeadSpace": 8,
            "mashEfficiency": 67.8,
            "waterCalculation": "Default_2",
            "_timestamp_ms": 1642345843000,
            "spargeWaterMax": 16,
            "fermenterLoss": 2,
            "spargeWaterReminderTime": 25,
            "hidden": false,
            "postBoilKettleVol": 22.8125,
            "batchSize": 21,
            "fermenterVolume": 21,
            "mashWaterMax": 45,
            "aromaHopUtilization": 0.23,
            "_version": "2.8.0",
            "boilOffPerHr": 1.7,
            "notes": "Efficiency omlaag naar 65%\nKoken op 2200 watt\nMaisen op 1500 watt\n\nMinder sparge zodat er meer in ketel zit, 17.5L water bij 3.8KG mout is minimaal (erg weinig) bij Brew Monk. Dit profiel compseerd door sparge  limiet op te geven en initieel meer mee te nemen bij mash.\n\nGemeten boiloff is 2,3 liter per uur (bij 20 liter getest @ 2200 watt)\nKetel verlies (wat achter blijft na transfer): 850ml\n\n",
            "spargeWaterReminderEnabled": true,
            "ambientTemperature": null,
            "calcBoilVolume": true,
            "waterGrainRatio": null,
            "efficiency": 65,
            "mashWaterMin": 15,
            "fermenterLossEstimate": 0,
            "_meta": {
                "mashEfficiencyIsCalculated": true,
                "efficiencyIsCalculated": true
            },
            "boilSize": 24.51
        },
        "primaryTemp": 18,
        "styleOg": false,
        "searchTags": [
            "Added",
            "Irish Red Ale",
            "Januari - 2022"
        ],
        "_timestamp": {
            "_seconds": 1642841769,
            "_nanoseconds": 953000000
        },
        "styleBuGu": true,
        "path": "",
        "totalGravity": 1.047049076,
        "water": {
            "diluted": null,
            "mashWaterAmount": null,
            "acidPhAdjustment": -0.03126,
            "mash": {
                "_id": "UYSW1BGv3wVgYLqsoJYcgH1aPXKhVD",
                "_timestamp": {
                    "_seconds": 1638292194,
                    "_nanoseconds": 465000000
                },
                "calcium": 70.918,
                "residualAlkalinity": 39.53404,
                "type": "source",
                "ionBalanceOff": false,
                "bicarbonateMeqL": 1.9503081159040252,
                "anions": 5.885,
                "_created": {
                    "_seconds": 1568990297,
                    "_nanoseconds": 187000000
                },
                "hardness": 228,
                "sodium": 31.031,
                "cations": 5.914,
                "name": "Amersfoort 2020",
                "_rev": "0ruDm8deroleiEAyZD0EeD9U7MThj6",
                "ph": 7.76,
                "_version": "2.8.0",
                "ionBalance": 0,
                "bicarbonate": 119,
                "hidden": false,
                "residualAlkalinityMeqLCalc": 0.50329,
                "alkalinity": 97.516,
                "_timestamp_ms": 1638292194465,
                "soClRatio": 0.99,
                "chloride": 80.616,
                "sulfate": 79.752,
                "magnesium": 12.46
            },
            "enableSpargeAdjustments": false,
            "meta": {
                "equalSourceTotal": false
            },
            "spargeWaterAmount": null,
            "source": {
                "name": "Amersfoort 2020",
                "_id": "UYSW1BGv3wVgYLqsoJYcgH1aPXKhVD",
                "_version": "2.8.0",
                "hardness": 95,
                "sulfate": 5,
                "chloride": 10,
                "residualAlkalinity": 72.02402,
                "bicarbonate": 119,
                "ionBalanceOff": false,
                "ph": 7.76,
                "hidden": false,
                "bicarbonateMeqL": 1.9503081159040252,
                "anions": 2.336,
                "calcium": 33.4,
                "cations": 2.365,
                "residualAlkalinityMeqLCalc": 1.31419,
                "_rev": "0ruDm8deroleiEAyZD0EeD9U7MThj6",
                "soClRatio": 0.5,
                "ionBalance": 0,
                "magnesium": 2.78,
                "alkalinity": 97.516,
                "type": "source",
                "sodium": 10.8,
                "_timestamp": {
                    "_seconds": 1638292194,
                    "_nanoseconds": 465000000
                },
                "_created": {
                    "_seconds": 1568990297,
                    "_nanoseconds": 187000000
                },
                "_timestamp_ms": 1638292194465
            },
            "mashPh": 5.63,
            "mashPhDistilled": 5.58,
            "mashAdjustments": {
                "magnesium": 9.68,
                "bicarbonate": 0,
                "sodiumBicarbonate": 0,
                "calciumCarbonate": 0,
                "volume": 21.39,
                "calciumChloride": 4,
                "ltAMS": 0,
                "ltDWB": 0,
                "sodiumChloride": 1.1,
                "sodium": 20.231,
                "calciumHydroxide": 0,
                "chloride": 70.616,
                "magnesiumChloride": 0,
                "sulfate": 74.752,
                "calciumSulfate": 1.4,
                "sodiumMetabisulfite": 0,
                "magnesiumSulfate": 2.1,
                "acids": [
                    {
                        "type": "lactic",
                        "concentration": 80,
                        "alkalinityMeqL": -0.3210087922570391,
                        "amount": 0.5
                    }
                ],
                "calcium": 37.518,
                "sodiumMetabisulfitePPM": 0
            },
            "enableAcidAdjustments": false,
            "spargeTargetDiff": {
                "ionBalance": -1,
                "soClRatio": 1.08,
                "sodium": -5.2,
                "bicarbonate": 83,
                "residualAlkalinity": 84.11742,
                "chloride": -60,
                "calcium": -16.6,
                "alkalinity": 68.0154,
                "bicarbonateMeqL": 1.3602989379834798,
                "ionBalanceOff": false,
                "residualAlkalinityMeqLCalc": 1.76224,
                "anions": -1.685,
                "hardness": -71,
                "sulfate": -65,
                "cations": -1.649,
                "magnesium": -7.22
            },
            "dilutionPercentage": null,
            "sourceTargetDiff": {
                "calcium": -16.6,
                "alkalinity": 68.0154,
                "bicarbonateMeqL": 1.3602989379834798,
                "sulfate": -65,
                "residualAlkalinityMeqLCalc": 1.76224,
                "hardness": -71,
                "bicarbonate": 83,
                "cations": -1.649,
                "anions": -1.685,
                "soClRatio": 1.08,
                "residualAlkalinity": 84.11742,
                "ionBalanceOff": false,
                "chloride": -60,
                "ionBalance": -1,
                "sodium": -5.2,
                "magnesium": -7.22
            },
            "total": {
                "alkalinity": 97.516,
                "anions": 4.933,
                "magnesium": 9.864,
                "_id": "UYSW1BGv3wVgYLqsoJYcgH1aPXKhVD",
                "bicarbonate": 119,
                "residualAlkalinity": 48.24823,
                "cations": 4.962,
                "soClRatio": 0.97,
                "name": "Amersfoort 2020",
                "_rev": "0ruDm8deroleiEAyZD0EeD9U7MThj6",
                "_version": "2.8.0",
                "sodium": 25.605,
                "sulfate": 59.702,
                "type": "source",
                "_timestamp": {
                    "_seconds": 1638292194,
                    "_nanoseconds": 465000000
                },
                "hardness": 192,
                "residualAlkalinityMeqLCalc": 0.72078,
                "ph": 7.76,
                "calcium": 60.855,
                "bicarbonateMeqL": 1.9503081159040252,
                "hidden": false,
                "_timestamp_ms": 1638292194465,
                "ionBalance": 0,
                "chloride": 61.676,
                "_created": {
                    "_seconds": 1568990297,
                    "_nanoseconds": 187000000
                },
                "ionBalanceOff": false
            },
            "totalTargetDiff": {
                "soClRatio": 1.24,
                "cations": 0.948,
                "sulfate": -10.298,
                "anions": 0.911,
                "calcium": 10.855,
                "ionBalance": 1,
                "residualAlkalinityMeqLCalc": 1.16884,
                "magnesium": -0.136,
                "chloride": -8.324,
                "bicarbonateMeqL": 1.3602989379834798,
                "hardness": 27,
                "residualAlkalinity": 60.34163,
                "ionBalanceOff": false,
                "sodium": 9.605,
                "bicarbonate": 83,
                "alkalinity": 68.0154
            },
            "spargeAcidPhAdjustment": 0,
            "spargeAdjustments": {
                "volume": 7.84,
                "sulfate": 0,
                "bicarbonate": 0,
                "sodium": 0,
                "acids": [
                    {
                        "type": "lactic",
                        "amount": 0,
                        "concentration": 80
                    }
                ],
                "chloride": 0,
                "calcium": 0,
                "magnesium": 0,
                "sodiumMetabisulfitePPM": 0
            },
            "sparge": {
                "type": "source",
                "residualAlkalinity": 72.02402,
                "sulfate": 5,
                "residualAlkalinityMeqLCalc": 1.31419,
                "soClRatio": 0.5,
                "ph": 7.76,
                "bicarbonateMeqL": 1.9503081159040252,
                "alkalinity": 97.516,
                "_created": {
                    "_seconds": 1568990297,
                    "_nanoseconds": 187000000
                },
                "ionBalance": 0,
                "_timestamp_ms": 1638292194465,
                "sodium": 10.8,
                "_rev": "0ruDm8deroleiEAyZD0EeD9U7MThj6",
                "cations": 2.365,
                "ionBalanceOff": false,
                "bicarbonate": 119,
                "magnesium": 2.78,
                "anions": 2.336,
                "_id": "UYSW1BGv3wVgYLqsoJYcgH1aPXKhVD",
                "hidden": false,
                "hardness": 95,
                "name": "Amersfoort 2020",
                "chloride": 10,
                "_version": "2.8.0",
                "_timestamp": {
                    "_seconds": 1638292194,
                    "_nanoseconds": 465000000
                },
                "calcium": 33.4
            },
            "target": {
                "description": "Hit minimums on calcium and magnesium, keep the sulfate:chloride ratio low and equal. Do not favour flavour/maltiness or bitterness/dryness. For balanced beers. Blonde Ale/Premium Lager, Cream Ale/Standard Lager, Schwarzbier, English Pub Ale, Irish Red Ale, Dry Irish Stout, Russian Imperial Stout, Belgian Wit, Weizen/Weissbier, Düsseldorf Altbier, Munich Helles, Kölsch, Belgian Tripel, Belgian Super Saison.",
                "ionBalance": 0,
                "sodium": 16,
                "alkalinity": 29.5006,
                "soClRatio": 1,
                "anions": 4.022,
                "calcium": 50,
                "magnesium": 10,
                "residualAlkalinity": -12.0934,
                "type": "target",
                "cations": 4.014,
                "ionBalanceOff": false,
                "_id": "default-balanced",
                "bicarbonateMeqL": 0.5900091779205454,
                "name": "Balanced",
                "hardness": 166,
                "bicarbonate": 36,
                "chloride": 70,
                "residualAlkalinityMeqLCalc": -0.44805,
                "sulfate": 70
            },
            "mashTargetDiff": {
                "chloride": 10.616,
                "magnesium": 2.46,
                "ionBalance": 0,
                "sulfate": 9.752,
                "calcium": 20.918,
                "alkalinity": 68.0154,
                "bicarbonate": 83,
                "ionBalanceOff": false,
                "bicarbonateMeqL": 1.3602989379834798,
                "residualAlkalinity": 51.62744,
                "anions": 1.863,
                "cations": 1.9,
                "residualAlkalinityMeqLCalc": 0.95134,
                "soClRatio": 0.92,
                "sodium": 15.031,
                "hardness": 62
            },
            "style": "default",
            "totalAdjustments": {
                "bicarbonate": 0,
                "calciumCarbonate": 0,
                "ltDWB": 0,
                "calcium": 27.455,
                "sodiumBicarbonate": 0,
                "calciumChloride": 4,
                "volume": 29.23,
                "magnesiumSulfate": 2.1,
                "sodiumMetabisulfitePPM": 0,
                "sodium": 14.805,
                "ltAMS": 0,
                "sulfate": 54.702,
                "acids": [
                    {
                        "type": "lactic",
                        "concentration": 80,
                        "alkalinityMeqL": -0.3210087922570391,
                        "amount": 0.5
                    }
                ],
                "sodiumMetabisulfite": 0,
                "calciumHydroxide": 0,
                "chloride": 51.676,
                "sodiumChloride": 1.1,
                "calciumSulfate": 1.4,
                "magnesiumChloride": 0,
                "magnesium": 7.084
            },
            "settings": {
                "calciumHydroxide": {
                    "auto": false,
                    "sparge": false,
                    "mash": false
                },
                "calciumChloride": {
                    "auto": true,
                    "mash": true,
                    "form": "liquid",
                    "sparge": true
                },
                "adjustSparge": true,
                "magnesiumSulfate": {
                    "auto": true,
                    "sparge": true,
                    "mash": true
                },
                "sodiumChloride": {
                    "mash": true,
                    "sparge": true,
                    "auto": true
                },
                "calciumSulfate": {
                    "mash": true,
                    "sparge": true,
                    "auto": true
                },
                "sodiumBicarbonate": {
                    "auto": false,
                    "mash": false,
                    "sparge": false
                },
                "magnesiumChloride": {
                    "auto": false,
                    "mash": false,
                    "sparge": false
                }
            }
        },
        "buGuRatio": 0.53,
        "postBoilGravity": 1.047049076,
        "hidden": false,
        "fermentablesTotalAmount": 4.96,
        "styleConformity": false,
        "_version": "2.8.0",
        "fgEstimated": 1.012,
        "data": {
            "mashVolumeSurplus": 0,
            "topUpWater": 0,
            "spargeWaterAmount": 7.84,
            "mashFermentables": [
                {
                    "protein": null,
                    "origin": "Netherlands",
                    "usedIn": "",
                    "maxInBatch": null,
                    "color": 1.9,
                    "ibuPerAmount": null,
                    "_timestamp_ms": 1642441437642,
                    "inventory": 0.1,
                    "_rev": "tCfi5G8rMulqla3CUb4IOMKK8KdOOa",
                    "fan": null,
                    "coarseFineDiff": null,
                    "fgdb": null,
                    "supplier": "The Swaen",
                    "bestBeforeDate": 1635721200000,
                    "cgdb": null,
                    "manufacturingDate": null,
                    "_created": {
                        "_seconds": 1621670411,
                        "_nanoseconds": 699000000
                    },
                    "potential": 1.0368,
                    "acid": null,
                    "percentage": 49.4,
                    "notes": "",
                    "name": "Swaen Pilsner",
                    "hidden": false,
                    "_version": "2.8.0",
                    "notFermentable": false,
                    "grainCategory": "Base (Pilsner)",
                    "costPerAmount": null,
                    "potentialPercentage": 80,
                    "amount": 2.45,
                    "_id": "default-c3ff8bb88f9",
                    "type": "Grain",
                    "moisture": null,
                    "diastaticPower": null,
                    "attenuation": null,
                    "friability": null,
                    "userNotes": "Vervangt Pale Malt (3850g)",
                    "substitutes": "",
                    "_timestamp": {
                        "_seconds": 1642441437,
                        "_nanoseconds": 642000000
                    }
                },
                {
                    "color": 2.538071,
                    "type": "Grain",
                    "notFermentable": false,
                    "_id": "default-33db684",
                    "potential": 1.03795,
                    "usedIn": "",
                    "name": "Pale Malt, Maris Otter",
                    "friability": null,
                    "fan": null,
                    "coarseFineDiff": 1.5,
                    "manufacturingDate": null,
                    "inventory": 5.5,
                    "_created": {
                        "_seconds": 1615637669,
                        "_nanoseconds": 272000000
                    },
                    "origin": "UK",
                    "_timestamp_ms": 1638517969843,
                    "grainCategory": "Base (Maris Otter)",
                    "fgdb": null,
                    "costPerAmount": null,
                    "cgdb": null,
                    "percentage": 28.23,
                    "_timestamp": {
                        "_seconds": 1638517969,
                        "_nanoseconds": 843000000
                    },
                    "userNotes": "Vervangt Pale Malt (3850g)",
                    "notes": "Premium base malt from the UK. Popular for many English styles of beer including ales, pale ales and bitters.",
                    "diastaticPower": 120,
                    "_rev": "aaTJInm3YDNT41giT4DRXT8aqhQAf2",
                    "amount": 1.4,
                    "protein": 9.4,
                    "attenuation": 0.81,
                    "moisture": 3,
                    "potentialPercentage": 82.5,
                    "bestBeforeDate": null,
                    "lovibond": 2.4,
                    "_version": "2.8.0",
                    "substitutes": "Pale Liquid Extract",
                    "hidden": false,
                    "supplier": "Thomas Fawcett",
                    "maxInBatch": 100,
                    "ibuPerAmount": null,
                    "acid": 0
                },
                {
                    "_id": "default-33b31a84570",
                    "supplier": "The Swaen",
                    "fgdb": null,
                    "protein": null,
                    "moisture": null,
                    "notes": "",
                    "name": "GoldSwaen Amber",
                    "notFermentable": false,
                    "inventory": null,
                    "potentialPercentage": 75,
                    "bestBeforeDate": null,
                    "userNotes": "Vervangt Caraamber Weyermann (820g)",
                    "grainCategory": "Crystal/Caramel",
                    "cgdb": null,
                    "costPerAmount": null,
                    "substitutes": "",
                    "potential": 1.0345,
                    "amount": 0.82,
                    "manufacturingDate": null,
                    "coarseFineDiff": null,
                    "type": "Grain",
                    "acid": null,
                    "color": 35.6,
                    "ibuPerAmount": null,
                    "origin": "Netherlands",
                    "maxInBatch": null,
                    "percentage": 16.53,
                    "diastaticPower": null,
                    "friability": null,
                    "usedIn": "",
                    "fan": null,
                    "attenuation": null
                },
                {
                    "fgdb": 81,
                    "grainCategory": "Base",
                    "friability": null,
                    "potential": 1.035,
                    "notFermentable": false,
                    "attenuation": 0.74,
                    "hidden": false,
                    "cgdb": null,
                    "moisture": 6,
                    "percentage": 4.64,
                    "name": "Pale Rye Malt",
                    "bestBeforeDate": null,
                    "userNotes": "Ter vervanging van Rye Malt (230g)",
                    "acid": null,
                    "origin": "Germany",
                    "_id": "default-a2fddf6",
                    "protein": null,
                    "lovibond": 3.2,
                    "notes": "Suitable for any pale or bright rye or specialty beers. Sensory: typical rye aroma, malty-sweet with notes of bread and honey. Rye malt also creates a velvety-soft mouthfeel.",
                    "diastaticPower": null,
                    "color": 3.553299,
                    "maxInBatch": 60,
                    "potentialPercentage": 75.2,
                    "amount": 0.23,
                    "usedIn": "",
                    "costPerAmount": null,
                    "inventory": null,
                    "fan": null,
                    "manufacturingDate": null,
                    "supplier": "Weyermann",
                    "substitutes": "",
                    "coarseFineDiff": 1,
                    "type": "Grain"
                },
                {
                    "usedIn": "",
                    "potentialPercentage": 70,
                    "ibuPerAmount": null,
                    "supplier": "Viking Malt",
                    "percentage": 1.21,
                    "coarseFineDiff": null,
                    "name": "Roasted Barley",
                    "grainCategory": "Roasted",
                    "inventory": 1,
                    "notFermentable": false,
                    "fgdb": null,
                    "maxInBatch": null,
                    "origin": "Poland",
                    "fan": null,
                    "manufacturingDate": null,
                    "_created": {
                        "_seconds": 1642621125,
                        "_nanoseconds": 65000000
                    },
                    "bestBeforeDate": 1650751200000,
                    "cgdb": null,
                    "diastaticPower": null,
                    "notes": "Roasted barley is produced from malting barley. The enzymatic activity is zero. Fermentable extract is low. Typical flavor is burnt and roasted.",
                    "userNotes": "Eigenlijk van Brewferm 1000-1300 ebc",
                    "substitutes": "",
                    "friability": null,
                    "type": "Grain",
                    "_timestamp": {
                        "_seconds": 1642841729,
                        "_nanoseconds": 314000000
                    },
                    "_rev": "Iz8ape6sCRdHp76Fo0cvEI5Jh1yBBD",
                    "amount": 0.06,
                    "attenuation": 0.15,
                    "_version": "2.8.0",
                    "acid": null,
                    "moisture": null,
                    "color": 558.3756345,
                    "costPerAmount": null,
                    "_id": "default-acecc92",
                    "_timestamp_ms": 1642841729314,
                    "hidden": false,
                    "potential": 1.0322,
                    "protein": null
                }
            ],
            "batchSpargeWaterAmount4": null,
            "allDiastaticPower": false,
            "totalDiastaticPower": 168,
            "batchSpargeWaterAmount3": null,
            "hltWaterAmount": 7.84,
            "otherFermentables": [],
            "mashVolume": 24.7132,
            "mashFermentablesAmount": 4.96,
            "batchSpargeWaterAmount1": null,
            "mashWaterAmount": 21.39,
            "hopsAmount": 92.9,
            "totalWaterAmount": 29.23,
            "strikeTemp": null,
            "batchSpargeWaterAmount2": null,
            "otherFermentablesAmount": 0
        },
        "yeastToleranceExceededBy": null,
        "sumDryHopPerLiter": 2,
        "carbonationStyle": {
            "carbMin": 2.4,
            "name": "Irish Red Ale",
            "_id": "15A",
            "carbMax": 2.8
        },
        "rbRatio": 0.51,
        "fermentables": [
            {
                "_timestamp": {
                    "_seconds": 1642441437,
                    "_nanoseconds": 642000000
                },
                "usedIn": "",
                "notes": "",
                "amount": 2.45,
                "type": "Grain",
                "cgdb": null,
                "userNotes": "Vervangt Pale Malt (3850g)",
                "_created": {
                    "_seconds": 1621670411,
                    "_nanoseconds": 699000000
                },
                "hidden": false,
                "manufacturingDate": null,
                "acid": null,
                "origin": "Netherlands",
                "_version": "2.8.0",
                "costPerAmount": null,
                "attenuation": null,
                "fgdb": null,
                "potential": 1.0368,
                "protein": null,
                "coarseFineDiff": null,
                "fan": null,
                "notFermentable": false,
                "moisture": null,
                "potentialPercentage": 80,
                "name": "Swaen Pilsner",
                "bestBeforeDate": 1635721200000,
                "friability": null,
                "grainCategory": "Base (Pilsner)",
                "supplier": "The Swaen",
                "ibuPerAmount": null,
                "_rev": "tCfi5G8rMulqla3CUb4IOMKK8KdOOa",
                "percentage": 49.4,
                "_id": "default-c3ff8bb88f9",
                "diastaticPower": null,
                "maxInBatch": null,
                "substitutes": "",
                "inventory": 0.1,
                "_timestamp_ms": 1642441437642,
                "color": 1.9
            },
            {
                "userNotes": "Vervangt Pale Malt (3850g)",
                "_timestamp": {
                    "_seconds": 1638517969,
                    "_nanoseconds": 843000000
                },
                "fgdb": null,
                "color": 2.538071,
                "percentage": 28.23,
                "usedIn": "",
                "_id": "default-33db684",
                "costPerAmount": null,
                "lovibond": 2.4,
                "maxInBatch": 100,
                "protein": 9.4,
                "notes": "Premium base malt from the UK. Popular for many English styles of beer including ales, pale ales and bitters.",
                "manufacturingDate": null,
                "acid": 0,
                "potential": 1.03795,
                "moisture": 3,
                "type": "Grain",
                "coarseFineDiff": 1.5,
                "notFermentable": false,
                "substitutes": "Pale Liquid Extract",
                "_rev": "aaTJInm3YDNT41giT4DRXT8aqhQAf2",
                "ibuPerAmount": null,
                "cgdb": null,
                "attenuation": 0.81,
                "friability": null,
                "name": "Pale Malt, Maris Otter",
                "supplier": "Thomas Fawcett",
                "hidden": false,
                "_timestamp_ms": 1638517969843,
                "diastaticPower": 120,
                "origin": "UK",
                "amount": 1.4,
                "_created": {
                    "_seconds": 1615637669,
                    "_nanoseconds": 272000000
                },
                "_version": "2.8.0",
                "fan": null,
                "potentialPercentage": 82.5,
                "grainCategory": "Base (Maris Otter)",
                "bestBeforeDate": null,
                "inventory": 5.5
            },
            {
                "fan": null,
                "fgdb": null,
                "inventory": null,
                "supplier": "The Swaen",
                "potential": 1.0345,
                "cgdb": null,
                "type": "Grain",
                "grainCategory": "Crystal/Caramel",
                "name": "GoldSwaen Amber",
                "coarseFineDiff": null,
                "moisture": null,
                "costPerAmount": null,
                "attenuation": null,
                "diastaticPower": null,
                "acid": null,
                "bestBeforeDate": null,
                "friability": null,
                "origin": "Netherlands",
                "color": 35.6,
                "potentialPercentage": 75,
                "notes": "",
                "notFermentable": false,
                "percentage": 16.53,
                "userNotes": "Vervangt Caraamber Weyermann (820g)",
                "_id": "default-33b31a84570",
                "maxInBatch": null,
                "usedIn": "",
                "protein": null,
                "amount": 0.82,
                "substitutes": "",
                "manufacturingDate": null,
                "ibuPerAmount": null
            },
            {
                "protein": null,
                "fgdb": 81,
                "notes": "Suitable for any pale or bright rye or specialty beers. Sensory: typical rye aroma, malty-sweet with notes of bread and honey. Rye malt also creates a velvety-soft mouthfeel.",
                "diastaticPower": null,
                "lovibond": 3.2,
                "notFermentable": false,
                "maxInBatch": 60,
                "inventory": null,
                "cgdb": null,
                "type": "Grain",
                "percentage": 4.64,
                "name": "Pale Rye Malt",
                "origin": "Germany",
                "hidden": false,
                "potentialPercentage": 75.2,
                "amount": 0.23,
                "friability": null,
                "moisture": 6,
                "usedIn": "",
                "costPerAmount": null,
                "coarseFineDiff": 1,
                "grainCategory": "Base",
                "manufacturingDate": null,
                "bestBeforeDate": null,
                "color": 3.553299,
                "supplier": "Weyermann",
                "userNotes": "Ter vervanging van Rye Malt (230g)",
                "potential": 1.035,
                "acid": null,
                "substitutes": "",
                "attenuation": 0.74,
                "fan": null,
                "_id": "default-a2fddf6"
            },
            {
                "amount": 0.06,
                "acid": null,
                "notes": "Roasted barley is produced from malting barley. The enzymatic activity is zero. Fermentable extract is low. Typical flavor is burnt and roasted.",
                "fgdb": null,
                "_timestamp_ms": 1642841729314,
                "percentage": 1.21,
                "substitutes": "",
                "userNotes": "Eigenlijk van Brewferm 1000-1300 ebc",
                "name": "Roasted Barley",
                "origin": "Poland",
                "hidden": false,
                "diastaticPower": null,
                "_id": "default-acecc92",
                "manufacturingDate": null,
                "inventory": 1,
                "_rev": "Iz8ape6sCRdHp76Fo0cvEI5Jh1yBBD",
                "_version": "2.8.0",
                "grainCategory": "Roasted",
                "coarseFineDiff": null,
                "friability": null,
                "cgdb": null,
                "fan": null,
                "notFermentable": false,
                "color": 558.3756345,
                "type": "Grain",
                "supplier": "Viking Malt",
                "costPerAmount": null,
                "_created": {
                    "_seconds": 1642621125,
                    "_nanoseconds": 65000000
                },
                "potential": 1.0322,
                "potentialPercentage": 70,
                "maxInBatch": null,
                "ibuPerAmount": null,
                "attenuation": 0.15,
                "usedIn": "",
                "_timestamp": {
                    "_seconds": 1642841729,
                    "_nanoseconds": 314000000
                },
                "bestBeforeDate": 1650751200000,
                "protein": null,
                "moisture": null
            }
        ],
        "defaults": {
            "gravity": "sg",
            "grainColor": "default",
            "temp": "c",
            "pressure": "bar",
            "color": "ebc",
            "weight": "kg",
            "hop": "g",
            "altitude": "m",
            "volume": "l",
            "preferred": "metric",
            "attenuation": "normal",
            "abv": "simple",
            "ibu": "tinseth",
            "carbonation": "vol"
        },
        "nutrition": {
            "calories": {
                "carbs": 18.15813291903967,
                "alcohol": 25.8291529976366,
                "kJ": 184.04280427537356,
                "total": 43.98728591667628
            },
            "carbs": {
                "total": 4.582802234842022
            }
        },
        "img": "users/Dm0ZCpbbf7RHuWTklVo3NHrlGRL2/images/recipes/8tiFhulCntROHmZz8Q8LpxXL8npKfP/8tiFhulCntROHmZz8Q8LpxXL8npKfP.jpeg",
        "carbonation": 2.4,
        "_uid": "v50ynXGwmlYgoysyyGqpRoKFJbS2",
        "styleCarb": true,
        "origin": null,
        "styleAbv": true,
        "tags": null,
        "teaser": "",
        "_ev": 1.1,
        "attenuation": 0.737,
        "_rev": "DTaq4JxDBGchfCtRjCMHmAc4OACsex",
        "hops": [
            {
                "type": "Pellet",
                "name": "Fuggles",
                "ibu": 14.1,
                "usage": "Aroma",
                "time": 60,
                "alpha": 4.5,
                "amount": 25.7,
                "use": "Boil",
                "_id": "default-f80149bd",
                "origin": "United Kingdom"
            },
            {
                "caryophyllene": null,
                "hsi": null,
                "usage": "Both",
                "bestBeforeDate": 1690754400000,
                "time": 30,
                "myrcene": null,
                "_rev": "2oG7dlZYcYucgsOXQxshOj4jnZPo3a",
                "name": "East Kent Goldings (EKG)",
                "farnesene": null,
                "_timestamp_ms": 1642600935503,
                "humulene": null,
                "userNotes": "",
                "use": "Boil",
                "hidden": false,
                "origin": "United Kingdom",
                "temp": null,
                "cohumulone": null,
                "_created": {
                    "_seconds": 1584258247,
                    "_nanoseconds": 820000000
                },
                "inventory": 0,
                "notes": "",
                "manufacturingDate": null,
                "year": null,
                "usedIn": "",
                "type": "Pellet",
                "alpha": 5.61,
                "_timestamp": {
                    "_seconds": 1642600935,
                    "_nanoseconds": 503000000
                },
                "_version": "2.8.0",
                "oil": null,
                "substitutes": "",
                "beta": null,
                "ibu": 6.6,
                "_id": "default-7f820fa1",
                "amount": 12.6
            },
            {
                "origin": "United Kingdom",
                "hidden": false,
                "humulene": null,
                "temp": null,
                "year": null,
                "time": 15,
                "type": "Pellet",
                "beta": null,
                "use": "Boil",
                "name": "East Kent Goldings (EKG)",
                "_timestamp_ms": 1642600935503,
                "_timestamp": {
                    "_seconds": 1642600935,
                    "_nanoseconds": 503000000
                },
                "amount": 12.6,
                "_version": "2.8.0",
                "_id": "default-7f820fa1",
                "usedIn": "",
                "usage": "Both",
                "hsi": null,
                "userNotes": "",
                "notes": "",
                "cohumulone": null,
                "inventory": 0,
                "caryophyllene": null,
                "bestBeforeDate": 1690754400000,
                "myrcene": null,
                "farnesene": null,
                "alpha": 5.61,
                "substitutes": "",
                "manufacturingDate": null,
                "ibu": 4.3,
                "_rev": "2oG7dlZYcYucgsOXQxshOj4jnZPo3a",
                "oil": null,
                "_created": {
                    "_seconds": 1584258247,
                    "_nanoseconds": 820000000
                }
            },
            {
                "origin": "US",
                "day": 5,
                "alpha": 12,
                "usage": "Both",
                "temp": null,
                "time": 5,
                "_id": "default-8e9450d5",
                "name": "Citra",
                "ibu": 0,
                "use": "Dry Hop",
                "amount": 42,
                "actualTime": 1643238000000,
                "timeUnit": "day",
                "type": "Pellet"
            }
        ],
        "thumb": "data:image/jpeg;base64,/9j/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCABIAEgDASIAAhEBAxEB/8QAGgAAAgMBAQAAAAAAAAAAAAAAAAcEBggFA//EADMQAAEDAwMCBAUCBgMAAAAAAAECAwQABREGEiEHMRNBUWEUInGRoUKBFSNyscHRMmLS/8QAGgEAAwEBAQEAAAAAAAAAAAAAAwQFAgEABv/EACERAAIDAAICAgMAAAAAAAAAAAABAgMREiEEQTLwMWFx/9oADAMBAAIRAxEAPwDVNKiyMqb6m3B5KM7H3yefIjGfzTXrLEHqHdoHWPUkd0NyYrMqa2ltKAlWELITz7BIrjeLo8o8hs3vRMC4XGRPk3CQhTuMoQgYGBjzqVY7darAFKjyZC1njLgGR6jjyOBSrvXVm9MpXstMdQHIC1KB9u1US5dbL22+ptyzQs5xne5Ssne/wg0YQHxcNK2O6b0O3WW0e+cI7jnjiuFeOmMGfbZMa3X4pfeGAt5kEDB47EUmXest1CsLtUROPR1dSbT1huDkpKV29tKSf0vH/VCau3WkGjVF/E59rt5g3mXCfeLrsR9TKltf8VEKwSM+XFMnQclhOprQhKVlRmMjKlf9wPIe9K6NqiNHmyHlsueI66p1R2pPJUTTW0E4p6/WV9Dzfhuy2FpAUBlJUPKl7eXNNor0uLraT9Gl6KKKsHzgVljqhYYGj+pEm9wFSXm7ozIfUlwghMhT5DgHHb0Hl61qes0a1vkC5zTbnHh/EbfdrpGdQUn5W3HVltWe3c/isyeI3Bdi81VqsJluJjBgoAG3uc8du1Lu73F6W+HT4aRuyE47VYLvFU86pasb1c59arMxkoIyOfSsRkO11RZ4vvfGPqWsJRnk1ItCQmc0ClSxux8vnUZllTpOAK7+k2ku3mGwkfOtwIz9TisWSxFPx/Gjjk2dKTpaW3GuUpbiQIyhub284OCk5+h/FOLpnDiRpOmw2H3QJDGxaljzUk5PHvVciMKkeJFW4CqXELZCjklaCUfccVZejEmW/FsjS3W9saamOpCiM/KsHt9CKQsk5Z+mjFMYx5Z7TNLUUUVXPnwrFur3IDWudXl6Y43PN2eLLHglSXUh5RWd/wCkjjg962lWP0Roc/qzrmDNZS44+u5/DrUMlt1K1LSQfLISR+9CteILUuyjXokHI7f2quTwHEhSe57/AFqx6gIakkJHyjAIP0zVZlr2OrKRls+XpQ4v2UKyKwopJru6UWtm9xH2hlbTgdA/pO7/ABXA3ck1cOmsdMrU0dC0lSdi8gf0GsWvEUoLK2Me85gajCtgDaZiXQpHbY+j/wBJ/NdDpPsj9TptsdDiU/GNzI6RjGCec/dP2rxm6dkz4cRHjbH2YiGFnBVlSCClXGOAB+a7Ol7S/G6k2e8trKHCpuM63t4WlSgCf7falYQfSf3sTndFa4/dRpGiiiqxECkRO0raWNd3O7tRiZypbzhUp0kblFQOE+4Jp70rbtLkW6+zhPZSIq31lMqMg5QCSQHEckjH6k59wKzJJrs1F4Zn6iMph6iuEdKdjbb3yo9Bj/WKo0weGsjPfsaZ3WVpKdYTnWXEyGnylaXUHcFApHINK6WlYOFJoHJFaiEmk0iMk800+hERErVv80K2IjuKJT5dh/mlc22oq4Bpy9Bor8ebcJoQ2AljwwXiUpJJBxuHY4FBm9kkihYuHjybHIhtlhSx4UZ/b38bcFY/bg/aptquLKb3bmRGRH3PtgFtO4ElQxyO374qtybi0oBUhBhqVwCpWUKz6L5T98VNsaXzqS1pS4hSPiGjneCCneDkEd6JnZB9DuooopsVClldG1t36Y4zK/mKcWdpOSAFHt6j6dqKK4zqF5r+HFedZC47a0ODGcYwe+Mj175qjmx6SfkJauJucR9XA2NhTZPscfjNFFLyri3rQ1X5FlayEsLpZNJ9OrcwJL1svd0fSM+EGyEHj1O0fmodyvdzud1iN2m3RbDYYoIRCaCXFLJxlTmBgnA4Azj1NFFY1R+KwJKU7PnJv+llt8lx5lW9YQRwNiBtP1zU2x2xLGobVJR4cZRlNg+CoJS5844KRxz7Ciiua9PYmh3UUUU6IH//2Q==",
        "_origin": "8tiFhulCntROHmZz8Q8LpxXL8npKfP",
        "miscs": [
            {
                "type": "Water Agent",
                "_id": "default-3b1827",
                "use": "Mash",
                "hidden": false,
                "timeIsDays": false,
                "amount": 4,
                "concentration": 33,
                "time": null,
                "_rev": "GjmGAk0CkMh3vWUrQDbxscKpSZW8zZ",
                "_version": "2.8.0",
                "_timestamp_ms": 1638520692376,
                "unit": "g",
                "name": "Calcium Chloride (CaCl2)",
                "_timestamp": {
                    "_seconds": 1638520692,
                    "_nanoseconds": 376000000
                },
                "inventory": -51.376,
                "waterAdjustment": true,
                "_created": {
                    "_seconds": 1592121510,
                    "_nanoseconds": 390000000
                }
            },
            {
                "hidden": false,
                "amount": 1.1,
                "_timestamp_ms": 1638520484285,
                "_rev": "2AFEvMJdsQrHMIrjOg21dcKfuOl0yI",
                "name": "Canning Salt (NaCl)",
                "timeIsDays": false,
                "_timestamp": {
                    "_seconds": 1638520484,
                    "_nanoseconds": 285000000
                },
                "_version": "2.8.0",
                "use": "Mash",
                "inventory": -13.48,
                "waterAdjustment": true,
                "type": "Water Agent",
                "unit": "g",
                "time": null,
                "_id": "default-bk9j78",
                "_created": {
                    "_seconds": 1594461222,
                    "_nanoseconds": 957000000
                }
            },
            {
                "_id": "default-4e9d62",
                "_created": {
                    "_seconds": 1592121509,
                    "_nanoseconds": 704000000
                },
                "hidden": false,
                "type": "Water Agent",
                "timeIsDays": false,
                "amount": 2.1,
                "_timestamp_ms": 1638520005445,
                "time": null,
                "inventory": -14.364,
                "waterAdjustment": true,
                "unit": "g",
                "name": "Epsom Salt (MgSO4)",
                "use": "Mash",
                "_version": "2.8.0",
                "_timestamp": {
                    "_seconds": 1638520005,
                    "_nanoseconds": 445000000
                },
                "_rev": "aLR6FYpVDzqk714i3FeppvpWLbSYrm"
            },
            {
                "_id": "default-1f88df",
                "hidden": false,
                "_rev": "3dh2lFum6hVrf6zJPuqQTCOWa9aKGC",
                "amount": 1.4,
                "_created": {
                    "_seconds": 1592121511,
                    "_nanoseconds": 471000000
                },
                "use": "Mash",
                "unit": "g",
                "waterAdjustment": true,
                "name": "Gypsum (CaSO4)",
                "_timestamp": {
                    "_seconds": 1638519934,
                    "_nanoseconds": 933000000
                },
                "_timestamp_ms": 1638519934933,
                "type": "Water Agent",
                "inventory": -21.416,
                "_version": "2.8.0",
                "timeIsDays": false,
                "time": null
            }
        ],
        "name": "Ryerish Red Ale",
        "styleColor": false,
        "ogPlato": 11.7,
        "ibu": 25,
        "styleIbu": true,
        "batchSize": 21,
        "mash": {
            "steps": [
                {
                    "displayStepTemp": 55,
                    "name": "Mash In",
                    "stepTime": 10,
                    "rampTime": null,
                    "stepTemp": 55,
                    "type": "Temperature"
                },
                {
                    "type": "Temperature",
                    "displayStepTemp": 65,
                    "stepTime": 40,
                    "rampTime": 10,
                    "stepTemp": 65,
                    "name": "First Rest"
                },
                {
                    "rampTime": 7,
                    "stepTime": 25,
                    "type": "Temperature",
                    "name": "Second Rest",
                    "displayStepTemp": 72,
                    "stepTemp": 72
                },
                {
                    "type": "Temperature",
                    "stepTemp": 77,
                    "name": "Mash Out",
                    "rampTime": 5,
                    "displayStepTemp": 77,
                    "stepTime": 10
                }
            ],
            "_timestamp": {
                "_seconds": 1544874170,
                "_nanoseconds": 428000000
            },
            "name": "Step Mash",
            "_version": "1.3.4",
            "_rev": "elaunoP7DKX1WW2tjK7giDRx0sE7Iz",
            "_id": "YDTK7QM1DNznBcYa4tdgtuAzx1OKm6",
            "_created": {
                "_seconds": 1544874063,
                "_nanoseconds": 692000000
            }
        },
        "boilTime": 60,
        "_timestamp_ms": 1642841769953,
        "efficiency": 65,
        "fgFormula": "normal",
        "extraGravity": 0,
        "yeasts": [
            {
                "_id": "default-e294c5",
                "name": "SafAle English Ale",
                "fermentsAll": false,
                "attenuation": 75,
                "amount": 1,
                "starterSize": null,
                "maxTemp": 20,
                "minTemp": 15,
                "form": "Dry",
                "productId": "S-04",
                "laboratory": "Fermentis",
                "unit": "pkg",
                "type": "Ale",
                "starter": null,
                "description": "English ale yeast selected for its fast fermentation character and its ability to form a compact sediment at the end of fermentation, helping to improve beer clarity. Recommended for the production of a large range of ales and specially adapted to cask-conditioned ones and fermentation in cylindo-conical tanks.",
                "flocculation": "Medium"
            }
        ],
        "diastaticPower": 33.87,
        "public": false,
        "style": {
            "carbMax": null,
            "styleLetter": "A",
            "abvMax": 5,
            "ibuMax": 28,
            "buGuMax": 0.68,
            "carbonationStyle": "15A",
            "fgMax": 1.014,
            "abvMin": 3.8,
            "buGuMin": 0.44,
            "fgMin": 1.01,
            "ibuMin": 18,
            "colorMin": 9,
            "_id": "default-46",
            "category": "Irish Beer",
            "carbMin": null,
            "name": "Irish Red Ale",
            "lovibondMin": 9,
            "type": "Amber Ale",
            "rbrMax": 0.64,
            "categoryNumber": "15",
            "colorMax": 14,
            "ogMin": 1.036,
            "rbrMin": 0.41,
            "styleGuide": "BJCP 2015",
            "ogMax": 1.046,
            "lovibondMax": 14
        },
        "_share": null,
        "avgWeightedHopstandTemp": 80,
        "preBoilGravity": 1.044,
        "fg": 1.012,
        "_id": "BpKdOc9K8ey60QTmeAVTHmFmggtzY0",
        "hopStandMinutes": 0,
        "notes": "Always a winner - especially with those people who don’t like “dark beers”. ",
        "ibuFormula": "tinseth",
        "color": 14.4,
        "mashEfficiency": 67.8,
        "abv": 4.59,
        "fermentation": {
            "_created": {
                "_seconds": 1544872751,
                "_nanoseconds": 983000000
            },
            "_version": "1.3.4",
            "steps": [
                {
                    "stepTime": 4,
                    "displayStepTemp": 18,
                    "type": "Primary",
                    "actualTime": 1642806000000,
                    "pressure": null,
                    "stepTemp": 18,
                    "displayPressure": null
                },
                {
                    "stepTemp": 20,
                    "type": "Primary",
                    "displayPressure": null,
                    "pressure": null,
                    "stepTime": 2,
                    "displayStepTemp": 20,
                    "actualTime": 1643151600000
                },
                {
                    "displayPressure": null,
                    "type": "Primary",
                    "stepTime": 2,
                    "actualTime": 1643324400000,
                    "displayStepTemp": 22,
                    "stepTemp": 22,
                    "pressure": null
                },
                {
                    "pressure": null,
                    "type": "Cold Crash",
                    "actualTime": 1643497200000,
                    "displayStepTemp": 2,
                    "stepTime": 4,
                    "stepTemp": 2,
                    "displayPressure": null
                }
            ],
            "name": "Fermentation Fridge",
            "_timestamp": {
                "_seconds": 1544872751,
                "_nanoseconds": 983000000
            },
            "_rev": "l36hZqM24smTcqg58YRSlRvQ6fU2zZ",
            "_id": "PVbg6UpXTeeuBWmLQycuK1AJYdXMX4"
        },
        "img_url": "https://firebasestorage.googleapis.com/v0/b/brewfather-app.appspot.com/o/users%2FDm0ZCpbbf7RHuWTklVo3NHrlGRL2%2Fimages%2Frecipes%2F8tiFhulCntROHmZz8Q8LpxXL8npKfP%2F8tiFhulCntROHmZz8Q8LpxXL8npKfP.jpeg?alt=media"
    },
    "estimatedTotalGravity": 1.053,
    "mashStepsCount": 0,
    "brewDate": 1642806000000,
    "estimatedIbu": 25,
    "measuredAttenuation": 74.6,
    "_init": true,
    "estimatedRbRatio": 0.47,
    "hidden": false,
    "measuredBatchSize": 21,
    "brewControllerEnabled": false,
    "batchFermentables": [
        {
            "_timestamp_ms": 1642620979741,
            "grainCategory": "Crystal/Caramel",
            "ibuPerAmount": null,
            "origin": "Netherlands",
            "diastaticPower": null,
            "notInRecipe": false,
            "acid": null,
            "supplier": "The Swaen",
            "bestBeforeDate": 1659304800000,
            "displayAmount": 0,
            "friability": null,
            "amount": 0.82,
            "notes": "",
            "attenuation": null,
            "protein": null,
            "potential": 1.0345,
            "moisture": null,
            "removedFromInventory": true,
            "removedAmount": 0.82,
            "_timestamp": {
                "_seconds": 1642620979,
                "_nanoseconds": 741000000
            },
            "coarseFineDiff": null,
            "potentialPercentage": 75,
            "maxInBatch": null,
            "_version": "2.8.0",
            "_rev": "axHWUBK77SqnjM2yZlZKaH7R6Q1lmK",
            "usedIn": "",
            "type": "Grain",
            "_created": {
                "_seconds": 1642620979,
                "_nanoseconds": 743000000
            },
            "hidden": false,
            "name": "GoldSwaen Amber",
            "costPerAmount": 0,
            "notFermentable": false,
            "fgdb": null,
            "checked": true,
            "totalCost": 0,
            "userNotes": "BBF onbekend dus ingeschat\n19-1-2022 gekocht",
            "_id": "default-33b31a84570",
            "substitutes": "",
            "manufacturingDate": null,
            "inventory": 0.18,
            "fan": null,
            "cgdb": null,
            "color": 35.6
        },
        {
            "attenuation": null,
            "_timestamp": {
                "_seconds": 1642621218,
                "_nanoseconds": 913000000
            },
            "color": 1.9,
            "bestBeforeDate": 1696111200000,
            "removedFromInventory": true,
            "maxInBatch": null,
            "grainCategory": "Base (Pilsner)",
            "substitutes": "",
            "acid": null,
            "userNotes": "",
            "_id": "default-c3ff8bb88f9",
            "type": "Grain",
            "coarseFineDiff": null,
            "manufacturingDate": null,
            "potentialPercentage": 80,
            "costPerAmount": 0,
            "moisture": null,
            "ibuPerAmount": null,
            "amount": 2.45,
            "origin": "Netherlands",
            "_rev": "EByJmjwjCVIx6ZGKBpDyPpZCwQt5db",
            "_version": "2.8.0",
            "notInRecipe": false,
            "hidden": false,
            "fgdb": null,
            "notes": "",
            "_timestamp_ms": 1642621218913,
            "usedIn": "",
            "cgdb": null,
            "friability": null,
            "totalCost": 0,
            "displayAmount": 0,
            "notFermentable": false,
            "fan": null,
            "diastaticPower": null,
            "name": "Swaen Pilsner",
            "inventory": 2.65,
            "supplier": "The Swaen",
            "protein": null,
            "checked": true,
            "removedAmount": 2.45,
            "_created": {
                "_seconds": 1621670411,
                "_nanoseconds": 699000000
            },
            "potential": 1.0368
        },
        {
            "notes": "Premium base malt from the UK. Popular for many English styles of beer including ales, pale ales and bitters.",
            "type": "Grain",
            "origin": "UK",
            "grainCategory": "Base (Maris Otter)",
            "_timestamp": {
                "_seconds": 1642442569,
                "_nanoseconds": 359000000
            },
            "substitutes": "Pale Liquid Extract",
            "manufacturingDate": null,
            "inventory": 3.6,
            "diastaticPower": 120,
            "_version": "2.8.0",
            "removedFromInventory": true,
            "cgdb": null,
            "_rev": "iRgiYabSKl8guOtDe2sX6RDPwYFJgP",
            "protein": 9.4,
            "name": "Pale Malt, Maris Otter",
            "hidden": false,
            "notInRecipe": false,
            "potential": 1.03795,
            "displayAmount": 0,
            "color": 2.538071,
            "usedIn": "",
            "ibuPerAmount": null,
            "totalCost": 0,
            "userNotes": "",
            "lovibond": 2.4,
            "costPerAmount": 0,
            "fgdb": null,
            "coarseFineDiff": 1.5,
            "acid": 0,
            "fan": null,
            "checked": true,
            "notFermentable": false,
            "amount": 1.4,
            "bestBeforeDate": 1638313200000,
            "moisture": 3,
            "friability": null,
            "_timestamp_ms": 1642442569359,
            "potentialPercentage": 82.5,
            "_created": {
                "_seconds": 1615637669,
                "_nanoseconds": 272000000
            },
            "supplier": "Thomas Fawcett",
            "attenuation": 0.81,
            "_id": "default-33db684",
            "removedAmount": 1.4,
            "maxInBatch": 100
        },
        {
            "friability": null,
            "costPerAmount": 0,
            "usedIn": "",
            "inventory": 0.77,
            "_version": "2.8.0",
            "color": 3.553299,
            "protein": null,
            "fgdb": 81,
            "_id": "default-a2fddf6",
            "removedFromInventory": true,
            "_created": {
                "_seconds": 1642621026,
                "_nanoseconds": 568000000
            },
            "attenuation": 0.74,
            "totalCost": 0,
            "cgdb": null,
            "_timestamp_ms": 1642621026568,
            "displayAmount": 0,
            "coarseFineDiff": 1,
            "potentialPercentage": 75.2,
            "hidden": false,
            "bestBeforeDate": 1669590000000,
            "notInRecipe": false,
            "notFermentable": false,
            "checked": true,
            "supplier": "Weyermann",
            "diastaticPower": null,
            "substitutes": "",
            "_rev": "WEVk7UKvYu61o6hc5rzDZwjgtgtgRK",
            "removedAmount": 0.23,
            "userNotes": "",
            "manufacturingDate": null,
            "name": "Pale Rye Malt",
            "type": "Grain",
            "notes": "Suitable for any pale or bright rye or specialty beers. Sensory: typical rye aroma, malty-sweet with notes of bread and honey. Rye malt also creates a velvety-soft mouthfeel.",
            "grainCategory": "Base",
            "_timestamp": {
                "_seconds": 1642621026,
                "_nanoseconds": 568000000
            },
            "moisture": 6,
            "acid": null,
            "lovibond": 3.2,
            "amount": 0.23,
            "origin": "Germany",
            "maxInBatch": 60,
            "fan": null,
            "potential": 1.035
        },
        {
            "removedFromInventory": true,
            "maxInBatch": null,
            "origin": "Poland",
            "potentialPercentage": 70,
            "_version": "2.8.0",
            "_rev": "qgkxawipURieRdJddZSmy8x4nNDJPP",
            "checked": true,
            "_created": {
                "_seconds": 1642621125,
                "_nanoseconds": 65000000
            },
            "supplier": "Viking Malt",
            "removedAmount": 0.06,
            "acid": null,
            "hidden": false,
            "totalCost": 0,
            "coarseFineDiff": null,
            "ibuPerAmount": null,
            "bestBeforeDate": 1650751200000,
            "_timestamp_ms": 1642621125065,
            "type": "Grain",
            "userNotes": "Eigenlijk van Brewferm 1000-1300 ebc",
            "friability": null,
            "fan": null,
            "_id": "default-acecc92",
            "potential": 1.0322,
            "name": "Roasted Barley",
            "usedIn": "",
            "inventory": 0.94,
            "cgdb": null,
            "_timestamp": {
                "_seconds": 1642621125,
                "_nanoseconds": 65000000
            },
            "notes": "Roasted barley is produced from malting barley. The enzymatic activity is zero. Fermentable extract is low. Typical flavor is burnt and roasted.",
            "color": 558.3756345,
            "attenuation": 0.15,
            "substitutes": "",
            "diastaticPower": null,
            "costPerAmount": 0,
            "manufacturingDate": null,
            "displayAmount": 0,
            "grainCategory": "Roasted",
            "notInRecipe": false,
            "fgdb": null,
            "protein": null,
            "amount": 0.06,
            "notFermentable": false,
            "moisture": null
        }
    ],
    "batchNotes": "1.3 liter water bij de kook gedaan, verdunt zodat pre boil sg naar 1.05 gaat (van 1.053)",
    "batchYeastsLocal": [],
    "batchFermentablesLocal": [],
    "estimatedOg": 1.053,
    "measuredKettleEfficiency": 73.22,
    "_type": "batch",
    "measuredMashEfficiency": 72.93,
    "batchMiscs": [
        {
            "totalCost": 0,
            "_version": "2.8.0",
            "costPerAmount": 0,
            "inventory": -22.816,
            "_timestamp": {
                "_seconds": 1638519934,
                "_nanoseconds": 933000000
            },
            "amount": 1.4,
            "_id": "default-1f88df",
            "use": "Mash",
            "checked": true,
            "type": "Water Agent",
            "_rev": "3dh2lFum6hVrf6zJPuqQTCOWa9aKGC",
            "notInRecipe": false,
            "displayAmount": 0,
            "_created": {
                "_seconds": 1592121511,
                "_nanoseconds": 471000000
            },
            "removedAmount": 1.4,
            "removedUnit": "g",
            "_timestamp_ms": 1638519934933,
            "unit": "g",
            "inventoryUnit": "g",
            "hidden": false,
            "time": null,
            "waterAdjustment": true,
            "removedFromInventory": true,
            "timeIsDays": false,
            "name": "Gypsum (CaSO4)"
        },
        {
            "name": "Calcium Chloride (CaCl2)",
            "unit": "g",
            "_id": "default-3b1827",
            "inventory": -55.376,
            "_version": "2.8.0",
            "removedAmount": 4,
            "costPerAmount": 0,
            "_created": {
                "_seconds": 1592121510,
                "_nanoseconds": 390000000
            },
            "removedUnit": "g",
            "hidden": false,
            "_timestamp_ms": 1638520692376,
            "type": "Water Agent",
            "displayAmount": 0,
            "_timestamp": {
                "_seconds": 1638520692,
                "_nanoseconds": 376000000
            },
            "waterAdjustment": true,
            "totalCost": 0,
            "timeIsDays": false,
            "use": "Mash",
            "_rev": "GjmGAk0CkMh3vWUrQDbxscKpSZW8zZ",
            "removedFromInventory": true,
            "notInRecipe": false,
            "checked": true,
            "time": null,
            "inventoryUnit": "g",
            "amount": 4
        },
        {
            "removedFromInventory": true,
            "_version": "2.8.0",
            "timeIsDays": false,
            "hidden": false,
            "_rev": "aLR6FYpVDzqk714i3FeppvpWLbSYrm",
            "time": null,
            "inventory": -16.464,
            "_created": {
                "_seconds": 1592121509,
                "_nanoseconds": 704000000
            },
            "checked": true,
            "totalCost": 0,
            "notInRecipe": false,
            "unit": "g",
            "removedUnit": "g",
            "costPerAmount": 0,
            "inventoryUnit": "g",
            "amount": 2.1,
            "waterAdjustment": true,
            "removedAmount": 2.1,
            "_timestamp": {
                "_seconds": 1638520005,
                "_nanoseconds": 445000000
            },
            "name": "Epsom Salt (MgSO4)",
            "_id": "default-4e9d62",
            "displayAmount": 0,
            "use": "Mash",
            "type": "Water Agent",
            "_timestamp_ms": 1638520005445
        },
        {
            "removedAmount": 1.1,
            "_version": "2.8.0",
            "inventory": -14.58,
            "use": "Mash",
            "_id": "default-bk9j78",
            "totalCost": 0,
            "hidden": false,
            "name": "Canning Salt (NaCl)",
            "removedFromInventory": true,
            "removedUnit": "g",
            "unit": "g",
            "_rev": "2AFEvMJdsQrHMIrjOg21dcKfuOl0yI",
            "waterAdjustment": true,
            "costPerAmount": 0,
            "_timestamp": {
                "_seconds": 1638520484,
                "_nanoseconds": 285000000
            },
            "time": null,
            "_created": {
                "_seconds": 1594461222,
                "_nanoseconds": 957000000
            },
            "amount": 1.1,
            "displayAmount": 0,
            "notInRecipe": false,
            "_timestamp_ms": 1638520484285,
            "type": "Water Agent",
            "checked": true,
            "inventoryUnit": "g",
            "timeIsDays": false
        }
    ],
    "estimatedFg": 1.013,
    "_timestamp_ms": 1642957959166,
    "fermentationStartDate": 1642806000000,
    "carbonationForce": 10.8,
    "cost": {
        "perBottlingLiter": 0.13,
        "miscs": 0,
        "yeasts": 0,
        "fermentablesShare": 0,
        "hopsShare": 1,
        "hops": 2.39,
        "total": 2.39,
        "miscsShare": 0,
        "fermentables": 0,
        "yeastsShare": 0
    },
    "estimatedBuGuRatio": 0.48,
    "bottlingDate": 1643842800000
}
"""

TESTDATA_BATCH_2 = r"""
{
    "_id": "BZFF1swDJnQWmkyzSEog28O2aIsZ12",
    "name": "Batch",
    "batchNo": 29,
    "status": "Fermenting",
    "brewer": "Steven Leadbeater",
    "brewDate": 1687561200000,
    "recipe": {
        "name": "Kolsch adjusted ",
        "fermentation": {
            "pressurized": true,
            "name": "Ale",
            "_id": "default",
            "steps": [
                {
                    "actualTime": 1687561200000,
                    "stepTemp": 17,
                    "displayPressure": 1,
                    "ramp": 3,
                    "displayStepTemp": 17,
                    "pressure": 14.503774,
                    "type": "Primary",
                    "stepTime": 10
                },
                {
                    "actualTime": 1688943600000,
                    "stepTemp": 20,
                    "actualRampTime": 1688684400000,
                    "displayPressure": null,
                    "ramp": 3,
                    "pressure": null,
                    "displayStepTemp": 20,
                    "stepTime": 3,
                    "type": "Primary"
                }
            ]
        }
    },
    "notes": [
        {
            "note": "",
            "type": "statusChanged",
            "timestamp": 1688232745570,
            "status": "Fermenting"
        },
        {
            "note": "",
            "type": "statusChanged",
            "timestamp": 1687609251831,
            "status": "Brewing"
        }
    ]
}
"""

TESTDATA_READINGS = r"""[
    {
        "temp": 22,
        "sg": null,
        "comment": "",
        "time": 1689162288098,
        "id": "manual",
        "type": "manual"
    },
    {
        "temp": 23,
        "sg": null,
        "comment": "",
        "time": 1689162288099,
        "id": "manual",
        "type": "manual"
    },
    {
        "temp": 21.9,
        "sg": null,
        "comment": "",
        "time": 1789162288099,
        "id": "manual",
        "type": "manual"
    },
    {
        "temp": 20.5,
        "sg": null,
        "comment": "",
        "time": 1589162288099,
        "id": "manual",
        "type": "manual"
    }
]"""

TESTDATA_BATCH_3 = r"""
{"_id":"tXyKX8BIL3jBVKT93g56UQ6VvWd9w1","name":"Batch","batchNo":34,"status":"Fermenting","brewer":"Jo H","brewDate":1733526000000,"recipe":{"name":"Kauk cerveza sour edition","fermentation":{"_id":"ROH9v0qw1fSb4toWwCSAigYpCpIScc","name":"Sour + novalager","steps":[{"actualTime":1733526000000,"pressure":0,"stepTemp":25,"displayPressure":0,"stepTime":1,"name":"Sour","type":"Primary","displayStepTemp":25,"ramp":null},{"name":"novalager","pressure":0,"actualTime":1733612400000,"ramp":0,"type":"Primary","stepTemp":18,"displayPressure":0,"displayStepTemp":18,"stepTime":5},{"actualTime":1734217200000,"name":"Diacetyl","displayStepTemp":19,"stepTime":2,"pressure":10.152642,"type":"Primary","ramp":2,"displayPressure":0.7,"stepTemp":19,"actualRampTime":1734044400000},{"stepTemp":2,"actualRampTime":1734390000000,"pressure":17.404529,"stepTime":2,"actualTime":1734735600000,"name":"Cold crash","type":"Cold Crash","displayPressure":1.2,"displayStepTemp":2,"ramp":4}],"pressurized":true}},"notes":[{"timestamp":1733580762888,"note":"","type":"statusChanged","status":"Fermenting"},{"timestamp":1733566571144,"note":"","type":"statusChanged","status":"Brewing"}]}
"""

TESTDATA_LAST_READINGS_1 = r"""
{"comment":"","id":"manual","type":"manual","temp":21,"sg":1.029,"time":1731236447317}
"""