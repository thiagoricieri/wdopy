#!/usr/bin/python

import re

class Symbol:

    def __init__(self, code):
        self.code = code
        valid = self.validate_code()
        if not valid:
            raise ValueError("Invalid symbol code: {}".format(self.code))
        else:
            self.month = valid.group(1).upper()
            self.year = valid.group(2)

    def validate_code(self):
        return re.match(r'wdo([fghjkmnquvxz])(\d{2})', self.code, re.I | re.M)
