""" from https://github.com/keithito/tacotron """
from . import cleaners
from .symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}


def _clean_text(text, cleaner_names):
    for name in cleaner_names:
        cleaner = getattr(cleaners, name)
        if not cleaner:
            raise Exception('Unknown cleaner: %s' % name)
        text = cleaner(text)
    return text


def text_to_sequence(text, cleaner_names):
    '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
        Args:
            text: string to convert to a sequence
            cleaner_names: names of the cleaner functions to run the text through
        Returns:
            List of integers corresponding to the symbols in the text
    '''
    sequence = []

    clean_text = _clean_text(text, cleaner_names)
    for symbol in clean_text:
        if symbol not in _symbol_to_id.keys():
            continue
        symbol_id = _symbol_to_id[symbol]
        sequence += [symbol_id]
    return sequence