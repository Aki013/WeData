import csv
import os

def readCSVFile(p_csv_full_name, p_print_html):
    with open(p_csv_full_name, 'r') as f:
        reader = csv.reader(f)
        result_list = list(reader)
        if(p_print_html):
            #print(result_list)
            for row in result_list:
                print(row)


clear = lambda: os.system('cls')
clear()

#readCSVFile('C:\\Dev\\Git\\WeData\\Data_Samples\\CSV\\sales.csv', True)
readCSVFile('D:\\Perso\\DEV\\WeData\\Data_Samples\CSV\\sales.csv', True)
