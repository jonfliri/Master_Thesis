
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