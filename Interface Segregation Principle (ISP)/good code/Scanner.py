"""
This class follows the ISP because the interface it implements does not have any method that the class doesnt use.
"""

import IScanner

class Scanner(IScanner):
    def scan(self):
        print("Scanning...")