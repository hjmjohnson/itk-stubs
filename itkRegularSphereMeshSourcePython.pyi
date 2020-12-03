import itk.itkMeshSourcePython
from itk.support import itkHelpers as itkHelpers
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkRegularSphereMeshSourceMF2_New(): ...

class itkRegularSphereMeshSourceMF2(itk.itkMeshSourcePython.itkMeshSourceMF2):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetResolution: Any = ...
    GetResolution: Any = ...
    SetCenter: Any = ...
    GetCenter: Any = ...
    SetScale: Any = ...
    GetScale: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkRegularSphereMeshSourceMF2___New_orig__: Any
itkRegularSphereMeshSourceMF2_cast: Any

def itkRegularSphereMeshSourceMF3_New(): ...

class itkRegularSphereMeshSourceMF3(itk.itkMeshSourcePython.itkMeshSourceMF3):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetResolution: Any = ...
    GetResolution: Any = ...
    SetCenter: Any = ...
    GetCenter: Any = ...
    SetScale: Any = ...
    GetScale: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkRegularSphereMeshSourceMF3___New_orig__: Any
itkRegularSphereMeshSourceMF3_cast: Any

def regular_sphere_mesh_source(*args: Any, **kwargs: Any): ...
def regular_sphere_mesh_source_init_docstring() -> None: ...