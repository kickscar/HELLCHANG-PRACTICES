import sys
from matplotlib import pyplot as plt
from itertools import count
from utils import crawling, clean_strings, filters


def fetch_week_records(week):
    return list(filter(
        lambda s: s.startswith('#'),
        filters(
            crawling(
                'https://raw.githubusercontent.com/kickscar/HELLCHANG-PRACTICES/main/training-record/Week0%02d.md' % week,
                err=lambda e: None),
            lambda d: [] if d is None else d.split('\n'),
            lambda d: clean_strings(d, str.strip))))


def arrange_week_records(records):
    results = []

    for record in records:
        if record.startswith('####'):
            exercise, recorditems = (record.replace('####', '').strip().split(':'))
            results.append((date, exercise, *recorditems.strip().split(' ')))
        elif record.startswith('##'):
            date = record.replace('##', '').strip()

    return results


for index in count(start=1):
    results_fectch = fetch_week_records(index)
    if len(results_fectch) == 0:
        break

    result_arrange = arrange_week_records(results_fectch)
    print(result_arrange)


