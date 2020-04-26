# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:48:47 2020

@author: crazY
"""

import sys
from time import sleep
from PyQt5 import QtGui, QtWidgets

import mainwindow
from spirograph import spirograph

M = 3 # scale multiplyer

pen_outer = QtGui.QPen(QtGui.QColor('red'))
pen_inner = QtGui.QPen(QtGui.QColor('blue'))
pen_plecho = QtGui.QPen(QtGui.QColor('green'))
pen_spiro = QtGui.QPen(QtGui.QColor('black'))
pen_spiro.setWidth(4)


def draw_circle(self, center_x, center_y, radius):
    self.drawEllipse(
        int(center_x - radius),
        int(center_y - radius),
        radius * 2,
        radius * 2)


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.init_widgets()
        self.init_pixmaps()
        self.but_save.clicked.connect(self.save_file)
        self.but_draw.clicked.connect(self.draw_image)

    def init_widgets(self):
        _l = QtWidgets.QStackedLayout()
        _l.setStackingMode(QtWidgets.QStackedLayout.StackAll)
        _l.addWidget(self.label_out_final)
        _l.addWidget(self.label_out)
        _l.addWidget(self.label_bg)
        self.mwLayout_2.addLayout(_l)

    def init_pixmaps(self):
        canvas = QtGui.QPixmap(400 * M, 400 * M)
        canvas.fill(QtGui.QColor('white'))

        canvas_final = QtGui.QPixmap(400 * M, 400 * M)
        canvas_final.fill(QtGui.QColor('transparent'))

        canvas_bg = QtGui.QPixmap(400 * M, 400 * M)
        canvas_bg.fill(QtGui.QColor('white'))

        self.label_out.setPixmap(canvas)
        self.label_out_final.setPixmap(canvas_final)
        self.label_bg.setPixmap(canvas_bg)

    def save_file(self):
        return

    def draw_image(self):
        R = self.spinBox_outer_diameter.value() * M
        r = self.spinBox_inner_diameter.value() * M
        d = self.spinBox_plecho.value() * M

        s = spirograph(R, r, d)
        s.calculate()
        res = s.get_results()

        self.label_out.setVisible(True)
        if self.cb_clean.isChecked():
            self.label_out_final.pixmap().fill(QtGui.QColor('transparent'))

        _p = QtGui.QPainter(self.label_out.pixmap())
        _p.translate(200 * M, 200 * M)
        _f = QtGui.QPainter(self.label_out_final.pixmap())
        _f.translate(200 * M, 200 * M)
        _f.setPen(pen_spiro)

        for i in range(1, len(res)):
            self.label_out.pixmap().fill(QtGui.QColor('#ffffff'))

            _p.setPen(pen_outer)
            draw_circle(_p, 0, 0, R)

            _p.setPen(pen_inner)
            draw_circle(_p, res[i][0], res[i][1], r)

            _p.setPen(pen_plecho)
            _p.drawLine(res[i][0], res[i][1], res[i][2], res[i][3])

            _f.drawLine(res[i][2], res[i][3], res[i - 1][2], res[i - 1][3])

            self.label_out.repaint()
        _p.end()
        _f.end()
        sleep(1)
        self.label_out.setVisible(False)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
