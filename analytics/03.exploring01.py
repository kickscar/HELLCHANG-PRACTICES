# Workout Analytics
# 03. Exploring Basically

import os
import pickle
from pathlib import Path

# Deserialize: Exercise Dictionary
pkldirectory = os.path.join(Path(os.getcwd()).parent, 'datasets', 'pickles')

pklfile = os.path.join(Path(os.getcwd()).parent, pkldirectory, 'transformation.data.pkl')
with open(pklfile, 'rb') as fpkl:
    transformdata = pickle.load(fpkl)
print(f'Loding Transformation Data Pickle[{pklfile}]')

#
# Exploring1: How Exercise Days?
days = list(set([t[0] for t in transformdata]))
print(f'Exercise Days: {len(days)}')

#
# Exploring2: Which Exercises?
exs = [t[1] for t in transformdata]
dataset_exs = [(ex, exs.count(ex)) for ex in list(set(exs))]

sorted_by_ex = sorted(dataset_exs, key=lambda t: t[0])
for d in sorted_by_ex:
    print(d)

#
# Exploring3: and How Often?
sorted_by_count = sorted(dataset_exs, key=lambda t: t[1], reverse=True)
for d in sorted_by_count:
    print(d)
