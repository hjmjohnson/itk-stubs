import itk.itkLevelSetFunctionPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkNarrowBandLevelSetImageFilterIF2IF2F(itk.itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF2IF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetFeatureImage: Any = ...
    GetFeatureImage: Any = ...
    SetInitialImage: Any = ...
    GetSpeedImage: Any = ...
    GetAdvectionImage: Any = ...
    SetUseNegativeFeaturesOn: Any = ...
    SetUseNegativeFeaturesOff: Any = ...
    SetUseNegativeFeatures: Any = ...
    GetUseNegativeFeatures: Any = ...
    SetReverseExpansionDirection: Any = ...
    GetReverseExpansionDirection: Any = ...
    ReverseExpansionDirectionOn: Any = ...
    ReverseExpansionDirectionOff: Any = ...
    SetFeatureScaling: Any = ...
    SetPropagationScaling: Any = ...
    GetPropagationScaling: Any = ...
    SetAdvectionScaling: Any = ...
    GetAdvectionScaling: Any = ...
    SetCurvatureScaling: Any = ...
    GetCurvatureScaling: Any = ...
    SetSegmentationFunction: Any = ...
    GetSegmentationFunction: Any = ...
    SetMaximumIterations: Any = ...
    GetMaximumIterations: Any = ...
    OutputHasNumericTraitsCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkNarrowBandLevelSetImageFilterIF2IF2F_cast: Any

class itkNarrowBandLevelSetImageFilterIF3IF3F(itk.itkNarrowBandImageFilterBasePython.itkNarrowBandImageFilterBaseIF3IF3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetFeatureImage: Any = ...
    GetFeatureImage: Any = ...
    SetInitialImage: Any = ...
    GetSpeedImage: Any = ...
    GetAdvectionImage: Any = ...
    SetUseNegativeFeaturesOn: Any = ...
    SetUseNegativeFeaturesOff: Any = ...
    SetUseNegativeFeatures: Any = ...
    GetUseNegativeFeatures: Any = ...
    SetReverseExpansionDirection: Any = ...
    GetReverseExpansionDirection: Any = ...
    ReverseExpansionDirectionOn: Any = ...
    ReverseExpansionDirectionOff: Any = ...
    SetFeatureScaling: Any = ...
    SetPropagationScaling: Any = ...
    GetPropagationScaling: Any = ...
    SetAdvectionScaling: Any = ...
    GetAdvectionScaling: Any = ...
    SetCurvatureScaling: Any = ...
    GetCurvatureScaling: Any = ...
    SetSegmentationFunction: Any = ...
    GetSegmentationFunction: Any = ...
    SetMaximumIterations: Any = ...
    GetMaximumIterations: Any = ...
    OutputHasNumericTraitsCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkNarrowBandLevelSetImageFilterIF3IF3F_cast: Any

def narrow_band_level_set_image_filter(*args: Any, **kwargs: Any): ...
def narrow_band_level_set_image_filter_init_docstring() -> None: ...
