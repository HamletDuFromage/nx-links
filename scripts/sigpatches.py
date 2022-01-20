from basemodule import BaseModule
from pathlib import Path

class Sigpatches(BaseModule):
    def __init__(self):
        self.config = [
            {
                "service": 1,
                "username": "ITotalJustice",
                "reponame": "patches",
                "assetRegex": "",
                "assetPatterns": [".*SigPatches.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for a in assets:
                self.out[a.name + " | " +
                         release.title] = a.browser_download_url
