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
        release = self.get_latest_release(0)
        assets = self.get_asset_links(release, self.config[0]["assetPatterns"][0])
        self.out[release.title] = asset[0].browser_download_url
        self.out["version"] = release.tag_name
