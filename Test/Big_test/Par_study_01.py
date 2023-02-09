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

nstep = 11

## Initialisation
# Test Attributes
test_var = [0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12]
test_str = ["" for x in range(len(test_var))]
for j in range(len(test_var)):
    test_str[j] = str(test_var[j])

# Calibration Attributes
path_cal = 'Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.'

# Input Attributes
path_input_mus = 'Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.'
mus_input = 'supraspinatus' # supraspinatus, subscapularis, infraspinatus, teres_minor
attribute_input = 'Lf0' # F0 [N], Lf0 [m], Vol0 [m^3], Lt0 [m], Gamma0 [rad], Epsilon0 [-], Fcfast [-] (0-1), Jt [-](rec = 3), Jpe [-](rec = 3), K1 [s^-1](2), K2 [s^-1](8), PEFactor [-], Lfbar [-], Gammabar [-], Epsilonbar [-]

# Movement attributes
mov = 120.0 # [°] Degrees
path_mov = 'Main.HumanModel.Mannequin.PostureVel.Right.'
mov_attribute = 'GlenohumeralAbduction' # GlenohumeralFlexion, GlenohumeralAbduction, GlenohumeralExternalRotation, ElbowFlexion, ElbowPronation

# Input Attributes
path_output_mus = 'Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.'
output_mus_attribute = 'Activity' # Fin, Fout, Lmt, Lm, Lt, LmtDot, LmDot, Activity, CorrectedActivity, Fm, Ft, Fp, Strength, Ft0, Ft0Grad, PennationAngle, EPOTt, EPOTt, EPOTmt, Pt, Pm, Pmt, Pmet
list_var = ['Lmt', 'Lm', 'Lt', 'LmtDot', 'LmDot', 'Activity', 'CorrectedActivity', 'Fm', 'Ft', 'Fp', 'Strength', 'Ft0', 'Ft0Grad', 'PennationAngle', 'EPOTt', 'EPOTt', 'EPOTmt', 'Pt', 'Pm', 'Pmt', 'Pmet']

#g=0

#for list in list_var:
    #print(list)
    #print(g)
    #g=g+1

# Plot Attributes
xlabel = 'Abduction [°]'
ylabel = 'Force [N]'
add_label = ' m'

## Muscles which are examined

# supraspinatus
SUPR_full_name = 'supraspinatus'
SUPR_short_name = 'SUPR'
muscle_nbr_SUPR = 6

# Subscapularis
SBSC_full_name = 'subscapularis'
SBSC_short_name = 'SBSC'
muscle_nbr_SBSC = 6

# Infraspinatus
INFR_full_name = 'infraspinatus'
INFR_short_name = 'INFR'
muscle_nbr_INFR = 6

# Teres minor
TMN_full_name = 'teres_minor'
TMN_short_name = 'TMN'
muscle_nbr_TMN = 6

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

