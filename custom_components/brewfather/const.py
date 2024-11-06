DOMAIN = "brewfather"
COORDINATOR = "coordinator"
CONNECTION_NAME = "connection_name"

UPDATE_INTERVAL = 3600
MS_IN_DAY = 86400000

TEST_URI = "https://api.brewfather.app/v2/batches/"
BATCHES_URI = "https://api.brewfather.app/v2/batches/?status=Fermenting"
BATCH_URI = "https://api.brewfather.app/v2/batches/{}?include=recipe.fermentation,notes,measuredOg"
READINGS_URI = "https://api.brewfather.app/v2/batches/{}/readings"

DRY_RUN = False