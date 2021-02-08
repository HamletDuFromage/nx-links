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
        Basemodule.__init__(self, config)

    def handleModule(self):
        out = {}
        path = "payloads.json"
        
        for i in range(len(config)):
            release = self.getLatestRelease(i)
            assets = self.getAssetLinks(release, i)
            for a in assets:
                out[a.name] = a.browser_download_url

        change = False
        try:
            with open(path, 'r') as read_file:
                old = json.load(read_file)
                if(json.dumps(old) != json.dumps(out)):
                    print(path + " changed")
                    change = True
        except FileNotFoundError:
            print("File doesn't exist")
            change = True

        if(change):
            with open(path, 'w') as write_file:
                json.dump(out, write_file)
            print("Updated " + path)

package = payloads(config)