import matplotlib.pyplot as plt
import numpy as np

def krestiki(coord:tuple):
    plt.plot(coord[0], coord[1], "gx", markersize = 65, markeredgewidth = 4)

def noliki(coord: tuple):
    plt.plot(coord[0], coord[1] ,"o",c = 'teal', markersize = 65, fillstyle = 'none', markeredgewidth = 4)

def sewerus(coord: tuple):
    ax = plt.gca()
    fn = r'C:\Users\Lera\Desktop\WEB\Table\Sew11.png'  # как сделать чтобы учитывалась png
    im = plt.imread(fn) # считывает изображениуе в файле, можно использовать url
    ax.figure.figimage(im,coord[0], coord[1]) # смещение изображения в пикселях

def damboldor(coord:tuple):
    ax = plt.gca()
    fn = r'C:\Users\Lera\Desktop\WEB\Table\Dam11.png'  # как сделать чтобы учитывалась png
    im = plt.imread(fn)  # считывает изображениуе в файле, можно использовать url
    ax.figure.figimage(im, coord[0], coord[1])  # смещение изображения в пикселях

def graph(input_array, graphics_mode = 'standart'):
    fig, ax = plt.subplots()
    plt.axis([0, 3, 0, 3])
    # plt.axis('equal')
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
    res_coord_standart = [l2,l1,l0]
    res_coord_HP = [[(30,260),(200,260),(370,260)], [(30, 135),(200, 135),(370, 135)], [(30, 10), (200, 10), (370, 10)]]
    if graphics_mode == 'standart':
        for i, column in enumerate(input_array):
            for j, elem in enumerate(column):
                if elem == 1:
                    krestiki(res_coord_standart[i][j])
                elif elem == 2:
                    noliki(res_coord_standart[i][j])

    elif graphics_mode =='HP':
        for i, column in enumerate(input_array):
            for j, elem in enumerate(column):
                if elem == 1:
                    damboldor(res_coord_HP[i][j])
                elif elem == 2:
                    sewerus(res_coord_HP[i][j])
    # ax.set_facecolor('ivory')
    if (input_array[0][0] == 1 and input_array[1][0] == 1 and input_array[2][0]== 1) or ((input_array[0][0] == 2 and input_array[1][0] == 2 and input_array[2][0]== 2)):
        plt.plot([0.5, 0.5], [0, 3], 'salmon', linewidth=3)
    elif (input_array[0][1] == 1 and input_array[1][1] ==1 and input_array[2][1] == 1) or (input_array[0][1] == 2 and input_array[1][1] ==2 and input_array[2][1] == 2):
        plt.plot([1.5, 1.5], [0, 3], 'salmon', linewidth=3)
    elif (input_array[0][2] == 1 and input_array[1][2] == 1 and input_array[2][2]==1) or (input_array[0][2] == 2 and input_array[1][2] == 2 and input_array[2][2]==2):
        plt.plot([2.5, 2.5], [0, 3], 'salmon', linewidth=3)
    elif (input_array[0][0] == 1 and input_array[0][1] == 1 and input_array[0][2] == 1) or (input_array[0][0] == 2 and input_array[0][1] == 2 and input_array[0][2] == 2):
        plt.plot([0, 3], [2.5, 2.5], 'salmon', linewidth=3)
    elif (input_array[1][0] == 1 and input_array[1][1] == 1 and input_array[1][2] ==1 ) or (input_array[1][0] == 2 and input_array[1][1] == 2 and input_array[1][2] == 2):
        plt.plot([0, 3], [1.5, 1.5], 'salmon', linewidth=3)
    elif (input_array[2][0] == 1 and input_array[2][1] == 1 and input_array[2][2]== 1) or (input_array[2][0] == 2 and input_array[2][1] == 2 and input_array[2][2]== 2):
        plt.plot([0, 3], [0.5, 0.5], 'salmon', linewidth=3)

    elif (input_array[0][0] == 1 and input_array[1][1] == 1 and input_array[2][2] == 1) or (input_array[0][0] == 2 and input_array[1][1] == 2 and input_array[2][2] == 2):
        plt.plot([0, 3], [3, 0], 'salmon', linewidth=3)
    elif (input_array[0][2] == 1 and input_array[1][1] == 1  and input_array[2][0] == 1) or (input_array[0][2] == 2 and input_array[1][1] == 2  and input_array[2][0] == 2):
        plt.plot([0, 3], [0, 3], 'salmon', linewidth=3)
    plt.savefig('my_plot.png', bbox_inches = 'tight',pad_inches = 0) # сохраняет картинку в той же директории, при повторном выполнении функцииб перезаписывается под тем же именеем
    plt.show()


if __name__ == "__main__":
    test = np.array([[2,2,1], [0,1,2], [1,2,1]])
    graph(test)
