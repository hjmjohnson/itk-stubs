import itk.itkVariableLengthVectorPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkSobelEdgeDetectionImageFilterIF2IF2_New(): ...

class itkSobelEdgeDetectionImageFilterIF2IF2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GenerateInputRequestedRegion: Any = ...
    SameDimensionCheck: Any = ...
    OutputHasNumericTraitsCheck: Any = ...
    OutputPixelIsFloatingPointCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkSobelEdgeDetectionImageFilterIF2IF2___New_orig__: Any
itkSobelEdgeDetectionImageFilterIF2IF2_cast: Any

def itkSobelEdgeDetectionImageFilterIF3IF3_New(): ...

class itkSobelEdgeDetectionImageFilterIF3IF3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GenerateInputRequestedRegion: Any = ...
    SameDimensionCheck: Any = ...
    OutputHasNumericTraitsCheck: Any = ...
    OutputPixelIsFloatingPointCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkSobelEdgeDetectionImageFilterIF3IF3___New_orig__: Any
itkSobelEdgeDetectionImageFilterIF3IF3_cast: Any

def sobel_edge_detection_image_filter(*args: Any, **kwargs: Any): ...
def sobel_edge_detection_image_filter_init_docstring() -> None: ...