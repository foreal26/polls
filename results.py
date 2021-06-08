from glob import glob
from sys import argv
import json
import pandas as pd

results = []
directory = argv[1]
for i in glob(f"{directory}/*.json"):
    with open(i, "r") as f:
        results.append(json.load(f))

frame = pd.DataFrame(results)
for symbol, group in frame.groupby("title"):
    print(f"Story: {symbol}")
    print(f"Total Votes: {group['title'].count()}")
    print(group["score"].value_counts())
