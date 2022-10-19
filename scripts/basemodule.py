from github import Github, GithubException
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
    def __init__(self, config={}):
        print("Init module: ", self.__module__)
        self.path = self.__module__ + ".json"
        self.out = {}
        self.handle_module()

    def get_latest_release(self, index):
        gh = Github(args.githubToken)
        try:
            repo = gh.get_repo(
                self.config[index]["username"] + "/" + self.config[index]["reponame"])
        except GithubException:
            print("Unable to get: ",
                  self.config[index]["username"], "/", self.config[index]["reponame"])
            return None
        releases = repo.get_releases()
        if releases.totalCount == 0:
            print("No available releases for: ",
                  self.config[index]["username"], "/", self.config[index]["reponame"])
            return None
        if self.config[index].get("prerelease", False) == False:
            for release in releases:
                if not release.prerelease:
                    return release
        return releases[0]

    def get_asset_link(self, release, pattern):
        assets = []
        for asset in release.get_assets():
            if re.search(pattern, asset.name):
                assets.append((asset, release.prerelease))
        return assets

    def get_asset_links(self, release, index):
        assetPaths = []
        if release is not None:
            for pattern in self.config[index]["assetPatterns"]:
                assetPaths += self.get_asset_link(release, pattern)
        return assetPaths

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for a in assets:
                name = a[1] * "[pre-release] " + a[0].name
                self.out[name] = a[0].browser_download_url

    def write_json(self):
        with open(self.path, 'w') as write_file:
            json.dump(self.out, write_file, indent=4)
