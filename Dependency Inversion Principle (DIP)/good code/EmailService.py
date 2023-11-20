"""
This low-level class now follows the DIP because it depends on the abstraction IMessageService.
"""

import IMessageService

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")