def startMacro2P(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute):

    macro = []
    for i in range(len(test_var)):
        macro.append([
            Load('Big_test.main.any'),

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


## Rmin, Rmax from Literature GARNER and PANDY 2002

def startMacroRR(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute):
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
            Load('Big_test.main.any'),

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
    return output

# Output

class GetOutput:

    def __init__(self, macro_output, path, number_mus, attribute_name, nbr_test, steps):
        self.macro_output = macro_output
        self.path = path
        self.number_mus = number_mus # nbr of muscle
        self.attribute_name = attribute_name
        self.nbr_test = nbr_test # nbr be tested
        self.steps = steps # time steps

    def extract_mus(self, name):

        temp = np.zeros((self.number_mus, len(self.nbr_test), self.steps))
        temp_nbr = [str(x + 1) for x in range(self.number_mus)]

        for i in range(self.number_mus):
            temp[i] = self.macro_output[self.path + name + '_' + temp_nbr[i] + '.' + self.attribute_name]

        return temp

    def sum_mus(self, muscles):
        sum = np.zeros((len(self.nbr_test),self.steps), dtype=float)

        for x in range(len(self.nbr_test)):
            for y in range(self.steps):
                for z in range(self.number_mus):
                    sum[x][y] = sum[x][y] + muscles[z][x][y]

        return sum

    def extract_mom(self, name):

        temp = np.zeros((self.number_mus, len(self.nbr_test), self.steps))
        temp_nbr = [str(x + 1) for x in range(self.number_mus)]

        for i in range(self.number_mus):
            temp[i] = self.macro_output[self.path + name + '_' + temp_nbr[i]]

        return temp

class MyPlot:

    def __init__(self, xaxis, yaxis, label, title = 'No title', xlab = 'x-label is not defined', ylab = 'y-label is not defined', add_label = '', con_fac = 1.0):  # Constructor: These parameters will be used upon class calling(Except self)
        self.xaxis = xaxis  # self refers to global variables that can only be used throughout the class
        self.yaxis = yaxis
        self.label = label
        self.add_label = add_label
        self.xlab = xlab
        self.ylab = ylab
        self.title = title
        self.con_fac = con_fac

    def plotting(self):
        for a in range(len(self.yaxis)):
            plt.plot(self.xaxis[a] * self.con_fac, self.yaxis[a], label=self.label[a] + self.add_label)

        plt.xlabel(self.xlab)
        plt.ylabel(self.ylab)
        plt.title(self.title)
        plt.legend()
        plt.savefig(self.title)
        plt.clf()

    def plotMom(self):

        print(self.yaxis[0])
        plt.plot(self.xaxis[0] * self.con_fac, self.yaxis[0])

        plt.xlabel(self.xlab)
        plt.ylabel(self.ylab)
        plt.title(self.title)
        plt.savefig(self.title)
        plt.clf()

out_mom_arm = startMacroMomentArm()

time_mom = out_mom_arm['Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.Abscissa.t']

print(time_mom)

path_output_mom = 'Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.'

mom_arm_get = GetOutput(macro_output=out_mom_arm, path=path_output_mom, number_mus=muscle_nbr_SUPR, attribute_name= '', nbr_test=[1], steps=10)

SUPR_mom_arm = mom_arm_get.sum_mus(muscles = mom_arm_get.extract_mom(name = SUPR_full_name))

print(SUPR_mom_arm)

SUPR_mom_arm_plt = MyPlot(xaxis = time_mom, yaxis = SUPR_mom_arm,label = '', title = 'Momentarm of ' + SUPR_full_name, xlab = xlabel, ylab = ylabel, add_label = '', con_fac=mov)
SUPR_mom_arm_plt.plotMom()

output = startMacroRR(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)

print(output)

#for i in range(len(list_var)):

#print(list_var)
#for list in list_var:
#print(list)
#output_mus_attribute = list
time = output['Main.Study.Output.Abscissa.t']

test = GetOutput(macro_output=output, path=path_output_mus, number_mus=muscle_nbr_SUPR,
                     attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)




SUPR = test.sum_mus(muscles = test.extract_mus(name = SUPR_full_name))
SBSC = test.sum_mus(muscles = test.extract_mus(name = SBSC_full_name))
INFR = test.sum_mus(muscles = test.extract_mus(name = INFR_full_name))
TMN = test.sum_mus(muscles = test.extract_mus(name = TMN_full_name))

# supraspinatus
SUPR_plt = MyPlot(xaxis = time, yaxis = SUPR, label = test_str, title = 'Influence of different ' + attribute_input + ' on Supraspinatus ' + output_mus_attribute + ' during ' + mov_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
SUPR_plt.plotting()

# Subscapularis
SBSC_plt = MyPlot(xaxis = time, yaxis = SBSC, label = test_str, title = 'Influence of different ' + attribute_input + ' on Subscapularis ' + output_mus_attribute + ' during ' + mov_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
SBSC_plt.plotting()

# Infraspinatus
INFR_plt = MyPlot(xaxis = time, yaxis = INFR, label = test_str, title = 'Influence of different ' + attribute_input + ' on Infraspinatus ' + output_mus_attribute + ' during ' + mov_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
INFR_plt.plotting()

# Teres minor
TMN_plt = MyPlot(xaxis = time, yaxis = TMN, label = test_str, title = 'Influence of different ' + attribute_input + ' on Teres minor ' + output_mus_attribute + ' during ' + mov_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
TMN_plt.plotting()

"""
for a in range(len(SUPR)):
    plt.plot(time[a]*120, SUPR[a], label=test_str[a]+' N')

plt.xlabel("Abduction [°]")
plt.ylabel("Force [N]")
plt.title("Influence of different F0")
plt.legend()
plt.show()
"""
"""

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


## End of initalisation of Rmin and Rmax

macro = []
for i in range(len(test_var)):
    macro.append([
        Load('Big_test.main.any'),

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

        Dump('Main.Study.Output.Abscissa.t'),

        # Dump Supraspinatus Strength
        Dump(path_output_mus + SUPR_full_name + '_1.' + output_mus_attribute),
        Dump(path_output_mus + SUPR_full_name + '_2.' + output_mus_attribute),
        Dump(path_output_mus + SUPR_full_name + '_3.' + output_mus_attribute),
        Dump(path_output_mus + SUPR_full_name + '_4.' + output_mus_attribute),
        Dump(path_output_mus + SUPR_full_name + '_5.' + output_mus_attribute),
        Dump(path_output_mus + SUPR_full_name + '_6.' + output_mus_attribute),

        # Dump Subscapularis Strength
        Dump(path_output_mus + SBSC_full_name + '_1.' + output_mus_attribute),
        Dump(path_output_mus + SBSC_full_name + '_2.' + output_mus_attribute),
        Dump(path_output_mus + SBSC_full_name + '_3.' + output_mus_attribute),
        Dump(path_output_mus + SBSC_full_name + '_4.' + output_mus_attribute),
        Dump(path_output_mus + SBSC_full_name + '_5.' + output_mus_attribute),
        Dump(path_output_mus + SBSC_full_name + '_6.' + output_mus_attribute),

        # Dump Infraspinatus Strength
        Dump(path_output_mus + INFR_full_name + '_1.' + output_mus_attribute),
        Dump(path_output_mus + INFR_full_name + '_2.' + output_mus_attribute),
        Dump(path_output_mus + INFR_full_name + '_3.' + output_mus_attribute),
        Dump(path_output_mus + INFR_full_name + '_4.' + output_mus_attribute),
        Dump(path_output_mus + INFR_full_name + '_5.' + output_mus_attribute),
        Dump(path_output_mus + INFR_full_name + '_6.' + output_mus_attribute),

        # Dump Teres Minor Strength
        Dump(path_output_mus + TMN_full_name + '_1.' + output_mus_attribute),
        Dump(path_output_mus + TMN_full_name + '_2.' + output_mus_attribute),
        Dump(path_output_mus + TMN_full_name + '_3.' + output_mus_attribute),
        Dump(path_output_mus + TMN_full_name + '_4.' + output_mus_attribute),
        Dump(path_output_mus + TMN_full_name + '_5.' + output_mus_attribute),
        Dump(path_output_mus + TMN_full_name + '_6.' + output_mus_attribute),

    ])

#parameter_study_macro = AnyMacro(macro, number_of_macros= len(parameters))
output = app.start_macro(macro)


# Output variables

# supraspinatus
SUPR = np.zeros((len(test_var),nstep),dtype=float)
# Subscapularis
SBSC = np.zeros((len(test_var),nstep),dtype=float)
# Infraspinatus
INFR = np.zeros((len(test_var),nstep),dtype=float)
# Teres minor
TMN = np.zeros((len(test_var),nstep),dtype=float)

# Get output values
# supraspinatus
SUPR_1 = output[path_output_mus + 'supraspinatus_1.' + output_mus_attribute]
SUPR_2 = output[path_output_mus + 'supraspinatus_2.' + output_mus_attribute]
SUPR_3 = output[path_output_mus + 'supraspinatus_3.' + output_mus_attribute]
SUPR_4 = output[path_output_mus + 'supraspinatus_4.' + output_mus_attribute]
SUPR_5 = output[path_output_mus + 'supraspinatus_5.' + output_mus_attribute]
SUPR_6 = output[path_output_mus + 'supraspinatus_6.' + output_mus_attribute]

# Subscapularis
SBSC_1 = output[path_output_mus + 'subscapularis_1.' + output_mus_attribute]
SBSC_2 = output[path_output_mus + 'subscapularis_2.' + output_mus_attribute]
SBSC_3 = output[path_output_mus + 'subscapularis_3.' + output_mus_attribute]
SBSC_4 = output[path_output_mus + 'subscapularis_4.' + output_mus_attribute]
SBSC_5 = output[path_output_mus + 'subscapularis_5.' + output_mus_attribute]
SBSC_6 = output[path_output_mus + 'subscapularis_6.' + output_mus_attribute]

# Infraspinatus
INFR_1 = output[path_output_mus + 'infraspinatus_1.' + output_mus_attribute]
INFR_2 = output[path_output_mus + 'infraspinatus_2.' + output_mus_attribute]
INFR_3 = output[path_output_mus + 'infraspinatus_3.' + output_mus_attribute]
INFR_4 = output[path_output_mus + 'infraspinatus_4.' + output_mus_attribute]
INFR_5 = output[path_output_mus + 'infraspinatus_5.' + output_mus_attribute]
INFR_6 = output[path_output_mus + 'infraspinatus_6.' + output_mus_attribute]

# Teres minor
TMN_1 = output[path_output_mus + 'teres_minor_1.' + output_mus_attribute]
TMN_2 = output[path_output_mus + 'teres_minor_2.' + output_mus_attribute]
TMN_3 = output[path_output_mus + 'teres_minor_3.' + output_mus_attribute]
TMN_4 = output[path_output_mus + 'teres_minor_4.' + output_mus_attribute]
TMN_5 = output[path_output_mus + 'teres_minor_5.' + output_mus_attribute]
TMN_6 = output[path_output_mus + 'teres_minor_6.' + output_mus_attribute]


for i in range(len(test_var)):
    SUPR[i] = SUPR_1[i]+SUPR_2[i]+SUPR_3[i]+SUPR_4[i]+SUPR_5[i]+SUPR_6[i]
    SBSC[i] = SBSC_1[i]+SBSC_2[i]+SBSC_3[i]+SBSC_4[i]+SBSC_5[i]+SBSC_6[i]
    INFR[i] = INFR_1[i]+INFR_2[i]+INFR_3[i]+INFR_4[i]+INFR_5[i]+INFR_6[i]
    TMN[i] = TMN_1[i]+TMN_2[i]+TMN_3[i]+TMN_4[i]+TMN_5[i]+TMN_6[i]




"""