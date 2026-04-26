import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        print(f"Error: {self.filename} not found.")
        return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, "r", encoding="utf-8-sig") as file:

                first_line = file.readline()
                if "student_id" not in first_line.lower():
                    header_line = file.readline()
                else:
                    header_line = first_line
                    file.seek(0)
                    file.readline()

                dialect = ';' if ';' in header_line else ','
                reader = csv.DictReader(file, fieldnames=header_line.strip().split(dialect), delimiter=dialect)

                for row in reader:
                    clean_row = {k.strip(): v for k, v in row.items() if k is not None}
                    self.students.append(clean_row)

            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: {self.filename} not found.")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("------------------------------")
        for i in range(min(n, len(self.students))):
            s = self.students[i]
            print(
                f"{s.get('student_id')} | {s.get('age')} | {s.get('gender')} | {s.get('country')} | GPA: {s.get('GPA')}")
        print("------------------------------")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):

        low_sleep_gpas = []
        high_sleep_gpas = []

        for s in self.students:
            try:
                sleep = float(s["sleep_hours"])
                gpa = float(s["GPA"])
                if sleep < 6:
                    low_sleep_gpas.append(gpa)
                else:
                    high_sleep_gpas.append(gpa)
            except (ValueError, KeyError):
                continue

        avg_low = round(sum(low_sleep_gpas) / len(low_sleep_gpas), 2) if low_sleep_gpas else 0
        avg_high = round(sum(high_sleep_gpas) / len(high_sleep_gpas), 2) if high_sleep_gpas else 0

        self.result = {
            "low_sleep_count": len(low_sleep_gpas),
            "low_sleep_avg_gpa": avg_low,
            "high_sleep_count": len(high_sleep_gpas),
            "high_sleep_avg_gpa": avg_high,
            "gpa_difference": round(abs(avg_high - avg_low), 2)
        }
        return self.result

    def print_results(self):
        print("Sleep vs GPA Analysis")
        print(
            f"Students sleeping < 6 hours : {self.result['low_sleep_count']} avg GPA: {self.result['low_sleep_avg_gpa']}")
        print(
            f"Students sleeping >= 6 hours: {self.result['high_sleep_count']} avg GPA: {self.result['high_sleep_avg_gpa']}")
        print(f"GPA difference: {self.result['gpa_difference']}")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


if __name__ == "__main__":

    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()


    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()


    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()


    print("------------------------------")
    print("Advanced Filtering (Lambda/Filter)")
    try:
        stressed = list(filter(lambda s: float(s.get("mental_stress_level", 0)) > 7, dl.students))
        print(f"Students with stress > 7: {len(stressed)}")

        high_gpa = list(filter(lambda s: float(s.get("GPA", 0)) > 3.8, dl.students))
        print(f"High performers (GPA > 3.8): {len(high_gpa)}")
    except Exception as e:
        print(f"Filtering error: {e}")
    print("------------------------------")


    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()


    print("\nTesting Error Handling...")
    try:
        test_dl = DataLoader("missing_file.csv")
        test_dl.load()
    except Exception:
        print("Error: File 'missing_file.csv' not found. Please check the filename.")