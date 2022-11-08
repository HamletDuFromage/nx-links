""" 
import internetarchive as ia
import re
from basemodule import BaseModule
import urllib.parse

class Firmwares(BaseModule):
    def __init__(self):
        self.collections = [
            {"title": "nintendo-switch-global-firmwares", "prefix": ""},
            {"title": "nintendo-switch-china-firmwares",
                "prefix": "[China Firmware] "}
        ]
        self.url = "https://archive.org/download/"
        BaseModule.__init__(self)

    def sort_firmwares(self, file):
        match = re.match(r"Firmware ([\d\.]+).*\.zip", file["name"])
        res = 0
        if match:
            ver = match[1].split(".")
            for i in range(len(ver)):
                res += (100**(len(ver) - 1 - i)) * int(ver[i])
        else:
            res = 0
        return res

    def handle_module(self):
        for collection in self.collections:
            item = ia.get_item(collection["title"])
            #files = sorted(item.files, key=lambda d: d.get("mtime", "0"), reverse=True)
            files = sorted(item.files, key=self.sort_firmwares, reverse=True)
            for file in files:
                match = re.match(r"(Firmware.+)\.zip", file["name"])
                if match:
                    download = self.url + \
                        collection["title"] + "/" + file['name']
                    self.out[collection["prefix"] + match[1]
                             ] = urllib.parse.quote(download, safe=":/")
"""

from basemodule import BaseModule
from bs4 import BeautifulSoup
import requests

class Firmwares(BaseModule):
    def __init__(self):
        self.url = "https://darthsternie.net/switch-firmwares/"
        self.limit = 5
        BaseModule.__init__(self)

    def get_content(self, tag):
        return tag.contents[0]

    def handle_module(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        tables = soup.find_all("tbody")
        if tables != []:
            titles = list(
                map(self.get_content, (tables[0].find_all("td", {"class": "column-1"}))))
            links_archive = tables[0].find_all("td", {"class": "column-5"})
            links_mega = tables[0].find_all("td", {"class": "column-4"})
            for i in range(min(self.limit, len(titles))):
                if links_archive[i].find("a"):
                    self.out[f"[archive.org] {titles[i]}"] = links_archive[i].find("a").get("href")
                if links_mega[i].find("a"):
                    self.out[f"[mega.nz] {titles[i]}"] = links_mega[i].find("a").get("href")

            china_titles = list(
                map(self.get_content, tables[1].find_all("td", {"class": "column-1"})))
            china_links_archive = tables[1].find_all("td", {"class": "column-5"})
            china_links_mega = tables[1].find_all("td", {"class": "column-4"})
            for i in range(min(self.limit, len(china_titles))):
                if china_links_archive[i].find("a"):
                    self.out[f"[archive.org] [China fw] {china_titles[i]}"] = china_links_archive[i].find("a").get("href")
                if china_links_mega[i].find("a"):
                    self.out[f"[mega.nz] [China fw] {china_titles[i]}"] = china_links_mega[i].find("a").get("href")