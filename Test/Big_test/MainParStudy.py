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

#Get tendon lenght
Cal_tpy = '_CALIBRATION_TYPE_2PAR_'

nstep = 100

## Initialisation
# Test Attributes
test_var = [76.0]
test_str = ["" for x in range(len(test_var))]
for j in range(len(test_var)):
    test_str[j] = str(test_var[j])

# Calibration Attributes
# Input Attributes
mus_input = 'infraspinatus' # supraspinatus, subscapularis, infraspinatus, teres_minor
attribute_input = 'F0' # F0 [N], Lf0 [m], Vol0 [m^3], Lt0 [m], Gamma0 [rad], Epsilon0 [-], Fcfast [-] (0-1), Jt [-](rec = 3), Jpe [-](rec = 3), K1 [s^-1](2), K2 [s^-1](8), PEFactor [-], Lfbar [-], Gammabar [-], Epsilonbar [-]
add_label = ' '
input_mus_full = INFR_full_name
mus_nbr = muscle_nbr_INFR
list_var_in = ['K2'] # ['F0', 'Lf0', 'Lt0', 'Epsilon0', 'Fcfast', 'Jt', 'Jpe', 'K1', 'PEFactor', 'Gamma0'] Gamma0, K2, Vol0

# Movement attributes
mov = -60.0 # [°] Degrees
mov_attribute = 'GlenohumeralExternalRotation' # GlenohumeralFlexion, GlenohumeralAbduction, GlenohumeralExternalRotation, ElbowFlexion, ElbowPronation

# Output Attributes
output_mus_attribute = ''  # Fin, Fout, Lmt, Lm, Lt, LmtDot, LmDot, Activity, CorrectedActivity, Fm, Ft, Fp, Strength, Ft0, Ft0Grad, PennationAngle, EPOTt, EPOTt, EPOTmt, Pt, Pm, Pmt, Pmet
list_var = ['Lm', 'Lt', 'Activity', 'PennationAngle'] # ['Lm', 'Lt', 'Activity', 'PennationAngle'], ['Strength', 'Fm', 'Ft', 'Fp']

# Plot Attributesss
xlabel = 'Abduction [°]'
ylabel = 'Strength [N]'
list_y_label = ['Muscle length [m]', 'Tendon length [m]', 'Activity [-]', 'Pennation Angle [rad]'] # ['Muscle length [m]', 'Tendon length [m]', 'Activity [-]', 'Pennation Angle [rad]'], ['Strength [N]', 'Fm [N]', 'Ft [N]', 'Fp [N]']
"""
x = 0
for y in list_var_in:

    output_var = startMacroRRGet(test_var, path_cal, path_input_mus, SUPR_full_name, SBSC_full_name, INFR_full_name,
                                 TMN_full_name, list_var_in[x], input_mus_full)

    auto_test_var = AutoExtrInput(output_var, path_input_mus, input_mus_full, list_var_in[x], mus_nbr)

    print(auto_test_var)

    output = startMacroRRParSty(auto_test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input,
                          list_var_in[x], path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name,
                          TMN_full_name, list_var)

    time = output['Main.Study.Output.Abscissa.t']
    z = 0

    SUPR = np.zeros((len(list_var), 7, nstep),  float)
    SBSC = np.zeros((len(list_var), 7, nstep),  float)
    INFR = np.zeros((len(list_var), 7, nstep),  float)
    TMN = np.zeros((len(list_var), 7, nstep),  float)

    test_str_aut = ["" for x in range(len(auto_test_var[0]))]

    for g in list_var:
        output_mus_attribute = list_var[z]
        ylabel = list_y_label[z]
        print(output_mus_attribute)
        print(ylabel)


        test_str_aut = ["" for x in range(len(auto_test_var[0]))]
        for j in range(len(auto_test_var[0])):
            test_str_aut[j] = str(auto_test_var[0][j])


        test = GetOutput(macro_output=output, path=path_output_mus, number_mus=muscle_nbr_SUPR,
                         attribute_name=output_mus_attribute, nbr_test=auto_test_var[0], steps=nstep)
        print(test.sum_mus(muscles=test.extract_mus(name=SUPR_full_name)))
        SUPR[z] = test.sum_mus(muscles=test.extract_mus(name=SUPR_full_name))
        SBSC[z] = test.sum_mus(muscles=test.extract_mus(name=SBSC_full_name))
        INFR[z] = test.sum_mus(muscles=test.extract_mus(name=INFR_full_name))
        TMN[z] = test.sum_mus(muscles=test.extract_mus(name=TMN_full_name))
        z = z + 1

    # supraspinatus
    #SUPR_plt = plotMulti(xaxis=time, yaxis=SUPR, label=test_str_aut,
    #                         title='Supraspinatus Input(Box) ' + list_var_in[x] + ', Output ' + output_mus_attribute,
    #                         xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov)
    print(SUPR)
    x = x + 1
"""

