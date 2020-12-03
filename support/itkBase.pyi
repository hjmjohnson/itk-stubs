from itk.support.itkTemplate import itkTemplate as itkTemplate
from typing import Any, Dict, Sequence, Union

def create_itk_module(name: str) -> Any: ...
def itk_load_swig_module(name: str, namespace: Any=...) -> Any: ...
def debug_print_error(error: Any) -> None: ...

class LibraryLoader:
    old_path: Any = ...
    old_cwd: Any = ...
    def __init__(self) -> None: ...
    def setup(self) -> None: ...
    def load(self, name: str) -> Any: ...
    def cleanup(self) -> None: ...

class ITKTemplateFeatures:
    def __init__(self, feature_tuple: Sequence[Union[str, bool]]) -> None: ...
    def is_itk_class(self) -> bool: ...
    def get_python_class_name(self) -> str: ...
    def get_cpp_class_name(self) -> str: ...
    def get_swig_class_name(self) -> str: ...
    def get_class_in_module(self) -> bool: ...
    def get_template_parameters(self) -> str: ...

class ITKModuleInfo:
    def __init__(self, path: str, snake_path: str) -> None: ...
    def get_module_dependencies(self) -> Sequence[str]: ...
    def get_all_template_features(self) -> Sequence[ITKTemplateFeatures]: ...
    def get_snake_case_functions(self) -> Sequence[str]: ...

itk_base_global_lazy_attributes: Dict[str, Any]
itk_base_global_module_data: Dict[str, ITKModuleInfo]