"""
ISP: 
No client should be forced to depend on methods/interfaces that it does not use.

In this example:
This implementation does not follow ISP.
Because Fax, Printer, Scananer and Copier depend on IMultiFunctionDevice, which is an interface with methods that no all of them use.
Each entity should only depend on an interface with methods that apply to it (eg: a Printer can not scan, a Fax can not print...). 
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