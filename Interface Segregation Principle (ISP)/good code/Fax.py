"""
This class now follows the ISP because the interface it implements does not have any method that the class doesnt use.
"""

import IFax

class Fax(IFax):
    def fax(self):
        print("Faxing...")