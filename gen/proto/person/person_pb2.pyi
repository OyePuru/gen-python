from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PersonWithId(_message.Message):
    __slots__ = ("id", "name", "age")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    age: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class PersonData(_message.Message):
    __slots__ = ("name", "age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class PersonId(_message.Message):
    __slots__ = ("personId",)
    PERSONID_FIELD_NUMBER: _ClassVar[int]
    personId: int
    def __init__(self, personId: _Optional[int] = ...) -> None: ...
