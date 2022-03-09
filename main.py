import queue
import copy
from english_words import english_words_set

ENGLISH_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dictionary_search = True


guesses = [
    "PANTS",
    "FJORD",
    "CHEWY"
]

scores = [
    "BBGGB",
    "BBYBB",
    "BYBBB"
]

def input_validation(guesses, scores):
    if len(guesses) != len(scores):
        raise ValueError(f"the tries and scores need to have the same length. Got tries: {len(guesses)} and scores: {len(scores)}")
    for guess, score in zip(guesses, scores):
        if len(guess) != 5:
            raise ValueError(f"the length of guess needs to be 5. {guess} is not length of 5")
        if len(score) != 5:
            raise ValueError(f"the length of guess needs to be 5. {score} is not length of 5")


def convert_to_loc_limitation(guesses,scores):
    options = [set(ENGLISH_CHARS) for i in range(5)]
    # all letters that need to be used but we don't know the location of
    need_to_use = set()
    for guess, score in zip(guesses, scores):
        for char, sc, ind in zip(guess, score, range(5)):
            if sc == "G":
                if char not in options[ind]:
                    raise RuntimeError("There is contradiction somewhere.")
                options[ind] = set(char)
                # there are edge cases where multiple of the same characters exist in a word
                need_to_use.discard(char)
            if sc == "Y":
                options[ind].discard(char)
                need_to_use.add(char)
            if sc == "B":
                if char in need_to_use:
                    raise RuntimeError("There is a contradiction")
                for op in options:
                    op.discard(char)
    return options, need_to_use



def get_known_chars(known_non_locs):
    return None

input_validation(guesses, scores)

options, need_to_use = convert_to_loc_limitation(guesses, scores)

que = queue.Queue()

for char in options[0]:
    next_need_to_use = copy.copy(need_to_use)
    next_need_to_use.discard(char)
    que.put([char, copy.copy(next_need_to_use)])

while not que.empty():
    word, need_to_use = que.get()
    if len(word) == 5:
        if dictionary_search:
            if word.lower() in english_words_set:
                print(word)
        else:
            print(word)
    else:
        option = options[len(word)]
        for next_char in option:
            if next_char in need_to_use:
                next_need_to_use = copy.copy(need_to_use)
                next_need_to_use.remove(next_char)
                que.put([word+next_char, next_need_to_use])
            else:
                if len(need_to_use) + len(word) < 5:
                    que.put([word+next_char, copy.copy(need_to_use)])

print("DONE")

