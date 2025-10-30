import os
import csv
import json
from tkinter import Tk, filedialog

# Select input folder containing CSV files
root = Tk()
root.withdraw()
input_folder = filedialog.askdirectory(title="Select folder with CSV files")
output_folder = filedialog.askdirectory(title="Select folder to save JSON files")
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".csv"):
        csv_path = os.path.join(input_folder, file_name)
        json_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".json")
        
        with open(csv_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
        
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(rows, json_file, indent=4, ensure_ascii=False)
        
        print(f"✅ Converted {file_name} → {os.path.basename(json_path)}")

print("All CSV files have been converted to JSON!")
