DOMAIN = "brewfather"
COORDINATOR = "coordinator"
CONNECTION_NAME = "connection_name"

UPDATE_INTERVAL = 3600

TEST_URI = "https://api.brewfather.app/v1/batches/"
BATCHES_URI = "https://api.brewfather.app/v1/batches/?status=Fermenting"
BATCH_URI = "https://api.brewfather.app/v1/batches/{}?include=recipe.fermentation,notes"
READINGS_URI = "https://api.brewfather.app/v1/batches/{}/readings"

DRY_RUN = False
