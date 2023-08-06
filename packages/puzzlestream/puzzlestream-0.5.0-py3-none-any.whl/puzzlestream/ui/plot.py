import gc
import pickle
import sys

import matplotlib
import matplotlib.backends.backend_qt5agg as mplAgg
from matplotlib import get_backend
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets


class Plot(QtWidgets.QWidget):

    def __init__(self, figure: Figure, parent=None):
        super().__init__(parent=parent)
        self.__fig = figure
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        canvas = mplAgg.FigureCanvasQTAgg(self.__fig)
        self.layout.addWidget(canvas)
        self.layout.addWidget(mplAgg.NavigationToolbar2QT(canvas, None))

    def clear(self):
        self.__fig.clear()


class KeyPlot(Plot):

    def __init__(self, data: dict, figureKey: str, parent=None):
        super().__init__(data[figureKey], parent)
