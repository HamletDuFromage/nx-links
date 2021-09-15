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


class Cfws(Basemodule):
    def __init__(self, config):
        self.path = "cfws.json"
        Basemodule.__init__(self, config)

    def handleModule(self):
        out = {}

        for i in range(len(self.config)):
            release = self.getLatestRelease(i)
            assets = self.getAssetLinks(release, i)
            for a in assets:
                if config[i]["reponame"] not in out:
                    out[config[i]["reponame"]] = {}
                out[config[i]["reponame"]][a.name] = a.browser_download_url

        with open(self.path, 'w') as write_file:
            json.dump(out, write_file, indent=4)


package = Cfws(config)
