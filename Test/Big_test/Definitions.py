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