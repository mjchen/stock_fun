import sys


import os
import logging.config
import yaml
import shared.resources

log_path = os.path.dirname(shared.resources.__file__)

def setup_logging(
    default_path = os.path.join(log_path,'logging.yaml'),
    default_level=logging.DEBUG,
    env_key='LOG_CFG'
):
    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()