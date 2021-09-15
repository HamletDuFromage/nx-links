from basemodule import Basemodule
from pathlib import Path
import configparser
import os
import json
parser = configparser.ConfigParser()

config = [
    {
        "service": 1,
        "username": "ITotalJustice",
        "reponame": "patches",
        "assetRegex": "",
        "assetPatterns": [".*hekate.*\\.zip", ".*fusee.*\\.zip"]
    }
]


class Sigpatches(Basemodule):
    def __init__(self, config):
        self.path = "sigpatches.json"
        Basemodule.__init__(self, config)

    def handleModule(self):
        out = {}
        path = "sigpatches.json"

        for i in range(len(config)):
            release = self.getLatestRelease(i)
            assets = self.getAssetLinks(release, i)
            for a in assets:
                out[a.name + " | " + release.title] = a.browser_download_url

        with open(path, 'w') as write_file:
            json.dump(out, write_file, indent=4)


package = Sigpatches(config)
