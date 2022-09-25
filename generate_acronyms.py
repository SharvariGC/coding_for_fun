# generate acronyms in python
# 
from random_word import RandomWords
import random

generator = RandomWords()

random_word = generator.get_random_word()


l = list(random_word)
random.shuffle(l)
acronym = ''.join(l)

print(random_word, acronym)