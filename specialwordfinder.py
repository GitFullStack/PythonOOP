from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    5 words read

    >>> swf.random() in ["ablution", "barbate", "caboose", "dacnomania", "ectype"]
    True

    >>> swf.random() in ["ablution", "barbate", "caboose", "dacnomania", "ectype"]
    True

    >>> with open("complex.txt") as file:
    ...     swf.parse(file) == swf.words    
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")] 