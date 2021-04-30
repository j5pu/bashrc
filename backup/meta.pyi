from types import GenericAlias
from typing import Any
from typing import Optional
from typing import overload


class Meta(type):
    _rv: list = ...
    infocls: Optional[InfoCls] = ...
    @overload
    def __new__(mcs, o: object) -> type: ...
    @overload
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> type: ...
    @property
    def rv(self) -> Any: ...
    @rv.setter
    def rv(self, value: Any) -> None: ...
    @rv.deleter
    def rv(self) -> None: ...
    __class_getitem__ = classmethod(GenericAlias)
