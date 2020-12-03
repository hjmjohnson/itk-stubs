import itk.itkImageRegionPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkKdTreeLSVF2_New(): ...

class itkKdTreeLSVF2(itk.ITKCommonBasePython.itkObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetMeasurementVectorSize: Any = ...
    SetBucketSize: Any = ...
    SetSample: Any = ...
    GetSample: Any = ...
    Size: Any = ...
    GetEmptyTerminalNode: Any = ...
    SetRoot: Any = ...
    GetRoot: Any = ...
    GetMeasurementVector: Any = ...
    GetFrequency: Any = ...
    GetDistanceMetric: Any = ...
    Search: Any = ...
    BallWithinBounds: Any = ...
    BoundsOverlapBall: Any = ...
    DeleteNode: Any = ...
    PrintTree: Any = ...
    PlotTree: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkKdTreeLSVF2___New_orig__: Any
itkKdTreeLSVF2_cast: Any

def itkKdTreeLSVF3_New(): ...

class itkKdTreeLSVF3(itk.ITKCommonBasePython.itkObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    GetMeasurementVectorSize: Any = ...
    SetBucketSize: Any = ...
    SetSample: Any = ...
    GetSample: Any = ...
    Size: Any = ...
    GetEmptyTerminalNode: Any = ...
    SetRoot: Any = ...
    GetRoot: Any = ...
    GetMeasurementVector: Any = ...
    GetFrequency: Any = ...
    GetDistanceMetric: Any = ...
    Search: Any = ...
    BallWithinBounds: Any = ...
    BoundsOverlapBall: Any = ...
    DeleteNode: Any = ...
    PrintTree: Any = ...
    PlotTree: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkKdTreeLSVF3___New_orig__: Any
itkKdTreeLSVF3_cast: Any

class itkKdTreeNodeLSVF2:
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    IsTerminal: Any = ...
    GetParameters: Any = ...
    Left: Any = ...
    Right: Any = ...
    Size: Any = ...
    GetWeightedCentroid: Any = ...
    GetCentroid: Any = ...
    GetInstanceIdentifier: Any = ...
    AddInstanceIdentifier: Any = ...
    __swig_destroy__: Any = ...

class itkKdTreeNodeLSVF3:
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    IsTerminal: Any = ...
    GetParameters: Any = ...
    Left: Any = ...
    Right: Any = ...
    Size: Any = ...
    GetWeightedCentroid: Any = ...
    GetCentroid: Any = ...
    GetInstanceIdentifier: Any = ...
    AddInstanceIdentifier: Any = ...
    __swig_destroy__: Any = ...