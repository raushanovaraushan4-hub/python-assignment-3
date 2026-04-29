class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_count = 0

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)

                if gpa > 3.5:
                    high_count += 1
            except:
                continue

        avg_gpa = sum(gpas) / len(gpas)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(gpas),
            "average_gpa": round(avg_gpa, 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_count
        }

        return self.result

    def print_results(self):
        print("\nGPA Analysis")
        print("---------------------")
        for key, value in self.result.items():
            print(f"{key}: {value}")