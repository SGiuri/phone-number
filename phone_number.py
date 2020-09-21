"""
The format is usually represented as

(NXX)-NXX-XXXX
where N is any digit from 2 through 9 and X is any digit from 0 through 9.

Your task is to clean up differently formatted telephone numbers by removing punctuation and the country code (1) if present.

For example, the inputs

+1 (613)-995-0253
613-995-0253
1 613 995 0253
613.995.0253
should all produce the output

6139950253
"""

import re

class PhoneNumber:
    def __init__(self, number):
        # removing and cleaning from not numbers
        clean_number = re.sub(r"[^0-9]", "", number)

        # checking if there are the initial 1:
        clean_number = re.sub(r"^1?", "", clean_number)
        if len(clean_number)!= 10:
            raise ValueError("Not Valid Number")
        #checking if it is a valid number#
        number_pattern = re.compile("([2-9]{1}[0-9]{2}[2-9]{1}[0-9]{2}[0-9]{4})")
        matches = re.search(number_pattern,clean_number)

        if matches:
            self.number = matches.group(1)
        else:
            raise ValueError("Not Valid Number")

        self.area_code = self.number[:3]

    def pretty(self):

        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"








number = PhoneNumber("+1 (223) 456-7890").number