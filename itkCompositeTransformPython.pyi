import itk.itkArray2DPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkCompositeTransformD2_New(): ...

class itkCompositeTransformD2(itk.itkMultiTransformPython.itkMultiTransformD22):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetNthTransformToOptimize: Any = ...
    SetNthTransformToOptimizeOn: Any = ...
    SetNthTransformToOptimizeOff: Any = ...
    SetAllTransformsToOptimize: Any = ...
    SetAllTransformsToOptimizeOn: Any = ...
    SetAllTransformsToOptimizeOff: Any = ...
    SetOnlyMostRecentTransformToOptimizeOn: Any = ...
    GetNthTransformToOptimize: Any = ...
    GetTransformsToOptimizeFlags: Any = ...
    GetInverse: Any = ...
    TransformVector: Any = ...
    TransformCovariantVector: Any = ...
    TransformDiffusionTensor3D: Any = ...
    TransformSymmetricSecondRankTensor: Any = ...
    UpdateTransformParameters: Any = ...
    FlattenTransformQueue: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkCompositeTransformD2___New_orig__: Any
itkCompositeTransformD2_cast: Any

def itkCompositeTransformD3_New(): ...

class itkCompositeTransformD3(itk.itkMultiTransformPython.itkMultiTransformD33):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetNthTransformToOptimize: Any = ...
    SetNthTransformToOptimizeOn: Any = ...
    SetNthTransformToOptimizeOff: Any = ...
    SetAllTransformsToOptimize: Any = ...
    SetAllTransformsToOptimizeOn: Any = ...
    SetAllTransformsToOptimizeOff: Any = ...
    SetOnlyMostRecentTransformToOptimizeOn: Any = ...
    GetNthTransformToOptimize: Any = ...
    GetTransformsToOptimizeFlags: Any = ...
    GetInverse: Any = ...
    TransformVector: Any = ...
    TransformCovariantVector: Any = ...
    TransformDiffusionTensor3D: Any = ...
    TransformSymmetricSecondRankTensor: Any = ...
    UpdateTransformParameters: Any = ...
    FlattenTransformQueue: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkCompositeTransformD3___New_orig__: Any
itkCompositeTransformD3_cast: Any