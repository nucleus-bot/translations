#!/usr/bin/env python3
import os
from typing import Optional, List


# File reader
class TranslationReader:
    # Intialize the Cursor and all of the lines
    def __init__(self, path: str, raw: bool):
        self.cursor = 0
        self.path = path
        self.comments = raw

        # Read the contents of the properties file
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                self.lines = file.read().splitlines()
        except FileNotFoundError:
            self.lines = []

    # Read the lines of the next value
    def read_next(self) -> Optional[tuple]:
        key = None
        val = ''

        # Poor mans python do-while to read the next key (even an array[]) and it's values (multiline!)
        while True:
            if self.cursor >= len(self.lines):
                break
            line = self.lines[self.cursor]
            self.cursor += 1

            if line.startswith('#') or not line.strip():
                if self.comments:
                    return line, None
                continue

            if key is None:
                split = line.split('=')
                key = split[0].strip()
                if len(split) > 1:
                    val = split[1].strip()
            else:
                val += f'\n{line}'

            if not val.endswith(';\\'):
                break

        if key is None:
            return None
        return key, val


# Get all the keys and values of a properties file
def get_file_key_values(path: str, raw: bool = False) -> List[tuple]:
    entries = []
    reader = TranslationReader(path, raw)
    while (next := reader.read_next()) is not None:
        entries.append(next)
    return entries


# Convert the Tuple-List into a map so that tuple[0] can be read
def as_dict(list: List[tuple]) -> dict:
    map = {}
    for (key, value) in list:
        map[key] = value
    return map


# Const of all the directories to search in
files = []
for folder in ['Bot/en_US', 'Website/en_US']:
    for file in os.listdir(folder):
        files.append(f'{folder}/{file}')

# Const of all supported language-codes
languages = [
    'Empty',
    'ar_SA',
    'bg_BG',
    'ca_ES',
    'cs_CZ',
    'zh_CN',
    'da_DK',
    'nl_NL',
    'en_GB',
    'fa_IR',
    'fi_FI',
    'fr_FR',
    'de_DE',
    'el_GR',
    'he_IL',
    'hi_IN',
    'hu_HU',
    'in_ID',
    'it_IT',
    'ja_JP',
    'ko_KR',
    'ms_MY',
    'nb_NO',
    'pl_PL',
    'pt_BR',
    'ro_RO',
    'ru_RU',
    'sk_SK',
    'es_ES',
    'sv_SE',
    'tr_TR',
    'uk_UA',
    'vi_VN'
]

for language in languages:
    for file in files:
        engl = get_file_key_values(file, True)

        # If the file should be empty, don't bother
        #   reading the file, just print with empty keys
        if language == 'Empty':
            path = file.replace('en_US', language, 1)
            curr = {}
        else:
            path = file.replace('en_US', language)
            curr = as_dict(get_file_key_values(path))

        print(path)
        continue

        output = None

        # Loop over all of the "Tuples" present in the English file
        #   If the 'value' of the tuple is 'None', the line is
        #   a Comment or Blank, and can just be printed directly
        for (key, value) in engl:
            new = None

            if value is None: # Comment/blank
                new = key
            elif key in curr: # Has existing translated value
                new = f'{key} = {curr[key]}'
            else: # A new empty const
                new = f'{key} ='

            if new is not None:
                if output is None:
                    output = f'{new}\n'
                else:
                    output += f'{new}\n'

        if output is not None:
            # Create the languages path if it doesn't exist
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)

            with open(path, 'w', encoding='UTF-8') as writer:
                writer.write(output)
