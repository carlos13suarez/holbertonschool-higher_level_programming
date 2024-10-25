#!/usr/bin/python3

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    args = load_from_json_file("add_item.json")
    args.extend(item for item in sys.argv[1:])
    save_to_json_file(args, "add_item.json")
except:
    args = sys.argv[1:]
    save_to_json_file(args, "add_item.json")
