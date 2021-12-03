from pathlib import Path
from github import Github
import re
import argparse
import json

parser = argparse.ArgumentParser(
    description="Get links for AiO-Switch-Updater")
requiredNamed = parser.add_argument_group('Require arguments')
requiredNamed.add_argument('-gt', '--githubToken',
                           help='Github Token', required=True)
args = parser.parse_args()


class BaseModule:
    def __init__(self, config = {}):
        print("Init module: ", self.__module__)
        self.path = self.__module__ + ".json"
        self.out = {}
        self.handle_module()

    def get_latest_release(self, index):
        gh = Github(args.githubToken)
        if self.config[index]["service"] == 1:
            try:
                repo = gh.get_repo(
                    self.config[index]["username"] + "/" + self.config[index]["reponame"])
            except:
                print("Unable to get: ",
                      self.config[index]["username"], "/", self.config[index]["reponame"])
                return None
            releases = repo.get_releases()
            if releases.totalCount == 0:
                print("No available releases for: ",
                      self.config[index]["username"], "/", self.config[index]["reponame"])
                return None
            for release in releases:
                if not release.prerelease:
                    return release
            return releases[0]

    def get_asset_link(self, release, index):
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

    def get_asset_links(self, release, index):
        assetPaths = []
        for pattern in self.config[index]["assetPatterns"]:
            self.config[index]["assetRegex"] = pattern
            assetPaths += self.get_asset_link(release, index)
        return assetPaths

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            try:
                assets = self.get_asset_links(release, i)
            except TypeError:
                print(f"In {self.config[i]['reponame']}: TypeError")
                return
            for a in assets:
                self.out[a.name] = a.browser_download_url

    def write_json(self):
        with open(self.path, 'w') as write_file:
            json.dump(self.out, write_file, indent=4)
