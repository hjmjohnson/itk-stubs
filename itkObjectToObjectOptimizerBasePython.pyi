import itk.itkCostFunctionPython
from typing import Any

class _SwigNonDynamicMeta(type):
    __setattr__: Any = ...

class itkObjectToObjectOptimizerBaseTemplateD(itk.ITKCommonBasePython.itkObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetMetric: Any = ...
    GetModifiableMetric: Any = ...
    GetMetric: Any = ...
    GetCurrentMetricValue: Any = ...
    GetValue: Any = ...
    SetScales: Any = ...
    GetScales: Any = ...
    GetScalesAreIdentity: Any = ...
    SetWeights: Any = ...
    GetWeights: Any = ...
    GetWeightsAreIdentity: Any = ...
    GetScalesInitialized: Any = ...
    SetScalesEstimator: Any = ...
    SetDoEstimateScales: Any = ...
    GetDoEstimateScales: Any = ...
    DoEstimateScalesOn: Any = ...
    DoEstimateScalesOff: Any = ...
    SetNumberOfWorkUnits: Any = ...
    GetNumberOfWorkUnits: Any = ...
    GetCurrentIteration: Any = ...
    SetNumberOfIterations: Any = ...
    GetNumberOfIterations: Any = ...
    GetCurrentPosition: Any = ...
    StartOptimization: Any = ...
    GetStopConditionDescription: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkObjectToObjectOptimizerBaseTemplateD_cast: Any

class itkObjectToObjectOptimizerBaseTemplateEnums:
    thisown: Any = ...
    StopConditionObjectToObjectOptimizer_MAXIMUM_NUMBER_OF_ITERATIONS: Any = ...
    StopConditionObjectToObjectOptimizer_COSTFUNCTION_ERROR: Any = ...
    StopConditionObjectToObjectOptimizer_UPDATE_PARAMETERS_ERROR: Any = ...
    StopConditionObjectToObjectOptimizer_STEP_TOO_SMALL: Any = ...
    StopConditionObjectToObjectOptimizer_CONVERGENCE_CHECKER_PASSED: Any = ...
    StopConditionObjectToObjectOptimizer_GRADIENT_MAGNITUDE_TOLEARANCE: Any = ...
    StopConditionObjectToObjectOptimizer_OTHER_ERROR: Any = ...
    def __init__(self, *args: Any) -> None: ...
    __swig_destroy__: Any = ...

class itkObjectToObjectOptimizerBaseTemplateF(itk.ITKCommonBasePython.itkObject):
    thisown: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    SetMetric: Any = ...
    GetModifiableMetric: Any = ...
    GetMetric: Any = ...
    GetCurrentMetricValue: Any = ...
    GetValue: Any = ...
    SetScales: Any = ...
    GetScales: Any = ...
    GetScalesAreIdentity: Any = ...
    SetWeights: Any = ...
    GetWeights: Any = ...
    GetWeightsAreIdentity: Any = ...
    GetScalesInitialized: Any = ...
    SetScalesEstimator: Any = ...
    SetDoEstimateScales: Any = ...
    GetDoEstimateScales: Any = ...
    DoEstimateScalesOn: Any = ...
    DoEstimateScalesOff: Any = ...
    SetNumberOfWorkUnits: Any = ...
    GetNumberOfWorkUnits: Any = ...
    GetCurrentIteration: Any = ...
    SetNumberOfIterations: Any = ...
    GetNumberOfIterations: Any = ...
    GetCurrentPosition: Any = ...
    StartOptimization: Any = ...
    GetStopConditionDescription: Any = ...
    __swig_destroy__: Any = ...
    cast: Any = ...

itkObjectToObjectOptimizerBaseTemplateF_cast: Any
