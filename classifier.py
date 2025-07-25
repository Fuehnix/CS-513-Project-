import csv
import requests
import json

# Step 1: Read CSV and extract "test" column into a list
def extract_test_column(csv_file):
    test_values = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_values.append(row['name'])
    return test_values

# Step 2: Query local Ollama instance
def query_ollama(item):
    prompt = (
        "Does the following list contain any endangered species? "
        "Answer ONLY with TRUE or FALSE. Item: " + item
    )
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    response.raise_for_status()
    answer = response.json()["response"].strip().upper()
    return answer

# Step 3: Main logic
def main():
    csv_path = "dish.csv"  # Replace with your file path
    test_list = extract_test_column(csv_path)
    
    endangered_list = []
    not_endangered_list = []
    for item in test_list:
        if query_ollama(item) == "TRUE":
            endangered_list.append(item)
        else:
            not_endangered_list.append(item)
        print(not_endangered_list)

    print("Endangered list:", endangered_list)

if __name__ == "__main__":
    main()