from basemodule import BaseModule


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
