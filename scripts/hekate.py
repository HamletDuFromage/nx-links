from basemodule import Basemodule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()

config = [
    {
        "service": 1,
        "username": "CTCaer",
        "reponame": "hekate",
        "assetRegex": "",
        "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
    }
]


class hekate(Basemodule):
    def __init__(self, config):
        self.path = "hekate.json"
        Basemodule.__init__(self, config)


package = hekate(config)
