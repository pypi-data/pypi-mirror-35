import os
import pickle

import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.backends.backend_qt5agg as mplAgg
import matplotlib.pyplot as plt
import psutil
from matplotlib import get_backend
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import gc
import sys


def getMemoryUsage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss


def pickleFigure():
    fig = plt.figure()
    plt.plot(np.random.random(int(1e5)))
    plt.close()
    with open("test", "bw") as f:
        pickle.dump(fig, f)
    del fig


def loadFigure():
    with open("test", "br") as f:
        fig = pickle.load(f)
    return fig


class Plot(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__fig = loadFigure()
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        canvas = mplAgg.FigureCanvasQTAgg(self.__fig)
        canvas.setParent(self)
        self.layout.addWidget(canvas)
        self.layout.addWidget(mplAgg.NavigationToolbar2QT(canvas, self))


class Wrap(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.btn = QtWidgets.QPushButton("Press me!")
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.layout.addWidget(self.btn)
        self.btn.pressed.connect(self.__btnPressed)
        self.__timer = QtCore.QTimer()
        self.__timer.setInterval(1000)
        self.__timer.timeout.connect(self.__print)
        self.__timer.start()
        self.setFixedSize(800, 600)
        self.__plot = None

    def __btnPressed(self):
        if self.__plot is None:
            self.__plot = Plot(self)
            self.layout.addWidget(self.__plot)
        else:
            self.layout.removeWidget(self.__plot)
            self.__plot.setParent(None)
            self.__plot.deleteLater()
            del self.__plot
            self.__plot = None

    def __print(self):
        gc.collect()
        print(getMemoryUsage())


if __name__ == "__main__":
    pickleFigure()
    gc.collect()
    print(getMemoryUsage())
    app = QtWidgets.QApplication(sys.argv)
    w = Wrap()
    w.show()
    app.exec_()
