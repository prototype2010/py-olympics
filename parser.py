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


        res = dict(zip(headers, values[0]))

        def header_value_mapping(event_row):
            event = {}



        # values.

        print(headers)







