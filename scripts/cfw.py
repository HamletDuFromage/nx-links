from basemodule import Basemodule
from pathlib import Path
import configparser
import os
parser = configparser.ConfigParser()

config = [
    {  
        "service": 1,
        "username": "CTCaer",
        "reponame": "hekate",
        "assetRegex": "",
        "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
    },
    {
        "service": 1,
        "username": "Guillem96",
        "reponame": "argon-nx",
        "assetRegex": "",
        "assetPatterns": [".*argon-nx.*\\.zip"]
    },
    {
        "service": 1,
        "username": "Reisyukaku",
        "reponame": "ReiNX",
        "assetRegex": "",
        "assetPatterns": [".*ReiNX.*\\.zip"]
    }
]

class CFW(Basemodule):
    def __init__(self, config):
        self.path = "cfw.json"
        Basemodule.__init__(self, config)

package = CFW(config)