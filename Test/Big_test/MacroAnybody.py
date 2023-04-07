from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)
from anypytools import AnyMacro
from anypytools import AnyPyProcess
import numpy as np
from MainRotSim import *

app = AnyPyProcess(num_processes=3)

def startMacroMomentArm ():
    macro = [
        Load('C:\Program Files\AnyBody Technology\AnyBody.7.3\AMMR\Application\Validation\EvaluateMomentArms\EvaluateMomentArms.main.any'),

        OperationRun('Main.RunApplication'),

        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_1'),
        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_2'),
        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_3'),
        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_4'),
        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_5'),
        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_6'),

        Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.Abscissa.t'),
    ]
    output = app.start_macro(macro)

    return output


def startMacro1P(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = '1P_Calib/1P_Calib.main.any'):

    macro = []
    for i in range(len(test_var)):
        macro.append([
            Load(load_var),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[i]),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),
            Dump('Main.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + TMN_full_name + '_6'),

        ])
    output = app.start_macro(macro)

    return output


def startMacro2P(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = 'Big_test.main.any'):

    macro = []
    for i in range(len(test_var)):
        macro.append([
            Load(load_var),

            SetValue('Main.HumanModel.Calibration.RMin', 0.35),  # average which fits overall
            SetValue('Main.HumanModel.Calibration.RMax', 1.1),  # average which fits overall

            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[i]),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),
            Dump('Main.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + TMN_full_name + '_6'),

        ])
    output = app.start_macro(macro)

    return output



## Rmin, Rmax from Literature GARNER and PANDY 2002

