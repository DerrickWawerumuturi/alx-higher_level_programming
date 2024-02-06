#!/usr/bin/python3
import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Function to add items to the list and save them to a JSON file
def add_items_and_save_to_json(filename, *args):
    # Load existing data from the JSON file if it exists
    try:
        existing_data = load_from_json_file(filename)
    except FileNotFoundError:
        existing_data = []

    # Add new items to the list
    existing_data.extend(args)

    # Save the updated list to the JSON file
    save_to_json_file(existing_data, filename)

# Usage
if __name__ == "__main__":
    # Add command line arguments to the list
    add_items_and_save_to_json("add_item.json", *sys.argv[1:])
