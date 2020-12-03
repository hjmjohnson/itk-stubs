from itk.support import itkTypes as itkTypes
from itk.support.itkTemplate import itkTemplate as itkTemplate, itkTemplateBase as itkTemplateBase
from typing import List, Union

DIMS: List[int]
USIGN_INTS: List[itkTypes.itkCType]
SIGN_INTS: List[itkTypes.itkCType]
REALS: List[itkTypes.itkCType]
VECTOR_REALS: List[itkTemplate]
COV_VECTOR_REALS: List[itkTemplate]
RGBS: List[itkTemplate]
RGBAS: List[itkTemplate]
COMPLEX_REALS: List[itkTemplate]
INTS: List[itkTypes.itkCType]
SCALARS: List[itkTypes.itkCType]
VECTORS: List[itkTemplate]
COLORS: List[itkTemplate]
ALL_TYPES: List[Union[itkTypes.itkCType, itkTemplate]]
