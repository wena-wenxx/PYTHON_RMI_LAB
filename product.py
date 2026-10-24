from abc import ABC, abstractmethod


class Product(ABC):
    """Remote interface: every product must have these three methods."""

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getDescription(self) -> str:
        pass

    @abstractmethod
    def getPrice(self) -> float:
        pass
