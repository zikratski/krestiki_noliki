import matplotlib.pyplot as plt
import numpy as np
def krestiki(coord:tuple):
    plt.plot(coord[0], coord[1], "gx", markersize = 45, markeredgewidth = 4)

def noliki(coord: tuple):
    plt.plot(coord[0], coord[1], "ro", markersize = 45, fillstyle = 'none', markeredgewidth = 4)

def graph(input_array):
    fig, ax = plt.subplots()
    plt.axis([0, 3, 0, 3])
    plt.xticks([])
    plt.yticks([])

    plt.plot([1, 1], [0, 3], 'gray', linewidth=3)
    plt.plot([2, 2], [0, 3], 'gray', linewidth=3)
    plt.plot([0, 3], [1, 1], 'gray', linewidth=3)
    plt.plot([0, 3], [2, 2], 'gray', linewidth=3)

    coordinat = []
    for i, column in enumerate(input_array):
        for j, elem in enumerate(column):
            coordinat.append((j+ 0.5, i + 0.5))
    l0 = coordinat[:3]
    l1 = coordinat[3:6]
    l2 = coordinat[6:]
    res_coord = [l2,l1,l0]

    for i, column in enumerate(input_array):
        for j, elem in enumerate(column):
            if elem == 1:
                krestiki(res_coord[i][j])
            elif elem == 2:
                noliki(res_coord[i][j])
    ax.set_facecolor('ivory')
    plt.show()

if __name__ == "__main__":
    test = np.array([[1,0,2], [0,2,1], [0,0,2]])
    graph(test)
