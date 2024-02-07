"""
A class that reads a text file in Common Log Format and converts to different formats
"""

class CLFReader:

    @staticmethod
    def parse_log(log):
        """
        receives a single line of CLF file and returns tuple of items
        """
        item1, residual = log.split(" ", 1)
        item2, residual = residual.split(" ", 1)
        item3, residual = residual.split(" ", 1)
        item4, residual = residual.split("] ", 1)
        item4 = item4.strip('[')
        item5, residual = residual.split('\" ', 1)
        item6, residual = residual.split(" ", 1)
        item7, residual = residual.split(" ", 1)
        item8, residual = residual.split(' \"', 1)
        item8 = item8.strip('\"')
        item9 = residual[:-1]
        return item1, item2, item3, item4, item5, item6, item7, item8, item9

    def __init__(self, filename):
        with open(filename) as f:
            logs = f.read().splitlines()
            self.logs = [self.parse_log(log) for log in logs]

    def to_dataframe(self):
        pass

    def to_json(self):
        pass 
