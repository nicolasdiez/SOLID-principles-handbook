"""
ISP: 
No client should be forced to depend on methods/interfaces it does not use
"""

class IMultiFunctionDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def copy(self):
        pass

    def fax(self):
        pass