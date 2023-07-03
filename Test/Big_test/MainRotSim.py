from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)
from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt
from MacroAnybody import *
from PlotMacro import *
from OutputCal import *
from Definitions import *
app = AnyPyProcess(num_processes=3)

## Initialisation

nstep = 100

mov = 120.0 # [°] Degrees
mov_attribute = 'GlenohumeralAbduction' # GlenohumeralFlexion, GlenohumeralAbduction, GlenohumeralExternalRotation, ElbowFlexion, ElbowPronation

input_mus_full = SUPR_full_name
mus_nbr = muscle_nbr_SUPR

output_mus_attribute = ['Strength', 'Fp', 'Lf0', 'Lt0']

Goutallier_Stage = 0 # 0-4

## Scaling

default_height = 1.75
pat_height = 1.75

default_weight = 75
pat_weight = 75


def Macro_opti(path_cal, path_mov, mov_attribute, mov, path_output_mus, SUPR_full_name, output_mus_attribute, load_var = 'Big_test.main.any', height = default_height, weight=default_weight, pen_angle_SUPR = SUPR_pen_ang):
    # coracobrachialis CRCB
    CRCB_Rmin = np.array([0.55, 0.55, 0.55, 0.55, 0.55, 0.55])
    CRCB_Rmax = np.array([0.95, 0.95, 0.95, 0.95, 0.95, 0.95])

    # deltoid scapular DLTs
    DLTs_Rmin = np.array([0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35])
    DLTs_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1])

    # deltoid clavicular DLTc
    DLTc_Rmin = np.array([0.55, 0.55, 0.55, 0.55])
    DLTc_Rmax = np.array([1.3, 1.3, 1.3, 1.3])

    # infraspinatus INFR
    INFR_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    INFR_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

    # pectoralis major thoratic PMJt
    PMJt_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4])  # Average from PMJs and PMJr
    PMJt_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4])  # Average from PMJs and PMJr

    # pectoralis major clavicular PMJc
    PMJc_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4])
    PMJc_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3])

    # pectoralis minor PMN
    PMN_Rmin = np.array([0.55, 0.5, 0.45, 0.45])  # 2-4 = 0.55 to 0.5, 3-4 to 0.45
    PMN_Rmax = np.array([1.05, 1.1, 1.1, 1.1])  # 2-4 = 1.05 to 1.1

    # romboideus RMB
    RMB_min = np.array([0.45, 0.45, 0.45])  # average of RMN, RMJt2 and RMJt3
    RMB_max = np.array([1.1, 1.1, 1.1])  # average of RMN, RMJt2 and RMJt3

    # serratus anterior SRA
    SRA_Rmin = np.array([0.6, 0.6, 0.5, 0.45, 0.45, 0.5])  # average of SRAs, SRAm and SRAi startet at 0.6 and than adjusted
    SRA_Rmax = np.array([1.1, 1.1, 1.2, 1.2, 1.2, 1.2])  # average of SRAs, SRAm and SRAi startet at 1.1 and than adjusted

    # subscapularis SBSC
    SBSC_Rmin = np.array([0.475, 0.475, 0.475, 0.475, 0.475, 0.475])
    SBSC_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    # supraspinatus SUPR
    SUPR_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
    SUPR_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])

    # teres major TMJ
    TMJ_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
    TMJ_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    # teres minor TMN
    TMN_Rmin = np.array([0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
    TMN_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

    # trapezius scapluar TRPS
    TRPS_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])  # average TRPc, TRPc7, TRPt1 and TRPt2
    TRPS_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1])  # average TRPc, TRPc7, TRPt1 and TRPt2

    ## End of initalisation of Rmin and Rmax

    macro = [
        Load(load_var), #, defs={'N_STEP': 100}

        SetValue('Main.HumanModel.Calibration.RMin', 0.35),  # average which fits overall
        SetValue('Main.HumanModel.Calibration.RMax', 1.1),  # average which fits overall
        SetValue(path_cal + 'coracobrachialisRmin', CRCB_Rmin),
        SetValue(path_cal + 'coracobrachialisRmax', CRCB_Rmax),
        SetValue(path_cal + 'deltoideus_scapularRmin', DLTs_Rmin),
        SetValue(path_cal + 'deltoideus_scapularRmax', DLTs_Rmax),
        SetValue(path_cal + 'deltoideus_clavicularRmin', DLTc_Rmin),
        SetValue(path_cal + 'deltoideus_clavicularRmax', DLTc_Rmax),
        SetValue(path_cal + 'infraspinatusRmin', INFR_Rmin),
        SetValue(path_cal + 'infraspinatusRmax', INFR_Rmax),
        SetValue(path_cal + 'pectoralis_major_thoracicRmin', PMJt_Rmin),
        SetValue(path_cal + 'pectoralis_major_thoracicRmax', PMJt_Rmax),
        SetValue(path_cal + 'pectoralis_major_clavicularRmin', PMJc_Rmin),
        SetValue(path_cal + 'pectoralis_major_clavicularRmax', PMJc_Rmax),
        SetValue(path_cal + 'pectoralis_minorRmin', PMN_Rmin),
        SetValue(path_cal + 'pectoralis_minorRmax', PMN_Rmax),
        SetValue(path_cal + 'rhomboideusRmin', RMB_min),
        SetValue(path_cal + 'rhomboideusRmax', RMB_max),
        SetValue(path_cal + 'serratus_anteriorRmin', SRA_Rmin),
        SetValue(path_cal + 'serratus_anteriorRmax', SRA_Rmax),
        SetValue(path_cal + 'subscapularisRmin', SBSC_Rmin),
        SetValue(path_cal + 'subscapularisRmax', SBSC_Rmax),
        SetValue(path_cal + 'supraspinatusRmin', SUPR_Rmin),
        SetValue(path_cal + 'supraspinatusRmax', SUPR_Rmax),
        SetValue(path_cal + 'teres_majorRmin', TMJ_Rmin),
        SetValue(path_cal + 'teres_majorRmax', TMJ_Rmax),
        SetValue(path_cal + 'teres_minorRmin', TMN_Rmin),
        SetValue(path_cal + 'teres_minorRmax', TMN_Rmax),
        SetValue(path_cal + 'trapezius_scapularRmin', TRPS_Rmin),
        SetValue(path_cal + 'trapezius_scapularRmax', TRPS_Rmax),
        SetValue('Main.HumanModel.Scaling.StandardParameters.BodyParameters.BodyHeight', height),
        SetValue('Main.HumanModel.Scaling.StandardParameters.BodyParameters.BodyMass', weight),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.PEFactor', 1.75),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Gamma0', pen_angle_SUPR),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Gamma0', pen_angle_SUPR),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Gamma0', pen_angle_SUPR),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Gamma0', pen_angle_SUPR),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Gamma0', pen_angle_SUPR),
        SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Gamma0', pen_angle_SUPR),
        UpdateValues(),

        OperationRun('HumanModel.Calibration.CalibrationSequence'),

        # Dump Muscle fiber length

        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.'+ output_mus_attribute[2]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.'+ output_mus_attribute[2]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.'+ output_mus_attribute[2]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.'+ output_mus_attribute[2]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.'+ output_mus_attribute[2]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.'+ output_mus_attribute[2]),

        # Dump Tendon length

        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.'+ output_mus_attribute[3]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.'+ output_mus_attribute[3]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.'+ output_mus_attribute[3]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.'+ output_mus_attribute[3]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.'+ output_mus_attribute[3]),
        Dump('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.'+ output_mus_attribute[3]),

        SetValue(path_mov + mov_attribute, mov),

        UpdateValues(),

        OperationRun('Main.Study.InverseDynamics'),

        Dump('Main.Study.Output.Abscissa.t'),

        # Dump Supraspinatus Strength

        Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[0]),
        Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[0]),
        Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[0]),
        Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[0]),
        Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[0]),
        Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[0]),

        # Dump Supraspinatus Passive Force

        Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[1]),
        Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[1]),
        Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[1]),
        Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[1]),
        Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[1]),
        Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[1]),

        # Dump Supraspinatus Tendon Force

        Dump(path_output_mus + SUPR_full_name + '_1.' + 'Ft'),
        Dump(path_output_mus + SUPR_full_name + '_2.' + 'Ft'),
        Dump(path_output_mus + SUPR_full_name + '_3.' + 'Ft'),
        Dump(path_output_mus + SUPR_full_name + '_4.' + 'Ft'),
        Dump(path_output_mus + SUPR_full_name + '_5.' + 'Ft'),
        Dump(path_output_mus + SUPR_full_name + '_6.' + 'Ft'),
    ]

    output = app.start_macro(macro)

    return output


