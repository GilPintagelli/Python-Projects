from interface import Interface
from list_episodes import ListEp
from text_converter import TextConverter
from get_script import ScriptRequest, RandomQuote

# list of episodes
episodes = ListEp()
episode = episodes.random_episode()
formatted_episode = TextConverter(episode).new_text()
script_request = ScriptRequest(script="TheMango")
# script_request = ScriptRequest(script=formatted_episode)

script = script_request.get_script()
character = RandomQuote(script, input("Choose your character: e.g. Jerry, Elaine, George ").title())

# character must be a RandomQuote() object
gui = Interface(character=character)
