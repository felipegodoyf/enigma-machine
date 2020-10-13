## :speech_balloon: Enigma Machine

The Enigma Machine was designed by Germany during the second world war.
It was used to send encrypted messages, and was the world's most complex cryptography system at the time.

This project simulates the original Enigma Machine by converting every mechanical operation into programming logic.

## ⚙️ Quick setup
Before using the Enigma, the file `settings.json` needs to be **randomized, so the encryption is unique**.
To do so, you can execute `setup.py`, which will do everything automatically for you:

    python setup.py

If you want, you can also customize which characters are going to be supported by the Enigma by changing the property "alphabet", in `settings.json`. Remember to run the setup again if you do so.

## :rocket: Executing:
From the project root folder, you can use any of the following commands to run Enigma:

    python enigma.py
    python enigma.py "message"
    python enigma.py "C:/file.txt"

The output is going to be **unique to the current settings**. That means the only way to decode it is to use the **same exact settings**.

## ⚙️ Custom setup
If you want or need to customize the machine's settings, here's a step-by-step:

**1. Alphabet**
The alphabet defines which characters are going to be supported by the Enigma.
This is up to you. The only requirement is that the total number of characters **must be even**.
Example:

    "alphabet": ["a", "b", "c", "d", "e", "f", ...]

**2. Rotors**
Each rotor must contain every number from **0** to the **length of the alphabet** you define **-1**.
I recommend you use any online list randomizer to define the values of each rotor.
Example:

    "rotors": [
	    [26,0,27,29,19,17,9,10,14,25,32,12,11,34,31,15,...],
	    [26,23,5,16,34,15,8,29,31,30,4,39,25,27,14,17,...],
	    [9,33,36,14,34,6,13,4,30,31,21,20,2,27,25,16,3,...]
    ]

**3. Initial rotations**
The initial rotation count of each rotor also needs to be randomized, like so:

    "initial_rotor_rotations": [10, 5, 21]

**4. Plugboard**
The plugboard basically re-routes every letter, or every index.
It also needs to be randomized, but it's a little more specific:
- It must contain every index from **0** to the **length of the alphabet** you define **-1**;
- Every index must be linked to another one;
- Indexes **must not repeat**.

Example:

    "plugboard": [[0, 2], [8, 7], [23, 10], ...]


**5. Reflector**
The reflector is responsible to send the signal back into the rotors.
It's requirements are **exactly the same as the Plugboard's**.
Example:

	"reflector": [[1, 9], [15, 3], [2, 17], ...]