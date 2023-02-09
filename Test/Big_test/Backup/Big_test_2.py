# WRITE PARAMETERS IN ANYBODY

# WRITE PARAMETERS IN ANYBODY

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)


from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt

app = AnyPyProcess(num_processes=3)

#Get tendon lenght
Cal_tpy = '_CALIBRATION_TYPE_2PAR_'

## Rmin, Rmax from Literature GARNER and PANDY 2002

#coracobrachialis CRCB
CRCB_Rmin = np.array([0.55, 0.55, 0.55, 0.55, 0.55, 0.55])
CRCB_Rmax = np.array([0.95, 0.95, 0.95, 0.95, 0.95, 0.95])

#deltoid scapular DLTs
DLTs_Rmin = np.array([0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35])
DLTs_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1])

#deltoid clavicular DLTc
DLTc_Rmin = np.array([0.55, 0.55, 0.55, 0.55])
DLTc_Rmax = np.array([1.3, 1.3, 1.3, 1.3])

#infraspinatus INFR
INFR_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
INFR_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

#pectoralis major thoratic PMJt
PMJt_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]) # Average from PMJs and PMJr
PMJt_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]) # Average from PMJs and PMJr

#pectoralis major clavicular PMJc
PMJc_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4])
PMJc_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3])

#pectoralis minor PMN
PMN_Rmin= np.array([0.55, 0.5, 0.45, 0.45]) # 2-4 = 0.55 to 0.5, 3-4 to 0.45
PMN_Rmax =np.array([1.05, 1.1, 1.1, 1.1])# 2-4 = 1.05 to 1.1

#romboideus RMB
RMB_min = np.array([0.45, 0.45, 0.45]) #average of RMN, RMJt2 and RMJt3
RMB_max = np.array([1.1, 1.1, 1.1]) #average of RMN, RMJt2 and RMJt3

#serratus anterior SRA
SRA_Rmin = np.array([0.6, 0.6, 0.5, 0.45, 0.45, 0.5]) #average of SRAs, SRAm and SRAi startet at 0.6 and than adjusted
SRA_Rmax = np.array([1.1, 1.1, 1.2, 1.2, 1.2, 1.2]) #average of SRAs, SRAm and SRAi startet at 1.1 and than adjusted

#subscapularis SBSC
SBSC_Rmin = np.array([0.475, 0.475, 0.475, 0.475, 0.475, 0.475])
SBSC_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

#supraspinatus SUPR
SUPR_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
SUPR_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])

#teres major TMJ
TMJ_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
TMJ_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

#teres minor TMN
TMN_Rmin = np.array([0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
TMN_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

#trapezius scapluar TRPS
TRPS_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5]) #average TRPc, TRPc7, TRPt1 and TRPt2
TRPS_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1]) #average TRPc, TRPc7, TRPt1 and TRPt2


## End of initalisation of Rmin and Rmax 28

calib = [
    Load('Big_test.main.any'),
    SetValue('Main.HumanModel.Calibration.RMin', 0.35),# average which fits overall
    SetValue('Main.HumanModel.Calibration.RMax', 1.1),# average which fits overall
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.coracobrachialisRmin', CRCB_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.coracobrachialisRmax', CRCB_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_scapularRmin', DLTs_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_scapularRmax', DLTs_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_clavicularRmin', DLTc_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_clavicularRmax', DLTc_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.infraspinatusRmin', INFR_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.infraspinatusRmax', INFR_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_thoracicRmin', PMJt_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_thoracicRmax', PMJt_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_clavicularRmin', PMJc_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_clavicularRmax', PMJc_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmin', PMN_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmax', PMN_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.rhomboideusRmin', RMB_min),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.rhomboideusRmax', RMB_max),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmin', SRA_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmax', SRA_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.subscapularisRmin', SBSC_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.subscapularisRmax', SBSC_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmin', SUPR_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmax', SUPR_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_majorRmin', TMJ_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_majorRmax', TMJ_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_minorRmin', TMN_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_minorRmax', TMN_Rmax),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.trapezius_scapularRmin', TRPS_Rmin),
    SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.trapezius_scapularRmax', TRPS_Rmax),
    UpdateValues(),
    OperationRun('HumanModel.Calibration.CalibrationSequence'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Lt0'),
    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmin'),
]

calib_value_tendon = app.start_macro(calib)

print(calib_value_tendon)

Lt1 = 0.0
Lt2 = 0.0
Lt3 = 0.0
Lt4 = 0.0
Lt5 = 0.0
Lt6 = 0.0

for data_cal in calib_value_tendon:
    Lt1 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Lt0']
    Lt2 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Lt0']
    Lt3 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Lt0']
    Lt4 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Lt0']
    Lt5 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Lt0']
    Lt6 = data_cal['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Lt0']

retrac_value = [0.0, 14.0, 27.1, 40.0]
Lt0_SS1 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS2 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS3 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS4 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS5 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS6 = np.zeros(len(retrac_value),dtype=float)

#print(Lt0_SS1)
#print(retrac_value)

for i in range(len(retrac_value)):
    Lt0_SS1[i] = Lt1-retrac_value[i]/1000
    Lt0_SS2[i] = Lt2-retrac_value[i]/1000
    Lt0_SS3[i] = Lt3-retrac_value[i]/1000
    Lt0_SS4[i] = Lt4-retrac_value[i]/1000
    Lt0_SS5[i] = Lt5-retrac_value[i]/1000
    Lt0_SS6[i] = Lt6-retrac_value[i]/1000



#print(Lt0_SS1)



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

            SetValue('Main.HumanModel.Calibration.RMin', 0.35),  # average which fits overall
            SetValue('Main.HumanModel.Calibration.RMax', 1.1),  # average which fits overall
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.coracobrachialisRmin', CRCB_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.coracobrachialisRmax', CRCB_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_scapularRmin', DLTs_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_scapularRmax', DLTs_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_clavicularRmin', DLTc_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.deltoideus_clavicularRmax', DLTc_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.infraspinatusRmin', INFR_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.infraspinatusRmax', INFR_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_thoracicRmin',
                     PMJt_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_thoracicRmax',
                     PMJt_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_clavicularRmin',
                     PMJc_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_major_clavicularRmax',
                     PMJc_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmin', PMN_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmax', PMN_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.rhomboideusRmin', RMB_min),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.rhomboideusRmax', RMB_max),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmin', SRA_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmax', SRA_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.subscapularisRmin', SBSC_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.subscapularisRmax', SBSC_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmin', SUPR_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmax', SUPR_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_majorRmin', TMJ_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_majorRmax', TMJ_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_minorRmin', TMN_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.teres_minorRmax', TMN_Rmax),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.trapezius_scapularRmin', TRPS_Rmin),
            SetValue('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.trapezius_scapularRmax', TRPS_Rmax),
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
    ax.set(xlabel='Abduction [°]', ylabel='Muscle Strength [N]')

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

