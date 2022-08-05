from basemodule import BaseModule


class Sigpatches(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "PHRetroGamers",
                "reponame": "signature_gpd",
                "assetPatterns": [".*signature_gpd.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        release = self.get_latest_release(0)
        assets = self.get_asset_links(release, self.config[0]["assetPatterns"][0])
        self.out[release.title] = asset[0].browser_download_url
        self.out["version"] = release.tag_name