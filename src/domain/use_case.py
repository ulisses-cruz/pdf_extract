from typing import Any
from abc import ABC, abstractmethod


class UseCase(ABC):
    @abstractmethod
    def execute(self, arg: Any) -> Any: pass

