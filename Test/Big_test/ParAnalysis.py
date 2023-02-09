from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)
from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt
from MacroAnybody import *
from anypytools.datautils import read_anyoutputfile
from PlotMacro import *
from OutputCal import *
from Definitions import *
app = AnyPyProcess(num_processes=3)

SUPR_Epsilon0 = app.load_results('Muscle_supraspinatus_Input_F0.db')



