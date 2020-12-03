import itk.itkImageToImageFilterAPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkCurvatureFlowImageFilterIF2IF2_New(): ...

class itkCurvatureFlowImageFilterIF2IF2(itk.itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterIF2IF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetTimeStep: Any = ...
    GetTimeStep: Any = ...
    DoubleConvertibleToOutputCheck: Any = ...
    OutputConvertibleToDoubleCheck: Any = ...
    OutputDivisionOperatorsCheck: Any = ...
    DoubleOutputMultiplyOperatorCheck: Any = ...
    IntOutputMultiplyOperatorCheck: Any = ...
    OutputLessThanDoubleCheck: Any = ...
    OutputDoubleAdditiveOperatorsCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkCurvatureFlowImageFilterIF2IF2___New_orig__: Any
itkCurvatureFlowImageFilterIF2IF2_cast: Any

def itkCurvatureFlowImageFilterIF3IF3_New(): ...

class itkCurvatureFlowImageFilterIF3IF3(itk.itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterIF3IF3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetTimeStep: Any = ...
    GetTimeStep: Any = ...
    DoubleConvertibleToOutputCheck: Any = ...
    OutputConvertibleToDoubleCheck: Any = ...
    OutputDivisionOperatorsCheck: Any = ...
    DoubleOutputMultiplyOperatorCheck: Any = ...
    IntOutputMultiplyOperatorCheck: Any = ...
    OutputLessThanDoubleCheck: Any = ...
    OutputDoubleAdditiveOperatorsCheck: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkCurvatureFlowImageFilterIF3IF3___New_orig__: Any
itkCurvatureFlowImageFilterIF3IF3_cast: Any

def curvature_flow_image_filter(*args: Any, **kwargs: Any): ...
def curvature_flow_image_filter_init_docstring() -> None: ...