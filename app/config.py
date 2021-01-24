from os import environ

DEBUG: bool = True if environ.get("DEBUG") == "true" else False

LINE_CHANNEL_SECRET: str = environ.get(
    "LINE_CHANNEL_SECRET", "LINE_CHANNEL_SECRET"
)
LINE_CHANNEL_TOKEN: str = environ.get(
    "LINE_CHANNEL_TOKEN", "LINE_CHANNEL_TOKEN"
)
