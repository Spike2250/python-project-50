import json


def format_json(diff_data):
    return json.dumps(diff_data, indent=2)
