"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        self.words = []
        with open(path) as file:
            for line in file:
                word = line.strip()
                if word:
                    self.words.append(word)

    def random_word(self):
        return random.choice(self.words)
    
    # def __init__(self, path):
    #     dict_file = open(path)

    #     self.words = self.parse(dict_file)

    #     print(f"{len(self.words)} words read")

    # def parse(self, dict file):
    #     return [w.strip() for w in dict_file]
    
    # def random(self):
    #     return random.choice(self.words)
        
