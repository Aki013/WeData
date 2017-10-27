import csv

def readCSVFile(p_csv_full_name):
    with open(p_csv_full_name, 'r') as f:
        reader = csv.reader(f)
        result_list = list(reader)


readCSVFile('C:\Dev\Git\WeData\Data_Samples\CSV\sales.csv')