from pathlib import Path
from github import Github
import urllib.request
import re
import argparse

import json

parser = argparse.ArgumentParser(description="Get links for AiO-Switch-Updater")
requiredNamed = parser.add_argument_group('Require arguments')
requiredNamed.add_argument('-gt', '--githubToken', help='Github Token', required=True)
args = parser.parse_args()

class Basemodule:
    def __init__(self, config):
        print("Init module: ", self.__module__)
        self.config = config
        self.handleModule()

    def getLatestRelease(self, index):
            gh = Github(args.githubToken)
            if self.config[index]["service"] == 1:
                try:
                    repo = gh.get_repo(self.config[index]["username"] + "/" + self.config[index]["reponame"])
                except:
                    print("Unable to get: ", self.config[index]["username"], "/", self.config[index]["reponame"])
                    return None
                releases = repo.get_releases()
                if releases.totalCount == 0:
                    print("No available releases for: ", self.config[index]["username"], "/", self.config[index]["reponame"])
                    return None
                return releases[0]

    def getAssetLink(self, release, index):
        pattern = self.config[index]["assetRegex"]
        assets = []
        if self.config[index]["service"] == 1:
            if release is None:
                return None
            for asset in release.get_assets():
                matched_asset = None
                if re.search(pattern, asset.name):
                    matched_asset = asset
                if matched_asset is not None:
                    assets.append(matched_asset)
            return assets

    def getAssetLinks(self, release, index):
        assetPaths = []
        for pattern in self.config[index]["assetPatterns"]:
            self.config[index]["assetRegex"] = pattern
            assetPaths += self.getAssetLink(release, index)
        return assetPaths

    def handleModule(self):
        out = {}

        for i in range(len(self.config)):
            release = self.getLatestRelease(i)
            assets = self.getAssetLinks(release, i)
            for a in assets:
                out[a.name] = a.browser_download_url

        change = False
        try:
            with open(self.path, 'r') as read_file:
                old = json.load(read_file)
            if old != out:
                print(f"{self.path} changed")
                change = True
        except FileNotFoundError:
            print(f"error: FileNotFoundError ({self.path})")
            change = True

        if(change):
            with open(self.path, 'w') as write_file:
                json.dump(out, write_file, indent=4)
            print(f"Updated {self.path}")

