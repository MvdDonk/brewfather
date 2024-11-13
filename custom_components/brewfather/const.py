DOMAIN = "brewfather"
COORDINATOR = "coordinator"

UPDATE_INTERVAL = 900 #15 minutes
MS_IN_DAY = 86400000

TEST_URI = "https://api.brewfather.app/v2/batches/"
BATCHES_URI = "https://api.brewfather.app/v2/batches/?status=Fermenting"
BATCH_URI = "https://api.brewfather.app/v2/batches/{}?include=recipe.fermentation,notes,measuredOg"
READINGS_URI = "https://api.brewfather.app/v2/batches/{}/readings"
LAST_READING_URI = "https://api.brewfather.app/v2/batches/{}/readings/last"

DRY_RUN = False
CONF_RAMP_TEMP_CORRECTION = "ramp_temp_correction"

VERSION_MAJOR = 1
VERSION_MINOR = 2