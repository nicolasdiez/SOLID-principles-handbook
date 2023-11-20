"""
DIP: 
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.

In this example:
This implementation does not follow DIP.
Because a high-level module (NotificationService) is dependent on EmailService and SmsService (low-level modules).
Also, low-level modules (EmailService and SmsService) depend on specific implementations, not on an abstraction.

To comply with DIP NotificationService should depend on an abstraction, not on EmailService or SmsService.
Also, low-level modules (EmailService and SmsService) should depend on the same abstraction as the high-level module.
"""

import EmailService
import SmsService

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)