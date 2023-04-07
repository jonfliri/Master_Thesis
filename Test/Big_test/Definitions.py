import numpy as np
# Calibration Attributes
path_cal = 'Main.HumanModel.Calibration.RightShoulderCal.ShoulderCal.'

# Input Attributes
path_input_mus = 'Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.'

# Movement attributes
path_mov = 'Main.HumanModel.Mannequin.PostureVel.Right.'

# Input Attributes
path_output_mus = 'Main.Study.Output.Model.BodyModel.Right.ShoulderArm.Mus.'

load_mom = 'C:\Program Files\AnyBody Technology\AnyBody.7.3\AMMR\Application\Validation\EvaluateMomentArms\EvaluateMomentArms.main.any'

## Muscles which are examined

# supraspinatus
SUPR_full_name = 'supraspinatus'
SUPR_short_name = 'SUPR'
muscle_nbr_SUPR = 6
SUPR_pen_ang = 6.3 # default value
SUPR_pen_ang = SUPR_pen_ang * np.pi / 180

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

tArray = np.linspace(0, 1, 100)

# Save
"""
tendon_leng = 0.3 * tear_1_len_MRI[0] + 0.23
MTJ_lat_shif = 0.67 * tear_1_len_MRI[0] - 0.23
# print(tendon_leng)
# print(MTJ_lat_shif)

tendon_leng_ratio = (ten_1_len[0] + tendon_leng) / mus_org_in_len[0] * ten_0_ratio
MTJ_lat_shif_ratio = (mus_1_len[0] + MTJ_lat_shif) / mus_org_in_len[0] * mus_0_ratio
# print(tendon_leng_ratio)
# print(MTJ_lat_shif_ratio)

ten_tear_ratio = ten_1_len[0] / (mus_org_in_len[0] * ten_0_ratio)
mus_tear_ratio = mus_1_len[0] / (mus_org_in_len[0] * mus_0_ratio)
# print(ten_tear_ratio)
# print(mus_tear_ratio)

Lt0_ratio = ten_tear_ratio + tendon_leng_ratio # ten_1_len[0] / (mus_org_in_len[0]*ten_0_ratio)
Lf0_ratio = mus_tear_ratio + MTJ_lat_shif_ratio # Default no degeneration

if Lt0_ratio > 1:
    Lt0_ratio = ten_1_len[0] / (mus_org_in_len[0]*ten_0_ratio)

if Lf0_ratio > 1:
    Lf0_ratio = 1.0

# print(Lt0_ratio)
# print(Lf0_ratio)

# Muscle retraction

# Goutallier Stage

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

Lf1 = Lf0_calib * Lf0_ratio
Lt1 = Lt0_calib * Lt0_ratio

SUPR_pen_ang_cor = 13.3 # 13.3
SUPR_pen_ang_cor = SUPR_pen_ang_cor * np.pi / 180
"""
