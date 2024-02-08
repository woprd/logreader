# File to run with python -m clfreader
from clfreader import CLFReader
clfr = CLFReader("apache.log")
print(clfr.logs)
