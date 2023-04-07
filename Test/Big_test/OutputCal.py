
import numpy as np

class GetOutput:

    def __init__(self, macro_output, path, number_mus, attribute_name, nbr_test, steps):
        self.macro_output = macro_output
        self.path = path
        self.number_mus = number_mus # nbr of muscle
        self.attribute_name = attribute_name
        self.nbr_test = nbr_test # nbr be tested
        self.steps = steps # time steps

    def extract_mus(self, name):

        temp = np.zeros((self.number_mus, len(self.nbr_test),  self.steps))
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

def AutoExtrInput(macro_output, path_input, mus_name, attribute_name, number_mus):

    temp = np.zeros((number_mus, 7),  float)
    temp_nbr = [str(x + 1) for x in range(number_mus)]

    for i in range(number_mus):
        print(path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name)
        temp[i][3] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name]

        p = 0.25
        for j in range(3):

            temp[i][3 - j - 1] = temp[i][3] - (p * temp[i][3])
            temp[i][3 + j + 1] = temp[i][3] + (p * temp[i][3])
            p = p + 0.25

    return temp

def AutoExtrInput3(macro_output, path_input, mus_name, attribute_name, number_mus):

    temp = np.zeros((number_mus, 3),  float)
    temp_nbr = [str(x + 1) for x in range(number_mus)]

    for i in range(number_mus):
        temp[i][3] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name]

        p = 0.75
        for j in range(1):

            temp[i][1 - j - 1] = temp[i][3] - (p * temp[i][3])
            temp[i][1 + j + 1] = temp[i][3] + (p * temp[i][3])
            p = p + 0.25

    return temp

def output_calib (macro_output, path_input, mus_name, attribute_name, number_mus, nstep):

    temp = np.zeros((number_mus, nstep), float)
    a = np.zeros((1,nstep), float)
    temp_nbr = [str(x + 1) for x in range(number_mus)]

    for i in range(number_mus):

        temp[i] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name]
        a[0] = a[0] + temp[i]

    return a

def output_sim (macro_output, path_input, mus_name, attribute_name, number_mus, nstep):

    temp_1 = np.zeros((number_mus, nstep), float)
    temp_2 = np.zeros((number_mus, nstep), float)
    temp_3 = np.zeros((number_mus, nstep), float)
    a_1 = np.zeros((1,nstep), float)
    a_2 = np.zeros((1, nstep), float)
    a_3 = np.zeros((1, nstep), float)
    temp_nbr = [str(x + 1) for x in range(number_mus)]

    for i in range(number_mus):

        temp_1[i] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name][0]
        temp_2[i] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name][1]
        temp_3[i] = macro_output[path_input + mus_name + '_' + temp_nbr[i] + '.' + attribute_name][2]
        a_1[0] = a_1[0] + temp_1[i]
        a_2[0] = a_2[0] + temp_2[i]
        a_3[0] = a_3[0] + temp_3[i]

    return a_1, a_2, a_3

def output_calib_one (macro_output, attribute_name, number_mus):

    temp = 0
    temp_nbr = [str(x + 1) for x in range(number_mus)]

    for i in range(number_mus):
        temp = temp + macro_output['Main.HumanModel.BodyModel.Right.ShoulderArm.MusPar.supraspinatus_' + temp_nbr[i] + '.' + attribute_name]
    return temp