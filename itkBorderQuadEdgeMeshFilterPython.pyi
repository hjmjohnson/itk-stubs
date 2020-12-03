import itk.itkImageRegionPython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkBorderQuadEdgeMeshFilterEnums:
    thisown: Any = ...
    BorderTransform_SQUARE_BORDER_TRANSFORM: Any = ...
    BorderTransform_DISK_BORDER_TRANSFORM: Any = ...
    BorderPick_LONGEST: Any = ...
    BorderPick_LARGEST: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

def itkBorderQuadEdgeMeshFilterQEMD2_New(): ...

class itkBorderQuadEdgeMeshFilterQEMD2(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetTransformType: Any = ...
    GetTransformType: Any = ...
    SetBorderPick: Any = ...
    GetBorderPick: Any = ...
    SetRadius: Any = ...
    GetRadius: Any = ...
    ComputeTransform: Any = ...
    GetBoundaryPtMap: Any = ...
    GetBorder: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBorderQuadEdgeMeshFilterQEMD2___New_orig__: Any
itkBorderQuadEdgeMeshFilterQEMD2_cast: Any

def itkBorderQuadEdgeMeshFilterQEMD3_New(): ...

class itkBorderQuadEdgeMeshFilterQEMD3(itk.itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetTransformType: Any = ...
    GetTransformType: Any = ...
    SetBorderPick: Any = ...
    GetBorderPick: Any = ...
    SetRadius: Any = ...
    GetRadius: Any = ...
    ComputeTransform: Any = ...
    GetBoundaryPtMap: Any = ...
    GetBorder: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkBorderQuadEdgeMeshFilterQEMD3___New_orig__: Any
itkBorderQuadEdgeMeshFilterQEMD3_cast: Any

def border_quad_edge_mesh_filter(*args: Any, **kwargs: Any): ...
def border_quad_edge_mesh_filter_init_docstring() -> None: ...