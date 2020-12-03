import itk.itkTransformIOBaseTemplatePython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

def itkTransformFileWriterTemplateF_New(): ...

class itkTransformFileWriterTemplateF(itk.ITKCommonBasePython.itkLightProcessObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __New_orig__: Any = ...
    Clone: Any = ...
    SetFileName: Any = ...
    GetFileName: Any = ...
    SetAppendOff: Any = ...
    SetAppendOn: Any = ...
    SetAppendMode: Any = ...
    GetAppendMode: Any = ...
    SetUseCompression: Any = ...
    GetUseCompression: Any = ...
    UseCompressionOn: Any = ...
    UseCompressionOff: Any = ...
    SetInput: Any = ...
    GetInput: Any = ...
    AddTransform: Any = ...
    Update: Any = ...
    SetTransformIO: Any = ...
    GetTransformIO: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...
    def New(*args: Any, **kargs: Any): ...
    New: Any = ...

itkTransformFileWriterTemplateF___New_orig__: Any
itkTransformFileWriterTemplateF_cast: Any