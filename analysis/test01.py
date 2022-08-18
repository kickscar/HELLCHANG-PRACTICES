import sys
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


def arrange_week_recored(logs):
    records = []

    for log in logs:
        if log.startswith('####'):
            exercise, recorditems = (log.replace('####', '').strip().split(':'))
            records.append((date, exercise, *recorditems.strip().split(' ')))
        elif log.startswith('##'):
            date = log.replace('##', '').strip()

    return records


for index in count(start=50):
    logs = fetch_week_records(index)
    if len(logs) == 0:
        break

    results = arrange_week_recored(logs)
    print(results)


