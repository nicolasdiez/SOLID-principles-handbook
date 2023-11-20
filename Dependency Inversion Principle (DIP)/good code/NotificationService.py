"""
This high-level class now follows the DIP because it depends on the abstraction IMessageService rather than specific classes EmailService and SmsService.
"""

import EmailService
import SmsService
import IMessageService

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)
        