def Macro_sim(path_cal, path_mov, mov_attribute, mov, path_output_mus, SUPR_full_name, output_mus_attribute, Medialization_x, Medialization_y, Medialization_z, Lf1, Lt1, load_var = 'Big_test.main.any', height = default_height, weight=default_weight, pen_angle_SUPR = SUPR_pen_ang, pen_angle_SUPR_a = SUPR_pen_ang, jpe = 3.0):
    # coracobrachialis CRCB
    CRCB_Rmin = np.array([0.55, 0.55, 0.55, 0.55, 0.55, 0.55])
    CRCB_Rmax = np.array([0.95, 0.95, 0.95, 0.95, 0.95, 0.95])

    # deltoid scapular DLTs
    DLTs_Rmin = np.array([0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35])
    DLTs_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1])

    # deltoid clavicular DLTc
    DLTc_Rmin = np.array([0.55, 0.55, 0.55, 0.55])
    DLTc_Rmax = np.array([1.3, 1.3, 1.3, 1.3])

    # infraspinatus INFR
    INFR_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    INFR_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

    # pectoralis major thoratic PMJt
    PMJt_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4])  # Average from PMJs and PMJr
    PMJt_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4])  # Average from PMJs and PMJr

    # pectoralis major clavicular PMJc
    PMJc_Rmin = np.array([0.4, 0.4, 0.4, 0.4, 0.4])
    PMJc_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3])

    # pectoralis minor PMN
    PMN_Rmin = np.array([0.55, 0.5, 0.45, 0.45])  # 2-4 = 0.55 to 0.5, 3-4 to 0.45
    PMN_Rmax = np.array([1.05, 1.1, 1.1, 1.1])  # 2-4 = 1.05 to 1.1

    # romboideus RMB
    RMB_min = np.array([0.45, 0.45, 0.45])  # average of RMN, RMJt2 and RMJt3
    RMB_max = np.array([1.1, 1.1, 1.1])  # average of RMN, RMJt2 and RMJt3

    # serratus anterior SRA
    SRA_Rmin = np.array(
        [0.6, 0.6, 0.5, 0.45, 0.45, 0.5])  # average of SRAs, SRAm and SRAi startet at 0.6 and than adjusted
    SRA_Rmax = np.array(
        [1.1, 1.1, 1.2, 1.2, 1.2, 1.2])  # average of SRAs, SRAm and SRAi startet at 1.1 and than adjusted

    # subscapularis SBSC
    SBSC_Rmin = np.array([0.475, 0.475, 0.475, 0.475, 0.475, 0.475])
    SBSC_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    # supraspinatus SUPR
    SUPR_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
    SUPR_Rmax = np.array([1.3, 1.3, 1.3, 1.3, 1.3, 1.3])

    # teres major TMJ
    TMJ_Rmin = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3])
    TMJ_Rmax = np.array([0.9, 0.9, 0.9, 0.9, 0.9, 0.9])

    # teres minor TMN
    TMN_Rmin = np.array([0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
    TMN_Rmax = np.array([1.4, 1.4, 1.4, 1.4, 1.4, 1.4])

    # trapezius scapluar TRPS
    TRPS_Rmin = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])  # average TRPc, TRPc7, TRPt1 and TRPt2
    TRPS_Rmax = np.array([1.1, 1.1, 1.1, 1.1, 1.1, 1.1])  # average TRPc, TRPc7, TRPt1 and TRPt2

    ## End of initalisation of Rmin and Rmax
    macro = []
    for j in range(len(Medialization_x)):
        macro.append([
            Load(load_var), #, defs={'N_STEP': 100}

            SetValue('Main.HumanModel.Calibration.RMin', 0.35),  # average which fits overall
            SetValue('Main.HumanModel.Calibration.RMax', 1.1),  # average which fits overall
            SetValue(path_cal + 'coracobrachialisRmin', CRCB_Rmin),
            SetValue(path_cal + 'coracobrachialisRmax', CRCB_Rmax),
            SetValue(path_cal + 'deltoideus_scapularRmin', DLTs_Rmin),
            SetValue(path_cal + 'deltoideus_scapularRmax', DLTs_Rmax),
            SetValue(path_cal + 'deltoideus_clavicularRmin', DLTc_Rmin),
            SetValue(path_cal + 'deltoideus_clavicularRmax', DLTc_Rmax),
            SetValue(path_cal + 'infraspinatusRmin', INFR_Rmin),
            SetValue(path_cal + 'infraspinatusRmax', INFR_Rmax),
            SetValue(path_cal + 'pectoralis_major_thoracicRmin', PMJt_Rmin),
            SetValue(path_cal + 'pectoralis_major_thoracicRmax', PMJt_Rmax),
            SetValue(path_cal + 'pectoralis_major_clavicularRmin', PMJc_Rmin),
            SetValue(path_cal + 'pectoralis_major_clavicularRmax', PMJc_Rmax),
            SetValue(path_cal + 'pectoralis_minorRmin', PMN_Rmin),
            SetValue(path_cal + 'pectoralis_minorRmax', PMN_Rmax),
            SetValue(path_cal + 'rhomboideusRmin', RMB_min),
            SetValue(path_cal + 'rhomboideusRmax', RMB_max),
            SetValue(path_cal + 'serratus_anteriorRmin', SRA_Rmin),
            SetValue(path_cal + 'serratus_anteriorRmax', SRA_Rmax),
            SetValue(path_cal + 'subscapularisRmin', SBSC_Rmin),
            SetValue(path_cal + 'subscapularisRmax', SBSC_Rmax),
            SetValue(path_cal + 'supraspinatusRmin', SUPR_Rmin),
            SetValue(path_cal + 'supraspinatusRmax', SUPR_Rmax),
            SetValue(path_cal + 'teres_majorRmin', TMJ_Rmin),
            SetValue(path_cal + 'teres_majorRmax', TMJ_Rmax),
            SetValue(path_cal + 'teres_minorRmin', TMN_Rmin),
            SetValue(path_cal + 'teres_minorRmax', TMN_Rmax),
            SetValue(path_cal + 'trapezius_scapularRmin', TRPS_Rmin),
            SetValue(path_cal + 'trapezius_scapularRmax', TRPS_Rmax),
            SetValue('Main.HumanModel.Scaling.StandardParameters.BodyParameters.BodyHeight', height),
            SetValue('Main.HumanModel.Scaling.StandardParameters.BodyParameters.BodyMass', weight),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.PEFactor', 1.75),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Gamma0', pen_angle_SUPR),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Gamma0', pen_angle_SUPR),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Gamma0', pen_angle_SUPR),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Gamma0', pen_angle_SUPR),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Gamma0', pen_angle_SUPR),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Gamma0', pen_angle_SUPR),
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_x', Medialization_x[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_y', Medialization_y[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Humerus.medialization_z', Medialization_z[j]),

            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.'+ output_mus_attribute[2], Lf1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.'+ output_mus_attribute[2], Lf1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.'+ output_mus_attribute[2], Lf1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.'+ output_mus_attribute[2], Lf1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.'+ output_mus_attribute[2], Lf1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.'+ output_mus_attribute[2], Lf1[j]),

            # Dump Tendon length

            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.'+ output_mus_attribute[3], Lt1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.'+ output_mus_attribute[3], Lt1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.'+ output_mus_attribute[3], Lt1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.'+ output_mus_attribute[3], Lt1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.'+ output_mus_attribute[3], Lt1[j]),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.'+ output_mus_attribute[3], Lt1[j]),

            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Gamma0', pen_angle_SUPR_a),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Gamma0', pen_angle_SUPR_a),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Gamma0', pen_angle_SUPR_a),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Gamma0', pen_angle_SUPR_a),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Gamma0', pen_angle_SUPR_a),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Gamma0', pen_angle_SUPR_a),

            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_1.Jpe', jpe),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_2.Jpe', jpe),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_3.Jpe', jpe),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_4.Jpe', jpe),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_5.Jpe', jpe),
            SetValue('Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_6.Jpe', jpe),

            SetValue(path_mov + mov_attribute, mov),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),

            Dump('Main.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength

            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[0]),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[0]),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[0]),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[0]),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[0]),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[0]),

            # Dump Supraspinatus Passive Force

            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[1]),

            # Dump Supraspinatus Tendon Force

            Dump(path_output_mus + SUPR_full_name + '_1.' + 'Ft'),
            Dump(path_output_mus + SUPR_full_name + '_2.' + 'Ft'),
            Dump(path_output_mus + SUPR_full_name + '_3.' + 'Ft'),
            Dump(path_output_mus + SUPR_full_name + '_4.' + 'Ft'),
            Dump(path_output_mus + SUPR_full_name + '_5.' + 'Ft'),
            Dump(path_output_mus + SUPR_full_name + '_6.' + 'Ft'),
        ])

    output = app.start_macro(macro)

    return output


