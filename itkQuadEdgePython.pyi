from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkQuadEdge:
    thisown: Any = ...
    BeginOnext: Any = ...
    EndOnext: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...
    SetOnext: Any = ...
    SetRot: Any = ...
    GetOnext: Any = ...
    GetRot: Any = ...
    Splice: Any = ...
    GetSym: Any = ...
    GetLnext: Any = ...
    GetRnext: Any = ...
    GetDnext: Any = ...
    GetOprev: Any = ...
    GetLprev: Any = ...
    GetRprev: Any = ...
    GetDprev: Any = ...
    GetInvRot: Any = ...
    GetInvOnext: Any = ...
    GetInvLnext: Any = ...
    GetInvRnext: Any = ...
    GetInvDnext: Any = ...
    IsHalfEdge: Any = ...
    IsIsolated: Any = ...
    IsEdgeInOnextRing: Any = ...
    IsLnextGivenSizeCyclic: Any = ...
    GetOrder: Any = ...
