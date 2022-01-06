import random
import string
from random_word import RandomWords

# Generate 5 random digits
Digit1 = str(random.randint(0,9))
Digit2 = str(random.randint(0,9))
Digit3 = str(random.randint(0,9))
Digit4 = str(random.randint(0,9))
Digit5 = str(random.randint(0,9))

print("Thinking...")

# Generate 4 random words
r = RandomWords()
Word1 = r.get_random_word().title()     # I should throw in some status messages here for giggles.
Word2 = r.get_random_word().title()
Word3 = r.get_random_word().title()
Word4 = r.get_random_word().title()

# Pull random symbol
symbols = string.punctuation
Symbol = ''.join(random.choice(symbols) for i in range (1))

# Join together
Sentence = str(Digit1+Word1+Digit2+Word2+Digit3+Word3+Digit4+Word4+Digit5+Symbol)
Password123 = Sentence.replace(' ', '-')

print("Your new password is:", Password123) # I had to throw this joke in here.