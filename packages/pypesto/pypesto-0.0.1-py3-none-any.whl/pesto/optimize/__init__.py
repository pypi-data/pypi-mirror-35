"""
Multistart optimization
=======================

"""

from .optimize import minimize
from .optimizer import (OptimizerResult,
                        Optimizer,
                        ScipyOptimizer,
                        DlibOptimizer   )
from .startpoint import uniform, latin_hypercube
