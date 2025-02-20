#!/usr/bin/python3
"""
This is the ``task_02_csv`` module
"""
import csv
import json 


def convert_csv_to_json(csvFile):
    """
    This function convert csv file to json file
    """
    data = []
    try:
        with open(csvFile) as file:
            csvReader = csv.DictReader(file)
            for rows
"""
Module for converting CSV to JSON.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Function that takes the CSV filename as its parameter
    and writes the JSON data to a file.
    Args:
        csv_file (str): The path to the input CSV file.
        json_file (str): The path to the output JSON file.
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_file, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            data = [row for row in csvReader]

        json_file = 'data.json'
        with open(json_file, 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, indent=4)

        return True
    except FileNotFoundError:
        print("file not found")
        return False
in csvReader:
                data.append(rows)
        with open('data.json', "w") as dataf:
            json.dump(data, dataf)
        return True
    except Exception:
        return False
