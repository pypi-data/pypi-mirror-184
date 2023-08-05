import sys
from pathlib import Path

import yaml

from . import opa


def run(argv=sys.argv):
    if len(argv) < 2:
        print("Usage: ib2influx config.yml")
    else:
        config_file = Path(argv[1])
        if config_file.is_file():
            with open(config_file, "r") as f:
                config = yaml.safe_load(f)
        else:
            raise FileNotFoundError

        opa.LoaderOPA(config)
