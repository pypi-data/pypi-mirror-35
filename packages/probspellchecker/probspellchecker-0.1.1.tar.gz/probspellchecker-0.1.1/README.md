# Probabilistic Spell Checker in Python

Spell checker based on edit distance (Levenshtein-ish) and word frequency
in a training corpus.

    For theoretical background, see Peter Norvig's article,
https://norvig.com/spell-correct.html

Comes with a dictionary trained from German Wikipedia articles.

Usage:

    import json
    import re
    import probspellchecker

    spellchecker = probspellchecker.ProbabilisticSpellChecker(
        word_counts=json.load(open("dictionary_dewiki_full10plus.json")),
        word_whitelist=["my", "custom", "wordlist"],
    )

    text = "lorem ipsum whatever"
    for word in re.findall(r"\w+", text):
        correction = spellchecker.correction(word.lower())
        if correction:
            print(correction)
        else:
            print(word)

Word counts is just that, a dict with word to count mapping. To build your
own dictionaries, see probdict-from-dewiki.py and probdict-from-text.py.
You may also specify a whitelist of words that should just be accepted by
the spell checker, which is useful if your name is not in the dictionary.

If your language sports special characters like the German umlauts, you
might need to pass an additional charset parameter which is a string with
all allowed characters of your language, to the ProbabilisticSpellChecker.
This is then used to generate candidate words.

## Logging

If the logging annoys you, just shut it up:

    spell_log = logging.getLogger("probspellchecker")
    spell_log.setLevel(logging.ERROR)  # log only errors

