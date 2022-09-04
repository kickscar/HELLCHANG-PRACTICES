import os
import pickle
from pathlib import Path


def main():
    dictdirectory = os.path.join(Path(os.getcwd()).parent, 'datasets')
    os.path.isdir(dictdirectory) or os.mkdir(dictdirectory)

    dictfile = os.path.join(os.getcwd(), dictdirectory, 'exercise-dict.pkl')
    with open(dictfile, 'wb') as fdict:
        pickle.dump(exercisedict, fdict, -1)

    print(f'Pickling the Exercise Dictionary Completed...[{dictfile}]')


exercisedict = {
    "equipment-dialects": {
        "Dumbbell": [],
        "Machine": ["Machin"],
        "Smith Machine": ["Machine, Smith"],
        "EZ Curl Bar": ["Ez Bar", "Ezbar"],
        "Pec Deck Machine": ["Machine, Pec Deck"]
    },
    "exercises": {
        "Arnold Press": {
            "dialects": [],
            "body-group": "Shoulder",
            "muscle-groups": ("Chest",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Dip": {
            "dialects": ["Assisted Dips"],
            "body-group": "Chest",
            "muscle-groups": ("Chest",),
            "recrod-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "body-group": "Back",
            "muscle-groups": ("Lats",),
            "recrod-type": ("Weight", "Repetition", "Set")
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "body-group": "Back",
            "muscle-groups": ("Back",),
            "recrod-type": ("Repetition", "Set")
        },
        "Body-Weight Squat": {
            "dialects": ["Basic Squat", "Basic Squats", "Air Squat"],
            "body-group": "Leg",
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Repetition", "Set")
        },
        "Power Leg Press": {
            "dialects": ["Power Leg Pres"],
            "body-groups": "Leg",
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Weight", "Repetition", "Set")
        },
        "Pull-Up": {
            "dialects": ["Pull Up", "Pullup"],
            "body-groups": "Back",
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Weight", "Repetition", "Set")
        }
    }
}

__name__ == '__main__' and main()
