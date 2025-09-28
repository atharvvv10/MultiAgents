import json
from uuid import uuid4

def save_trace(trace):
    with open(f"traces/{uuid4()}.json", "w") as f:
        json.dump(trace, f)

def load_traces():
    import glob
    return [json.load(open(f)) for f in glob.glob("traces/*.json")]
