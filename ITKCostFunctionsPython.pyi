import itk.itkArray2DPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkMultipleValuedCostFunction(itk.itkCostFunctionPython.itkCostFunctionTemplateD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    GetValue: Any = ...
    GetNumberOfValues: Any = ...
    GetDerivative: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkMultipleValuedCostFunction_cast: Any

class itkMultipleValuedVnlCostFunctionAdaptor(itk.vnl_least_squares_functionPython.vnl_least_squares_function):
    thisown: Any = ...
    SetCostFunction: Any = ...
    GetCostFunction: Any = ...
    compute: Any = ...
    ConvertExternalToInternalGradient: Any = ...
    ConvertExternalToInternalMeasures: Any = ...
    SetUseGradient: Any = ...
    UseGradientOn: Any = ...
    UseGradientOff: Any = ...
    GetUseGradient: Any = ...
    SetScales: Any = ...
    AddObserver: Any = ...
    GetCachedValue: Any = ...
    GetCachedDerivative: Any = ...
    GetCachedCurrentParameters: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

class itkSingleValuedCostFunction(itk.itkCostFunctionPython.itkCostFunctionTemplateD):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    GetValue: Any = ...
    GetDerivative: Any = ...
    GetValueAndDerivative: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkSingleValuedCostFunction_cast: Any

class itkSingleValuedVnlCostFunctionAdaptor(itk.vnl_cost_functionPython.vnl_cost_function):
    thisown: Any = ...
    SetCostFunction: Any = ...
    GetCostFunction: Any = ...
    ConvertExternalToInternalGradient: Any = ...
    SetScales: Any = ...
    SetNegateCostFunction: Any = ...
    GetNegateCostFunction: Any = ...
    NegateCostFunctionOn: Any = ...
    NegateCostFunctionOff: Any = ...
    AddObserver: Any = ...
    GetCachedValue: Any = ...
    GetCachedDerivative: Any = ...
    GetCachedCurrentParameters: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

def itkCumulativeGaussianCostFunction_New(): ...

class itkCumulativeGaussianCostFunction(itkMultipleValuedCostFunction):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SpaceDimension: Any = ...
    GetValuePointer: Any = ...
    CalculateFitError: Any = ...
    EvaluateCumulativeGaussian: Any = ...
    Initialize: Any = ...
    SetOriginalDataArray: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkCumulativeGaussianCostFunction___New_orig__: Any
itkCumulativeGaussianCostFunction_cast: Any
