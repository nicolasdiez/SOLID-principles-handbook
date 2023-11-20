"""
OCP: 
A software component (class, application...) should be Closed for Modification, but Open for Extension.
"""
import Circle
import Rectangle

class AreaCalculator:
    def area (self, shape):
        if isinstance (shape, Circle):
            return 3.14159 * shape.radius**2
        elif isinstance (shape, Rectangle):
            return shape.width * shape.height
        
