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
            "default-equipment": None,
            "body-group": "Shoulder",
            "muscle-groups": ("Deltoids", "Anterial Head"),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Dips": {
            "dialects": ["Assisted Dip"],
            "default-equipment": None,
            "body-group": "Chest",
            "muscle-groups": ("Pectorialis Major",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "default-equipment": None,
            "body-group": "Back",
            "muscle-groups": ("Latissimus Dorsi",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "default-equipment": None,
            "body-group": "Back",
            "muscle-groups": ("Erector Spinae", "Gluteus Maximus", ""),
            "record-type": ("Repetition", "Set")
        },
        "Body-Weight Squat": {
            "dialects": ["Basic Squat", "Basic Squats", "Air Squat"],
            "default-equipment": None,
            "body-group": "Legs",
            "muscle-groups": ("Quardriceps Femoris", "Gluteus Maximus"),
            "record-type": ("Repetition", "Set")
        },
        "Deadlift": {
            "dialects": ["Daedlift"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Flat Bench Press": {
            "dialects": ["Flat Chest Press"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Lying Leg Curls": {
            "dialects": ["Leg Curl"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Long Pull Row": {
            "dialects": ["Low Pulley", "Low Row", "Seated Low Row"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Incline Bench Press": {
            "dialects": ["Incline Chest Press"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "One Arm Bent Over Row": {
            "dialects": ["One Arm Dumbbell Row"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Power Leg Press": {
            "dialects": ["Power Leg Pres"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Pull-Up": {
            "dialects": ["Pull Up", "Pullup"],
            "default-equipment": None,
            "body-groups": "Back",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Push-Up": {
            "dialects": ["Push Up"],
            "default-equipment": None,
            "body-groups": "Back",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Seated Chest Press": {
            "dialects": ["Chest Press", "Seated Chest Press(One Arm)"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Seated Leg Press": {
            "dialects": ["Seated One-Leg Press"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Seated Row": {
            "dialects": ["Seated Row(One Arm)"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Shoulder Press": {
            "dialects": ["Shouder Press"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Triceps Pushdown": {
            "dialects": ["Tricep Pushdown", "Cable Triceps Pushdown"],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        }
    }
}

__name__ == '__main__' and main()
