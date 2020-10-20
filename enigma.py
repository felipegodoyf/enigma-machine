import sys
import json
import os


def load_settings():
    with open('settings.json') as json_file:
        return json.load(json_file)


def rotate_rotor(rotor_index, rotate_next):
    # rotating
    rotor = rotors[rotor_index]
    rotors[rotor_index] = get_rotated_rotor(rotor)

    # counting total rotations
    add_rotor_rotation(rotor_index)

    # rotating next rotor if needed
    if (rotate_next & (rotor_rotation_count[rotor_index] >= len(alphabet))):
        rotor_rotation_count[rotor_index] = 0
        next_rotor = rotor_index + 1 if rotor_index < (len(rotors) - 1) else 0
        rotate_rotor(next_rotor, rotate_next)

def get_rotated_rotor(rotor):
    # instantiating empty rotor
    result_rotor = []

    # getting last value
    last_index = len(rotor) - 1
    result_rotor.append(rotor[last_index])

    # getting other values
    for i in range(0, len(rotor) - 1):
        result_rotor.append(rotor[i])

    return result_rotor

def add_rotor_rotation(rotor_index):
    rotor_rotation_count[rotor_index] = rotor_rotation_count[rotor_index] + 1
    return{}


def plugboard_convert(number):
    for plug in plugboard:
        if (plug[0] == number):
            return plug[1]
            break
        elif (plug[1] == number):
            return plug[0]
            break


def reflect(number):
    for connection in reflector:
        if (connection[0] == number):
            return connection[1]
            break
        elif (connection[1] == number):
            return connection[0]
            break


def filter_message(message):
    message = message.lower()
    result = ''
    for c in message:
        if (c in alphabet):
            result = result + c
    return result


# loading settings
settings = load_settings()
alphabet = settings['alphabet']
plugboard = settings['plugboard']
rotors = settings['rotors']
reflector = settings['reflector']
initial_rotor_rotations = settings['initial_rotor_rotations']

# getting input message from argument
if (len(sys.argv) == 2):
    argument = sys.argv[1]
    # argument refers to a file
    if (os.path.exists(os.path.dirname(argument))):
        print('reading input from file "' + argument + '":')
        with open(argument, 'r') as file:
            input_message = file.read()
        print(input_message)
    # argument is the message
    else:
        input_message = argument
# getting input from user
else:
    input_message = input('\ninput: ')
input_message = filter_message(input_message)

# internal variables
rotor_rotation_count = [0, 0, 0]
output_message = ''

# setting up rotors initial state
for i in range(0, len(initial_rotor_rotations)):
    for a in range(0, initial_rotor_rotations[i]):
        rotate_next = False
        rotate_rotor(i, rotate_next)

# resetting rotation counter
rotor_rotation_count = [0, 0, 0]

# main process
for i in range(0, len(input_message)):
    # getting current letter
    typed_letter = input_message[i]

    # getting corresponding number
    typed_number = alphabet.index(typed_letter)

    # converting using the plugboard
    plugboard_output = plugboard_convert(typed_number)

    # passing through rotors
    rotor_output = plugboard_output
    for rotor in rotors:
        rotor_output = rotor[rotor_output]

    # reflector
    reflector_output = reflect(rotor_output)

    # passing through rotors (reverse)
    rotor_output = reflector_output
    for r in range(len(rotors) - 1, -1, -1):
        next_value = rotors[r].index(rotor_output)
        rotor_output = next_value

    # converting at the plugboard
    rotor_output = plugboard_convert(rotor_output)

    # adding output letter to the output message
    output_letter = alphabet[rotor_output]
    output_message = output_message + output_letter

    # rotating rotors
    rotate_next = True
    rotate_rotor(0, rotate_next)

print('\noutput: ' + output_message)