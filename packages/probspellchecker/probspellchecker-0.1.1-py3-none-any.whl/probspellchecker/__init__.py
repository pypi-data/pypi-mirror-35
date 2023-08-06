# -*- coding: utf-8 -*-

import logging

_log = logging.getLogger(__name__)
_log.setLevel(logging.ERROR)


def get_dict_path():
    """ Get directory of (bundled) dictionaries.
        Helper to access the dictionaries that are bundled wwith this package.
    """
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


class ProbabilisticSpellChecker(object):
    """ Probabilistic Spell Checker.

        checker = ProbabilisticSpellChecker(word_count_dict, word_whitelist)
        suggestion = checker.correction(word)
        if suggestion:
            word = suggestion
    """

    def __init__(self, word_counts, word_whitelist, charset=None):
        """ Initialize probabilistic spell checker.

            @param word_counts (dict: str -> int) Word to frequency map of
                known words.
            @param word_whitelist (list of str) Additional preferred words,
                e.g. your exotic name.
            @param charset (str) String containing all allowed characters
                (used for generating word variations, defaults to lowercase
                German alphabet, i.e. a-zäöüß).
        """
        total_word_count = float(sum(word_counts.values()))
        self.word_probabilities = {
            word: count / total_word_count
            for word, count in word_counts.items()
        }
        self.word_probabilities.update({
            word: 1.0
            for word in word_whitelist
        })
        self.words = set(self.word_probabilities.keys())
        _log.debug(
            "probabilistic spell checker, %i words represent a %i word corpus",
            len(self.words),
            total_word_count,
        )
        if charset:
            self.charset = charset
        else:
            self.charset = "abcdefghijklmnopqrstuvwxyzäöüß"

    def correction(self, word):
        """ Find corrected word.

            @param word (str) The suspect word.
            @returns str The corrected word (may be the original word if it
                is found to be correct), or None.
        """
        if word in self.words:
            return word
        candidates = self.candidates(word)
        _log.debug("word: %s, candidates: %s", word, candidates)
        if not candidates:
            return None
        most_probable_candidate = max(
            candidates,
            key=self.word_probabilities.get,
        )
        _log.debug(
            "word: %s, most probable candidate: %s",
            word,
            most_probable_candidate,
        )
        return most_probable_candidate

    def candidates(self, word):
        """ Set of candidates for correct word, based on the suspect word. """
        leven_1 = self.levenshtein_1(word).intersection(self.words)
        if leven_1:
            return leven_1
        if len(word) > 2:
            return self.levenshtein_2(word).intersection(self.words)
        return set()

    def levenshtein_1(self, word):
        """ Candidates with a Levenshtein distance of 1. """
        splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
        inserts = [
            left + ch + right
            for left, right in splits
            for ch in self.charset
        ]
        deletes = [
            left + right[1:]
            for left, right in splits
            if right
        ]
        swaps = [
            left + right[1] + right[0] + right[2:]
            for left, right in splits
            if len(right) > 1
        ]
        replaces = [
            left + ch + right[1:]
            for left, right in splits
            if right
            for ch in self.charset
        ]
        return set(inserts + deletes + swaps + replaces)

    def levenshtein_2(self, word):
        """ Candidates with a Levenshtein distance of 2. """
        return set(
            leven_2
            for leven_1 in self.levenshtein_1(word)
            for leven_2 in self.levenshtein_1(leven_1)
        )