x = 0

for y in list_var_in:

    # output_var = startMacroRRGet(test_var, path_cal, path_input_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, list_var_in[x], input_mus_full)
    # print(output)

    # auto_test_var = AutoExtrInput(output_var, path_input_mus, input_mus_full, list_var_in[x], mus_nbr)

    auto_test_var = [[2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5], [2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5],
                     [2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5], [2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5],
                     [2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5], [2.5, 5.0, 7.5, 10, 12.5, 15.0, 17.5]] # K2

    # Vol0/Sup auto_test_var = [[0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009], [0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009],
    #                 [0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009], [0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009],
    #                 [0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009], [0.00003, 0.00004, 0.00005, 0.00006, 0.00007, 0.00008, 0.00009]]

    # auto_test_var = [[0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021],
    #                 [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021],
    #                 [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021]] # Vol0/Sub

    # auto_test_var = [[0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021],
    #                 [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021],
    #                 [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021], [0.00003, 0.00006, 0.00009, 0.00012, 0.00015, 0.00018, 0.00021]] # Vol0/Inf

    # auto_test_var = [[0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007], [0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007],
    #                 [0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007], [0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007],
    #                 [0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007], [0.00001, 0.00002, 0.00003, 0.00004, 0.00005, 0.00006, 0.00007]] # Vol0/Ter

    # Gamma0/Sup auto_test_var = [[0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619], [0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619],
    #                 [0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619], [0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619],
    #                 [0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619], [0.043633231, 0.087266463, 0.130899694, 0.174532925, 0.218166156, 0.261799388, 0.305432619]]

    # auto_test_var = [[0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776]] # Gamma0/Sub

    # auto_test_var = [[0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776]] # Gamma0/Inf

    # auto_test_var = [[0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776],
    #                 [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776], [0.0, 0.087266463, 0.174532925, 0.261799388, 0.34906585, 0.436332313, 0.523598776]] # Gamma0/Ter

    print(auto_test_var)

    output = startMacroRRParSty(auto_test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input,
                          list_var_in[x], path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name,
                          TMN_full_name, list_var, tArray=tArray)
    # app.save_results(mus_input + 'Input_' + list_var_in[x] + '_Output_' + output_mus_attribute)
    # output = app.load_results('test.db')

    time = output['Main.Study.Output.Abscissa.t']
    # print(output)
    z = 0

    for g in list_var:
        output_mus_attribute = list_var[z]
        ylabel = list_y_label[z]
        # print(output_mus_attribute)
        # print(ylabel)
        z = z + 1

        test_str_aut = ["" for x in range(len(auto_test_var[0]))]
        for j in range(len(auto_test_var[0])):
            test_str_aut[j] = str(auto_test_var[0][j])


        test = GetOutput(macro_output=output, path=path_output_mus, number_mus=muscle_nbr_SUPR,
                         attribute_name=output_mus_attribute, nbr_test=auto_test_var[0], steps=nstep)

        #app.save_results('Input ' + list_var_in[x] + ', Output ' + output_mus_attribute)

        SUPR = test.sum_mus(muscles=test.extract_mus(name=SUPR_full_name))
        SBSC = test.sum_mus(muscles=test.extract_mus(name=SBSC_full_name))
        INFR = test.sum_mus(muscles=test.extract_mus(name=INFR_full_name))
        TMN = test.sum_mus(muscles=test.extract_mus(name=TMN_full_name))

        np.savetxt('Supraspinatus Input ' + list_var_in[x] + ', Output ' + output_mus_attribute, SUPR, delimiter=',')
        np.savetxt('Subscapularis Input ' + list_var_in[x] + ', Output ' + output_mus_attribute, SBSC, delimiter=',')
        np.savetxt('Infraspinatus Input ' + list_var_in[x] + ', Output ' + output_mus_attribute, INFR, delimiter=',')
        np.savetxt('Teres minor Input ' + list_var_in[x] + ', Output ' + output_mus_attribute, TMN, delimiter=',')



        # supraspinatus
        SUPR_plt = plotMulti(xaxis=time, yaxis=SUPR, label=test_str_aut,
                             title='Supraspinatus Input(Box) ' + list_var_in[x] + ', Output ' + output_mus_attribute,
                             xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov, con_fac_y=(1.0))
        # Subscapularis
        SBSC_plt = plotMulti(xaxis=time, yaxis=SBSC, label=test_str_aut,
                             title='Subscapularis Input(Box) ' + list_var_in[x] + ', Output ' + output_mus_attribute,
                             xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov, con_fac_y=(1.0))
        # Infraspinatus
        INFR_plt = plotMulti(xaxis=time, yaxis=INFR, label=test_str_aut,
                             title='Infraspinatus Input(Box) ' + list_var_in[x] + ', Output ' + output_mus_attribute,
                             xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov, con_fac_y=(1.0))
        # Teres minor
        TMN_plt = plotMulti(xaxis=time, yaxis=TMN, label=test_str_aut,
                            title='Teres minor Input(Box) ' + list_var_in[x] + ', Output ' + output_mus_attribute,
                            xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov, con_fac_y=(1.0))

    x=x+1

