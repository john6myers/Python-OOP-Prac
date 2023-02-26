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
    def __init__(self, start = 0):
        """Initialize the generator with a starting number"""
        self.start = start
        self.current = start

    def __repr__(self):
        """show representation..."""
        return f"<SerialGenerator start={self.start} next={self.current}"

    def generate(self):
        """return the next serial number and increment the counter"""
        result = self.current
        self.current += 1
        return result

    def reset(self):
        """reset the counter to starting number"""
        self.current = self.start