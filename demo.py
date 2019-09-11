import time
from glob import glob

import numpy as np
from PIL import Image

import model

paths = glob('./test/*.*')

if __name__ == '__main__':
    x1 = 1
    while x1 <= 7200:
        im = Image.open("./test/1"+str(x1)+".jpg")
        img = np.array(im.convert('RGB'))
        t = time.time()
        result, img, angle = model.model(
            img, model='keras', adjust=True, detectAngle=True)
        print("It takes time:{}s".format(time.time() - t))
        print("---------------------------------------")
        for key in result:
            print(result[key][1])
        x1 = x1+1
