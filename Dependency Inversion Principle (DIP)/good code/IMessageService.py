from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass