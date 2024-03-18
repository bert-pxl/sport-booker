import logging.config
import sys
import pathlib

output_file = 'sport-booker.log'
logger_name = 'sport-booker'

simple_formatter = logging.Formatter("%(levelname)s: %(message)s")
detailed_formatter = logging.Formatter("[%(levelname)s|%(module)s|L%(lineno)d] %(asctime)s: %(message)s",
                                       datefmt="%Y-%m-%dT%H:%M:%S%z")
logger = logging.getLogger(logger_name)

if not logger.handlers:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(simple_formatter)
    location_output_file = pathlib.Path(__file__).resolve().parent / output_file
    file_handler = logging.handlers.RotatingFileHandler(filename=location_output_file, maxBytes=100000, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
