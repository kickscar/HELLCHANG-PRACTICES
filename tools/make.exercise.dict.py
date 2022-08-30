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
        "EZ Curl Bar": ["Ez Bar", "Ezbar"],
        "Pec Deck Machine": ["Machine, Pec Deck"]
    },
    "exercises": {
        "Arnold Press": {
            "dialects": [],
            "body-groups": ("Upper Body", "Shoulder"),
            "muscle-groups": ("Chest",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Dip": {
            "dialects": ["Assisted Dips"],
            "body-groups": ("Upper Body", "Chest"),
            "muscle-groups": ("Chest",),
            "recrod-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "body-groups": ("Upper Body", "Back"),
            "muscle-groups": ("Lats",),
            "recrod-type": ["Weight", "Repetition", "Set"]
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "body-groups": ("Upper Body", "Back"),
            "muscle-groups": ("Back",),
            "recrod-type": ("Repetition", "Set")
        },
        "Body-Weight Squat": {
            "dialects": ["Basic Squat", "Basic Squats", "Air Squat"],
            "body-groups": ("Lower Body", ),
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Repetition", "Set")
        },
        "Power Leg Press": {
            "dialects": ["Power Leg Pres"],
            "body-groups": ("Lower Body", "Leg"),
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Weight", "Repetition", "Set")
        },
        "Pull-Up": {
            "dialects": ["Pull Up", "Pullup"],
            "body-groups": ("Upper Body", "Chest"),
            "muscle-groups": ("Quadriceps",),
            "recrod-type": ("Weight", "Repetition", "Set")
        }
    }
}

__name__ == '__main__' and main()
