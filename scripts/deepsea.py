from basemodule import Basemodule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()

config = [
    {
        "service": 1,
        "username": "Team-Neptune",
        "reponame": "DeepSea",
        "assetRegex": "",
        "assetPatterns": [".*deepsea.*\\.zip"]
    }
]


class Deepsea(Basemodule):
    def __init__(self, config):
        self.path = "deepsea.json"
        Basemodule.__init__(self, config)


package = Deepsea(config)
