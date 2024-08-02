from PIL import Image
import os
import matplotlib.pyplot as plt
import pandas as pd 

# Определяет количество пикселей, которые отличаются друг от друга
def differ():

    current_path = os.getcwd()
    train_paths = []
    path = current_path + "/train/"
    for i in os.listdir(path):
        train_paths.append(path + i)

    after_paths = []
    path = current_path + "/after/"
    for i in os.listdir(path):
        after_paths.append(path + i)

    print(f"threshold=5")  
    for a, b in zip(train_paths, after_paths):
        img1 = Image.open(a)
        imgg1 = img1.convert('L')
        im1 = imgg1.load()
        img2 = Image.open(b)
        imgg2 = img2.convert('L')
        im2 = imgg2.load()
        i = 0
        if (img1.size == img2.size):
            x1, y1 = img1.size
            for x in range(0, x1):
                for y in range(0, y1):
                    if im1[x, y] != im2[x, y]:
                        i = i + 1          
            print(f"Количество разных пикселей: {i}")
        else:
            print("Размер изображений не совпадают!")

if __name__ == '__main__':
    differ()
