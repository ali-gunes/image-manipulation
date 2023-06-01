# Contains related functionalities for Segmentation
import os

import numpy as np
from PyQt5.QtGui import QPixmap
from skimage.color import rgb2gray
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese, checkerboard_level_set
from skimage.segmentation import morphological_chan_vese



class Segmentation():
    def __init__(self, sourceImage, segmentationType, outputViewer):
        self.outputImage = None
        self.sourceImage = sourceImage
        self.outputViewer = outputViewer

        self.fileName = "output.png" if self.sourceImage[0][-3::] == "jpg" else "output.jpg"

        if segmentationType == "multiOtsu":
            self.multiOtsuSegmentation()
        elif segmentationType == "chanVese":
            self.chanVeseSegmentation()
        elif segmentationType == "morphological":
            self.morphologicalSegmentation()

    def multiOtsuSegmentation(self):
        sourceImage = io.imread(self.sourceImage)

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage
        thresholds = threshold_multiotsu(grayScale)
        self.outputImage = np.digitize(grayScale, bins=thresholds)


        self.fileName = "Multi-Otsu_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='jet')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)

    def chanVeseSegmentation(self):
        sourceImage = io.imread(self.sourceImage)

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        self.outputImage = chan_vese(grayScale, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                                     max_num_iter=200, dt=0.5, init_level_set="checkerboard",
                                     extended_output=True)[1]

        self.fileName = "Chan-Vese_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)

    def morphologicalSegmentation(self):
        sourceImage = io.imread(self.sourceImage)

        grayScale = rgb2gray(sourceImage) if len(sourceImage.shape) == 3 else sourceImage

        init_ls = checkerboard_level_set(grayScale.shape, 6)

        self.outputImage = morphological_chan_vese(grayScale, num_iter=35, init_level_set=init_ls,
                                     smoothing=3)

        self.fileName = "Morphological-Snake_" + self.fileName

        plt.imsave(self.fileName, self.outputImage, cmap='gray')
        self.outputViewer.setPixmap(QPixmap(self.fileName))
        os.remove(self.fileName)
