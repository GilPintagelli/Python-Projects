from tkinter import Tk, Label, PhotoImage, Button, Canvas
from random import choice


class Interface:
    """tkinter interface"""

    def __init__(self, character):
        self.character = character

        self.bg = ["#FFC600", "#B3541E", "#548CFF", "#95CD41"]
        random_color = choice(self.bg)

        self.window = Tk()
        self.window.title("Seinfeld quotes")
        self.window.minsize(width=300, height=300)
        self.window.config(pady=30, padx=30, bg=random_color)

        # LABEL
        self.character_name = Label(text=self.character.name, font=("Arial", 25), highlightthickness=0, bg=random_color,
                                    foreground="white")
        self.character_name.grid(column=1, row=0)

        # BUTTON
        button_img = PhotoImage(file=f"./resources/{self.character.name.lower()}_button.png")
        self.character_button = Button(image=button_img, borderwidth=0, highlightthickness=0,
                                       activebackground=random_color, background=random_color, command=self.quote)
        self.character_button.grid(column=1, row=1, pady=15)

        # CANVAS TEXT
        self.canvas = Canvas(width=300, height=170, highlightthickness=0, bg=random_color)
        self.character_quote = self.canvas.create_text(150, 80, text="", width=300, font=("Arial", 16,),
                                                       fill="white")
        self.canvas.grid(column=1, row=2)
        self.quote()

        self.window.mainloop()

    def quote(self):
        # here "character" is an object of RandomQuote() --> e.g. RandomQuote(script, "jerry")
        # RandomQuote(script, "jerry") has a script from which we can get the quote
        # we just use a method from RandomQuote()
        quote = self.character.get_quote()
        # BUG: the quote is full of \n
        self.canvas.itemconfig(self.character_quote, text=quote.strip())
