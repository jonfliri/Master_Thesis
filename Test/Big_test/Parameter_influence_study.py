# WRITE PARAMETERS IN ANYBODY

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)


from anypytools import AnyMacro
from anypytools import AnyPyProcess
import sys
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt

app = AnyPyProcess(num_processes=3)

#Get tendon lenght '_CALIBRATION_TYPE_2PAR_'

calib = [
    Load('Big_test.main.any'),
    SetValue('Main.HumanModel.Calibration.RMin', 0.2),
    SetValue('Main.HumanModel.Calibration.RMax', 1.0),
    UpdateValues(),

    OperationRun('HumanModel.Calibration.CalibrationSequence'),

    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6'),
]

cal = app.start_macro(calib)

print(cal)

SS_UpdConfig = 0.0
SS_UpdDesign = 0.0
SS_UpdOutput = 0.0
SS_t = 0.0
SS_F0 = 0.0
SS_Lf0 = 0.0
SS_Vol0 = 0.0
SS_Lt0 = 0.0
SS_Gamma0 = 0.0
SS_Epsilon0 = 0.0
SS_Fcfast = 0.0
SS_Jt = 0.0
SS_Jpe = 0.0
SS_K1 = [cal['1.K1''T'], cal['2.K1''T'], cal['3.K1''T'], cal['4.K1''T'], cal['5.K1''T'], cal['6.K1''T']]
SS_K2 = [cal['1.K2''T'], cal['2.K2''T'], cal['3.K2''T'], cal['4.K2''T'], cal['5.K2''T'], cal['6.K2''T']]
SS_PEFactor = 0.0
SS_Lfbar = 0.0
SS_Gammabar = 0.0
SS_Epsilonbar = 0.0
SS_PCSA = 0.0
SS_Lf0Temp = 0.0
SS_Epsilon0Temp = 0.0
SS_K1Temp = 0.0
SS_K2Temp = 0.0
SS_FcfastTemp = 0.0
SS_JtTemp = 0.0
SS_JpeTemp = 0.0
SS_PEFactorTemp = 0.0

print(SS_K1)
print(SS_K1[0])

"""

for data in calib_value_tendon:
    SS_UpdConfig = data[]
    SS_UpdDesign =
    SS_UpdOutput =
    SS_t =
    SS_F0 =
    SS_Lf0 =
    SS_Vol0 =
    SS_Lt0 =
    SS_Gamma0 =
    SS_Epsilon0 =
    SS_Fcfast =
    SS_Jt =
    SS_Jpe =
    SS_K1 =
    SS_K2 =
    SS_PEFactor =
    SS_Lfbar =
    SS_Gammabar =
    SS_Epsilonbar =
    SS_PCSA =
    SS_Lf0Temp =
    SS_Epsilon0Temp =
    SS_K1Temp =
    SS_K2Temp =
    SS_FcfastTemp =
    SS_JtTemp =
    SS_JpeTemp =
    SS_PEFactorTemp =


"""


