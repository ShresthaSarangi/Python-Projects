"""
🌦️ Real-Time Weather API Logger

Description:
This script fetches real-time weather data using a weather API and logs
the information into a JSON file for storage and future analysis.


Author: Your Name
Date: 2026-03-18
"""

import os
import csv
from datetime import datetime 
import requests 


FILENAME = "weather_logs.csv"
API_KEY = os.getenv("API_KEY")

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])

    
def log_weather():
    city = input("Enter your city name: ").strip().lower()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if date == row["Date"] and city == row["City"].lower():
                print("Entry for this city and date already exists.")
                return


    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("Status Code: ",response.status_code)
            print("Response: ",response.text)
            return
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        with open(FILENAME, "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print(f"Logged: {temp} {condition} in {city.title()} on {date}.")
    except Exception as e:
        print("Error: ",e)

def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <=1:
            print("No entries.")
            return
        for row in reader[1:]:
            print(f"row[0] : row[1] : row[2] : row[3]")

def main():
    while True:
        print("===== Real Time Weather Logger =====")
        print("1. Add weather log")
        print("2. View weather logs")

        choice = input("Enter an option: ").strip()
        match choice:
            case "1": log_weather()
            case "2": view_logs()
            case _: print("Invalid choice.")

if __name__ == "__main__":
    main()



