# File to run with python -m clfreader
from clfreader import CLFReader
from pathlib import Path
import json 

current_directory = Path(__file__).resolve().parent

clfr = CLFReader(current_directory / "apache.log")

json_data = json.dumps(clfr.logs, indent=4)

print(json_data)
