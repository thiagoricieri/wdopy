#!/usr/bin/python
# Data Library

from os import walk

# Variables
_data_folder = "data/"


# Data Loader
class DataLoader():

    # Select part of the data set to be used
    # after filtering it
    def select(self, selection="all"):
        m_sorted = self.sort_months()
        return m_sorted

    # Sort each value received as how it should
    # be sorted in the first place
    def sort_months(self):
        months = self.load_month_folders()
        return months

    # Load only valid months for each
    # future stock symbol
    def load_month_folders(self):
        folders = self.load_folders()
        return folders

    # Load every folder in data that correspond
    # to a month in the asset
    def load_folders(self):
        months = [dirnames for (_, dirnames, _) in walk(_data_folder)].pop(0)
        return months

    # Describe contents of data folder
    def describe(self):
        for (dirpath, dirnames, filenames) in walk(_data_folder):
            print("Dir {}".format(dirpath))
            print("Dir Name {}".format(dirnames))
            print("File names {}".format(filenames))
            print("\n")