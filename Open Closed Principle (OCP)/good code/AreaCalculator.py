"""
This class follows the OCP because we can add more shapes (triangle, rombus...) without modifying the AreaCalculator class.
"""

class AreaCalculator:
    def area (self, shape):
        return shape.area()