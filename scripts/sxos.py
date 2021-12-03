from bs4 import BeautifulSoup
import requests
import json

url = "https://sx.xecuter.com/#prod-sxos"


class SXOS():
    def __init__(self):
        self.path = "sxos.json"
        self.handle_module()

    def fetch_sxos_links(self, url):
        try:
            page = requests.get(url)
            page.raise_for_status()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.HTTPError):
            print("sx.xecuter.com is down")
            return None

        soup = BeautifulSoup(page.content, "html.parser")
        section = soup.find("section", {"id": "download"}).find_all("a")
        # print(section[0])
        titles = [None] * 2
        links = [None] * 2
        for i in range(2):
            # https://sx.xecuter.com/download/SXOS_beta_v3.0.5.zip
            links[i] = f"https://sx.xecuter.com/{str(section[i].get('href'))[2:]}"
            titles[i] = str(section[i].contents[1]).replace("download ", "")
        return [titles, links]

    def handle_module(self):
        print("Init module: ", self.__module__)
        out = {}
        res = self.fetch_sxos_links(url)
        if (res is not None):
            for i in range(len(res[0])):
                title = res[0][i]
                link = res[1][i]
                out[title] = link

        with open(self.path, 'w') as write_file:
            json.dump(out, write_file, indent=4)


package = SXOS()
