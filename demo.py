from utils import *

def hopfield(train_files, test_files, theta=0.5, time=10, size=(135, 135), threshold=5, current_path=None):
    # тренировка
    print("Обработка тренировочных изображений...")
    num_files = 0
    for path in train_files:
        print(path)
        x = readImg2array(file=path, size=size, threshold=threshold)
        x_vec = mat2vec(x)
        if num_files == 0:
            w = create_W(x_vec)
            num_files = 1
        else:
            tmp_w = create_W(x_vec)
            w = w + tmp_w
            num_files += 1

    # тестирование
    counter = 0
    for path in test_files:
        y = readImg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        y_img = array2img(y)
        y_img.show()
        y_vec = mat2vec(y)
        y_vec_after = update(w=w, y_vec=y_vec, theta=theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)
        if current_path is not None:
            outfile = current_path + "/after/after_" + str(counter) + ".png"
            array2img(y_vec_after, outFile=outfile)
        counter += 1
