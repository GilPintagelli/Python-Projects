# Ceasar Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,plain_shift):
    
    list_text = []

    # split text in letter
    # we can do that with text.split() but we need a position
    for position in range(len(plain_text)):
        letter = plain_text[position]
        list_text.append(letter)
    
        if letter in alphabet:
            # index() checks the index of a specific value
            index = alphabet.index(letter)
            # assign alphabet's value to list_index
            # adding shift to index changes the actual letter
            if index + plain_shift > 25:
                alp_2 = alphabet + alphabet
                list_text[position] = alp_2[index + plain_shift]
            else:
                list_text[position] = alphabet[index + plain_shift]

        # join letters
        cyper_text = ''.join(list_text)
    
    print(f'the encoded text is {cyper_text}')
    # how do we solve an IndexError? two ways:
    # add another alphabet at the end of the first one
            #if index + shift > 25:
                #alp_2 = alphabet + alphabet
                #list_text[position] = alp_2[index + shift]
            #else:
                #list_text[position] = alphabet[index + shift]
    

def decrypt(plain_text,plain_shift):
    
    decrypt_text = []
    
    for position in range(len(plain_text)):
        letter = plain_text[position]
        decrypt_text.append(letter)
        index = alphabet.index(letter)
        
        if index - position < 0:
            alp_2 = alphabet + alphabet
            decrypt_text[position] = alp_2[index - plain_shift]
        else:
            decrypt_text[position] = alphabet[index - plain_shift]
        
        decode_text = ''.join(decrypt_text)
    
    print(decode_text)
            
            
if direction == 'encode':
    encrypt(plain_text=text,plain_shift=shift)
if direction == 'decode':
    decrypt(plain_text=text,plain_shift=shift)