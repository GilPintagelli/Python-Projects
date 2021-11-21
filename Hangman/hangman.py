import random
word_list = ["ardvark", "baboon", "camel"]

random_word = random.choice(word_list)

# generate '_ _ _ _'
blanks = []
for letter in random_word:
    blanks+= '_'
    
print(blanks)

end_game = False # while loop's condition
lives = 6
# 'not false' means True and it sarts the while loop
# while end_game doesn't work because end_game = False

last_letter = [] # while loop resets the value inside the list each time that runs
# so it should be placed outside the while loop

while not end_game: 
    
    guess = input('Guess a letter: ').lower()
    
    for position in range(len(random_word)): # convert random_word in numbers where each n tells us the position of a letter
        letter = random_word[position] # access each letter in random_word with 'position', which is a number
        if letter == guess:
            blanks[position] = guess

    # to-do n.2 --> keep track of 'lives'
    # if statement that checks for 'repeated letters' must go here
    # otherwise the user will loose a life even when they have already guessed a letter
    if guess in last_letter:
        print('already used')
    elif guess not in random_word:
        lives-=1
        print(f'{guess} is not in the word')
        if lives == 0:
            end_game = True
            print(stages[lives])
            print(f'sorry, the correct word is {random_word}')
            print('you lose')
         
    print(blanks)
    
    # this is the last piece of 'repeated word'
    # at the end of the while loop we need to update last_letter
    for letter in guess:
        last_letter.append(letter)

    if '_' not in blanks:
        end_game = True
        print('you won')