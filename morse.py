import subprocess
import time

CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ': '***'
}

UNIT = 0.05
FREQ = 800

template = ["play", "--no-show-progress", "--null",
            "--channels", "1", "synth"]


def dot():
    subprocess.run(template + [str(UNIT), "sine", str(FREQ)])
    time.sleep(UNIT)


def dash():
    subprocess.run(template + [str(UNIT*3), "sine", str(FREQ)])
    time.sleep(UNIT)


def morse(char):
    return CODE[char.upper()]


def main():
    message = input("Enter a message: ")
    for char in message:
        if char == ' ':
            time.sleep(UNIT*2)
        try:
            for d in morse(char):
                if d == '-':
                    dash()
                elif d == '.':
                    dot()
        except KeyError:
            print("Unknown char", char)
        time.sleep(UNIT)


if __name__ == "__main__":
    main()
