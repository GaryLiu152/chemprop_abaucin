import csv
import os
import pandas as pd
import glob

directory = './data/raw/ZINC15/'

files_converted = 0
for filename in os.listdir(directory):
    if filename.endswith('.smi'):
        files_converted += 1
        with open(directory + filename, newline= '\n') as input: #, (open(filename[0:-4]) + '.csv', 'w+')) as output:
            csv_name = filename[0:-4] + '.csv.'
            with open(directory + '_compiled.csv', 'a+', newline = '') as output:
                writer = csv.writer(output, delimiter= ',')
                for line in input:
                    writer.writerow(line.split())
        if files_converted %10 == 0:
            print(files_converted)