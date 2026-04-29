from FileManager import FileManager
from DataLoader import DataLoader
from DataAnalyser import DataAnalyser
from ResultSaver import ResultSaver   # если создашь

fm = FileManager("students.csv")

if not fm.check_file():
    exit()

fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()