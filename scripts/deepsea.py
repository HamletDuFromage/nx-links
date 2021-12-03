from basemodule import BaseModule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()


class Deepsea(BaseModule):
    def __init__(self):
        self.config = [
            {
                "service": 1,
                "username": "Team-Neptune",
                "reponame": "DeepSea",
                "assetRegex": "",
                "assetPatterns": [".*deepsea.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)
