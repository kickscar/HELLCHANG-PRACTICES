import os
import pickle
from pathlib import Path


def main():
    pkldirectory = os.path.join(Path(os.getcwd()).parent, 'datasets', 'pickles')
    os.path.isdir(pkldirectory) or os.mkdir(pkldirectory)

    pklfile = os.path.join(os.getcwd(), pkldirectory, 'exercise-dict.pkl')
    with open(pklfile, 'wb') as fpkl:
        pickle.dump(exercisedict, fpkl, -1)

    print(f'Pickling the Exercise Dictionary Completed...[{pklfile}]')


exercisedict = {
    "equipment-dialects": {
        "Dumbbell": [],
        "Machine": ["Machin"],
        "Smith Machine": ["Machine, Smith"],
        "EZ Curl Bar": ["Ez Bar", "Ezbar", "Ez Curl Bar"],
        "Pec Deck Machine": ["Machine, Pec Deck"]
    },
    "exercises": {
        "Arnold Press": {
            "dialects": [],
            "body-group": "Shoulder",
            "muscle-groups": ("Deltoids", "Anterial Head"),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Dips": {
            "dialects": ["Assisted Dip"],
            "body-group": "Chest",
            "muscle-groups": ("Pectorialis Major",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "body-group": "Back",
            "muscle-groups": ("Latissimus Dorsi",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "body-group": "Back",
            "muscle-groups": ("Erector Spinae", "Gluteus Maximus", ""),
            "record-type": ("Repetition", "Set")
        },
        "Body-Weight Squat": {
            "dialects": ["Basic Squat", "Basic Squats", "Air Squat"],
            "body-group": "Legs",
            "muscle-groups": ("Quardriceps Femoris", "Gluteus Maximus"),
            "record-type": ("Repetition", "Set")
        },
        "Power Leg Press": {
            "dialects": ["Power Leg Pres"],
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Pull-Up": {
            "dialects": ["Pull Up", "Pullup"],
            "body-groups": "Back",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        }
    }
}

__name__ == '__main__' and main()
