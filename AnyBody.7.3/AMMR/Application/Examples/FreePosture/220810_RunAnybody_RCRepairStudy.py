# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:25:10 2021

@author: johan
"""

from anypytools import AnyPyProcess
from anypytools import AnyMacro
from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun, SaveData)



import numpy as np
import matplotlib.pyplot as plt

# Inputs to variables that are changed 

# Slack length of supraspinatus after tendon retraction 
# --> values of tendon retraction of 80 MRI : [none, lower std, mean, upper std] (meter)


# 1-parameter calibration
# Lt0_SS1 = [0.0996349,  0.0856349,  0.0725349,  0.0594349 ]
# Lt0_SS2 = [0.08742721, 0.07342721, 0.06032721, 0.04722721]
# Lt0_SS3 = [0.09512845, 0.08112845, 0.06802845, 0.05492845 ]
# Lt0_SS4 = [0.07621618, 0.06221618, 0.04911618, 0.03601618]
# Lt0_SS5 = [0.08151371, 0.06751371, 0.05441371, 0.04131371]
# Lt0_SS6 = [0.0695552, 0.0555552,  0.0424552,  0.0293552 ]

# # 2-parameter calibration
# Lt0_SS1 = [0.04709778, 0.04709778, 0.01999778,  0.00689778 ]
# Lt0_SS2 = [0.03619282, 0.02219282, 0.00909282, -0.00400718]
# Lt0_SS3 = [0.04747839, 0.03347839, 0.02037839,  0.00727839]
# Lt0_SS4 = [0.0301985,  0.0161985,  0.0030985,  -0.0100015]
# Lt0_SS5 = [0.03873769, 0.02473769, 0.01163769, -0.00146231]
# Lt0_SS6 = [0.02755053, 0.01355053, 0.00045053, -0.13054947]


# 2-parameter calibration- new Rmin and Rmax
Lt0_SS1 = [0.08107405, 0.06707405, 0.05397405, 0.04087405]
Lt0_SS2 = [0.06955478, 0.05555478, 0.04245478, 0.02935478]
Lt0_SS3 = [0.08024488, 0.06624488, 0.05314488, 0.04004488]
Lt0_SS4 = [0.06202005, 0.04802005, 0.03492005, 0.02182005]
Lt0_SS5 = [0.0699235,  0.0559235,  0.0428235,  0.0297235]
Lt0_SS6 = [0.05823378, 0.04423378, 0.03113378, 0.01803378]



# ID for output file name 
# Ordering = np.arange(1,13)
Ordering = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
k = 0
TendonRetr = ['healthy','lowerstd','mean','upperstd']
Medialization = ['0mm', '5mm', '10mm']


# supraspinatus tendon insertion medialization of 0mmm, 5mm and 10mm
Medialization_x = [ 0.008,  0.003, -0.002]
Medialization_y = [-0.005,  0.000,  0.003]
Medialization_z = [-0.005, -0.005, -0.005]



parameter_study_macro = []



for j in range(len(Medialization)):
    
    for i in range(len(TendonRetr)):
        parameter_study_macro.append([
            Load('FreePostureFullBodyShoulderRhythmMove.Main.Any' ),    
            
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_x', Medialization_x[j] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_y', Medialization_y[j] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_z', Medialization_z[j] ),
            SetValue('Main.Study.file_ID4', Ordering[k]    ),
            SetValue('Main.Study.file_ID5', TendonRetr[i]    ),
            SetValue('Main.Study.file_ID6', Medialization[j] ),
            UpdateValues(),
            
            # 1) Run Calibration Sequence  
            # ---> one Parameter Calibration
            OperationRun('HumanModel.Calibration.CalibrationSequence'),
                    
            
            # 2) Set values of tendon slack length after calibration sequence
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Lt0', Lt0_SS1[i] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Lt0', Lt0_SS2[i] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Lt0', Lt0_SS3[i] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Lt0', Lt0_SS4[i] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Lt0', Lt0_SS5[i] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Lt0', Lt0_SS6[i] ),
            UpdateValues(),
           
            # 3) Run Inverse Dynamics Sequence  
            OperationRun('Main.Study.InverseDynamics'),
       ])
        
        # increase counter for naming
        k= k+1
         


app = AnyPyProcess(
    num_processes=3,
    anybodycon_path=r"C:\Program Files\AnyBody Technology\AnyBody.7.4\AnyBodyCon.exe"
)

# parameter_study_macro = AnyMacro(macro, number_of_macros= len(LS_ROM))

output = app.start_macro(parameter_study_macro)

# app.save_results("Results_MomentArms_StaticDiagnosticTests.db")





