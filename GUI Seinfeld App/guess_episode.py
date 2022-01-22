class GuessEp:

    def __init__(self, episode):
        self.ep = episode

    def user_guess(self):
        user_input = input("Waht episode is this quote from? ")
        if user_input.lower() == self.ep.lower():
            print("That's right,")
        else:
            print("No, I'm sorry")
        return print(f"the episode is {self.ep}")