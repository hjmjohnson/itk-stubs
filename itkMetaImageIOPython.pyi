import itk.stdcomplexPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkMetaImageIO_New(): ...

class itkMetaImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetMetaImagePointer: Any = ...
    SetDataFileName: Any = ...
    SetDoublePrecision: Any = ...
    SetSubSamplingFactor: Any = ...
    GetSubSamplingFactor: Any = ...
    SetDefaultDoublePrecision: Any = ...
    GetDefaultDoublePrecision: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkMetaImageIO___New_orig__: Any
itkMetaImageIO_SetDefaultDoublePrecision: Any
itkMetaImageIO_GetDefaultDoublePrecision: Any
itkMetaImageIO_cast: Any

def itkMetaImageIOFactory_New(): ...

class itkMetaImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    RegisterOneFactory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkMetaImageIOFactory___New_orig__: Any
itkMetaImageIOFactory_RegisterOneFactory: Any
itkMetaImageIOFactory_cast: Any
