from basemodule import BaseModule
import configparser
parser = configparser.ConfigParser()


class Bootloaders(BaseModule):
    def __init__(self):
        self.config = [
            {
                "service": 1,
                "username": "CTCaer",
                "reponame": "hekate",
                "assetRegex": "",
                "assetPatterns": [".*hekate_ctcaer.*\\.zip"]
            },
            {
                "service": 1,
                "username": "Guillem96",
                "reponame": "argon-nx",
                "assetRegex": "",
                "assetPatterns": [".*argon-nx.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)
