# File to run with python -m clfreader
from logreader import CLFReader
from logreader import MongoDBReader

from pathlib import Path
import json 

current_directory = Path(__file__).resolve().parent

print("Combined Log Format")
clfr = CLFReader(current_directory / "apache.log")
json_data = json.dumps(clfr.logs, indent=4)
print(json_data)
print("Pandas Dataframe: ", clfr.df.head())

print("Mongo DB")
mdbr = MongoDBReader(current_directory / "mongodb.log")
json_data = json.dumps(mdbr.logs, indent=4)
print(json_data)
print("Pandas Dataframe: ", mdbr.df.head())



