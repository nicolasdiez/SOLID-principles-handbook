"""
OCP: 
A software component (class, application...) should be Closed for Modification, but Open for Extension.

In this example:
AreaCalculator does not follow OCP because it can not be extended with more shapes without modifying its code.
"""

import Circle
import Rectangle

class AreaCalculator:
    def area (self, shape):
        if isinstance (shape, Circle):
            return 3.14159 * shape.radius**2
        elif isinstance (shape, Rectangle):
            return shape.width * shape.height
        
