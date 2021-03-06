import itk.itkRGBPixelPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkBlockMatchingImageFilterIF3_Superclass_Superclass_New(): ...

class itkBlockMatchingImageFilterIF3_Superclass_Superclass(itk.ITKCommonBasePython.itkProcessObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetOutput: Any = ...
    SetOutput: Any = ...
    GraftOutput: Any = ...
    GraftNthOutput: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBlockMatchingImageFilterIF3_Superclass_Superclass___New_orig__: Any
itkBlockMatchingImageFilterIF3_Superclass_Superclass_cast: Any

def itkPointSetVF33_New(): ...

class itkPointSetVF33(itk.ITKCommonBasePython.itkDataObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetMaximumNumberOfRegions: Any = ...
    PassStructure: Any = ...
    GetNumberOfPoints: Any = ...
    SetPoints: Any = ...
    GetPoints: Any = ...
    SetPoint: Any = ...
    GetPoint: Any = ...
    SetPointData: Any = ...
    GetPointData: Any = ...
    SetRequestedRegion: Any = ...
    GetRequestedRegion: Any = ...
    SetBufferedRegion: Any = ...
    GetBufferedRegion: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkPointSetVF33___New_orig__: Any
itkPointSetVF33_cast: Any

def itkBlockMatchingImageFilterIF3_Superclass_New(): ...

class itkBlockMatchingImageFilterIF3_Superclass(itkBlockMatchingImageFilterIF3_Superclass_Superclass):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetInput: Any = ...
    GetInput: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBlockMatchingImageFilterIF3_Superclass___New_orig__: Any
itkBlockMatchingImageFilterIF3_Superclass_cast: Any

def itkBlockMatchingImageFilterIF3_New(): ...

class itkBlockMatchingImageFilterIF3(itkBlockMatchingImageFilterIF3_Superclass):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetBlockRadius: Any = ...
    GetBlockRadius: Any = ...
    SetSearchRadius: Any = ...
    GetSearchRadius: Any = ...
    SetFixedImage: Any = ...
    GetFixedImage: Any = ...
    SetMovingImage: Any = ...
    GetMovingImage: Any = ...
    SetFeaturePoints: Any = ...
    GetFeaturePoints: Any = ...
    GetDisplacements: Any = ...
    GetSimilarities: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBlockMatchingImageFilterIF3___New_orig__: Any
itkBlockMatchingImageFilterIF3_cast: Any

def mesh_to_mesh_filter(*args: Any, **kwargs: Any): ...
def mesh_to_mesh_filter_init_docstring() -> None: ...
def mesh_source(*args: Any, **kwargs: Any): ...
def mesh_source_init_docstring() -> None: ...
def block_matching_image_filter(*args: Any, **kwargs: Any): ...
def block_matching_image_filter_init_docstring() -> None: ...
