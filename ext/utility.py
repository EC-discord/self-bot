import json

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}