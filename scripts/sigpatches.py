from basemodule import BaseModule


class Sigpatches(BaseModule):
    def __init__(self):
        self.config = [
            {
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
            for asset in assets:
                self.out[release.title] = asset.browser_download_url