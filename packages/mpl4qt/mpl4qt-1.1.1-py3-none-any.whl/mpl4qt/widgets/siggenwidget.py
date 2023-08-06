#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Signal generator widget.
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import pyqtProperty, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

import numpy as np


class SignalGeneratorWidget(QWidget):

    valueChanged = pyqtSignal('PyQt_PyObject')

    def __init__(self, parent=None):
        super(SignalGeneratorWidget, self).__init__(parent)

        self._value = [1.0]
        signal_chart = SignalChartWidget(self, self.getValue())
        line_edit1 = QLineEdit(str(signal_chart.getValue()))

        vbox = QVBoxLayout()
        vbox.addWidget(signal_chart)
        vbox.addWidget(line_edit1)
        self.setLayout(vbox)
        self.adjustSize()

        # signals/slots
        self.valueChanged.connect(signal_chart.setValue)
        line_edit1.textChanged.connect(self.setValue)

    def getValue(self):
        return self._value

    @pyqtSlot('PyQt_PyObject')
    def setValue(self, x):
        self._value = x
        print(x)
        import ast
        xx = ast.literal_eval(x)
        self.valueChanged.emit(xx)
        self.update()

    #value = pyqtProperty('PyQt_PyObject', getValue, setValue)


class SignalChartWidget(QWidget):
    def __init__(self, parent=None, value=0):
        self._value = value
        super(SignalChartWidget, self).__init__(parent)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 217, 217)))
        painter.drawRect(event.rect())
        tx, ty = self.width() / 2.0, self.height() / 2.0
        painter.drawText(tx - 10, ty, str(self.getValue()))
        painter.end()

    def getValue(self):
        return self._value

    def setValue(self, x):
        self._value = x


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = SignalGeneratorWidget()
    #w = SignalChartWidget()
    w.show()
    sys.exit(app.exec_())
