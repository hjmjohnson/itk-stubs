import itk.itkContinuousIndexPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class vectoritkDTITubeSpatialObjectPoint3:
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
    reserve: Any = ...
    capacity: Any = ...
    __swig_destroy__: Any = ...

class itkDTITubeSpatialObjectPoint3(itk.itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3):
    thisown: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...
    SetTensorMatrix: Any = ...
    GetTensorMatrix: Any = ...
    AddField: Any = ...
    SetField: Any = ...
    GetFields: Any = ...
    GetField: Any = ...

class itkDTITubeSpatialObjectPointEnums:
    thisown: Any = ...
    DTITubeSpatialObjectPointField_FA: Any = ...
    DTITubeSpatialObjectPointField_ADC: Any = ...
    DTITubeSpatialObjectPointField_GA: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...