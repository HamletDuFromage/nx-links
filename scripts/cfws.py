from basemodule import BaseModule
import configparser


class Cfws(BaseModule):
    def __init__(self):
        self.config = [
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
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for a in assets:
                if self.config[i]["reponame"] not in self.out:
                    self.out[self.config[i]["reponame"]] = {}
                self.out[self.config[i]["reponame"]
                         ][a.name] = a.browser_download_url
