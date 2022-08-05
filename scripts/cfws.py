from basemodule import BaseModule

class Cfws(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "THZoria",
                "reponame": "AtmoPack-Vanilla",
                "assetPatterns": [".*AtmoPack-Vanilla_Latest.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for asset in assets:
                self.out[release.title] = asset.browser_download_url
            self.out["version"] = release.tag_name
