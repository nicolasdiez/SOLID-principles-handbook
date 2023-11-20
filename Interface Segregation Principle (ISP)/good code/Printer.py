"""
This class follows the ISP because the interface it implements does not have any method that the class doesnt use.
"""

import IPrinter

class Printer(IPrinter):
    def print(self):
        print("Printing...")