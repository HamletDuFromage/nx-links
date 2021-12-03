from bs4 import BeautifulSoup
import requests
import internetarchive as ia
import regex as re
import urllib.parse
import json

class Firmwares():
    def __init__(self):
        self.collections = [
            {"title": "nintendo-switch-global-firmwares", "prefix": ""},
            {"title": "nintendo-switch-china-firmwares", "prefix": "[China Firmware] "}
        ]
        self.path = "firmwares.json"
        self.url = "https://archive.org/download/"
        self.handleModule()

    def sort_firmwares(self, file):
        match = re.match(r"Firmware ([\d\.]+).*\.zip", file["name"])
        res = 0
        if match:
            ver = match[1].split(".")
            for i in range(len(ver)):
                res += (100**(len(ver) -1 - i)) * int(ver[i])
        else:
            res = 0
        return res

    def handleModule(self):
        print("Init module: ", self.__module__)
        out = {}
        for collection in self.collections:
            item = ia.get_item(collection["title"])
            #files = sorted(item.files, key=lambda d: d.get("mtime", "0"), reverse=True)
            files = sorted(item.files, key=self.sort_firmwares, reverse=True)
            for file in files:
                match = re.match(r"(Firmware.+)\.zip", file["name"])
                if match:
                    download = self.url + collection["title"] + "/" + file['name']
                    out[collection["prefix"] + match[1]] = urllib.parse.quote(download, safe=":/")

        with open(self.path, 'w') as write_file:
            json.dump(out, write_file, indent=4, sort_keys=False)


package = Firmwares()
