from ..support import itkBase as itkBase
from ..support.itkExtras import output as output
from ..support.itkTypes import itkCType as itkCType
from collections.abc import Mapping
from typing import Any, Callable, Dict, List, Optional

class itkTemplateBase:
    __template_instantiations_name_to_object__: Dict[str, _SWIG_CALLABLE_TYPE] = ...
    __template_instantiations_object_to_name__: Dict[_SWIG_CALLABLE_TYPE, itkTemplate] = ...
    __named_template_registry__: Dict[str, itkTemplate] = ...

class itkTemplate(Mapping):
    @staticmethod
    def normalizeName(name: str) -> str: ...
    @staticmethod
    def registerNoTpl(name: str, cl: itkTemplate) -> None: ...
    __template__: Any = ...
    __name__: Any = ...
    def __local__init__(self, new_object_name: str) -> None: ...
    def __new__(cls: Any, new_object_name: str) -> itkTemplate: ...
    def __getnewargs_ex__(self): ...
    def __add__(self, paramSetString: str, cl: Callable[..., Any]) -> None: ...
    def __instancecheck__(self, instance: Any) -> bool: ...
    def __find_param__(self, paramSetString: Any) -> List[Any]: ...
    def __getitem__(self, parameters: Any) -> _SWIG_CALLABLE_TYPE: ...
    def __getattr__(self, attr: Any): ...
    def __dir__(self): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def New(self, *args: Any, **kwargs: Any): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key: Any): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def __len__(self): ...
    def GetTypes(self) -> None: ...
    def GetTypesAsList(self): ...

def New(self, *args: Any, **kargs: Any): ...
