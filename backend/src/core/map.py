from typing import TypeVar, Callable, Any

T = TypeVar('T')


class Map(dict):
    """
    Extended dict. With some extra util methods
    """

    def compute_if_absent(self, key, callback: Callable[[Any], T] | Callable[[], T], key_callback=True) -> T:
        """
        Like setDefault. But will only evaluate the callback if key is not present.
        optionally provide if the callback is called with the key argument. True by default.
        """
        if key not in self.keys():
            self[key] = callback(key) if key_callback else callback()
        return self.get(key, None)


class ListMultiMap(Map):
    def __setitem__(self, key, value):
        if not isinstance(value, list):
            raise ValueError("Values of ListMultiMaps have to be list")
        return super().__setitem__(key, value)

    def add(self, key, val) -> "ListMultiMap":
        self.compute_if_absent(key, list, key_callback=False).append(val)
        return self
