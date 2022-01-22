import re
import requests
from random import choice
from bs4 import BeautifulSoup


class ScriptRequest:
    """this request gets the script from the episode"""

    def __init__(self, script):
        self.script = script
        self.request = None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }

        try:
            url = f"https://www.seinfeldscripts.com/{self.script}.html"
            self.response = requests.get(url=url, headers=headers)
            self.response.raise_for_status()

        # if the block above fails
        except requests.HTTPError:

            url = f"https://www.seinfeldscripts.com/{self.script}.htm"
            self.response = requests.get(url=url, headers=headers)

    def get_script(self):
        """get the script of the episode"""
        soup = BeautifulSoup(self.response.text, "html.parser")
        return soup


class RandomQuote:
    """random quote from character's lines"""

    def __init__(self, script, name):
        self.script = script
        self.name = name

    # since the scripts have two ways of formatting the name (NAME and Name) we need two formatted names
    def double_name(self):
        """we get the uppercase and the capitalized version of the name """

        upper_name = self.name.upper()
        title_name = self.name.title()

        return upper_name, title_name

    def get_quote(self):
        """check the version of the name that is compatible with the script and get one random quote"""

        upper_name, title_name = self.double_name()
        # here we use "r" for regex and "f" for f-strings
        # https://stackoverflow.com/questions/8194470/python-regex-with-look-behind-and-alternatives
        pattern = re.compile(fr"(?<={upper_name}:).*|(?<={title_name}).*", re.DOTALL)
        quotes = self.script.find_all(text=pattern)

        # this is a list of quotes
        quotes = [re.findall(pattern, quote) for quote in quotes]
        quotes = [quote[0].strip() for quote in quotes if len(quote[0].split()) >= 3]
        quote = choice(quotes)
        return quote
