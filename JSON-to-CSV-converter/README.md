# 📄 JSON to CSV Converter

A simple and efficient Python script that converts structured JSON data into CSV format for easier analysis and usage.

---

## 🚀 Features

- 📥 Reads data from a JSON file  
- 🔄 Converts JSON to CSV format  
- 🧠 Automatically detects field names  
- ⚠️ Handles missing or invalid files gracefully  
- ✅ Lightweight and beginner-friendly  

---

## 📁 Project Structure

```
JSON-to-CSV-converter/
│── json_to_csv.py
│── api_data.json
│── converted_data.csv  (generated after running)
│── README.md
```


---

## 📝 Example Input (JSON)

```json
[
  {
    "name": "John",
    "age": 25,
    "city": "New York"
  },
  {
    "name": "Alice",
    "age": 30,
    "city": "London"
  }
]
```

---

## 📊 Output (CSV)

```csv
name,age,city
John,25,New York
Alice,30,London
```

---

## ⚙️ Configuration

Inside the script, you can change file names:

```python
INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"
```

---

## ⚠️ Error Handling

- Prints message if file does not exist  
- Handles invalid JSON format  
- Prevents conversion of empty data  

---

## 🛠️ Tech Used

- Python  
- Built-in libraries: `json`, `csv`, `os`  

---

## 👨‍💻 Author

**Shrestha Sarangi**