def decision(sim_0, sim_5, sim_10):
    print(sim_0)
    print(sim_5)
    print(sim_10)
    pas_0 = 0
    pas_5 = 0
    pas_10 = 0

    operation = 1

    medialization = 99

    print(max(sim_0))

    if np.amax(sim_0) <= 216.61: # 216.61, 108.32
        if sim_0[59] <= 90.23: #179.2
            if sim_0[0] >= 37.35:
                pas_0 = 1
    if np.amax(sim_5) <= 216.61: # 216.61
        if sim_5[59] <= 90.23: #179.2
            if sim_5[0] >= 37.35:
                pas_5 = 1
    if np.amax(sim_10) <= 216.61:  # 216.61
        if sim_10[59] <= 90.23: #179.2
            if sim_10[0] >= 37.35:
                pas_10 = 1

    if pas_10 == 0:
        if pas_5 == 0:
            if pas_0 == 0:
                operation = 0

    if pas_0 == 1:
        medialization = 0
    else:
        if pas_5 == 1:
            medialization = 5
        else:
            if pas_10 == 1:
                medialization = 10
            else:
                medialization = 99

    return operation, medialization

## Calibration

out_calib = Macro_opti(path_cal, path_mov, mov_attribute, mov, path_output_mus, SUPR_full_name, output_mus_attribute, load_var = 'Big_test.main.any', height = pat_height, weight = pat_weight)

