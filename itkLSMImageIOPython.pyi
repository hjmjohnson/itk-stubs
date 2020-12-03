import itk.itkFixedArrayPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkLSMImageIO_New(): ...

class itkLSMImageIO(itk.itkTIFFImageIOPython.itkTIFFImageIO):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkLSMImageIO___New_orig__: Any
itkLSMImageIO_cast: Any

def itkLSMImageIOFactory_New(): ...

class itkLSMImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    RegisterOneFactory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkLSMImageIOFactory___New_orig__: Any
itkLSMImageIOFactory_RegisterOneFactory: Any
itkLSMImageIOFactory_cast: Any