## Start Momentarm calculations

#out_mom_arm = startMacroMomentArm()
#app.save_results("test")
"""
out_mom_arm = app.load_results('test.db')

time_mom = out_mom_arm['Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.Abscissa.t']
path_output_mom = 'Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.'

mom_arm_get = GetOutput(macro_output=out_mom_arm, path=path_output_mom, number_mus=muscle_nbr_SUPR, attribute_name= '', nbr_test=[1], steps=len(time_mom[0]))

SUPR_mom_arm = mom_arm_get.sum_mus(muscles = mom_arm_get.extract_mom(name = SUPR_full_name))

SUPR_mom_arm_plt = plotSingle(xaxis = time_mom[0], yaxis = SUPR_mom_arm[0]/6, title = 'Momentarm of ' + SUPR_full_name, xlab = xlabel, ylab = ylabel, con_fac=mov)


#SUPR_mom_arm_plt = plotSingle(xaxis = time_mom[0], yaxis = out_mom_arm['Main.HumanModel.EvaluateMomentArms.Right.Arm.GHAbduction.Study.Output.MomentArmCalculations.supraspinatus_1'][0], title = 'Test_1 ', xlab = xlabel, ylab = ylabel, con_fac=mov)
"""
## End Momentarm calculations """

## Start RR 2 Phase different Parameter influence calculations """
"""
output = startMacroRR(auto_test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input,
                          attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name,
                          TMN_full_name, output_mus_attribute)
# app.save_results("test.db")
# output = app.load_results('test.db')

time = output['Main.Study.Output.Abscissa.t']

test = GetOutput(macro_output=output, path=path_output_mus, number_mus=muscle_nbr_SUPR,
                     attribute_name=output_mus_attribute, nbr_test=auto_test_var[0], steps=nstep)

SUPR = test.sum_mus(muscles=test.extract_mus(name=SUPR_full_name))
SBSC = test.sum_mus(muscles=test.extract_mus(name=SBSC_full_name))
INFR = test.sum_mus(muscles=test.extract_mus(name=INFR_full_name))
TMN = test.sum_mus(muscles=test.extract_mus(name=TMN_full_name))

# supraspinatus
SUPR_plt = plotMulti(xaxis=time, yaxis=SUPR, label=test_str_aut,
                         title='Supraspinatus Input(Box) ' + attribute_input + ', Output ' + output_mus_attribute,
                         xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov)
# Subscapularis
SBSC_plt = plotMulti(xaxis=time, yaxis=SBSC, label=test_str_aut,
                         title='Subscapularis Input(Box) ' + attribute_input + ', Output ' + output_mus_attribute,
                         xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov)
# Infraspinatus
INFR_plt = plotMulti(xaxis=time, yaxis=INFR, label=test_str_aut,
                         title='Infraspinatus Input(Box) ' + attribute_input + ', Output ' + output_mus_attribute,
                         xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov)
# Teres minor
TMN_plt = plotMulti(xaxis=time, yaxis=TMN, label=test_str_aut,
                        title='Teres minor Input(Box) ' + attribute_input + ', Output ' + output_mus_attribute,
                        xlab=xlabel, ylab=ylabel, add_label=add_label, con_fac=mov)
"""
## End RR 2 Phase different Parameter influence calculations """

## Start Difference RR 2 Phase and single 2 Phase """

