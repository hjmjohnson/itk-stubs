import itk.itkMatrixOffsetTransformBasePython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkSimilarity2DTransformD_New(): ...

class itkSimilarity2DTransformD(itk.itkRigid2DTransformPython.itkRigid2DTransformD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetScale: Any = ...
    GetScale: Any = ...
    CloneInverseTo: Any = ...
    GetInverse: Any = ...
    CloneTo: Any = ...
    SetMatrix: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkSimilarity2DTransformD___New_orig__: Any
itkSimilarity2DTransformD_cast: Any
