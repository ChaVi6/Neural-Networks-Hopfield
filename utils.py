import numpy as np
import random
from PIL import Image


# Преобразовывает матрицу в вектор
def mat2vec(x):
    m = x.shape[0] * x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1
    


# Создает матрицу весов на основе входного вектора
def create_W(x):
    if len(x.shape) != 1:
        print("The input is not vector")
        return
    else:
        w = np.zeros([len(x), len(x)])
        for i in range(len(x)):
            for j in range(i, len(x)):
                if i == j:          # текущий элемент расположен на главной диагонали матрицы
                    w[i, j] = 0     # по правилам Хопфилда элементы на главной диагонали должны быть равны нулю
                else:
                    w[i, j] = x[i] * x[j]
                    w[j, i] = w[i, j]
    return w


# Строит матрицу каждого холста, состоящую из -1 и 1 на основе порога
def readImg2array(file, size, threshold=200):
    # threshold - определяет, какие пиксели считаются "светлыми" или "темными"
    pilIN = Image.open(file).convert(mode="L")
    pilIN = pilIN.resize(size)
    imgArray = np.asarray(pilIN, dtype=np.int8)
    x = np.zeros(imgArray.shape, dtype=np.int8)
    x[imgArray > threshold] = -1    # темные
    x[x == 0] = 1                   # светлые
    return x


# Преобразовывает массив в матрицу
def array2img(data, outFile=None):
    # data в виде матрицы с элементами -1 и 1
    y = np.zeros(data.shape, dtype=np.uint8)
    # основной цвет
    y[data == 1] = 255
    y[data == -1] = 0
    img = Image.fromarray(y, mode="L")
    if outFile is not None:
        img.save(outFile)
    return img


# Применяет обновление для вектора на основе весовой матрицы
# Функция используется в алгоритме Хопфилда для обновления 
# состояний нейронов вектора на основе весовой матрицы в определенное количество итераций
def update(w, y_vec, theta=0.5, time=3):
    for s in range(time):
        m = len(y_vec)
        i = random.randint(0, m - 1)
        u = np.dot(w[i][:], y_vec) - theta
        for i in range (len(y_vec)):
            if u > 0:
                y_vec[i] = 1
            elif u < 0:
                y_vec[i] = -1

    return y_vec