"""

# 1-parameter calibration
#Lt0_SS1 = [0.0996349,  0.0856349,  0.0725349,  0.0594349 ]
#Lt0_SS2 = [0.08742721, 0.07342721, 0.06032721, 0.04722721]
#Lt0_SS3 = [0.09512845, 0.08112845, 0.06802845, 0.05492845 ]
#Lt0_SS4 = [0.07621618, 0.06221618, 0.04911618, 0.03601618]
#Lt0_SS5 = [0.08151371, 0.06751371, 0.05441371, 0.04131371]
#Lt0_SS6 = [0.0695552, 0.0555552,  0.0424552,  0.0293552 ]

#Lt0_SS1 = [0.08107405, 0.06707405, 0.05397405, 0.04087405]
#Lt0_SS2 = [0.06955478, 0.05555478, 0.04245478, 0.02935478]
#Lt0_SS3 = [0.08024488, 0.06624488, 0.05314488, 0.04004488]
#Lt0_SS4 = [0.06202005, 0.04802005, 0.03492005, 0.02182005]
#Lt0_SS5 = [0.0699235,  0.0559235,  0.0428235,  0.0297235]
#Lt0_SS6 = [0.05823378, 0.04423378, 0.03113378, 0.01803378]

# supraspinatus tendon insertion medialization of 0mmm, 5mm and 10mm
Medialization_x = [ 0.008,  0.003, -0.002]
Medialization_y = [-0.005,  0.000,  0.003]
Medialization_z = [-0.005, -0.005, -0.005]

Ordering = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
k = 0
TendonRetr = ['healthy','lowerstd','mean','upperstd']
Medialization = ['0mm', '5mm', '10mm']


nstep = 11
#print(parameters)

macro = []
for j in range(len(Medialization)):

    for i in range(len(TendonRetr)):
        macro.append([
            Load('Big_test.main.any'),

            SetValue('Main.HumanModel.Calibration.RMin', 0.2),
            SetValue('Main.HumanModel.Calibration.RMax', 1.0),
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue('Main.HumanModel.Mannequin.PostureVel.Right.GlenohumeralAbduction', 120.0 ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_x', Medialization_x[j] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_y', Medialization_y[j] ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_z', Medialization_z[j] ),

            #OperationRun('HumanModel.Calibration.CalibrationSequence'),

            #SetValue('Main.Study.nStep', nstep ),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Lt0', Lt0_SS1[i]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Lt0', Lt0_SS2[i]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Lt0', Lt0_SS3[i]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Lt0', Lt0_SS4[i]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Lt0', Lt0_SS5[i]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Lt0', Lt0_SS6[i]),
            #SetValue('Main.HumanModel.Config.Messages.msg_BM_CALIBRATION_TYPE.Type', Cal_tpy),
            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),

            Dump('Main.Study.Output.Abscissa.t'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_1.Strength'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_2.Strength'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_3.Strength'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_4.Strength'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_5.Strength'),
            Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_6.Strength'),
        ])

#parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
output = app.start_macro(macro)

print(output)



supraspinatus_temp = np.zeros((6,nstep),dtype=float)
supraspinatus = np.zeros((len(Medialization)*len(TendonRetr),nstep),dtype=float)
time = np.zeros((1,nstep),dtype=float)
#print(supraspinatus)
i=0

for data in output:
    supraspinatus_temp[0] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_1.Strength']
    supraspinatus_temp[1] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_2.Strength']
    supraspinatus_temp[2] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_3.Strength']
    supraspinatus_temp[3] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_4.Strength']
    supraspinatus_temp[4] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_5.Strength']
    supraspinatus_temp[5] = data['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_6.Strength']
    time = data['Main.Study.Output.Abscissa.t']
    supraspinatus[i] = np.sum(supraspinatus_temp,axis=0)
    i = i + 1
print(supraspinatus)

c=0;

fig, axs = plt.subplots(len(Medialization), len(TendonRetr))

for j in range(len(Medialization)):

    for i in range(len(TendonRetr)):
        #plt.plot(time, supraspinatus[c])
        print(Medialization[j])
        print(TendonRetr[i])
        print(Ordering[c])
        print(supraspinatus[c])

        axs[j, i].plot(time*120, supraspinatus[c])
        axs[j, i].set_title(f'Medialization: {Medialization[j]} Tendon retraction: {TendonRetr[i]}')
        #axs[j, i].set()
        #axs[j, i].set_ylim(0, 400)
        #axs[j, i].set_grid(True)



        c=c+1;

for ax in axs.flat:
    ax.set(xlabel='Muscle Strength [N]', ylabel='Abduction [°]')

plt.setp(axs, xlim=(0,120), ylim=(0,400))
# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
#    ax.label_outer()

#plt.xlim(0, 120)
#plt.ylim(0, 400)
#plt.grid(True)

#plt.title('Effect of Abduction angle')
#plt.xlabel('Time steps')
#plt.ylabel('Sup_1')
plt.show()

"""