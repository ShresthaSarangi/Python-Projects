'''
# 📊 CSV to JSON Converter 

A simple and efficient command-line tool that converts CSV files into JSON format.  
It also allows previewing data before conversion, making it useful for beginners working with data processing in Python.
 
Author : Shrestha Sarangi

'''

import csv
import json
import os

input_filename = input("Enter CSV file name: ")
INPUT_FILE = input_filename
OUTPUT_FILE = "converted_data.json"

def load_data_csv(filename):
    if not os.path.exists(filename):
        print("CSV file not found.")
        return []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print("✅ Data Added succesfully.")
        return data

def convert_to_json(data, filename):
    if not data:
        print("No data to convert.")
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Converted {len(data)} records into {filename}")

def preview_data(data, count=3):
    for record in data[ : count]:
        print(json.dumps(record, indent=2))
    print("......")

def main():
    data = []
    while True:
        print("==== CSV to JSON converter ====")
        print("1. Add data from CSV.")
        print("2. Convert to json.")
        print("3. View data.")
        print("4. Exit.")
        choice = input("Choose an operation: ")

        match choice:
            case "1": 
                data = load_data_csv(INPUT_FILE)
            case "2":
                convert_to_json(data, OUTPUT_FILE)
            case "3":
                preview_data(data)
            case "4":
                print("Exiting program...")
                break
            case _:
                print("Choose a valid option.")

if __name__ == "__main__":
    main()