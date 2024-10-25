#!/usr/bin/python3
"""
This module contains script that adds all arguments to a Python list, and
then save them to a file
"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    args = load_from_json_file("add_item.json")
    args.extend(item for item in sys.argv[1:])
    save_to_json_file(args, "add_item.json")
except Exception:
    args = sys.argv[1:]
    save_to_json_file(args, "add_item.json")
