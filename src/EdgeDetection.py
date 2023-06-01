# Author: Ali Gunes
# Contains related functionalities for Edge Detection
import os

import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from skimage import io
from skimage.color import rgb2gray
from skimage.filters import roberts, sobel, scharr, prewitt

class EdgeDetection():
    def __init__(self, sourceImage, edgeDetectionType, outputViewer):
        self.outputImage = None
        self.sourceImage = sourceImage
        self.outputViewer = outputViewer

        self.fileName = "output.png" if self.sourceImage[0][-3::] == "jpg" else "output.jpg"

        if edgeDetectionType == "roberts":
            self.robertsEdgeDetection()
        elif edgeDetectionType == "sobel":
            self.sobelEdgeDetection()
        elif edgeDetectionType == "scharr":
            self.scharrEdgeDetection()
        elif edgeDetectionType == "prewitt":
            self.prewittEdgeDetection()


    def robertsEdgeDetection(self):

        sourceImage = io.imread(self.sourceImage)[:,:,:3]

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        self.outputImage = roberts(grayScale)

        self.fileName = "Roberts_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)



    def sobelEdgeDetection(self):
        sourceImage = io.imread(self.sourceImage)[:,:,:3]

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        self.outputImage = sobel(grayScale)

        self.fileName = "Sobel_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)

    def scharrEdgeDetection(self):
        sourceImage = io.imread(self.sourceImage)[:,:,:3]

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        self.outputImage = scharr(grayScale)

        self.fileName = "Scharr_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)

    def prewittEdgeDetection(self):
        sourceImage = io.imread(self.sourceImage)[:,:,:3]

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        self.outputImage = prewitt(grayScale)

        self.fileName = "Prewitt_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)
