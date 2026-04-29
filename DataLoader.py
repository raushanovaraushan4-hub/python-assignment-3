import os
import csv
import json

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    self.students.append(row)

            print("Data loaded:", len(self.students), "students")
        except FileNotFoundError:
            print("File not found")

    def preview(self, n=5):
        print("\nFirst", n, "rows:")
        for student in self.students[:n]:
            print(student)