import inline as inline
import matplotlib
from anypytools import AnyPyProcess
app = AnyPyProcess()
"""
macrolist = [
    ['load "Knee.any"',
     'operation Main.MyStudy.Kinematics',
     'run'],
    ['load "Knee.any"',
     'operation Main.MyStudy.InverseDynamics',
     'run'],
]
app.start_macro(macrolist);

macrolist = []
for i in range(40):
    macro = [
        'load "Knee.any"',
        'operation Main.MyStudy.InverseDynamics',
        'run',
    ]
    macrolist.append(macro)


# First sequentially
app = AnyPyProcess(num_processes = 1)
app.start_macro(macrolist);

# Then with parallization
app = AnyPyProcess(num_processes = 4)
app.start_macro(macrolist);

import numpy as np
macrolist = [
    'load "Knee.any"',
    'operation Main.MyStudy.InverseDynamics',
    'run',
    'classoperation Main.MyStudy.Output.MaxMuscleActivity "Dump"',
]

results = app.start_macro(macrolist)

max_muscle_act = results[0]['Main.MyStudy.Output.MaxMuscleActivity']

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

plt.plot(max_muscle_act);
plt.show()
"""

"""

WRITE PARAMETERS IN ANYBODY

from anypytools.macro_commands import (MacroCommand, Load, SetValue, SetValue_random,  Dump, SaveDesign,
                                       LoadDesign, SaveValues, LoadValues, UpdateValues, OperationRun)

macrolist = [
    Load('Knee.any', defs={'SUBJECT':'"S02"', 'TRIAL':'"T04"'}),
    OperationRun('Main.MyStudy.InverseDynamics'),
    Dump('Main.MyStudy.Output.MaxMuscleActivity'),
]
from anypytools import AnyPyProcess
app = AnyPyProcess()
app.start_macro(macrolist);

from anypytools import AnyMacro

macrolist = [
    Load('Knee.any' ),
    OperationRun('Main.MyStudy.InverseDynamics'),
]

mg = AnyMacro(macrolist, number_of_macros=5)
app.start_macro(mg);

mg.create_macros(2)

from anypytools import AnyPyProcess

app = AnyPyProcess()
output = app.start_macro(mg.create_macros(100))

parameter_list = [2.2, 2.5, 2.7, 2.9, 3.1]

mg = AnyMacro(SetValue('Main.MyParameter', parameter_list ))
mg.create_macros(5)
print(mg)

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


# Monte Carlo Study

from scipy.stats import distributions
# Truncated normal between +/- 2SD.
patella_tendon_insertion = distributions.truncnorm(-2,2,[0.02, 0.12, 0], [0.01,0.01,0.01])
patella_tendon_origin = distributions.truncnorm(-2,2,[0.0,-0.03, 0], [0.01,0.01,0.01])

from anypytools import macro_commands as mc

macro = [
    mc.SetValue_random('Main.MyModel.Tibia.Patella2.sRel', patella_tendon_insertion),
    mc.SetValue_random('Main.MyModel.Patella.Lig.sRel', patella_tendon_origin)
]

macro

from anypytools import AnyMacro

mg = AnyMacro(macro)
monte_carlo_macros = mg.create_macros_MonteCarlo(100)

monte_carlo_macros[0]

monte_carlo_macros[1:4]

macro = [
    mc.Load('Knee.any'),
    mc.SetValue_random('Main.MyModel.Tibia.Patella2.sRel', patella_tendon_insertion ) ,
    mc.SetValue_random('Main.MyModel.Patella.Lig.sRel', patella_tendon_origin ) ,
    mc.OperationRun('Main.MyStudy.InverseDynamics'),
    mc.Dump('Main.MyStudy.Output.Abscissa.t'),
    mc.Dump('Main.MyStudy.Output.MaxMuscleActivity')
]
mg = AnyMacro(macro, seed=1)
monte_carlo_macros = mg.create_macros_MonteCarlo(100)

from anypytools import AnyPyProcess

app = AnyPyProcess()
monte_carlo_results = app.start_macro( monte_carlo_macros )

print('Length :', len(monte_carlo_results) )
print('Data keys in first element: ', list(monte_carlo_results[0].keys()))

monte_carlo_results[:] = [
    output
    for output in monte_carlo_results
    if 'ERROR' not in output
]

monte_carlo_results['Main.MyStudy.Output.MaxMuscleActivity']

max_muscle_activity = monte_carlo_results['MaxMus']

#matplotlib inline
import matplotlib.pyplot as plt

time = monte_carlo_results['Abscissa.t'][0]
plt.fill_between(time, max_muscle_activity.min(0), max_muscle_activity.max(0),alpha=0.4  )
for trace in max_muscle_activity:
    plt.plot(time, trace,'b', lw=0.2 )
# Plot result with the mean of the inputs ( stored in the first run)
plt.plot(time, max_muscle_activity[0],'r--', lw = 2, )

#plt.show()


#Latin Hypercube sampling

from scipy.stats import distributions
from anypytools import AnyPyProcess

patella_tendon_insertion = distributions.norm([0.02, 0.12, 0], [0.01,0.01,0.01])
patella_tendon_origin = distributions.norm([0.0,-0.03, 0], [0.01,0.01,0.01])

macro = [
    mc.Load('Knee.any'),
    mc.SetValue_random('Main.MyModel.Tibia.Patella2.sRel', patella_tendon_insertion ) ,
    mc.SetValue_random('Main.MyModel.Patella.Lig.sRel', patella_tendon_origin ) ,
    mc.OperationRun('Main.MyStudy.InverseDynamics'),
    mc.Dump('Main.MyStudy.Output.Abscissa.t'),
    mc.Dump('Main.MyStudy.Output.MaxMuscleActivity')
]
mg = AnyMacro(macro, seed=1)
LHS_macros = mg.create_macros_LHS(25)

from anypytools import AnyPyProcess

app = AnyPyProcess()
lhs_results = app.start_macro(LHS_macros)

#matplotlib inline
import matplotlib.pyplot as plt

time = lhs_results['Abscissa.t'][0]
plt.fill_between(time, lhs_results['MaxMus'].min(0), lhs_results['MaxMus'].max(0),alpha=0.4  )
for trace in lhs_results['MaxMus']:
    plt.plot(time, trace,'b', lw=0.2 )
# Plot the mean value that was stored in the first results
plt.plot(time, lhs_results['MaxMus'].mean(0),'r--', lw = 2, )

plt.show()

