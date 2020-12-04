import itk.itkFastMarchingStoppingCriterionBasePython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkFastMarchingImageFilterEnums:
    thisown: Any = ...
    Label_FarPoint: Any = ...
    Label_AlivePoint: Any = ...
    Label_TrialPoint: Any = ...
    Label_InitialTrialPoint: Any = ...
    Label_OutsidePoint: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

def itkFastMarchingImageFilterIF2IF2_New(): ...

class itkFastMarchingImageFilterIF2IF2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetOutsidePoints: Any = ...
    SetAlivePoints: Any = ...
    GetAlivePoints: Any = ...
    SetTrialPoints: Any = ...
    GetTrialPoints: Any = ...
    GetLabelImage: Any = ...
    SetSpeedConstant: Any = ...
    GetSpeedConstant: Any = ...
    SetNormalizationFactor: Any = ...
    GetNormalizationFactor: Any = ...
    SetStoppingValue: Any = ...
    GetStoppingValue: Any = ...
    SetCollectPoints: Any = ...
    GetCollectPoints: Any = ...
    CollectPointsOn: Any = ...
    CollectPointsOff: Any = ...
    GetProcessedPoints: Any = ...
    SetOutputSize: Any = ...
    GetOutputSize: Any = ...
    SetOutputRegion: Any = ...
    GetOutputRegion: Any = ...
    SetOutputSpacing: Any = ...
    GetOutputSpacing: Any = ...
    SetOutputDirection: Any = ...
    GetOutputDirection: Any = ...
    SetOutputOrigin: Any = ...
    GetOutputOrigin: Any = ...
    SetOverrideOutputInformation: Any = ...
    GetOverrideOutputInformation: Any = ...
    OverrideOutputInformationOn: Any = ...
    OverrideOutputInformationOff: Any = ...
    SameDimensionCheck: Any = ...
    SpeedConvertibleToDoubleCheck: Any = ...
    DoubleConvertibleToLevelSetCheck: Any = ...
    LevelSetOStreamWritableCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkFastMarchingImageFilterIF2IF2___New_orig__: Any
itkFastMarchingImageFilterIF2IF2_cast: Any

def itkFastMarchingImageFilterIF3IF3_New(): ...

class itkFastMarchingImageFilterIF3IF3(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetOutsidePoints: Any = ...
    SetAlivePoints: Any = ...
    GetAlivePoints: Any = ...
    SetTrialPoints: Any = ...
    GetTrialPoints: Any = ...
    GetLabelImage: Any = ...
    SetSpeedConstant: Any = ...
    GetSpeedConstant: Any = ...
    SetNormalizationFactor: Any = ...
    GetNormalizationFactor: Any = ...
    SetStoppingValue: Any = ...
    GetStoppingValue: Any = ...
    SetCollectPoints: Any = ...
    GetCollectPoints: Any = ...
    CollectPointsOn: Any = ...
    CollectPointsOff: Any = ...
    GetProcessedPoints: Any = ...
    SetOutputSize: Any = ...
    GetOutputSize: Any = ...
    SetOutputRegion: Any = ...
    GetOutputRegion: Any = ...
    SetOutputSpacing: Any = ...
    GetOutputSpacing: Any = ...
    SetOutputDirection: Any = ...
    GetOutputDirection: Any = ...
    SetOutputOrigin: Any = ...
    GetOutputOrigin: Any = ...
    SetOverrideOutputInformation: Any = ...
    GetOverrideOutputInformation: Any = ...
    OverrideOutputInformationOn: Any = ...
    OverrideOutputInformationOff: Any = ...
    SameDimensionCheck: Any = ...
    SpeedConvertibleToDoubleCheck: Any = ...
    DoubleConvertibleToLevelSetCheck: Any = ...
    LevelSetOStreamWritableCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkFastMarchingImageFilterIF3IF3___New_orig__: Any
itkFastMarchingImageFilterIF3IF3_cast: Any

def fast_marching_image_filter(*args: Any, **kwargs: Any): ...
def fast_marching_image_filter_init_docstring() -> None: ...
