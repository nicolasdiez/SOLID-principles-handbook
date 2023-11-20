import Shape

class Rectangle (Shape):
    def __init_ (self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height