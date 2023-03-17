import csv
from pathlib import Path

def check(currency):
    folder = Path(__file__).parent
    with open(folder / "currency.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if currency in row[1]:
                return True
    return False