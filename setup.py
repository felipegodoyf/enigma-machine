import json
import random


def load_settings():
    with open('settings.json') as json_file:
        return json.load(json_file)


def save_settings(settings):
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile)


def list_all_indexes():
    result = []
    for i in range(0, len(alphabet)):
        result.append(i)
    return result


def generate_rotors(rotor_count, indexes):
    result = []
    for i in range(0, rotor_count):
        new_rotor = []
        indexes_copy = indexes.copy()
        for j in range(0, len(indexes_copy)):
            ind = indexes_copy.pop(random.randint(0, len(indexes_copy) - 1))
            new_rotor.append(ind)
        result.append(new_rotor)
    return result


def generate_rotors_rotations(rotor_count, indexes):
    result = []
    for i in range(0, rotor_count):
        result.append(random.randint(0, len(indexes)))
    return result


def generate_plugboard(indexes):
    result = []
    for i in range(0, int(len(indexes) / 2)):
        plug = [indexes.pop(random.randint(0, len(indexes) - 1)),
                indexes.pop(random.randint(0, len(indexes) - 1))]
        result.append(plug)
    return result


def generate_reflector(indexes):
    result = []
    for i in range(0, int(len(indexes) / 2)):
        connection = [indexes.pop(random.randint(0, len(indexes) - 1)),
                    indexes.pop(random.randint(0, len(indexes) - 1))]
        result.append(connection)
    return result


# parameters
rotor_count = 3

print('randomizing settings...')

# getting info
settings = load_settings()
alphabet = settings['alphabet']
indexes = list_all_indexes()

# randomizing
rotors = generate_rotors(rotor_count, indexes.copy())
initial_rotor_rotations = generate_rotors_rotations(rotor_count, indexes.copy())
plugboard = generate_plugboard(indexes.copy())
reflector = generate_reflector(indexes.copy())

# saving
settings['rotors'] = rotors
settings['initial_rotor_rotations'] = initial_rotor_rotations
settings['plugboard'] = plugboard
settings['reflector'] = reflector
save_settings(settings)

print('successfully randomized.')