import itk.itkMatrixPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkTranslationTransformD2_New(): ...

class itkTranslationTransformD2(itk.itkTransformBasePython.itkTransformD22):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetOffset: Any = ...
    SetOffset: Any = ...
    Compose: Any = ...
    Translate: Any = ...
    TransformVector: Any = ...
    BackTransform: Any = ...
    GetInverse: Any = ...
    SetIdentity: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkTranslationTransformD2___New_orig__: Any
itkTranslationTransformD2_cast: Any

def itkTranslationTransformD3_New(): ...

class itkTranslationTransformD3(itk.itkTransformBasePython.itkTransformD33):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetOffset: Any = ...
    SetOffset: Any = ...
    Compose: Any = ...
    Translate: Any = ...
    TransformVector: Any = ...
    BackTransform: Any = ...
    GetInverse: Any = ...
    SetIdentity: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkTranslationTransformD3___New_orig__: Any
itkTranslationTransformD3_cast: Any
