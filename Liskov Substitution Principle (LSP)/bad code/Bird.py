"""
LSP: 
Objects should be replaceable with their subtypes without affecting the correctness of the program.

In this example:
This implementation does not follow LSP because a Penguin is a Bird, which can not fly. 
So a Bird could not be replaced with a Penguin without crashing the program.
"""

class Bird:
    def fly (self):
        print("I can fly")