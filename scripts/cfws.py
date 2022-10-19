from basemodule import BaseModule


class Cfws(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "Atmosphere-NX",
                "reponame": "Atmosphere",
                "assetPatterns": [".*atmosphere.*\\.zip"]
            },
            {
                "username": "Atmosphere-NX",
                "reponame": "Atmosphere",
                "prerelease": True,
                "assetPatterns": [".*atmosphere.*\\.zip"]
            },
            {
                "username": "Team-Neptune",
                "reponame": "DeepSea",
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
                name = a[1] * "[pre-release] " + a[0].name
                self.out[self.config[i]["reponame"]][name] = a[0].browser_download_url
