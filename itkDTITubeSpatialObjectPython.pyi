import itk.itkSpatialObjectPointPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class listitkPointBasedSpatialObjectDTITube3_Pointer(collections.abc.MutableSequence):
    thisown: Any = ...
    iterator: Any = ...
    def __iter__(self) -> Any: ...
    __nonzero__: Any = ...
    __bool__: Any = ...
    __len__: Any = ...
    __getslice__: Any = ...
    __setslice__: Any = ...
    __delslice__: Any = ...
    __delitem__: Any = ...
    __getitem__: Any = ...
    __setitem__: Any = ...
    pop: Any = ...
    append: Any = ...
    empty: Any = ...
    size: Any = ...
    swap: Any = ...
    begin: Any = ...
    end: Any = ...
    rbegin: Any = ...
    rend: Any = ...
    clear: Any = ...
    get_allocator: Any = ...
    pop_back: Any = ...
    erase: Any = ...
    def __init__(self, *args: Any) -> None: ...
    push_back: Any = ...
    front: Any = ...
    back: Any = ...
    assign: Any = ...
    resize: Any = ...
    insert: Any = ...
    pop_front: Any = ...
    push_front: Any = ...
    reverse: Any = ...
    __swig_destroy__: Any = ...

def itkPointBasedSpatialObjectDTITube3_New(): ...

class itkPointBasedSpatialObjectDTITube3(itk.itkSpatialObjectBasePython.itkSpatialObject3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    AddPoint: Any = ...
    RemovePoint: Any = ...
    SetPoints: Any = ...
    GetPoints: Any = ...
    GetPoint: Any = ...
    GetNumberOfPoints: Any = ...
    ClosestPointInWorldSpace: Any = ...
    ClosestPointInObjectSpace: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkPointBasedSpatialObjectDTITube3___New_orig__: Any
itkPointBasedSpatialObjectDTITube3_cast: Any

def itkDTITubeSpatialObject3_Superclass_New(): ...

class itkDTITubeSpatialObject3_Superclass(itkPointBasedSpatialObjectDTITube3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetEndRounded: Any = ...
    GetEndRounded: Any = ...
    EndRoundedOn: Any = ...
    EndRoundedOff: Any = ...
    ComputeTangentsAndNormals: Any = ...
    RemoveDuplicatePointsInObjectSpace: Any = ...
    SetParentPoint: Any = ...
    GetParentPoint: Any = ...
    SetRoot: Any = ...
    GetRoot: Any = ...
    RootOn: Any = ...
    RootOff: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkDTITubeSpatialObject3_Superclass___New_orig__: Any
itkDTITubeSpatialObject3_Superclass_cast: Any

def itkDTITubeSpatialObject3_New(): ...

class itkDTITubeSpatialObject3(itkDTITubeSpatialObject3_Superclass):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkDTITubeSpatialObject3___New_orig__: Any
itkDTITubeSpatialObject3_cast: Any
