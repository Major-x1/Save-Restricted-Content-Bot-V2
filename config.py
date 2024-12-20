# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24828869"))
API_HASH = getenv("API_HASH", "3b0dce801ac887dca64ca774a0f2e421")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1801203400").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://arupmondalofficial007:WLmgnUK3qUShlQBj@cluster0.pr055.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4654199868")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002191627636"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BQFxJpUAO7O7eS99vAcaDX3Qf9lATtupVb51P3EyXYvch2oIovog0kGQwULO6AkipwW4Ns8DfjEdqwaDJb0kRYtd_uytyzuIXMXeEPcSlTR2iE8BAMN-qc1tqLGIU4zsjcLP1j1QYXSa1DBzmo8rTkRCBNCTTclydQL5v9-sW713uTVAu56MC6i-s2Vt1ELYJ6aMal8xbfICikQmXkXfj7bjTMPommjLwrlGJh3EZn2Ua2DjjTQorL5SyCghrXFIdh85BUvcjEZt_ZMqec7K8fqf9lyh4K5mV-_RVBTw5L8WwmQ9hv2L4gNQpHImcoJ4t7d63MfOClC_HeOF-fHdCygkwEJzUwAAAABrXC7IAA")
