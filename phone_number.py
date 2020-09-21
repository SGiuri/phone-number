import re

class PhoneNumber:

    def __init__(self, number):
        # removing and cleaning everything that in not a a number
        clean_number = re.sub(r"[^0-9]", "", number)

        # checking if there are the initial 1, if so, removing it:
        clean_number = re.sub(r"^1?", "", clean_number)

        # the number must now be in the length of 10
        if len(clean_number)!= 10:
            raise ValueError("Not Valid Number")

        #checking if it is a valid number#
        number_pattern = re.compile("([2-9]{1}[0-9]{2}[2-9]{1}[0-9]{2}[0-9]{4})")
        matches = re.search(number_pattern,clean_number)

        # if valid i found something matching the pattern
        if matches:
            self.number = matches.group(1)
        else:
            raise ValueError("Not Valid Number")

        # isolatging the area code
        self.area_code = self.number[:3]

    def pretty(self):
        """
        A method that return the Phonenumber like this:
        (266)-266-1234
        """

        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"








number = PhoneNumber("+1 (223) 456-7890").number