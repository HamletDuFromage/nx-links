import internetarchive as ia
import re
from basemodule import BaseModule
import urllib.parse

class Firmwares(BaseModule):
    def __init__(self):
        self.collections = [
            {"title": "nintendo-switch-global-firmwares", "prefix": ""},
            {"title": "nintendo-switch-china-firmwares",
                "prefix": "[China Firmware] "}
        ]
        self.url = "https://archive.org/download/"
        BaseModule.__init__(self)

    def sort_firmwares(self, file):
        match = re.match(r"Firmware ([\d\.]+).*\.zip", file["name"])
        res = 0
        if match:
            ver = match[1].split(".")
            for i in range(len(ver)):
                res += (100**(len(ver) - 1 - i)) * int(ver[i])
        else:
            res = 0
        return res

    def handle_module(self):
        for collection in self.collections:
            item = ia.get_item(collection["title"])
            #files = sorted(item.files, key=lambda d: d.get("mtime", "0"), reverse=True)
            files = sorted(item.files, key=self.sort_firmwares, reverse=True)
            for file in files:
                match = re.match(r"(Firmware.+)\.zip", file["name"])
                if match:
                    download = self.url + \
                        collection["title"] + "/" + file['name']
                    self.out[collection["prefix"] + match[1]
                             ] = urllib.parse.quote(download, safe=":/")
