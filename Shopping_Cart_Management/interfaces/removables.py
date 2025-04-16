from abc import ABC, abstractmethod

class ItemRemover(ABC):
    
    @abstractmethod
    def remove_item(self):
        pass