import os
import csv
import json
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print("File found:", self.filename)
            return True
        else:
            print("Error: file not found")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created:", folder)
        else:
            print("Output folder already exists")