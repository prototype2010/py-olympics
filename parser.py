import abc
import csv
from abc import ABC

FILE_NAME = 'athlete_events.csv'


def parse():
    with open(FILE_NAME, 'r') as file:
        rows = csv.reader(file)
        all_rows = list(rows)
        headers = all_rows[0]
        values = all_rows[1:]

        print(headers)







