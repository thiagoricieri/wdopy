#!/usr/bin/python

import re
from os import walk

# Variables
_data_folder = "data/"

# Data Loader
class SymbolsReader():

    # Select part of the data set to be used
    # after filtering it
    def select(self, selection="all"):
        m_sorted = self.sorted_symbols()
        return m_sorted

    # Sort each value received as how it should
    # be sorted in the first place
    def sorted_symbols(self):
        symbols = self.load_symbols()
        return sorted(symbols, key=lambda s: [s.year, s.month])

    # Load only valid months for each
    # future stock symbol
    def load_symbols(self):
        pf = self.load_folders()
        symbols = [Symbol(f) for f in pf]
        return symbols

    # Load every folder in data that correspond
    # to a month in the asset
    def load_folders(self):
        months = [dn for (_, dn, _) in walk(_data_folder)].pop(0)
        return months

    # Describe contents of data folder
    def walk_data(self):
        for (dirpath, dirnames, filenames) in walk(_data_folder):
            print("Dir {}".format(dirpath))
            print("Dir Name {}".format(dirnames))
            print("File names {}".format(filenames))
            print("\n")


# Symbol to be traded
class Symbol:

    # Automatically create each property
    # based on the string given.
    def __init__(self, code):
        self.code = code
        valid = self.validate_code()
        if not valid:
            raise ValueError("Invalid symbol code: {}".format(self.code))
        else:
            self.month = valid.group(1).upper()
            self.year = valid.group(2)

    # It won't create a Symbol if it does not comply
    # with the pattern WDO + <letter> + <2 mumbers year>
    def validate_code(self):
        return re.match(r'wdo([fghjkmnquvxz])(\d{2})', self.code, re.I | re.M)

    # Easy to read print statements
    def __str__(self):
        return self.code.upper()

    def __repr__(self):
        return self.__str__()