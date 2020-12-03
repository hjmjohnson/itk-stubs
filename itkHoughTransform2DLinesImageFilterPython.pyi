import itk.itkContinuousIndexPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkHoughTransform2DLinesImageFilterFF_New(): ...

class itkHoughTransform2DLinesImageFilterFF(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GenerateData: Any = ...
    SetThreshold: Any = ...
    GetThreshold: Any = ...
    SetAngleResolution: Any = ...
    GetAngleResolution: Any = ...
    Simplify: Any = ...
    GetModifiableSimplifyAccumulator: Any = ...
    GetSimplifyAccumulator: Any = ...
    GetLines: Any = ...
    SetNumberOfLines: Any = ...
    GetNumberOfLines: Any = ...
    SetDiscRadius: Any = ...
    GetDiscRadius: Any = ...
    SetVariance: Any = ...
    GetVariance: Any = ...
    IntConvertibleToOutputCheck: Any = ...
    InputGreaterThanFloatCheck: Any = ...
    OutputPlusIntCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkHoughTransform2DLinesImageFilterFF___New_orig__: Any
itkHoughTransform2DLinesImageFilterFF_cast: Any

def hough_transform2_d_lines_image_filter(*args: Any, **kwargs: Any): ...
def hough_transform2_d_lines_image_filter_init_docstring() -> None: ...
