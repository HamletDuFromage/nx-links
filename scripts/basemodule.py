from distutils.dir_util import copy_tree
from pathlib import Path
from github import Github
import urllib.request
import uuid, os, re
import zipfile
import shutil
import argparse
import glob


parser = argparse.ArgumentParser(description="Get links for AiO-Switch-Updater")
requiredNamed = parser.add_argument_group('Require arguments')
requiredNamed.add_argument('-gt', '--githubToken', help='Github Token', required=True)
args = parser.parse_args()

class Basemodule:
    def __init__(self, config):
        print("Init module: ", self.__module__)
        self.config = config
        self.uuid = ""
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
    
