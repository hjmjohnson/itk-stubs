import itk.stdcomplexPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkJPEG2000ImageIO_New(): ...

class itkJPEG2000ImageIO(itk.ITKIOImageBaseBasePython.itkStreamingImageIOBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetHeaderSize: Any = ...
    SetTileSize: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkJPEG2000ImageIO___New_orig__: Any
itkJPEG2000ImageIO_cast: Any

def itkJPEG2000ImageIOFactory_New(): ...

class itkJPEG2000ImageIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    FactoryNew: Any = ...
    RegisterOneFactory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkJPEG2000ImageIOFactory___New_orig__: Any
itkJPEG2000ImageIOFactory_FactoryNew: Any
itkJPEG2000ImageIOFactory_RegisterOneFactory: Any
itkJPEG2000ImageIOFactory_cast: Any

class itkJPEG2000ImageIOInternalEnums:
    thisown: Any = ...
    DecodingFormat_J2K_CFMT: Any = ...
    DecodingFormat_JP2_CFMT: Any = ...
    DecodingFormat_JPT_CFMT: Any = ...
    DecodingFormat_MJ2_CFMT: Any = ...
    DFMFormat_PXM_DFMT: Any = ...
    DFMFormat_PGX_DFMT: Any = ...
    DFMFormat_BMP_DFMT: Any = ...
    DFMFormat_YUV_DFMT: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...