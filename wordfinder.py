import random 
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
        App for finding random words from dictionary.

        >>> wf = WordFinder("words.txt")
        235886 words read

        >>> with open("words.txt") as file:
        ...     wf.parse(file) == wf.words
        True

        >>> wf.random() in wf.words
        True
       
       
    """

    def __init__(self, path):
        """Read dictionary and print dictionary items read."""

        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")


    def random(self):
        """Return random word."""        

        return random.choice(self.words)
       
    
    def parse(self, file):
        """Parse file -> list of words."""
        return [w.strip() for w in file]
        



