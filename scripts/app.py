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
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["AtmoPackUpdater"] = asset[0].browser_download_url
        self.out["version"] = release.tag_name
