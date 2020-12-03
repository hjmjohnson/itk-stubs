import itk.ITKOptimizersBasePython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkShapePriorSegmentationLevelSetImageFilterIF2IF2F(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF2IF2F):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetShapeFunction: Any = ...
    GetModifiableShapeFunction: Any = ...
    GetShapeFunction: Any = ...
    SetCostFunction: Any = ...
    GetModifiableCostFunction: Any = ...
    GetCostFunction: Any = ...
    SetOptimizer: Any = ...
    GetModifiableOptimizer: Any = ...
    GetOptimizer: Any = ...
    SetInitialParameters: Any = ...
    GetInitialParameters: Any = ...
    SetShapePriorScaling: Any = ...
    GetShapePriorScaling: Any = ...
    SetShapePriorSegmentationFunction: Any = ...
    GetShapePriorSegmentationFunction: Any = ...
    GetCurrentParameters: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkShapePriorSegmentationLevelSetImageFilterIF2IF2F_cast: Any

class itkShapePriorSegmentationLevelSetImageFilterIF3IF3F(itk.itkSegmentationLevelSetImageFilterPython.itkSegmentationLevelSetImageFilterIF3IF3F):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetShapeFunction: Any = ...
    GetModifiableShapeFunction: Any = ...
    GetShapeFunction: Any = ...
    SetCostFunction: Any = ...
    GetModifiableCostFunction: Any = ...
    GetCostFunction: Any = ...
    SetOptimizer: Any = ...
    GetModifiableOptimizer: Any = ...
    GetOptimizer: Any = ...
    SetInitialParameters: Any = ...
    GetInitialParameters: Any = ...
    SetShapePriorScaling: Any = ...
    GetShapePriorScaling: Any = ...
    SetShapePriorSegmentationFunction: Any = ...
    GetShapePriorSegmentationFunction: Any = ...
    GetCurrentParameters: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkShapePriorSegmentationLevelSetImageFilterIF3IF3F_cast: Any

def shape_prior_segmentation_level_set_image_filter(*args: Any, **kwargs: Any): ...
def shape_prior_segmentation_level_set_image_filter_init_docstring() -> None: ...
