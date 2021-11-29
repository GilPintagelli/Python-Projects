from art import logo

print(logo)

def ceasar(plain_text, plain_shift, plain_direction):
    
    ceasar_text = ''
    
    # in order for this to work we have to put this statement outside the for loop
    # otherwise plain_shift becomes negative and then positive 
    # if plain_direction == 'decode':
        # plain_shift *= -1
    
    # for each letter in text do something (find that same letter in alphabet)
    for letter in plain_text:
        
        # check for symbols/numbers/spaces --> not in alphabet       
        if letter not in alphabet:
            ceasar_text += letter
        else:   
            # give me the index of that letter in alphabet
            position = alphabet.index(letter)
            # shift position based on plain_direction
            if plain_direction == 'encode':
                shifting = position + plain_shift
            elif plain_direction == 'decode':
                shifting = position - plain_shift
            # another simplier way uses only one if statement (above)
            #shifting = position + plain_shift

            # assign new letters to the variable string encode_text
            new_letter = alphabet[shifting]
            ceasar_text += new_letter
        
    
    print(f'the {plain_direction}d text is {ceasar_text}')
    
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
    
# Ceasar Cypher
exit = False
while not exit:
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #Try running the program and entering a shift number of 45 ---> #IndexError: list index out of range

    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    if shift > 26:
        shift = shift % 26
        # shift is the remainder
    
    #if shift > 26:
    #    for letter in alphabet:                 ---> this snippet doesn't go over well
    #        if shift % len(alphabet) != 0:
    #            alphabet.append(letter)
 
    
    ceasar(plain_text=text, plain_shift=shift, plain_direction=direction)
    
    # this must be indented with the function because it's going to be executed after the function
    status_game = input('Do you want to restart the Ceasar Cyper? y or n ').lower()
    if status_game == 'y':
        print('See you next time!')
        exit = True
        # above the while loop becomes not true, so false and it ceases to run