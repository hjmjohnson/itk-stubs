import itk.pyBasePython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkNormalVariateGenerator_New(): ...

class itkNormalVariateGenerator(itk.ITKCommonBasePython.itkRandomVariateGeneratorBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    Initialize: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkNormalVariateGenerator___New_orig__: Any
itkNormalVariateGenerator_cast: Any
