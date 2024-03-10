import logging.config
import logging.handlers
import pathlib
import json


def setup_logging(file_name: str = "../logs/logging-config.json"):
    try:
        config_file = pathlib.Path(file_name)
        if not config_file.exists():
            raise FileNotFoundError(f"The file '{file_name}' was not found.")

        with config_file.open(mode='r') as f_in:
            config = json.load(f_in)
        logging.config.dictConfig(config)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found in the same directory as the script.")
        return None


setup_logging()
LOGGER = logging.getLogger('sport-booker')


