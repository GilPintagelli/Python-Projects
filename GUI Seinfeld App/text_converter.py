import re


class TextConverter:

    def __init__(self, ep):
        self.ep = ep

    def new_text(self):
        string = re.sub(r'[\n]', '', self.ep)
        # this is evaluated as true if the string has a number and false if it doesn't
        if re.findall(r'\d',string):
            string = string.split()
            string = [word.title() for word in string]
            string = "-".join(string)
            string = re.sub(r"[()]",'',string)
            return string
        string = string.split()
        string = [word.title() for word in string]
        return "".join(string)