import os
import pickle

exercisedict = {
    "equipments-dialects": {
        "Dumbbell": [],
        "Machine": ["Machin"]
    },
    "exercises": {
        "Arnold Press": {
            "dialects": [],
            "muscle-groups": "Chest",
            "record-type": ["Weight", "Repetion", "Set"]
        },
        "Assisted Dip": {
            "dialects": [],
            "equipment-dialects": {
                "Machine": [""]
            },
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

#########
dictfile = os.path.join(os.getcwd(), 'exercise-dict.pkl')

with open(dictfile, 'wb') as fdict:
    pickle.dump(exercisedict, fdict, -1)
