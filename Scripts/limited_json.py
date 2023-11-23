import json
from pathlib import Path

def read_json_file(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def write_json_file(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

data = read_json_file(Path("./Data/pytopia.json"))
data['messages'] = data['messages'][0:1000]
write_json_file(data, Path("./Data/pytopia_limited.json"))