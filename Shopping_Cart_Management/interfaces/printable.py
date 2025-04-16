from abc import ABC, abstractmethod

class ItemPrinter(ABC):
    @abstractmethod
    def print_items(self):
        pass