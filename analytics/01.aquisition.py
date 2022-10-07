# Workout Analytics
# 01. Aquisition with Crawling

import os
import pickle
import ssl
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from functools import reduce
from itertools import count

try:
    ssl._create_default_https_context = ssl._create_unverified_context

    resfetch = []
    for idx in count(start=1):
        url = 'https://raw.githubusercontent.com/kickscar/HELLCHANG-PRACTICES/main/datasets/Week0%02d.md' % idx
        print('%s: request [%s]' % (datetime.now(), url))

        ln = len(resfetch)
        resfetch[ln:] = list(filter(
            lambda s: s.startswith('#'),
            reduce(
                lambda param, func: func(param),
                [
                    lambda raw: [] if raw is None else raw.splitlines(),
                    lambda strs: [f(s) for f in [str.strip] for s in strs]
                ],
                urlopen(Request(url)).read().decode('utf-8', errors='replace')
            )
        ))

        if len(resfetch) == ln:
            break

    # Serialize
    pkldirectory = os.path.join(Path(os.getcwd()).parent, 'datasets', 'pickles')
    os.path.isdir(pkldirectory) or os.mkdir(pkldirectory)

    pklfile = os.path.join(os.getcwd(), pkldirectory, 'aquisition.raw.data.pkl')
    with open(pklfile, 'wb') as fpkl:
        pickle.dump(resfetch, fpkl, -1)

    # print(resfetch)
    print(f'Pickling Aquisition Raw Data Completed...[{pklfile}]')
except Exception as err:
    # (lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr))(err)
    (lambda e: None)(err)
