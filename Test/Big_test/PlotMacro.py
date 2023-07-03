import matplotlib.pyplot as plt


def plotMulti(xaxis, yaxis, label, title = 'No title', xlab = 'x-label is not defined', ylab = 'y-label is not defined', add_label = '', con_fac = 1.0, con_fac_y = 1.0):
    for a in range(len(yaxis)):
        plt.plot(xaxis[a] * con_fac, yaxis[a]*con_fac_y , label=label[a] + add_label)

    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(title)
    plt.clf()

def plotSingle(xaxis, yaxis, title = 'No title', xlab = 'x-label is not defined', ylab = 'y-label is not defined', con_fac = 1.0):

    plt.figure()
    plt.plot(xaxis * con_fac, yaxis, 'b')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.grid()
    plt.savefig(title)
    plt.clf()

