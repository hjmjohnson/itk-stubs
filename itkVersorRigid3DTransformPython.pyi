import itk.itkVersorPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkVersorRigid3DTransformD_New(): ...

class itkVersorRigid3DTransformD(itk.itkVersorTransformPython.itkVersorTransformD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    UpdateTransformParameters: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkVersorRigid3DTransformD___New_orig__: Any
itkVersorRigid3DTransformD_cast: Any
