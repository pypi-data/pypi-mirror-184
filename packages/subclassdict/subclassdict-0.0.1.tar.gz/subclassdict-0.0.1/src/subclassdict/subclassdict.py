from typedict import TypeDict
from typing import Any, Hashable


class HashableType(Hashable, type):
    ...


class SubclassDict(TypeDict):
    def __getitem__(self, value: HashableType) -> Any:
        try:
            out = self[value]
        except KeyError as e:
            super_key = self._get_super_key(value)
            if super_key is not None:
                return self[super_key]
            raise e
        return out

    def __setitem__(self, key: HashableType, value: Any) -> None:
        try:
            self[key]
        except KeyError as e:
            super_key = self._get_super_key(key)
            if super_key is not None:
                self[super_key] = value
        else:
            self[key] = value
        
    def _get_super_key(self, value) -> HashableType | None:
        for key in self.data:
            if issubclass(value, key):
                return key
        return None
