@singledispatch
def asdict(data: Union[Semaphore, Enum, Chain, Environs, GitSymbolicReference, IgnoreStr,
                       Logger, MutableMapping, NamedType, Remote],
           convert: bool = ...) -> Union[MappingProxyType, Semaphore]: ...
@asdict.register
def asdict_chain(data: Chain, convert: bool = ...) -> Union[MappingProxyType, Chain]: ...
@asdict.register
def asdict_enum(data: Enum, convert: bool = ...) -> Union[MappingProxyType, Enum]: ...
@asdict.register
def asdict_environs(data: Environs, convert: bool = ...) -> Union[MappingProxyType, Environs]: ...
@asdict.register
def asdict_gettype(data: GetType, convert: bool = ...) -> Union[MappingProxyType, GetType]: ...
@asdict.register
def asdict_gitsymbolic(data: GitSymbolicReference, convert: bool = ...
                       ) -> Union[MappingProxyType, GitSymbolicReference]: ...
@asdict.register
def asdict_logger(data: Logger, convert: bool = ...) -> Union[MappingProxyType, Logger]: ...
@asdict.register
def asdict_namedtype(data: NamedType, convert: bool = ...) -> Union[MappingProxyType, NamedType]: ...
@asdict.register
def asdict_remote(data: Remote, convert: bool = ...) -> Union[MappingProxyType, Remote]: ...
def asdict_ignorestr(data: IgnoreStr, convert: bool = ...) -> Union[str, IgnoreStr]: ...
def asdict_props(data: Any, key: Attr = ..., pprop: bool = ...) -> dict[str, Any]: ...
def asdict_type(data: Type[Enum], convert: bool =  ...) -> Type[Enum]: ...
