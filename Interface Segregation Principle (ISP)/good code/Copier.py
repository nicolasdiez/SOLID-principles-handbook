"""
This class follows the ISP because the interface it implements does not have any method that the class doesnt use.
"""
import ICopier

class Copier(ICopier):
    def copy(self):
        print("Copying...")