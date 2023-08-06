# -*- coding: utf-8 -*-
"""Plot view module.

contains PSPlotView, a subclass of QMainWindow
"""

import sys
import gc
from matplotlib import get_backend
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg as mplAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

from puzzlestream.backend.stream import PSStream
from puzzlestream.ui.plot import KeyPlot


class PSPlotView(QtWidgets.QMainWindow):

    def __init__(self, manager, puzzleItem, parent=None, numberOfViewers=1):
        super().__init__(parent)
        self.__viewers = []
        self.__viewerWindows = []
        self.__manager = manager
        self.__config = manager.config
        self.__puzzleItem = puzzleItem
        self.__autotile = self.__config["autotilePlots"]
        self.__createGUI(numberOfViewers)

        if puzzleItem is None:
            self.setWindowTitle("Plot view - complete stream")
        else:
            self.setWindowTitle("Plot view - " + str(puzzleItem))

    def statusUpdate(self, item):
        if self.__puzzleItem is None or item == self.__puzzleItem:
            if item.status == "finished" or self.__puzzleItem is None:
                self.__update()

    def __update(self):
        for v in self.__viewers:
            v.update()

    def updatePuzzleItem(self, puzzleItem):
        for v in self.__viewers:
            v.updatePuzzleItem(puzzleItem)

    def __createGUI(self, numberOfViewers=1):
        self.mdi = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi)

        self.toolbar = QtWidgets.QToolBar()
        addAction = self.toolbar.addAction("Add viewer")
        tileAction = self.toolbar.addAction("Tile windows")

        tileChkBox = QtWidgets.QCheckBox("auto tile")
        tileChkBox.setChecked(self.__config["autotilePlots"])
        tileChkBox.stateChanged.connect(self.__autotileChanged)
        self.toolbar.addWidget(tileChkBox)

        addAction.triggered.connect(self.__addViewer)
        tileAction.triggered.connect(self.mdi.tileSubWindows)
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)

        for i in range(numberOfViewers):
            self.__addViewer()

    def __addViewer(self):
        viewer = PSSinglePlotView(self.__manager, self.__puzzleItem, self)
        window = QtWidgets.QMdiSubWindow()
        window.setWidget(viewer)
        window.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # don't allow maximise, remove Qt icon
        window.setWindowFlags(
            Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        window.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(1, 1)))

        self.__viewers.append(viewer)
        self.__viewerWindows.append(window)
        self.mdi.addSubWindow(window)
        window.show()

        if self.__autotile:
            self.mdi.tileSubWindows()

    def __autotileChanged(self, state):
        self.__autotile = state == 2

    def updatePlots(self):
        for viewer in self.__viewers:
            viewer.updatePlots()

    def closeEvent(self, event):
        self.__config["autotilePlots"] = self.__autotile
        self.setParent(None)
        self.close()
        event.accept()

    def close(self):
        for v in self.__viewers:
            v.close()
        gc.collect()


class PSSinglePlotView(QtWidgets.QWidget):

    def __init__(self, manager, puzzleItem=None, parent=None):
        super().__init__(parent)
        self.__manager = manager
        self.__stream = manager.stream
        self.__modules = manager.scene.modules
        self.__puzzleItem = puzzleItem

        if puzzleItem is None:
            self.__data = self.__stream
        else:
            self.__data = puzzleItem.streamSection.data

        self.__parent = parent
        self.box = QtWidgets.QGridLayout()
        self.setLayout(self.box)
        self.__plots = []

        self.switchLayout = QtWidgets.QHBoxLayout()
        self.previousBtn = QtWidgets.QPushButton("previous", self)
        self.nextBtn = QtWidgets.QPushButton("next", self)
        self.combo = QtWidgets.QComboBox()
        self.combo.currentIndexChanged.connect(self.__selectionChanged)
        self.switchLayout.addWidget(self.previousBtn)
        self.switchLayout.addWidget(self.nextBtn)
        self.switchLayout.addWidget(self.combo)
        self.box.addLayout(self.switchLayout, 0, 0)

        self.previousBtn.pressed.connect(
            lambda: self.combo.setCurrentIndex(self.combo.currentIndex() - 1))
        self.nextBtn.pressed.connect(
            lambda: self.combo.setCurrentIndex(self.combo.currentIndex() + 1))
        self.previousBtn.setFixedWidth(120)
        self.nextBtn.setFixedWidth(120)
        self.previousBtn.setEnabled(False)
        self.nextBtn.setEnabled(False)

        self.__plotWidget = None
        self.updatePlots()

    def __translateKeyToUser(self, key):
        if isinstance(self.__data, PSStream):
            ID = key.split("-")[0]
            return key.replace(ID + "-", self.__modules[int(ID)].name + ": ")
        return key

    def __translateKeyToInternal(self, key):
        if key in self.__retranslatedKeys:
            return self.__retranslatedKeys[key]

    def updatePlots(self):
        plotList = []

        for key in self.__data:
            if isinstance(self.__data[key], Figure):
                plotList.append(key)

        self.__retranslatedKeys = {self.__translateKeyToUser(item[0]): item[0]
                                   for item in plotList}

        self.__plots = sorted(plotList)
        self.combo.clear()
        for key in self.__plots:
            self.combo.addItem(self.__translateKeyToUser(key))

        if self.__puzzleItem is not None:
            self.__data.cleanRam()

    def update(self):
        self.__data.reload()
        i = self.combo.currentIndex()
        self.updatePlots()
        self.combo.setCurrentIndex(i)

    def updatePuzzleItem(self, puzzleItem):
        self.__puzzleItem = puzzleItem
        self.__data = puzzleItem.streamSection.data
        self.update()

    def __setFigure(self, index=0):
        self.__closeCurrentPlotWidget()

        if len(self.__plots) > 0 and self.__plotWidget is None:
            self.__plotWidget = KeyPlot(self.__data, self.__plots[index], self)
            self.box.addWidget(self.__plotWidget, 1, 0)

    def __selectionChanged(self):
        self.__setFigure(self.combo.currentIndex())
        self.previousBtn.setEnabled(self.combo.currentIndex() != 0)
        self.nextBtn.setEnabled(
            self.combo.currentIndex() < len(self.__plots) - 1)

    def __closeCurrentPlotWidget(self):
        if self.__plotWidget is not None:
            self.__plotWidget.clear()
            plt.close("all")
            self.box.removeWidget(self.__plotWidget)
            self.__plotWidget.setParent(None)
            self.__plotWidget.hide()
            del self.__plotWidget
            self.__plotWidget = None

        if self.__puzzleItem is not None:
            self.__data.cleanRam()

        gc.collect()

    def close(self):
        self.setParent(None)

        if self.__puzzleItem is not None:
            self.__data.cleanRam()

        self.__closeCurrentPlotWidget()
