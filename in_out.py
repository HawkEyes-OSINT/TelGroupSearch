import os
import json


def checkconfig():
    """
    Check if config file exists
    """
    set = True
    # verify file exists
    if os.path.isfile("config.csv"):
        # verify sufficient data
        with open("config.csv", "r") as f:
            lines = f.readlines()
            if not lines[0].split(',')[1]:
                set = False
                print('[-] Missing api_id in inputs/config.csv')
            if not lines[1].split(',')[1]:
                set = False
                print('[-] Missing api_hash in inputs/config.csv')
            if not lines[2].split(',')[1]:
                set = False
                print('[-] Missing phone in inputs/config.csv')
    else:
        set = False
        print('[-] Missing inputs/config.csv')

    return set

def getconfig():
    """
    Get bot configurations from config file
    """
    # check configurations
    if not checkconfig():
        exit(0)

    # retreive configuration from file
    with open("config.csv", "r") as f:
        lines = f.readlines()
        config = {
                'api_id': lines[0].split(',')[1].strip(),
                'api_hash': lines[1].split(',')[1].strip(),
                'phone': lines[2].split(',')[1].strip()
                }

    return config


def validate_json_format(data):
    if not isinstance(data, list):
        raise ValueError("Error: JSON file should contain a list of dictionaries")
    
    for entry in data:
        if not isinstance(entry, dict) or 'name' not in entry or 'keywords' not in entry:
            raise ValueError("Error: Each entry in JSON should be a dictionary with 'name' and 'keywords' keys.")
        if not isinstance(entry['name'], str) or not isinstance(entry['keywords'], list):
            raise ValueError("Error: 'name' should be a string, and 'keywords' should be a list of strings.")


def get_keywords():
    try:
        with open('keywords.json', 'r') as f:
            keywords = json.load(f)
            validate_json_format(keywords)
    except FileNotFoundError:
        print('[-] Missing keywords.json')
        exit(0)
    except json.JSONDecodeError as e:
        print('[-] Invalid JSON format: ' + e)
        exit(0)
    except Exception as e:
        print('[-] ' + e)
        exit(0)