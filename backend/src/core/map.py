from typing import TypeVar, Callable, Any

T = TypeVar('T')

class Map(dict):
    """
    Extended dict. With some extra util methods
    """

    def compute_if_absent(self, key, callback: Callable[[Any], T]) -> T:
        """
        Like setDefault. But will only evaluate the callback if key is not present.
        """
        if key not in self.keys():
            self[key] = callback(key)
        return self[key]
