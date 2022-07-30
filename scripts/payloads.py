from basemodule import BaseModule


class Payloads(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "Atmosphere-NX",
                "reponame": "Atmosphere",
                "assetRegex": "",
                "assetPatterns": [".*fusee.*\\.bin"]
            },
            {
                "username": "shchmue",
                "reponame": "Lockpick_RCM",
                "assetRegex": "",
                "assetPatterns": [".*Lockpick_RCM.*\\.bin"]
            },
            {
                "username": "suchmememanyskill",
                "reponame": "TegraExplorer",
                "assetRegex": "",
                "assetPatterns": [".*TegraExplorer.*\\.bin"]
            }
        ]
        BaseModule.__init__(self)
