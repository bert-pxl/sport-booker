import logging.config
import logging.handlers
import pathlib
import json


def setup_logging():
    config_file = pathlib.Path("logging-config.json")
    with config_file.open(mode='r') as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)


setup_logging()
logger = logging.getLogger('sport-booker')