def startMacroRR(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = 'Big_test.main.any'):
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
    for i in range(len(test_var[0])):
        macro.append([
            Load(load_var),

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
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[0][i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[1][i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[2][i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[3][i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[4][i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[5][i]),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),

            Dump('Main.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + TMN_full_name + '_6'),

        ])

    # parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
    output = app.start_macro(macro)
    # app.save_results("test.db")
    return output


## Momentarm

def startMacro2PMoM(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = 'C:\Program Files\AnyBody Technology\AnyBody.7.3\AMMR\Application\Validation\EvaluateMomentArms\EvaluateMomentArms.main.any'):

    macro = []
    for i in range(len(test_var)):
        macro.append([
            Load(load_var),

            SetValue('Main.HumanModel.Calibration.RMin', 0.35),  # average which fits overall
            SetValue('Main.HumanModel.Calibration.RMax', 1.1),  # average which fits overall

            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[i]),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),
            Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1'),
            Dump(path_output_mus + SUPR_full_name + '_2'),
            Dump(path_output_mus + SUPR_full_name + '_3'),
            Dump(path_output_mus + SUPR_full_name + '_4'),
            Dump(path_output_mus + SUPR_full_name + '_5'),
            Dump(path_output_mus + SUPR_full_name + '_6'),
            # Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1'),
            Dump(path_output_mus + SBSC_full_name + '_2'),
            Dump(path_output_mus + SBSC_full_name + '_3'),
            Dump(path_output_mus + SBSC_full_name + '_4'),
            Dump(path_output_mus + SBSC_full_name + '_5'),
            Dump(path_output_mus + SBSC_full_name + '_6'),
            # Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1'),
            Dump(path_output_mus + INFR_full_name + '_2'),
            Dump(path_output_mus + INFR_full_name + '_3'),
            Dump(path_output_mus + INFR_full_name + '_4'),
            Dump(path_output_mus + INFR_full_name + '_5'),
            Dump(path_output_mus + INFR_full_name + '_6'),
            # Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1'),
            Dump(path_output_mus + TMN_full_name + '_2'),
            Dump(path_output_mus + TMN_full_name + '_3'),
            Dump(path_output_mus + TMN_full_name + '_4'),
            Dump(path_output_mus + TMN_full_name + '_5'),
            Dump(path_output_mus + TMN_full_name + '_6'),
            # Dump(path_output_mus + TMN_full_name + '_6'),

        ])
    output = app.start_macro(macro)

    return output



## Rmin, Rmax from Literature GARNER and PANDY 2002

def startMacroRRMoM(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = 'C:\Program Files\AnyBody Technology\AnyBody.7.3\AMMR\Application\Validation\EvaluateMomentArms\EvaluateMomentArms.main.any'):
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
    for i in range(len(test_var)):
        macro.append([
            Load(load_var),

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
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[i]),

            UpdateValues(),

            OperationRun('Main.Study.InverseDynamics'),

            Dump('Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1'),
            Dump(path_output_mus + SUPR_full_name + '_2'),
            Dump(path_output_mus + SUPR_full_name + '_3'),
            Dump(path_output_mus + SUPR_full_name + '_4'),
            Dump(path_output_mus + SUPR_full_name + '_5'),
            Dump(path_output_mus + SUPR_full_name + '_6'),
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1'),
            Dump(path_output_mus + SBSC_full_name + '_2'),
            Dump(path_output_mus + SBSC_full_name + '_3'),
            Dump(path_output_mus + SBSC_full_name + '_4'),
            Dump(path_output_mus + SBSC_full_name + '_5'),
            Dump(path_output_mus + SBSC_full_name + '_6'),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1'),
            Dump(path_output_mus + INFR_full_name + '_2'),
            Dump(path_output_mus + INFR_full_name + '_3'),
            Dump(path_output_mus + INFR_full_name + '_4'),
            Dump(path_output_mus + INFR_full_name + '_5'),
            Dump(path_output_mus + INFR_full_name + '_6'),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1'),
            Dump(path_output_mus + TMN_full_name + '_2'),
            Dump(path_output_mus + TMN_full_name + '_3'),
            Dump(path_output_mus + TMN_full_name + '_4'),
            Dump(path_output_mus + TMN_full_name + '_5'),
            Dump(path_output_mus + TMN_full_name + '_6'),
            #Dump(path_output_mus + TMN_full_name + '_6'),

        ])

    # parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
    output = app.start_macro(macro)
    return output




## Rmin, Rmax from Literature GARNER and PANDY 2002

def startMacroRRGet(test_var, path_cal, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, input_mus_full,  load_var = 'Big_test.main.any'):
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
    for i in range(len(test_var)):
        macro.append([
            Load(load_var),

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
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            OperationRun('Main.Study.InverseDynamics'),

            Dump('Main.Study.Output.Abscissa.t'),

            # Dump Supraspinatus Strength
            Dump(path_output_mus + input_mus_full + '_1.' + output_mus_attribute),
            Dump(path_output_mus + input_mus_full + '_2.' + output_mus_attribute),
            Dump(path_output_mus + input_mus_full + '_3.' + output_mus_attribute),
            Dump(path_output_mus + input_mus_full + '_4.' + output_mus_attribute),
            Dump(path_output_mus + input_mus_full + '_5.' + output_mus_attribute),
            Dump(path_output_mus + input_mus_full + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute),
            #Dump(path_output_mus + TMN_full_name + '_6'),

        ])

    # parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
    output = app.start_macro(macro)
    return output


def startMacroRRParSty(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute, load_var = 'Big_test.main.any', tArray = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]):
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
    for i in range(len(test_var[0])):
        macro.append([
            Load(load_var, defs={'N_STEP': 100}),

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
            UpdateValues(),

            OperationRun('HumanModel.Calibration.CalibrationSequence'),

            SetValue(path_mov + mov_attribute, mov),

            SetValue(path_input_mus + mus_input + '_1.' + attribute_input, test_var[0][i]),
            SetValue(path_input_mus + mus_input + '_2.' + attribute_input, test_var[1][i]),
            SetValue(path_input_mus + mus_input + '_3.' + attribute_input, test_var[2][i]),
            SetValue(path_input_mus + mus_input + '_4.' + attribute_input, test_var[3][i]),
            SetValue(path_input_mus + mus_input + '_5.' + attribute_input, test_var[4][i]),
            SetValue(path_input_mus + mus_input + '_6.' + attribute_input, test_var[5][i]),

            # SetValue('Main.Study.tArray', tArray),

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
            #Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute[0]),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute[0]),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute[0]),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute[0]),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute[0]),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute[0]),
            #Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute[0]),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute[0]),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute[0]),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute[0]),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute[0]),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute[0]),
            #Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute[0]),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute[0]),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute[0]),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute[0]),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute[0]),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute[0]),
            #Dump(path_output_mus + TMN_full_name + '_6'),

            ## Lt
            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[1]),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[1]),
            # Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute[1]),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute[1]),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute[1]),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute[1]),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute[1]),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute[1]),
            # Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute[1]),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute[1]),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute[1]),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute[1]),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute[1]),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute[1]),
            # Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute[1]),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute[1]),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute[1]),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute[1]),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute[1]),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute[1]),
            # Dump(path_output_mus + TMN_full_name + '_6'),

            ## Lm
            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[2]),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[2]),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[2]),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[2]),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[2]),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[2]),
            # Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute[2]),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute[2]),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute[2]),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute[2]),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute[2]),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute[2]),
            # Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute[2]),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute[2]),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute[2]),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute[2]),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute[2]),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute[2]),
            # Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute[2]),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute[2]),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute[2]),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute[2]),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute[2]),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute[2]),
            # Dump(path_output_mus + TMN_full_name + '_6'),

            ## Activity
            # Dump Supraspinatus Strength
            Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute[3]),
            Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute[3]),
            Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute[3]),
            Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute[3]),
            Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute[3]),
            Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute[3]),
            # Dump(path_output_mus + SUPR_full_name + '_6'),

            # Dump Subscapularis Strength
            Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute[3]),
            Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute[3]),
            Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute[3]),
            Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute[3]),
            Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute[3]),
            Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute[3]),
            # Dump(path_output_mus + SBSC_full_name + '_6'),

            # Dump Infraspinatus Strength
            Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute[3]),
            Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute[3]),
            Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute[3]),
            Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute[3]),
            Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute[3]),
            Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute[3]),
            # Dump(path_output_mus + INFR_full_name + '_6'),

            # Dump Teres Minor Strength
            Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute[3]),
            Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute[3]),
            Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute[3]),
            Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute[3]),
            Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute[3]),
            Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute[3]),
            # Dump(path_output_mus + TMN_full_name + '_6'),

        ])

    # parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
    output = app.start_macro(macro)
    app.save_results('Muscle_' + mus_input + '_Input_' + attribute_input + '.db')
    app.save_results('Muscle_' + mus_input + '_Input_' + attribute_input + '.xlsx')
    return output




