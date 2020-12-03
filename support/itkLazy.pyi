import types
from itk.support import itkBase as itkBase
from typing import Any

not_loaded: str

class LazyITKModule(types.ModuleType):
    def __init__(self, name: Any, lazy_attributes: Any) -> None: ...
    def __getattribute__(self, attr: Any): ...
    def __reduce_ex__(self, proto: Any): ...
