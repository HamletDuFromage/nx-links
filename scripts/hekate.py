from basemodule import BaseModule


class Hekate(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "CTCaer",
                "reponame": "hekate",
                "assetRegex": "",
                "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)
