"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
            """Create a new serial generator, and initialize it with the value of start."""

            self.start = start
            self.next = start

    def __repr__(self):
        """Shows the SerialGenerator and its start and next values."""

        return f"(SerialGenerator start={self.start} next={self.next})"

    def generate(self):
        """Return next serial number."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset number to the start number."""

        self.next = self.start

serial = SerialGenerator()
serial.generate()

