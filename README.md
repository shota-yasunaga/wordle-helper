# wordle-helper
Wordle helper for busy people

# How to use
In main.py, edit guesses and scores according to what you have guessed.

guesses are the words you have guessed. 
scores are the results you have got. 
Scores are either B, G, or Y, corresponding to 
B: black, or non-hit
G: green, or char is right and the location is right
Y: yellow, or char is right and the location is wrong.
ex) 
```python
guesses = [
    "PANTS",
    "FJORD",
    "CHEWY",
    "VINER",
    "LUMBI",
]

scores = [
    "BBYBB",
    "BBBYB",
    "BBYBB",
    "BYYYY",
    "BBBYY"
]

```
USE UPPER ALL CASE CHARATERS.