import itk.itkRGBPixelPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkDistanceMetricVF2(itk.itkFunctionBasePython.itkFunctionBaseVF2D):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetOrigin: Any = ...
    GetOrigin: Any = ...
    Evaluate: Any = ...
    SetMeasurementVectorSize: Any = ...
    GetMeasurementVectorSize: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkDistanceMetricVF2_cast: Any

class itkDistanceMetricVF3(itk.itkFunctionBasePython.itkFunctionBaseVF3D):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetOrigin: Any = ...
    GetOrigin: Any = ...
    Evaluate: Any = ...
    SetMeasurementVectorSize: Any = ...
    GetMeasurementVectorSize: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkDistanceMetricVF3_cast: Any
