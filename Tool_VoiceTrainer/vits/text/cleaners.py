'''
Edited
'''

'''
Cleaners are transformations that run over the input text at both training and eval time.

Cleaners can be selected by passing a comma-delimited list of cleaner names as the "cleaners"
hyperparameter. Some cleaners are English-specific. You'll typically want to use:
  1. "english_cleaners" for English text
  2. "transliteration_cleaners" for non-English text that can be transliterated to ASCII using
     the Unidecode library (https://pypi.python.org/pypi/Unidecode)
  3. "basic_cleaners" if you do not want to transliterate (in this case, you should also update
     the symbols in symbols.py to match your data).
'''

import re

from .mandarin import number_to_chinese, chinese_to_bopomofo, latin_to_bopomofo, chinese_to_ipa#, chinese_to_ipa2
from .english import english_to_ipa2#, english_to_lazy_ipa2
#from .chinesedialect import chinesedialect_to_ipa


def mandarin_cleaners(text):
   '''Pipeline for Chinese text'''
   text = number_to_chinese(text)
   text = chinese_to_bopomofo(text)
   text = latin_to_bopomofo(text)
   text = re.sub(
      pattern = r'([ˉˊˇˋ˙])$',
      repl = r'\1。',
      string = text
   )
   return text


def mandarin_english_cleaners(text):
   text = re.sub(
      pattern = r'\[ZH\](.*?)\[ZH\]',
      repl = lambda x: chinese_to_ipa(x.group(1)) + ' ',
      string = text
   )
   text = re.sub(
      pattern = r'\[EN\](.*?)\[EN\]',
      repl = lambda x: english_to_ipa2(x.group(1)) + ' ',
      string = text
   )
   text = re.sub(
      pattern = r'\s+$',
      repl = '',
      string = text
   )
   text = re.sub(
      pattern = r'([^\.,!\?\-…~])$',
      repl = r'\1.',
      string = text
   )
   return text


'''
def mandarin_english_chinesedialect_cleaners(text):
   text = re.sub(
      pattern = r'\[ZH\](.*?)\[ZH\]',
      repl = lambda x: chinese_to_ipa2(x.group(1)) + ' ',
      string = text
   )
   text = re.sub(
      pattern = r'\[EN\](.*?)\[EN\]',
      repl = lambda x: english_to_lazy_ipa2(x.group(1)) + ' ',
      string = text
   )
   text = re.sub(
      pattern = r'\[([A-Z]{2})\](.*?)\[\1\]',
      repl = lambda x: chinesedialect_to_ipa(x.group(2), x.group(1)).replace('ʣ', 'dz').replace('ʥ', 'dʑ').replace('ʦ', 'ts').replace('ʨ', 'tɕ') + ' ',
      string = text
   )
   text = re.sub(
      pattern = r'\s+$',
      repl = '',
      string = text
   )
   text = re.sub(
      pattern = r'([^\.,!\?\-…~])$',
      repl = r'\1.',
      string = text
   )
   return text
'''