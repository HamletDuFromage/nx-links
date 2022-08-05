from basemodule import BaseModule

class App(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "PoloNX",
                "reponame": "AtmoPackUpdater",
                "assetPatterns": [".*AtmoPackUpdater.*\\.nro"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for asset in assets:
                self.out[release.title] = asset.browser_download_url
