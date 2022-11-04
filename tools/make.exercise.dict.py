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
        "Dumbbell": ["Dumbbel"],
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
            "dilects": ["Assisted Dip"],
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
        "Deadlift": {
            "dialects": ["Daedlift"],
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Flat Bench Press": {
            "dialects": ["Flat Chest Press"],
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Hanging Leg Raise": {
            "dialects": ["Hanging Leg Raises"],
            "default-equipment": "Captain's Chair",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Hip Abduction": {
            "dialects": [],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Long Pull Row": {
            "dialects": ["Low Pulley", "Low Row", "Seated Low Row"],
            "default-equipment": "Cable",
            "equipment-dialects": ["Machine"],
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Lying Leg Curls": {
            "dialects": ["Leg Curl"],
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Incline Bench Press": {
            "dialects": ["Incline Chest Press"],
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "One Arm Bent Over Row": {
            "dialects": ["One Arm Dumbbell Row"],
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
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
        },
        "Push-Up": {
            "dialects": ["Push Up"],
            "body-groups": "Back",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Running": {
            "default-equipment": None,
            "equipment-dialects": ["Treadmill"],
        },
        "Seated Chest Press": {
            "dialects": ["Chest Press", "Seated Chest Press(One Arm)"],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Seated Leg Press": {
            "dialects": ["Seated One-Leg Press"],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Seated Row": {
            "dialects": ["Seated Row(One Arm)"],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Shoulder Press": {
            "dialects": ["Shouder Press"],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Triceps Pushdown": {
            "dialects": ["Tricep Pushdown", "Cable Triceps Pushdown"],
            "default-equipment": "Cable",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Trx Lunge": {
            "default-equipment": "Trx Suspension Anchor",
            "record-type": ("Repetition", "Set")
        },
        "Trx Row": {
            "default-equipment": "Trx Suspension Anchor",
            "record-type": ("Repetition", "Set")
        },
        "Trx Suspended Lunge": {
            "default-equipment": "Trx Suspension Anchor",
            "record-type": ("Repetition", "Set")
        },
        "Vipr Ice Skater": {
            "default-equipment": "Vipr Tube",
            "record-type": ("Repetition", "Set")
        },
        "Vipr Lateral Shuffle": {
            "default-equipment": "Vipr Tube",
            "record-type": ("Repetition", "Set")
        },
        "Vipr Overhead Squat": {
            "default-equipment": "Vipr Tube",
            "record-type": ("Repetition", "Set")
        },
        "Walking": {
            "default-equipment": None,
            "equipment-dialects": ["Treadmill"],
        }
    }
}

__name__ == '__main__' and main()
