import itk.itkVersorPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkVersorTransformD_New(): ...

class itkVersorTransformD(itk.itkRigid3DTransformPython.itkRigid3DTransformD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetRotation: Any = ...
    GetVersor: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkVersorTransformD___New_orig__: Any
itkVersorTransformD_cast: Any