"""
# With RR adjustment
output_RR = startMacroRR(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
time_RR = output_RR['Main.Study.Output.Abscissa.t']

test_RR = GetOutput(macro_output=output_RR, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_RR = test_RR.sum_mus(muscles = test_RR.extract_mus(name = SUPR_full_name))

# supraspinatus
SUPR_plt_RR = plotMulti(xaxis = time_RR, yaxis = SUPR_RR, label = test_str, title = '2 phasen calib with RR, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)


# Single

output_single = startMacro2P(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
time_single = output_single['Main.Study.Output.Abscissa.t']

test_single = GetOutput(macro_output=output_single, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_single = test_single.sum_mus(muscles = test_single.extract_mus(name = SUPR_full_name))

# supraspinatus
SUPR_plt_single = plotMulti(xaxis = time_single, yaxis = SUPR_single, label = test_str, title = '2 phasen calib single, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)

# 1 Phase Calibration

output_oneP = startMacro1P(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
print(output_oneP)
time_oneP = np.zeros((3,11))
time_oneP[0] = output_oneP['Main.Study.Output.Abscissa.t']
time_oneP[1] = output_oneP['Main.Study.Output.Abscissa.t']
time_oneP[2] = output_oneP['Main.Study.Output.Abscissa.t']

test_onePe = GetOutput(macro_output=output_oneP, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_oneP = test_onePe.sum_mus(muscles = test_onePe.extract_mus(name = SUPR_full_name))
print(SUPR_oneP)
# supraspinatus
SUPR_plt_oneP = plotMulti(xaxis = time_oneP, yaxis = SUPR_oneP, label = test_str, title = '1 phasen calib, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)

SUPR_all = np.zeros((3,11))
SUPR_all[0] = SUPR_oneP[0]
SUPR_all[1] = SUPR_single[0]
SUPR_all[2] = SUPR_RR[0]

print(SUPR_all)

label_all = ['1 phase', '2 phase single', '2 phase with RR']

SUPR_all = plotMulti(xaxis = time_oneP, yaxis = SUPR_all, label = label_all, title = 'Calibrations, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
"""
## End Difference RR 2 Phase and single 2 Phase """


## Start Calib Momentarm """
"""
# With RR adjustment
output_RR = startMacroRRMoM(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
time_RR = output_RR['Main.Study.Output.Abscissa.t']

test_RR = GetOutput(macro_output=output_RR, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_RR = test_RR.sum_mus(muscles = test_RR.extract_mus(name = SUPR_full_name))

# supraspinatus
SUPR_plt_RR = plotMulti(xaxis = time_RR, yaxis = SUPR_RR, label = test_str, title = '2 phasen calib with RR, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)


# Single

output_single = startMacro2PMoM(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
time_single = output_single['Main.Study.Output.Abscissa.t']

test_single = GetOutput(macro_output=output_single, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_single = test_single.sum_mus(muscles = test_single.extract_mus(name = SUPR_full_name))

# supraspinatus
SUPR_plt_single = plotMulti(xaxis = time_single, yaxis = SUPR_single, label = test_str, title = '2 phasen calib single, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)

# 1 Phase Calibration

output_oneP = startMacro1PMoM(test_var, path_cal, path_mov, mov_attribute, mov, path_input_mus, mus_input, attribute_input, path_output_mus, SUPR_full_name, SBSC_full_name, INFR_full_name, TMN_full_name, output_mus_attribute)
print(output_oneP)
time_oneP = np.zeros((3,11))
time_oneP[0] = output_oneP['Main.Study.Output.Abscissa.t']
time_oneP[1] = output_oneP['Main.Study.Output.Abscissa.t']
time_oneP[2] = output_oneP['Main.Study.Output.Abscissa.t']

test_onePe = GetOutput(macro_output=output_oneP, path=path_output_mus, number_mus=muscle_nbr_SUPR, attribute_name=output_mus_attribute, nbr_test=test_var, steps=nstep)

SUPR_oneP = test_onePe.sum_mus(muscles = test_onePe.extract_mus(name = SUPR_full_name))
print(SUPR_oneP)
# supraspinatus
SUPR_plt_oneP = plotMulti(xaxis = time_oneP, yaxis = SUPR_oneP, label = test_str, title = '1 phasen calib, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)

SUPR_all = np.zeros((3,11))
SUPR_all[0] = SUPR_oneP[0]
SUPR_all[1] = SUPR_single[0]
SUPR_all[2] = SUPR_RR[0]§

print(SUPR_all)

label_all = ['1 phase', '2 phase single', '2 phase with RR']

SUPR_all = plotMulti(xaxis = time_oneP, yaxis = SUPR_all, label = label_all, title = 'Calibrations, on Supraspinatus ' + output_mus_attribute, xlab = xlabel, ylab = ylabel, add_label = add_label, con_fac=mov)
"""
## Start Calib Momentarm """
