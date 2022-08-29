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
dictdirectory = os.path.join(os.getcwd(), '../dataset/')
os.mkdir(dictdirectory)

dictfile = os.path.join(os.getcwd(), dictdirectory, 'exercise-dict.pkl')
with open(dictfile, 'wb') as fdict:
    pickle.dump(exercisedict, fdict, -1)
