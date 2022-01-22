import requests
from random import choice
from bs4 import BeautifulSoup


class ListEp:
    """get all the titles"""

    def __init__(self):

        url = f"https://www.seinfeldscripts.com/seinfeld-scripts.html"

        headers = {
            # http://myhttpheader.com/
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # here we get the list of episodes
        episodes = soup.select(selector="td a")[:-1]
        # we want to use this list, so we give it a self
        self.episodes = [episode.string for episode in episodes]

    def random_episode(self):
        """get random episode from the list of episodes"""

        return choice(self.episodes)
