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
        self.number = number
        pattern = re.compile(r"(/+)?1?[2-9][0-9]{2}")

        pass
