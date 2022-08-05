from basemodule import BaseModule


class Bootloaders(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "CTCaer",
                "reponame": "hekate",
                "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
            },
            {
                "username": "Guillem96",
                "reponame": "argon-nx",
                "assetPatterns": [".*argon-nx.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)
