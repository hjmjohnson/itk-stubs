import itk.itkFixedArrayPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkBMPImageIO_New(): ...

class itkBMPImageIO(itk.ITKIOImageBaseBasePython.itkImageIOBase):
    thisown: Any = ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetFileLowerLeft: Any = ...
    GetBMPCompression: Any = ...
    GetColorPalette: Any = ...
    def __init__(self) -> None: ...
    PrintSelf: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBMPImageIO___New_orig__: Any
itkBMPImageIO_cast: Any

def itkBMPImageIOFactory_New(): ...

class itkBMPImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    RegisterOneFactory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBMPImageIOFactory___New_orig__: Any
itkBMPImageIOFactory_RegisterOneFactory: Any
itkBMPImageIOFactory_cast: Any
