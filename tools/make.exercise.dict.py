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
            "default-equipment": "Dumbbell",
            "body-group": "Shoulder",
            "muscle-groups": ("Deltoids", "Anterial Head"),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Dips": {
            "dialects": ["Assisted Dip"],
            "default-equipment": "Machine",
            "body-group": "Chest",
            "muscle-groups": ("Pectorialis Major",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Assisted Pull-Up": {
            "dialects": ["Assisted Pullup"],
            "default-equipment": "Machine",
            "body-group": "Back",
            "muscle-groups": ("Latissimus Dorsi",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Back Extension": {
            "dialects": ["Back Extensions"],
            "default-equipment": "Machine",
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
        "Cross Lunges": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Dead Bug": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Dips": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Deadlift": {
            "dialects": ["Daedlift"],
            "default-equipment": "Barbell",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Flat Bench Press": {
            "dialects": ["Flat Chest Press"],
            "default-equipment": "Barbell",
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
        "Hip Bridge": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Hip External Rotation": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Hip Thrust": {
            "dialects": [],
            "default-equipment": "Barbell",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Lying Leg Curls": {
            "dialects": ["Leg Curl"],
            "default-equipment": "Machine",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Long Pull Row": {
            "dialects": ["Low Pulley", "Low Row", "Seated Low Row"],
            "default-equipment": "Cable",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Incline Bench Press": {
            "dialects": ["Incline Chest Press"],
            "default-equipment": "Barbell",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "One Arm Bent Over Row": {
            "dialects": ["One Arm Dumbbell Row"],
            "default-equipment": "Dumbbell",
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Plank": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Times", "Repetition", "Set")
        },
        "Power Leg Press": {
            "dialects": ["Power Leg Pres"],
            "default-equipment": "Machine",
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
        "Reverse Crunch": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Running": {
            "dialects": [],
            "default-equipment": "Treadmill",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Times", "Distance")
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
        "Split Squat": {
            "dialects": [],
            "default-equipment": "",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Side-Lying Hip Abduction": {
            "dialects": [],
            "default-equipment": None,
            "body-groups": "Legs",
            "muscle-groups": ("Quardriceps Femoris",),
            "record-type": ("Repetition", "Set")
        },
        "Triceps Pushdown": {
            "dialects": ["Tricep Pushdown", "Cable Triceps Pushdown"],
            "default-equipment": "Cable",
            "body-groups": "Legs",
            "muscle-groups": ("Quadriceps",),
            "record-type": ("Weight", "Repetition", "Set")
        },
        "Trx Lunge": {
            "dialects": [],
            "default-equipment": "Trx Suspension Anchor",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Trx Row": {
            "dialects": [],
            "default-equipment": "Trx Suspension Anchor",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Trx Suspended Lunge": {
            "dialects": [],
            "default-equipment": "Trx Suspension Anchor",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Vipr Ice Skater": {
            "dialects": [],
            "default-equipment": "Vipr Tube",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Vipr Lateral Shuffle": {
            "dialects": [],
            "default-equipment": "Vipr Tube",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Vipr Overhead Squat": {
            "dialects": [],
            "default-equipment": "Vipr Tube",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Repetition", "Set")
        },
        "Walking": {
            "dialects": [],
            "default-equipment": "Treadmill",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Times", "Distance")
        },
        "Wrist Roller": {
            "dialects": [],
            "default-equipment": "Wrist Roller",
            "body-groups": "",
            "muscle-groups": ("",),
            "record-type": ("Weight", "Repetition", "Set")
        }
    }
}

__name__ == '__main__' and main()
