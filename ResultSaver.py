import os
import csv
import json

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f, indent=4)
            print("\nSaved to", self.output_path)
        except:
            print("Error saving file")