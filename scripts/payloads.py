from basemodule import BaseModule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()


class Payloads(BaseModule):
    def __init__(self):
        self.config = [
            {
                "service": 1,
                "username": "Atmosphere-NX",
                "reponame": "Atmosphere",
                "assetRegex": "",
                "assetPatterns": [".*fusee.*\\.bin"]
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
        BaseModule.__init__(self)
