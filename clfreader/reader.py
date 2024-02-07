"""
A class that reads a text file in Common Log Format and converts to different formats
"""

class CLFReader:

    def __init__(self, filename):
        with open(filename) as f:
            self.logs = f.read()

    def to_dataframe(self):
        pass

    def to_json(self):
        pass 

        
