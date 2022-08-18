import sys
from itertools import count
from utils import crawling, clean_strings, filters


for week in count(start=50):
    url = 'https://raw.githubusercontent.com/kickscar/HELLCHANG-PRACTICES/main/training-record/Week0%02d.md' % week

    lines = filter(
        lambda s: s.startswith('#'),
        filters(
            crawling(url, err=lambda e: sys.exit(0)),
            lambda d: ('' if d is None else d).split('\n'),
            lambda d: clean_strings(d, str.strip)))

    for line in lines:
        print(line)
