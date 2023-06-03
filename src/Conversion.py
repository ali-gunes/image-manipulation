# Author: Ali Gunes
# Contains related functionalities for RGB to Grayscale and RGB to HSV
from PyQt5.QtGui import QPixmap
from skimage.color import rgb2gray
from skimage import io
import matplotlib.pyplot as plt
import os
from skimage.color import rgb2hsv


class RGBConversions():
    def __init__(self, sourceImage, conversionType, outputViewer, undoHistory):
        self.outputImage = None
        self.sourceImage = sourceImage
        self.outputViewer = outputViewer

        self.undoHistory = undoHistory

        self.fileName = "output.png" if self.sourceImage[0][-3::] == "jpg" else "output.jpg"

        self.rgbToGrayscale() if conversionType == "rgb2gray" else self.rgbToHsv()

    def rgbToGrayscale(self):
        sourceImage = io.imread(self.sourceImage, as_gray=False)

        self.outputImage = rgb2gray(sourceImage)

        self.fileName = "RGB-to-Grayscale_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap=plt.cm.gray)
        self.outputViewer.setPixmap(QPixmap(self.fileName))

        self.undoHistory.append(QPixmap(self.fileName))

        os.remove(self.fileName)

    def rgbToHsv(self):
        sourceImage = io.imread(self.sourceImage, as_gray=False)
        self.outputImage = rgb2hsv(sourceImage)

        hue_img = self.outputImage[:, :, 0]
        value_img = self.outputImage[:, :, 2]

        hue_threshold = 0.04
        self.outputImage = hue_img > hue_threshold

        value_threshold = 0.10
        self.outputImage = (hue_img > hue_threshold) | (value_img < value_threshold)

        self.fileName = "RGB-to-HSV_" + self.fileName

        plt.imsave(self.fileName, self.outputImage)
        self.outputViewer.setPixmap(QPixmap(self.fileName))

        self.undoHistory.append(QPixmap(self.fileName))

        os.remove(self.fileName)
