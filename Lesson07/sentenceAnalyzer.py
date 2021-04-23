text = """
The programming language Python was conceived in the late 1980s, and its implementation was started in December 1989
by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with 
the Amoeba operating system. Van Rossum is Python's principal author, and his continuing central role in deciding 
the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life 
(BDFL). Python was named for the BBC TV show Monty Python's Flying Circus.
"""


def text_analyzer(text):
    solution = {}
    for c in text:
        c = c.lower()
        if c is not ' ':
            if c in solution:
                solution[c] += 1
            else:
                solution[c] = 1
    return solution


letterFrequencies = text_analyzer(text)

for c in letterFrequencies:
    print('The letter', c, 'repeats', letterFrequencies[c], 'times')
