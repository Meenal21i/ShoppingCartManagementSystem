from abc import ABC, abstractmethod

class ItemAdder(ABC):

    @abstractmethod
    def add_item(self, item_name, quantity):
        pass