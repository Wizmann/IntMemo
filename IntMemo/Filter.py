#coding=utf-8
import json

def to_brief_json(view):
    tags = ['Metadata', 'Tags', 'Process']
    d = {}
    print view
    for tag in tags:
        if isinstance(view[tag], dict):
            for (key, value) in view[tag].items():
                d[key.lower()] = value
        else:
            d[tag.lower()] = view[tag]
    return json.dumps(d)
