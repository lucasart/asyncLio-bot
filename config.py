import logging
import yaml

logger = logging.getLogger(__name__)

CONFIG = {}


def load_config(filename: str):
    with open(filename, "r") as config_file:
        try:
            config = yaml.safe_load(config_file)
        except Exception as e:
            logger.critical(f"Cannot parse {filename}.")
            raise e

    global CONFIG
    CONFIG.clear()
    CONFIG.update(config)
