import csv
import os

def readCSVFile(p_csv_full_name, p_print_html):
    with open(p_csv_full_name, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        result_list = list(reader)
        if(p_print_html):
            #print(result_list)
            print('<table>')
            print('<tr><th>' + '</th><th>'.join(result_list[0]) + '</th></tr>')
            for idx in range(1, len(result_list)):
                #print('ligne : ' + row[1])
                print('<tr><td>' + '</td><td>'.join(result_list[idx]) + '</td></tr>')
            
            print('</table>')


clear = lambda: os.system('cls')
clear()

readCSVFile('C:\\Dev\\Git\\WeData\\Data_Samples\\CSV\\sales.csv', True)
#readCSVFile('D:\\Perso\\DEV\\WeData\\Data_Samples\CSV\\sales.csv', True)