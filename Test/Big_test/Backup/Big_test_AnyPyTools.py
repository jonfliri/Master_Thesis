# WRITE PARAMETERS IN ANYBODY

# WRITE PARAMETERS IN ANYBODY

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)


from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt

app = AnyPyProcess(num_processes=1)

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
]

calib_value_tendon = app.start_macro(calib)

print(calib_value_tendon)

"""

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)


from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt

app = AnyPyProcess(num_processes=1)

#Get tendon lenght
Cal_tpy = '_CALIBRATION_TYPE_2PAR_'

calib = [
    Load('Big_test.main.any'),
    #SetValue('Main.HumanModel.Calibration.RMin', 0.2),
    #SetValue('Main.HumanModel.Calibration.RMax', 1.0),
    UpdateValues(),
    OperationRun('HumanModel.Calibration.CalibrationSequence'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Lt0'),
    Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Lt0'),
    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmin'),
    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmax'),

    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmin'),
    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmax'),

    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmin'),
    Dump('Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmax'),
]

calib_value_tendon = app.start_macro(calib)


print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmin'])
print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.supraspinatusRmax'])

print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmin'])
print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.serratus_anteriorRmax'])

print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmin'])
print(calib_value_tendon['Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.pectoralis_minorRmax'])
"""

"""
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

print(Lt1)

retrac_value = [0.0, 14.0, 27.1, 40.0]
Lt0_SS1 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS2 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS3 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS4 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS5 = np.zeros(len(retrac_value),dtype=float)
Lt0_SS6 = np.zeros(len(retrac_value),dtype=float)

print(Lt0_SS1)
print(retrac_value)

for i in range(len(retrac_value)):
    Lt0_SS1[i] = Lt1-retrac_value[i]/1000
    Lt0_SS2[i] = Lt2-retrac_value[i]/1000
    Lt0_SS3[i] = Lt3-retrac_value[i]/1000
    Lt0_SS4[i] = Lt4-retrac_value[i]/1000
    Lt0_SS5[i] = Lt5-retrac_value[i]/1000
    Lt0_SS6[i] = Lt6-retrac_value[i]/1000

print(Lt0_SS1)
"""
"""                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)
import numpy as np
parameter = [45, 90, 135]
#print(len(parameter))

macro = [
    [Load('Big_test.main.any'),
     SetValue('Main.HumanModel.BodyModel.Right.JointPos.GlenohumeralAbduction', parameter),
     OperationRun('Main.RunApplication'),
     Dump('Main.Study.Output.Abscissa.t'),
     Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_1.Ft'),
     Dump('Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus'),
     ]
]
#app.start_macro(macrolist);

results_1 = AnyMacro(macro, number_of_macros= len(parameter) )
results = app.start_macro(results_1)
#print(results)

mus_supraspinatus_1 = results [0]['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.supraspinatus_1.Ft']
#abscissa = results [0]['Main.Study.Output.Abscissa.t']
#shoulderarm_muscle = results [0]['Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus']

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

print(mus_supraspinatus_1)
#print(mus_supraspinatus_1)

plt.plot(mus_supraspinatus_1);
plt.show()
"""
"""
patella_tendon_lengths = [
    0.02 + i*0.01
    for i in range(7)
]
print(patella_tendon_lengths)

macro = [
    Load('Knee.any'),
    SetValue('Main.MyModel.PatellaLigament.DriverPos', patella_tendon_lengths ),
    OperationRun('Main.MyStudy.InverseDynamics'),
    Dump('Main.MyStudy.Output.Abscissa.t'),
    Dump('Main.MyStudy.Output.MaxMuscleActivity'),
    Dump('Main.MyModel.PatellaLigament.DriverPos'),
]

parameter_study_macro = AnyMacro(macro, number_of_macros= len(patella_tendon_lengths) )

output = app.start_macro(parameter_study_macro)

#matplotlib inline
import matplotlib.pyplot as plt

for data in output:
    max_activity = data['Main.MyStudy.Output.MaxMuscleActivity']
    time = data['Main.MyStudy.Output.Abscissa.t']
    patella_ligament_length = data['Main.MyModel.PatellaLigament.DriverPos'][0]
    plt.plot(time, max_activity, label='{:.1f} cm'.format(100* patella_ligament_length) )

plt.title('Effect of changing patella tendon length')
plt.xlabel('Time steps')
plt.ylabel('Max muscle activity')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2);
plt.show()

"""