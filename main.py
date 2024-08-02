import os
import demo

current_path = os.getcwd()
train_paths = []
path = current_path + "/train/"
for i in os.listdir(path):
    train_paths.append(path + i)

test_paths = []
path = current_path + "/test/"
for i in os.listdir(path):
    test_paths.append(path + i)

if __name__ == '__main__':
    demo.hopfield(train_files=train_paths, test_files=test_paths, theta=0.5, time=10, size=(135, 135), threshold=5,
                  current_path=current_path)
