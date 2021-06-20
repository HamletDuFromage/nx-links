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
        "assetPatterns": [".*fusee-primary.*\\.bin"]
    },
    {
        "service": 1,
        "username": "shchmue",
        "reponame": "Lockpick_RCM",
        "assetRegex": "",
        "assetPatterns": [".*Lockpick_RCM.*\\.bin"]
    },
    {
        "service": 1,
        "username": "suchmememanyskill",
        "reponame": "TegraExplorer",
        "assetRegex": "",
        "assetPatterns": [".*TegraExplorer.*\\.bin"]
    },
    {
        "service": 1,
        "username": "jimzrt",
        "reponame": "Incognito_RCM",
        "assetRegex": "",
        "assetPatterns": [".* Incognito_RCM.*\\.bin"]
    }
]

class payloads(Basemodule):
    def __init__(self, config):
        self.path = "payloads.json"
        Basemodule.__init__(self, config)

package = payloads(config)