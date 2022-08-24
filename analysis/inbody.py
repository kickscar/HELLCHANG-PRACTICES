import sys
from datetime import datetime
from itertools import cycle
from matplotlib import pyplot as plt
from utils import crawling, clean_strings, filters, seperate_value


def fetch_inbody():
    return list(filter(
        lambda s: s.startswith('#'),
        filters(
            crawling(
                'https://raw.githubusercontent.com/kickscar/HELLCHANG-PRACTICES/main/InBody.md',
                err=lambda e: None),
            lambda lines: [] if lines is None else lines.split('\n'),
            lambda s: clean_strings(s, str.strip))))


def arrange_fetch_inbody(records):
    results = []

    for record in records:
        if record.startswith('####'):
            item, value = (s.strip() for s in record.replace('####', '').strip().split(':'))
            results.append((date, item, *seperate_value(value)))
        elif record.startswith('##'):
            date = record.replace('##', '').strip()

    return results


results_fetch = fetch_inbody()

if len(results_fetch) == 0:
    sys.exit(0)

results_arrange = arrange_fetch_inbody(results_fetch)

print(dataset_y)
# graph
cycol = cycle('bgrcmk')
legendhandles = []
fig, subplot = plt.subplots(1, 1)

for key in dataset_y.keys():
    subplot = subplot.twinx()
    line, = subplot.plot(
        [(x - dataset_x[0]).days for x in dataset_x],
        dataset_y[key]['values'],
        'o-',
        color=next(cycol),
        label=f"{key}({dataset_y[key]['unit']})")
    legendhandles.append(line)

plt.legend(handles=legendhandles, loc='best')
plt.show()
