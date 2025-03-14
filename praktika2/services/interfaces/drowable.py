from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @classmethod
    def set_object(cls, item):
        if not hasattr(cls, "_objects"):
            cls._objects = []  
        if isinstance(item, Drawable):
            cls._objects.append(item)
            return len(cls._objects) - 1
        else:
            raise ValueError("Об'ъект не  бути намальований")