## Healthy simulation

strength_calib = output_calib(out_calib, path_output_mus, SUPR_full_name, output_mus_attribute[0], muscle_nbr_SUPR, nstep)
np.savetxt('Healthy Simulation Strength ', strength_calib, delimiter=',')

pas_for_calib = output_calib(out_calib, path_output_mus, SUPR_full_name, output_mus_attribute[1], muscle_nbr_SUPR, nstep)
np.savetxt('Healthy Simulation Passive Force ', pas_for_calib, delimiter=',')

Ft_calib = output_calib(out_calib, path_output_mus, SUPR_full_name, 'Ft', muscle_nbr_SUPR, nstep)
np.savetxt('Healthy Simulation Tendon Force ', Ft_calib, delimiter=',')

Lf0_calib = output_calib_one(out_calib, output_mus_attribute[2], muscle_nbr_SUPR)
Lt0_calib = output_calib_one(out_calib, output_mus_attribute[3], muscle_nbr_SUPR)
Lf0_calib = Lf0_calib/6.0
Lt0_calib = Lt0_calib/6.0

time_calib = out_calib['Main.Study.Output.Abscissa.t']
np.savetxt('Time', time_calib, delimiter=',')

SUPR_strength_cal = plotSingle(time_calib[0] * 120, strength_calib[0], 'Healthy Supraspinatus  Strength', 'Abduction [°]', 'Strength [N]', 1.0)
SUPR_pas_for_cal = plotSingle(time_calib[0] * 120, pas_for_calib[0], 'Healthy Supraspinatus Passive Force', 'Abduction [°]', 'Passive Force [N]', 1.0)
SUPR_Ft_cal = plotSingle(time_calib[0] * 120, Ft_calib[0], 'Healthy Supraspinatus Tendon Force', 'Abduction [°]', 'Tendon Force [N]', 1.0)

