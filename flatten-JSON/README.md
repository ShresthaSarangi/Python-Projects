# 🧩 Flatten JSON CLI Tool

A simple Python script to convert nested JSON into a flat dictionary format using a custom separator.

---

## 🚀 Features

- Flattens deeply nested JSON structures  
- Supports both dictionaries and lists  
- Custom separator (., -, etc.)  
- Reads from input file and writes to output file  
- Simple CLI-based usage  

---

## 📂 Project Structure

flatten-json/
│── flatten_json.py
│── input.json
│── output.json
│── README.md

---

## 🛠️ How It Works

Example input (input.json):

{
  "user": {
    "name": "John",
    "details": {
      "age": 25
    }
  }
}

Output (output.json):

{
  "user.name": "John",
  "user.details.age": 25
}

---


## ⚙️ Configuration

You can modify these variables in the script:

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"

---

## ❗ Error Handling

The script handles:
- Missing input file  
- Invalid JSON format  
- Unexpected errors  

---

## 📌 Use Cases

- Preparing data for APIs  
- Data preprocessing  
- Logging and analytics  
- Converting nested JSON for CSV/export  

---

## 🧠 Concepts Used

- Recursion  
- JSON handling (json module)  
- File handling  
- CLI input  

---


## ⭐ Author

Shrestha Sarangi