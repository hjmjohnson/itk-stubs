import itk.itkImageToImageFilterCommonPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkLabelImageToLabelMapFilterIUC2LM2_New(): ...

class itkLabelImageToLabelMapFilterIUC2LM2(itk.ITKLabelMapBasePython.itkImageToImageFilterIUC2LM2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetBackgroundValue: Any = ...
    GetBackgroundValue: Any = ...
    SameDimensionCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkLabelImageToLabelMapFilterIUC2LM2___New_orig__: Any
itkLabelImageToLabelMapFilterIUC2LM2_cast: Any

def itkLabelImageToLabelMapFilterIUC3LM3_New(): ...

class itkLabelImageToLabelMapFilterIUC3LM3(itk.ITKLabelMapBasePython.itkImageToImageFilterIUC3LM3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetBackgroundValue: Any = ...
    GetBackgroundValue: Any = ...
    SameDimensionCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkLabelImageToLabelMapFilterIUC3LM3___New_orig__: Any
itkLabelImageToLabelMapFilterIUC3LM3_cast: Any

def itkScanlineFilterCommonIUC2LM2_New(): ...

class itkScanlineFilterCommonIUC2LM2:
    thisown: Any = ...
    __New_orig__: Any = ...
    SameDimension: Any = ...
    def __init__(self, enclosingFilter: itkImageToImageFilterIUC2LM2) -> None: ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkScanlineFilterCommonIUC2LM2___New_orig__: Any
itkScanlineFilterCommonIUC2LM2_cast: Any

def itkScanlineFilterCommonIUC3LM3_New(): ...

class itkScanlineFilterCommonIUC3LM3:
    thisown: Any = ...
    __New_orig__: Any = ...
    SameDimension: Any = ...
    def __init__(self, enclosingFilter: itkImageToImageFilterIUC3LM3) -> None: ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkScanlineFilterCommonIUC3LM3___New_orig__: Any
itkScanlineFilterCommonIUC3LM3_cast: Any

def label_image_to_label_map_filter(*args: Any, **kwargs: Any): ...
def label_image_to_label_map_filter_init_docstring() -> None: ...
