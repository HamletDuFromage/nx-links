from basemodule import Basemodule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()

config = [
    {  
        "service": 1,
        "username": "Atmosphere-NX",
        "reponame": "Atmosphere",
        "assetRegex": "",
        "assetPatterns": [".*atmosphere.*\\.zip"]
    },
    {
        "service": 1,
        "username": "Team-Neptune",
        "reponame": "DeepSea",
        "assetRegex": "",
        "assetPatterns": [".*deepsea.*\\.zip"]
    }
]

class Atmosphere(Basemodule):
    def __init__(self, config):
        self.path = "ams.json"
        Basemodule.__init__(self, config)

package = Atmosphere(config)