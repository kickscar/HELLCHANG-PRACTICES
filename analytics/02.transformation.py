# Workout Analytics
# 02. Transformation with Cleansing, Denoising, Imputation and Normalization(using Exercise-Dictionary)

import os
import re
import pickle
from datetime import datetime
from pathlib import Path

# Deserialize: Exercise Dictionary
pkldirectory = os.path.join(Path(os.getcwd()).parent, 'datasets', 'pickles')

pklfile = os.path.join(Path(os.getcwd()).parent, pkldirectory, 'exercise-dict.pkl')
with open(pklfile, 'rb') as fpkl:
    exercisedict = pickle.load(fpkl)
print(f'Loding Exercise Dictionary Pickle[{pklfile}]')

# Deserialize: Aquisition Raw Data
pklfile = os.path.join(Path(os.getcwd()).parent, pkldirectory, 'aquisition.raw.data.pkl')
with open(pklfile, 'rb') as fpkl:
    rawdata = pickle.load(fpkl)

print(f'Loding Aquisition Raw Data Pickle[{pklfile}]')

# Tranformation
restransform = []
exs_dict = exercisedict['exercises']
eqptdials_dict = exercisedict['equipment-dialects']

exercise_rawdata_count = 0
date_rawdata_count = 0
for raw in rawdata:
    if raw.startswith('####'):
        exercise_rawdata_count = exercise_rawdata_count + 1

        # 1. split exercise name & record
        exname, exrecord = (s.strip() for s in raw.replace('####', '').strip().split(':'))

        # 2. normalize exercise name with equipment
        exname = re.sub(r'[\d+\\.]', '', exname).strip()
        pttrmatch = re.compile(r'([a-zA-Z\s\',]+)\s*\[([a-zA-Z\s\',]+)\]').match(exname)
        exname, equipment = (exname, None) if pttrmatch is None else pttrmatch.groups()

        # 2-1. name
        exname = exname.strip().title()
        for exkey in exs_dict:
            exdials = exs_dict[exkey]['dialects']
            if exname in exdials:
                exname = exkey
                break

        # 2-2. equipment
        if equipment:
            equipment = equipment.strip().title()
            for eqptdials_key in eqptdials_dict:
                if equipment in eqptdials_dict[eqptdials_key]:
                    equipment = eqptdials_key
                    break

            exname = f'{exname}[{equipment}]'

        restransform[len(restransform):] = [(date, exname, *re.split(r'\s+', exrecord.strip()))]
    elif raw.startswith('##'):
        date_rawdata_count = date_rawdata_count + 1
        date = datetime.strptime(raw.replace('##', '').strip(), '%Y/%m/%d')

print(f'Raw Exercise Data Count(Exercise, Date): ({exercise_rawdata_count}, {date_rawdata_count})')
print(f'Exercise Transform Data(Tuple) Count: {len(restransform)}')

# Serialize
pkldirectory = os.path.join(Path(os.getcwd()).parent, 'datasets', 'pickles')
os.path.isdir(pkldirectory) or os.mkdir(pkldirectory)

pklfile = os.path.join(os.getcwd(), pkldirectory, 'transformation.data.pkl')
with open(pklfile, 'wb') as fpkl:
    pickle.dump(restransform, fpkl, -1)

# print(restransform)
print(f'Pickling Transformation Data Completed...[{pklfile}]')
