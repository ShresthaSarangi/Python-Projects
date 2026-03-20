"""
Flatten JSON CLI Tool

This script takes a nested JSON file and converts it into a flat dictionary.
Supports custom separators like '.' or '-'.

Author: Shrestha Sarangi
"""

import json
import os

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"

def flatten_json(data, parent_key="", sep="."):
    items = {}

    if isinstance(data,dict):
        for k,v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k 
            items.update(flatten_json(v, full_key, sep=sep))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep=sep))
    else:
        items[parent_key] = data
    return items
def main():
    if not os.path.exists(INPUT_FILE):
        print("No input file found.")
        return

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        sep = input("Enter a separator (default = '.'): ").strip() or "."

        flattened = flatten_json(data, sep=sep)
        with open (OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(flattened, f, indent=2)

        print(f"Flattened JSON converted to {OUTPUT_FILE}")
    except FileNotFoundError:
        print("Input file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as e:
        print(f"Unexpected error:{e}")

if __name__ == "__main__":
    main()