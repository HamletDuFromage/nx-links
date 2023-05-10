import re
from basemodule import BaseModule

class Firmwares(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "THZoria",
                "reponame": "NX_Firmware",
                "assetPatterns": [".*Firmware.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_releases(i)
            for j in range(release.totalCount):
                assets = self.get_asset_links(release[j], i)
                for asset in assets:
                    self.out[release[j].title] = asset.browser_download_url
