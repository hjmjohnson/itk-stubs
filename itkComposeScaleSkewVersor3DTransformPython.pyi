import itk.itkVersorPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkComposeScaleSkewVersor3DTransformD_New(): ...

class itkComposeScaleSkewVersor3DTransformD(itk.itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetMatrix: Any = ...
    SetScale: Any = ...
    GetScale: Any = ...
    SetSkew: Any = ...
    GetSkew: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkComposeScaleSkewVersor3DTransformD___New_orig__: Any
itkComposeScaleSkewVersor3DTransformD_cast: Any
