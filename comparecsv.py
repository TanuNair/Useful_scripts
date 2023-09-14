import csv
import difflib

def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

file1_data = read_csv("Prod-data.csv")
file2_data = read_csv("SAT-data.csv")

def compare_rows(row1, row2):
    return row1 == row2

mismatched_rows = []

with open('diff_report.txt', 'w') as report_file:
    for i, (row1, row2) in enumerate(zip(file1_data, file2_data), start=1):
        if compare_rows(row1, row2):
            report_file.write(f'Row {i} matches\n')
        else:
            report_file.write(f'Row {i} does not match\n')
            mismatched_rows.append((row1, row2))

# Write mismatched rows from both files
with open('diff_report.txt', 'a') as report_file:
    for i, (row1, row2) in enumerate(mismatched_rows, start=1):
      report_file.write(f'\nMismatched columns for Row {i}:\n')
      report_file.write(f'File 1 PROD: {",".join(row1)}\n')
      report_file.write(f'File 2 SAT: {",".join(row2)}\n')
