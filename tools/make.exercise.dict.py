import os
import pickle
from pathlib import Path


def main():
    dictdirectory = os.path.join(Path(os.getcwd()).parent, 'datasets')
    os.path.isdir(dictdirectory) or os.mkdir(dictdirectory)

    dictfile = os.path.join(os.getcwd(), dictdirectory, 'exercise-dict.pkl')
    with open(dictfile, 'wb') as fdict:
        pickle.dump(exercisedict, fdict, -1)


exercisedict = {
    "equipment-dialects": {
        "Dumbbell": [],
        "Machine": ["Machin"],
        "Smith Machine": ["Machine, Smith"],
        "Pec Deck Machine": ["Machine, Pec Deck"]
    },
    "exercises": {
        "Arnold Press": {
            "dialects": [],
            "muscle-groups": "Chest",
            "record-type": ["Weight", "Repetition", "Set"]
        },
        "Assisted Dip": {
            "dialects": [],
            "muscle-groups": "Chest",
            "recrod-type": ["Weight", "Repetition", "Set"]
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "muscle-groups": "Lats",
            "recrod-type": ["Weight", "Repetition", "Set"]
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "muscle-groups": "Back",
            "recrod-type": ["Repetition", "Set"]
        },
        "Body-Weight Squat": {
            "dialects": ["Basic Squat", "Basic Squats", "Air Squat"],
            "muscle-groups": "Quadriceps",
            "recrod-type": ["Repetition", "Set"]
        }

    }
}

__name__ == '__main__' and main()
