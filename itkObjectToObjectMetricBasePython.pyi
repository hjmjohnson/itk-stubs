import itk.itkCostFunctionPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkObjectToObjectMetricBaseTemplateD(itk.itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetFixedObject: Any = ...
    GetFixedObject: Any = ...
    SetMovingObject: Any = ...
    GetMovingObject: Any = ...
    SetGradientSource: Any = ...
    GetGradientSource: Any = ...
    GetGradientSourceIncludesFixed: Any = ...
    GetGradientSourceIncludesMoving: Any = ...
    Initialize: Any = ...
    GetDerivative: Any = ...
    GetNumberOfLocalParameters: Any = ...
    SetParameters: Any = ...
    GetParameters: Any = ...
    HasLocalSupport: Any = ...
    UpdateTransformParameters: Any = ...
    GetCurrentValue: Any = ...
    GetMetricCategory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkObjectToObjectMetricBaseTemplateD_cast: Any

class itkObjectToObjectMetricBaseTemplateEnums:
    thisown: Any = ...
    GradientSource_GRADIENT_SOURCE_FIXED: Any = ...
    GradientSource_GRADIENT_SOURCE_MOVING: Any = ...
    GradientSource_GRADIENT_SOURCE_BOTH: Any = ...
    MetricCategory_UNKNOWN_METRIC: Any = ...
    MetricCategory_OBJECT_METRIC: Any = ...
    MetricCategory_IMAGE_METRIC: Any = ...
    MetricCategory_POINT_SET_METRIC: Any = ...
    MetricCategory_MULTI_METRIC: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

class itkObjectToObjectMetricBaseTemplateF(itk.itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetFixedObject: Any = ...
    GetFixedObject: Any = ...
    SetMovingObject: Any = ...
    GetMovingObject: Any = ...
    SetGradientSource: Any = ...
    GetGradientSource: Any = ...
    GetGradientSourceIncludesFixed: Any = ...
    GetGradientSourceIncludesMoving: Any = ...
    Initialize: Any = ...
    GetDerivative: Any = ...
    GetNumberOfLocalParameters: Any = ...
    SetParameters: Any = ...
    GetParameters: Any = ...
    HasLocalSupport: Any = ...
    UpdateTransformParameters: Any = ...
    GetCurrentValue: Any = ...
    GetMetricCategory: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkObjectToObjectMetricBaseTemplateF_cast: Any
