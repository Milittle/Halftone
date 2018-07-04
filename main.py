#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 22:45
# @Author  : milittle
# @Site    : www.weaf.top
# @File    : main.py
# @Software: PyCharm
import sys
from Halftone import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PIL.ImageQt import ImageQt
tri = True

class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def enable_menu_item(self):
        self.actionBayer.setEnabled(tri)
        self.actionHalftone.setEnabled(tri)
        self.actionScrew.setEnabled(tri)
        self.actionCoarseFatting.setEnabled(tri)
        self.action_global.setEnabled(tri)
        self.action_local.setEnabled(tri)
        self.actionFloydSteinberg.setEnabled(tri)
        self.actionFloydSteinberg1.setEnabled(tri)
        self.actionBurkes.setEnabled(tri)
        self.actionJarrisJudiceNinke.setEnabled(tri)
        self.actionStucki.setEnabled(tri)
        self.action_mutil.setEnabled(tri)


    # set slots
    def openimage(self):
        # 打开文件路径
        #设置文件扩展名过滤,注意用双分号间隔
        self.imgName, self.imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    ".",
                                    "*.png;;*.jpg;;*.jpeg;;*.bmp")

        print('filename{}'.format(self.imgName))

        #利用qlabel显示图片
        if self.imgName != '':
            self.png = QtGui.QPixmap(self.imgName).scaled(self.image_source.width(), self.image_source.height())
            self.image_source.setPixmap(self.png)
            self.enable_menu_item()


    def Bayer(self):
        from PIL import Image

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))

        # Bayer Ordered Dithering
        Mask = [0, 32, 8, 40, 2, 34, 10, 42,
                48, 16, 56, 42, 50, 18, 58, 26,
                12, 44, 4, 36, 14, 46, 6, 38,
                60, 28, 52, 20, 62, 30, 54, 22,
                3, 35, 11, 43, 1, 33, 9, 41,
                51, 19, 59, 27, 49, 17, 57, 25,
                15, 47, 7, 39, 13, 45, 5, 37,
                63, 31, 55, 23, 61, 29, 53, 21]

        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > Mask[k * L + l]:
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)

        im2.save('Bayer.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Halftone(self):
        from PIL import Image

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))

        # Halftone Ordered Dithering
        Mask = [28, 10, 18, 26, 36, 44, 52, 34,
                22, 2, 4, 12, 48, 58, 60, 42,
                14, 6, 0, 20, 40, 56, 62, 50,
                24, 16, 8, 30, 32, 54, 46, 38,
                37, 45, 53, 35, 29, 11, 19, 27,
                49, 59, 61, 43, 23, 3, 5, 13,
                41, 57, 63, 51, 15, 7, 1, 21,
                33, 55, 47, 39, 25, 17, 9, 31]

        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > Mask[k * L + l]:
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)
        im2.save('Halftone.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Screw(self):
        from PIL import Image

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))

        # Screw Ordered Dithering
        Mask = [64, 53, 42, 26, 27, 43, 54, 61,
                60, 41, 25, 14, 15, 28, 44, 55,
                52, 40, 13, 5, 6, 16, 29, 45,
                39, 24, 12, 1, 2, 7, 17, 30,
                38, 23, 11, 4, 3, 8, 18, 31,
                51, 37, 22, 10, 9, 19, 32, 41,
                59, 50, 36, 21, 20, 33, 47, 56,
                63, 58, 49, 35, 34, 48, 57, 62]

        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > Mask[k * L + l]:
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)
        im2.save('Screw.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def CoarseFatting(self):
        from PIL import Image

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))

        # CoarseFatting Ordered Dithering
        Mask = [4, 14, 52, 58, 56, 45, 20, 6,
                16, 26, 38, 50, 48, 36, 28, 18,
                43, 35, 31, 9, 11, 25, 33, 41,
                61, 46, 23, 1, 3, 13, 55, 60,
                57, 47, 21, 7, 5, 15, 53, 59,
                49, 37, 29, 19, 17, 27, 39, 51,
                10, 24, 32, 40, 42, 34, 30, 8,
                2, 12, 54, 60, 51, 44, 22, 0]

        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > Mask[k * L + l]:
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)
        im2.save('CoarseFatting.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def global_dou(self):
        from PIL import Image
        import random

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))

        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > random.randint(0, 64):
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)
        im2.save('global_dou.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)
    def local_dou(self):
        from PIL import Image
        import random

        time = 1
        K = 8
        L = 8
        N = 63
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        Mask = [0] * im.size[0] * time * im.size[1] * time
        for i in range(63):
            Mask[i] = random.randint(0, 64)
        for m in range(im2.size[0]):
            k = m % K
            for n in range(im2.size[1]):
                l = n % L
                pix = int(im.getpixel((m / time, n / time)) / 255.0 * N + 0.5)
                if pix > Mask[k * L + l]:
                    im2.putpixel((m, n), 1)
                else:
                    im2.putpixel((m, n), 0)
        im2.save('local_dou.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Floyd_Steinberg(self):
        from PIL import Image

        time = 1
        N = 144
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(im2.size[0] - 1):
            for n in range(1, im2.size[1] - 1):
                if pix[m * im2.size[1] + n] <= 72:
                    nError = pix[m * im2.size[1] + n]
                    im2.putpixel((m, n), 0)
                else:
                    nError = pix[m * im2.size[1] + n] - N
                    im2.putpixel((m, n), 1)
                pix[m * im2.size[1] + n + 1] += nError * 7 / 16.0
                pix[(m + 1) * im2.size[1] + n - 1] += nError * 3 / 16.0
                pix[(m + 1) * im2.size[1] + n] += nError * 5 / 16.0
                pix[(m + 1) * im2.size[1] + n + 1] += nError * 1 / 16.0

        im2.save('Floyd_Steinberg.jpg')
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Floyd_Steinberg1(self):
        from PIL import Image

        time = 1
        N = 144
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(im2.size[0] - 1):
            if m % 2 == 1:
                for n in range(1, im2.size[1] - 1):
                    if pix[m * im2.size[1] + n] <= 72:
                        nError = pix[m * im2.size[0] + n]
                        im2.putpixel((m, n), 0)
                    else:
                        nError = pix[m * im2.size[1] + n] - N
                        im2.putpixel((m, n), 1)
                    pix[m * im2.size[1] + n + 1] += nError * 7 / 16.0
                    pix[(m + 1) * im2.size[1] + n - 1] += nError * 3 / 16.0
                    pix[(m + 1) * im2.size[1] + n] += nError * 5 / 16.0
                    pix[(m + 1) * im2.size[1] + n + 1] += nError * 1 / 16.0
            else:
                for n in range(im2.size[1] - 2, 0, -1):
                    if pix[m * im2.size[1] + n] <= 72:
                        nError = pix[m * im2.size[0] + n]
                        im2.putpixel((m, n), 0)
                    else:
                        nError = pix[m * im2.size[0] + n] - N
                        im2.putpixel((m, n), 1)
                    pix[m * im2.size[1] + n - 1] += nError * 7 / 16.0
                    pix[(m + 1) * im2.size[1] + n + 1] += nError * 3 / 16.0
                    pix[(m + 1) * im2.size[1] + n] += nError * 5 / 16.0
                    pix[(m + 1) * im2.size[1] + n - 1] += nError * 1 / 16.0
        im2.save("Floyd_Steinberg1.jpg")
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Burkes(self):
        from PIL import Image

        time = 1
        N = 144
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(1, im2.size[0] - 1):
            for n in range(2, im2.size[1] - 2):
                if pix[m * im2.size[1] + n] <= 72:
                    nError = pix[m * im2.size[1] + n]
                    im2.putpixel((m, n), 0)
                else:
                    nError = pix[m * im2.size[1] + n] - N
                    im2.putpixel((m, n), 1)
                pix[m * im2.size[1] + n + 1] += nError * 8 / 32.0
                pix[m * im2.size[1] + n + 2] += nError * 4 / 32.0
                pix[(m + 1) * im2.size[1] + n - 2] += nError * 2 / 32.0
                pix[(m + 1) * im2.size[1] + n - 1] += nError * 4 / 32.0
                pix[(m + 1) * im2.size[1] + n] += nError * 8 / 32.0
                pix[(m + 1) * im2.size[1] + n + 1] += nError * 4 / 32.0
                pix[(m + 1) * im2.size[1] + n + 2] += nError * 2 / 32.0

        im2.save("Burkes.jpg")
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)
    def Jarris_Judice_Ninke(self):
        from PIL import Image

        time = 1
        N = 144
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(im2.size[0] - 2):
            for n in range(2, im2.size[1] - 2):
                if pix[m * im2.size[1] + n] <= 72:
                    nError = pix[m * im2.size[1] + n]
                    im2.putpixel((m, n), 0)
                else:
                    nError = pix[m * im2.size[1] + n] - N
                    im2.putpixel((m, n), 1)
                pix[m * im2.size[1] + n + 1] += nError * 7 / 48.0
                pix[m * im2.size[1] + n + 2] += nError * 5 / 48.0
                pix[(m + 1) * im2.size[1] + n - 2] += nError * 3 / 48.0
                pix[(m + 1) * im2.size[1] + n - 1] += nError * 5 / 48.0
                pix[(m + 1) * im2.size[1] + n] += nError * 7 / 48.0
                pix[(m + 1) * im2.size[1] + n + 1] += nError * 5 / 48.0
                pix[(m + 1) * im2.size[1] + n + 2] += nError * 3 / 48.0
                pix[(m + 2) * im2.size[1] + n - 2] += nError * 1 / 48.0
                pix[(m + 2) * im2.size[1] + n - 1] += nError * 3 / 48.0
                pix[(m + 2) * im2.size[1] + n] += nError * 5 / 48.0
                pix[(m + 2) * im2.size[1] + n + 1] += nError * 3 / 48.0
                pix[(m + 2) * im2.size[1] + n + 2] += nError * 1 / 48.0

        im2.save("Jarris_Judice_Ninke.jpg")
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def Stucki(self):
        from PIL import Image

        time = 1
        N = 144
        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("1", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(im2.size[0] - 2):
            for n in range(2, im2.size[1] - 2):
                if pix[m * im2.size[1] + n] <= 72:
                    nError = pix[m * im2.size[1] + n]
                    im2.putpixel((m, n), 0)
                else:
                    nError = pix[m * im2.size[1] + n] - N
                    im2.putpixel((m, n), 1)
                pix[m * im2.size[1] + n + 1] += nError * 8 / 42.0
                pix[m * im2.size[1] + n + 2] += nError * 4 / 42.0
                pix[(m + 1) * im2.size[1] + n - 2] += nError * 2 / 42.0
                pix[(m + 1) * im2.size[1] + n - 1] += nError * 4 / 42.0
                pix[(m + 1) * im2.size[1] + n] += nError * 8 / 42.0
                pix[(m + 1) * im2.size[1] + n + 1] += nError * 4 / 42.0
                pix[(m + 1) * im2.size[1] + n + 2] += nError * 2 / 42.0
                pix[(m + 2) * im2.size[1] + n - 2] += nError * 1 / 42.0
                pix[(m + 2) * im2.size[1] + n - 1] += nError * 2 / 42.0
                pix[(m + 2) * im2.size[1] + n] += nError * 4 / 42.0
                pix[(m + 2) * im2.size[1] + n + 1] += nError * 2 / 42.0
                pix[(m + 2) * im2.size[1] + n + 2] += nError * 1 / 42.0

        im2.save("Stucki.jpg")
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

    def mutil(self):
        from PIL import Image

        time = 1
        N = 144
        R = 2
        M = R * 2

        im = Image.open(self.imgName).convert('L')
        im2 = Image.new("L", (im.size[0] * time, im.size[1] * time))
        pix = [0.0] * im2.size[0] * im2.size[1]

        for m in range(im2.size[0]):
            for n in range(im2.size[1]):
                pix[m * im2.size[1] + n] = im.getpixel((m / time, n / time)) * N / 255.0 + 0.5

        for m in range(1, im2.size[0] - 1):
            for n in range(1, im2.size[1] - 1):
                if pix[m * im2.size[1] + n] <= N / M:
                    nError = pix[m * im2.size[1] + n]
                    im2.putpixel((m, n), 0)
                elif pix[m * im2.size[1] + n] <= 3 * N / M:
                    nError = pix[m * im2.size[1] + n] - 2 * N / M
                    im2.putpixel((m, n), 255 // R)
                else:
                    nError = pix[m * im2.size[1] + n] - 144
                    im2.putpixel((m, n), 255)
                pix[m * im2.size[1] + n + 1] += nError * 7 / 16.0
                pix[(m + 1) * im2.size[1] + n - 1] += nError * 3 / 16.0
                pix[(m + 1) * im2.size[1] + n] += nError * 5 / 16.0
                pix[(m + 1) * im2.size[1] + n + 1] += nError * 1 / 16.0

        im2.save("mutil.bmp")
        qim = ImageQt(im2)
        self.img_change = QtGui.QPixmap.fromImage(qim).scaled(self.image_change.width(), self.image_change.height())
        self.image_change.setPixmap(self.img_change)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # load icon
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    MainWindows = mywindow()
    MainWindows.setWindowIcon(icon)
    MainWindows.show()
    sys.exit(app.exec_())