## Value adaption

ten_0_ratio = 0.37 #Muscle / Tendon ratio in a healty patient --> literatur research 37%
mus_0_ratio = 1-ten_0_ratio

# Patient Data Julian
mus_org_in_len = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]#[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # cm
mus_1_len = [7.896,	6.129, 6.475, 7.984, 5.88, 6.601, 6.541, 9.225, 6.203, 9.65, 8.193, 11.001, 6.562, 8.584, 7.166, 6.831, 7.894, 7.773]#[7.896, 7.984, 5.88, 9.225, 6.203, 8.193, 6.562, 8.584, 7.166, 7.894, 7.773] # cm 7.773(last), 7.984(second)
ten_1_len = [2.577, 2.835, 2.362, 2.599, 2.731, 4.643, 4.414, 3.04, 2.813, 2.433, 4.159, 2.948, 3.512, 3.583, 3.849, 3.628, 2.986, 4.124]#[2.577, 2.599, 2.731, 3.04, 2.813, 4.159, 3.512, 3.583, 3.849, 2.986, 4.124] # cm 4.124(last), 2.599(second)
tear_1_len_MRI = [2.947, 5.156, 5.243, 4.627, 4.609, 2.446, 0.985, 1.565, 2.534, 0.987, 1.488, 0.891, 1.626, 1.993, 1.805, 1.851, 1.32, 1.123]#[2.947, 4.627, 4.609, 1.565, 2.534, 1.488, 1.626, 1.993, 1.805, 1.32, 1.123] # cm 1.123(last), 4.627(second)

for y in range(len(mus_1_len)):
    mus_org_in_len[y] = mus_1_len[y] + ten_1_len[y] + tear_1_len_MRI[y]

## Repair simulation

## Repair optimisation

Medialization = ['0mm', '5mm', '10mm']

# supraspinatus tendon insertion medialization of 0mmm, 5mm and 10mm
Medialization_x = [ 0.008,  0.003, -0.002]
Medialization_y = [-0.005,  0.000,  0.003]
Medialization_z = [-0.005, -0.005, -0.005]

Lf1 = np.zeros(3, dtype=float)
Lt1 = np.zeros(3, dtype=float)

z = 0
b = ['001', '002', '003', '005', '007', '008', '012', '016-L', '016-R', '019', '020', '021', '028-L', '028-R', '033-L', '033-R_blade', '033-R_tse', '036']#['patient_001', 'patient_005', 'patient_007', 'patient_016-L', 'patient_016_R', 'patient_020', 'patient_028_L', 'patient_028_R', 'patient_033_L', 'patient_033_R_tse', 'patient_036']

strength_sim_0 = np.zeros(nstep, dtype=float)
strength_sim_1 = np.zeros(nstep, dtype=float)
strength_sim_2 = np.zeros(nstep, dtype=float)
pas_for_sim_0 = np.zeros(nstep, dtype=float)
pas_for_sim_1 = np.zeros(nstep, dtype=float)
pas_for_sim_2 = np.zeros(nstep, dtype=float)

