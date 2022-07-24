# string as input and returns numbers as string output (a = 1), (b = 2), without punctuation marks

# import letters
from string import ascii_lowercase

# use enumerate to map letters with letter indexes (a = 1, b = 2,...) {dict?}

LETTERS = {letter : str(index) for index, letter in enumerate(ascii_lowercase, start = 1)}

def alphabet_position(text):
    #make lowercase
    text = text.lower()
    
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    
    # join and return string
    return ' '.join(numbers)