for i in range(len(mus_org_in_len)):

    if Goutallier_Stage == 0:
        Gt_tend = 0
    elif Goutallier_Stage == 1:
        Gt_tend = 0
    elif Goutallier_Stage == 2:
        Gt_tend = 0
    elif Goutallier_Stage == 3:
        Gt_tend = 0
    elif Goutallier_Stage == 4:
        Gt_tend = 0
    else:
        Gt_tend = 0

    Lf1[0] = Lf0_calib * 1.0
    Lf1[1] = Lf0_calib * 1.0
    Lf1[2] = Lf0_calib * 1.0

    Lt1[0] = Lt0_calib * (ten_1_len[i]+(0.3*tear_1_len_MRI[i]+0.23))/(ten_0_ratio*(mus_1_len[i]+ten_1_len[i]+tear_1_len_MRI[i]))
    Lt1[1] = Lt0_calib * (ten_1_len[i]+(0.3*(tear_1_len_MRI[i]-0.5)+0.23))/(ten_0_ratio*(mus_1_len[i]+ten_1_len[i]+tear_1_len_MRI[i])-0.5)
    Lt1[2] = Lt0_calib * (ten_1_len[i]+(0.3*(tear_1_len_MRI[i]-1.0)+0.23))/(ten_0_ratio*(mus_1_len[i]+ten_1_len[i]+tear_1_len_MRI[i])-1.0)

    if tear_1_len_MRI[i] < 1:
        SUPR_pen_ang_cor = 8.32
        SUPR_jpe = 3.0 * 1.305
    elif tear_1_len_MRI[i] < 1 and tear_1_len_MRI[i] >= 3:
        SUPR_pen_ang_cor = 9.9
        SUPR_jpe = 3.0 * 2.035
    elif tear_1_len_MRI[i] < 3 and tear_1_len_MRI[i] >= 5:
        SUPR_pen_ang_cor = 13.3
        SUPR_jpe = 3.0 * 2.2
    elif tear_1_len_MRI[i] > 5:
        SUPR_pen_ang_cor = 13.3
        SUPR_jpe = 3.0 * 2.2
    else:
        SUPR_pen_ang_cor = 6.6
        SUPR_jpe = 3.0

    SUPR_pen_ang_cor = SUPR_pen_ang_cor * np.pi / 180

    np.savetxt('Data ' + b[i], np.r_[mus_1_len[i], Lf1[0], Lf1[1], Lf1[2], ten_1_len[1], Lt1[0], Lt1[1], Lt1[2], tear_1_len_MRI[i]], delimiter=',')

    out_sim = Macro_sim(path_cal, path_mov, mov_attribute, mov, path_output_mus, SUPR_full_name, output_mus_attribute, Medialization_x, Medialization_y, Medialization_z, Lf1, Lt1, load_var = 'Big_test.main.any', height = pat_height, weight = pat_weight, pen_angle_SUPR=SUPR_pen_ang, pen_angle_SUPR_a= SUPR_pen_ang_cor, jpe= SUPR_jpe)

    strength_sim_0, strength_sim_1, strength_sim_2 = output_sim(out_sim, path_output_mus, SUPR_full_name, output_mus_attribute[0], muscle_nbr_SUPR, nstep)
    pas_for_sim_0, pas_for_sim_1, pas_for_sim_2 = output_sim(out_sim, path_output_mus, SUPR_full_name, output_mus_attribute[1], muscle_nbr_SUPR, nstep)
    Ft_sim_0, Ft_sim_1, Ft_sim_2 = output_sim(out_sim, path_output_mus, SUPR_full_name, 'Ft', muscle_nbr_SUPR, nstep)

    np.savetxt('Repair simulation strength med 0 mm pat ' + b[i], strength_sim_0, delimiter=',')
    np.savetxt('Repair simulation strength med 5 mm pat ' + b[i], strength_sim_1, delimiter=',')
    np.savetxt('Repair simulation strength med 10 mm pat ' + b[i], strength_sim_2, delimiter=',')
    np.savetxt('Repair simulation passive force med 0 mm pat ' + b[i], pas_for_sim_0, delimiter=',')
    np.savetxt('Repair simulation passive force med 5 mm pat ' + b[i], pas_for_sim_1, delimiter=',')
    np.savetxt('Repair simulation passive force med 10 mm pat ' + b[i], pas_for_sim_2, delimiter=',')
    np.savetxt('Repair simulation Ft med 0 mm pat ' + b[i], Ft_sim_0, delimiter=',')
    np.savetxt('Repair simulation Ft med 5 mm pat ' + b[i], Ft_sim_1, delimiter=',')
    np.savetxt('Repair simulation Ft med 10 mm pat ' + b[i], Ft_sim_2, delimiter=',')

    # Rehab
    op, med = decision(sim_0=pas_for_sim_0[0], sim_5=pas_for_sim_1[0], sim_10=pas_for_sim_2[0])

    if op == 1:
        med_x = np.zeros(1, dtype=float)
        med_y = np.zeros(1, dtype=float)
        med_z = np.zeros(1, dtype=float)
        Lf1_op = np.zeros(1, dtype=float)
        Lt1_op = np.zeros(1, dtype=float)

        if tear_1_len_MRI[i] < 1:
            SUPR_pen_ang_cor = 8.32
            SUPR_jpe = 3.0 * 1.305
            SUPR_jpe = SUPR_jpe - SUPR_jpe * 0.167
        elif tear_1_len_MRI[i] < 1 and tear_1_len_MRI[i] >= 3:
            SUPR_pen_ang_cor = 9.9
            SUPR_jpe = 3.0 * 2.035
            SUPR_jpe = SUPR_jpe - SUPR_jpe * 0.167
        elif tear_1_len_MRI[i] < 3 and tear_1_len_MRI[i] >= 5:
            SUPR_pen_ang_cor = 13.3
            SUPR_jpe = 3.0 * 2.2
            SUPR_jpe = SUPR_jpe - SUPR_jpe * 0.167
        elif tear_1_len_MRI[i] > 5:
            SUPR_pen_ang_cor = 13.3
            SUPR_jpe = 3.0 * 2.2
            SUPR_jpe = SUPR_jpe - SUPR_jpe * 0.167
        else:
            SUPR_pen_ang_cor = 6.6
            SUPR_jpe = 3.0
            SUPR_jpe = SUPR_jpe - SUPR_jpe * 0.167

        if med == 0:
            med_x[0] = Medialization_x[0]
            med_y[0] = Medialization_y[0]
            med_z[0] = Medialization_z[0]
            Lt1_op[0] = Lt1[0] + Lt1[0] * 0.063
            Lf1_op[0] = Lf1[0]
        if med == 5:
            med_x[0] = Medialization_x[1]
            med_y[0] = Medialization_y[1]
            med_z[0] = Medialization_z[1]
            Lt1_op[0] = Lt1[1] + Lt1[1] * 0.063
            Lf1_op[0] = Lf1[1]
        if med == 10:
            med_x[0] = Medialization_x[2]
            med_y[0] = Medialization_y[2]
            med_z[0] = Medialization_z[2]
            Lt1_op[0] = Lt1[2] + Lt1[2] * 0.063
            Lf1_op[0] = Lf1[2]

        out_reh = Macro_sim(path_cal, path_mov, mov_attribute, mov, path_output_mus, SUPR_full_name,
                            output_mus_attribute,
                            med_x, med_y, med_z, Lf1_op, Lt1_op, load_var='Big_test.main.any',
                            height=pat_height, weight=pat_weight, pen_angle_SUPR=SUPR_pen_ang,
                            pen_angle_SUPR_a=SUPR_pen_ang_cor, jpe=SUPR_jpe)
        pas_for_sim_rehab = output_calib(out_reh, path_output_mus, SUPR_full_name, output_mus_attribute[1],
                                              muscle_nbr_SUPR, nstep)
        strength_sim_rehab = output_calib(out_reh, path_output_mus, SUPR_full_name, output_mus_attribute[0],
                                               muscle_nbr_SUPR, nstep)
        Ft_sim_rehab = output_calib(out_reh, path_output_mus, SUPR_full_name, 'Ft',
                                          muscle_nbr_SUPR, nstep)


    SUPR_strength_sim_0 = plotSingle(time_calib[0] * 120, strength_sim_0[0], 'Supraspinatus Strength ' + b[z]+ ', Medialization 0 mm', 'Abduction [°]', 'Strength [N]', 1.0)
    SUPR_pas_for_sim_0 = plotSingle(time_calib[0] * 120, pas_for_sim_0[0], 'Supraspinatus Passive Force ' + b[z]+ ' Medialization 0 mm', 'Abduction [°]', 'Passive Force [N]', 1.0)
    SUPR_Ft_sim_0 = plotSingle(time_calib[0] * 120, Ft_sim_0[0], 'Supraspinatus Tendon Force ' + b[z] + ' Medialization 0 mm', 'Abduction [°]', 'Tendon Force [N]', 1.0)

    SUPR_strength_sim_5 = plotSingle(time_calib[0] * 120, strength_sim_1[0], 'Supraspinatus Strength ' + b[z]+ ' Medialization 5 mm', 'Abduction [°]', 'Strength [N]', 1.0)
    SUPR_pas_for_sim_5 = plotSingle(time_calib[0] * 120, pas_for_sim_1[0], 'Supraspinatus Passive Force ' + b[z]+ ' Medialization 5 mm', 'Abduction [°]', 'Passive Force [N]', 1.0)
    SUPR_Ft_sim_5 = plotSingle(time_calib[0] * 120, Ft_sim_1[0], 'Supraspinatus Tendon Force ' + b[z] + ' Medialization 5 mm', 'Abduction [°]', 'Tendon Force [N]', 1.0)

    SUPR_strength_sim_10 = plotSingle(time_calib[0] * 120, strength_sim_2[0], 'Supraspinatus Strength ' + b[z]+ ' Medialization 10 mm', 'Abduction [°]', 'Strength [N]', 1.0)
    SUPR_pas_for_sim_10 = plotSingle(time_calib[0] * 120, pas_for_sim_2[0], 'Supraspinatus Passive Force ' + b[z]+ ' Medialization 10 mm', 'Abduction [°]', 'Passive Force [N]', 1.0)
    SUPR_Ft_sim_10 = plotSingle(time_calib[0] * 120, Ft_sim_2[0], 'Supraspinatus Tendon Force ' + b[z] + ' Medialization 10 mm', 'Abduction [°]', 'Tendon Force [N]', 1.0)


    if op == 1:
        rem_ten = 'Error'
        if med == 0:
            rem_ten = Lt1[0]*100
        elif med == 5:
            rem_ten = Lt1[1]*100
        elif med == 10:
            rem_ten = Lt1[2]*100

        fig, axs = plt.subplots(3, 5, figsize=(20, 15))
        fig.suptitle('Rotator cuff repairment simulation of ' + b[z] + ', Surgery recommended: Yes, Recommended medialization: %1i' % med + ' mm, Remaining tendon: %1.3f' % rem_ten + ' cm, Tear size: %1.3f' % tear_1_len_MRI[i] + ' cm')
        axs[0, 0].plot(time_calib[0] * 120, strength_calib[0], 'b')
        axs[1, 0].plot(time_calib[0] * 120, pas_for_calib[0], 'r')
        axs[2, 0].plot(time_calib[0] * 120, Ft_calib[0], 'g')
        axs[0, 0].set_title("Healthy Simulation")
        axs[0, 0].grid()
        axs[1, 0].grid()
        axs[2, 0].grid()
        axs[0, 0].set_ylabel("Supraspinatus strength [N]")
        axs[1, 0].set_ylabel("Supraspinatus passive force [N]")
        axs[2, 0].set_ylabel("Supraspinatus tendon force [N]")
        axs[2, 0].set_xlabel("Abduction [°]")

        axs[0, 1].plot(time_calib[0] * 120, strength_sim_0[0], 'b')
        axs[1, 1].plot(time_calib[0] * 120, pas_for_sim_0[0], 'r')
        axs[2, 1].plot(time_calib[0] * 120, Ft_sim_0[0], 'g')
        axs[0, 1].set_title("RCR with 0 mm medialization")
        axs[0, 1].grid()
        axs[1, 1].grid()
        axs[2, 1].grid()
        axs[2, 1].set_xlabel("Abduction [°]")

        axs[0, 2].plot(time_calib[0] * 120, strength_sim_1[0], 'b')
        axs[1, 2].plot(time_calib[0] * 120, pas_for_sim_1[0], 'r')
        axs[2, 2].plot(time_calib[0] * 120, Ft_sim_1[0], 'g')
        axs[0, 2].set_title("RCR with 5 mm medialization")
        axs[0, 2].grid()
        axs[1, 2].grid()
        axs[2, 2].grid()
        axs[2, 2].set_xlabel("Abduction [°]")

        axs[0, 3].plot(time_calib[0] * 120, strength_sim_2[0], 'b')
        axs[1, 3].plot(time_calib[0] * 120, pas_for_sim_2[0], 'r')
        axs[2, 3].plot(time_calib[0] * 120, Ft_sim_2[0], 'g')
        axs[0, 3].set_title("RCR with 10 mm medialization")
        axs[0, 3].grid()
        axs[1, 3].grid()
        axs[2, 3].grid()
        axs[2, 3].set_xlabel("Abduction [°]")

        axs[0, 4].plot(time_calib[0] * 120, strength_sim_rehab[0], 'b')
        axs[1, 4].plot(time_calib[0] * 120, pas_for_sim_rehab[0], 'r')
        axs[2, 4].plot(time_calib[0] * 120, Ft_sim_rehab[0], 'g')
        axs[0, 4].set_title("Rehabilitation prediction")
        axs[0, 4].grid()
        axs[1, 4].grid()
        axs[2, 4].grid()
        axs[2, 4].set_xlabel("Abduction [°]")

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.savefig(b[z])
        fig.clf()


    else:
        rem_ten = Lt1[0]

        fig, axs = plt.subplots(3, 4, figsize=(20, 15))
        fig.suptitle('Rotator cuff repairment simulation of ' + b[z] + ', Surgery recommended: No,' + ' Remaining tendon: %1.3f' % rem_ten + ' cm,' + ' Tear size: %1.3f' % tear_1_len_MRI[i] + ' cm')
        axs[0, 0].plot(time_calib[0] * 120, strength_calib[0], 'b')
        axs[1, 0].plot(time_calib[0] * 120, pas_for_calib[0], 'r')
        axs[0, 0].set_title("Healthy Simulation")
        axs[0, 0].grid()
        axs[1, 0].grid()
        axs[2, 0].grid()
        axs[0, 0].set_ylabel("Supraspinatus strength [N]")
        axs[1, 0].set_ylabel("Supraspinatus passive force [N]")
        axs[2, 0].set_ylabel("Supraspinatus tendon force [N]")
        axs[2, 0].set_xlabel("Abduction [°]")

        axs[0, 1].plot(time_calib[0] * 120, strength_sim_0[0], 'b')
        axs[1, 1].plot(time_calib[0] * 120, pas_for_sim_0[0], 'r')
        axs[2, 1].plot(time_calib[0] * 120, Ft_sim_0[0], 'g')
        axs[0, 1].set_title("RCR with 0 mm medialization")
        axs[0, 1].grid()
        axs[1, 1].grid()
        axs[2, 1].grid()
        axs[2, 1].set_xlabel("Abduction [°]")

        axs[0, 2].plot(time_calib[0] * 120, strength_sim_1[0], 'b')
        axs[1, 2].plot(time_calib[0] * 120, pas_for_sim_1[0], 'r')
        axs[2, 2].plot(time_calib[0] * 120, Ft_sim_1[0], 'g')
        axs[0, 2].set_title("RCR with 5 mm medialization")
        axs[0, 2].grid()
        axs[1, 2].grid()
        axs[2, 2].grid()
        axs[2, 2].set_xlabel("Abduction [°]")

        axs[0, 3].plot(time_calib[0] * 120, strength_sim_2[0], 'b')
        axs[1, 3].plot(time_calib[0] * 120, pas_for_sim_2[0], 'r')
        axs[2, 3].plot(time_calib[0] * 120, Ft_sim_2[0], 'g')
        axs[0, 3].set_title("RCR with 10 mm medialization")
        axs[0, 3].grid()
        axs[1, 3].grid()
        axs[2, 3].grid()
        axs[2, 3].set_xlabel("Abduction [°]")

        fig.tight_layout()
        fig.subplots_adjust(top=0.9)
        fig.savefig(b[z])
        fig.clf()

    z = z +1