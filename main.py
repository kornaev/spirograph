# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:48:47 2020

@author: crazY
"""


import sys
from math import cos, sin, pi
from time import sleep

from PyQt5 import QtGui, QtWidgets

import mainwindow

# R = 125 # радиус внешней окружности
# r = 70 # радиус внутренней окружности
# d = 25 # длина плеча
M = 3 # scale multiplyer

pen_outer = QtGui.QPen(QtGui.QColor('red'))
pen_inner = QtGui.QPen(QtGui.QColor('blue'))
pen_plecho = QtGui.QPen(QtGui.QColor('green'))
pen_spiro = QtGui.QPen(QtGui.QColor('black'))
pen_spiro.setWidth(4)
PEN_CLEAR = QtGui.QPen(QtGui.QColor('white'))


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
        _l = QtWidgets.QStackedLayout()
        _l.addWidget(self.label_out_final)
        _l.addWidget(self.label_out)
        _l.addWidget(self.label_bg)
        _l.setStackingMode(QtWidgets.QStackedLayout.StackAll)
        self.mwLayout_2.addLayout(_l)
#        self.label_out_final.setVisible(False)
        self.but_save.clicked.connect(self.save_file)
        self.but_draw.clicked.connect(self.draw_image)

        canvas = QtGui.QPixmap(400 * M, 400 * M)
        canvas.fill(QtGui.QColor('white'))
        canvas_bg = QtGui.QPixmap(400 * M, 400 * M)
        canvas_bg.fill(QtGui.QColor('white'))
        canvas_final = QtGui.QPixmap(400 * M, 400 * M)
        canvas_final.fill(QtGui.QColor('transparent'))

        self.label_out.setPixmap(canvas)
        self.label_bg.setPixmap(canvas_bg)
        self.label_out_final.setPixmap(canvas_final)
        self.update()

    def save_file(self):
        return

    def draw_image(self):
        r_o = self.spinBox_outer_diameter.value() * M
        r_i = self.spinBox_inner_diameter.value() * M
        d = self.spinBox_plecho.value() * M
        theta = 0.02
        angle = 0
        _inner_center_x_0 = (r_o - r_i) * cos(angle)
        _inner_center_y_0 = (r_o - r_i) * sin(angle)

        _spiro_x = 0
        _spiro_y = 0

        while int(angle) != int(2 * pi / theta):
            _inner_center_x = (r_o - r_i) * cos(angle)
            _inner_center_y = (r_o - r_i) * sin(angle)

            _spiro_x_new = _inner_center_x + d * cos(((r_o-r_i)/r_i)*angle)
            _spiro_y_new = _inner_center_y - d * sin(((r_o-r_i)/r_i)*angle)

            self.label_out.pixmap().fill(QtGui.QColor('#ffffff'))

            _p = QtGui.QPainter(self.label_out.pixmap())
            _p.translate(200 * M, 200 * M)

            _p.setPen(pen_outer)
            _p.drawPoint(0, 0)
            draw_circle(_p, 0, 0, r_o)

            _p.setPen(pen_inner)
            _p.drawPoint(_inner_center_x, _inner_center_y)
            draw_circle(_p, _inner_center_x, _inner_center_y, r_i)

            _p.setPen(pen_plecho)
            _p.drawLine(_inner_center_x,
                        _inner_center_y,
                        _spiro_x_new,
                        _spiro_y_new)

#            _p.setPen(pen_spiro)
#            _p.drawPoint(_spiro_x, _spiro_y)

            if _spiro_x != 0 and _spiro_y != 0:
                _p_final = QtGui.QPainter(self.label_out_final.pixmap())
                _p_final.translate(200 * M, 200 * M)
                _p_final.setPen(pen_spiro)
                _p_final.drawLine(
                    _spiro_x,
                    _spiro_y,
                    _spiro_x_new,
                    _spiro_y_new)
                _p_final.end()

            _spiro_x = _spiro_x_new
            _spiro_y = _spiro_y_new

            angle += theta
            self.label_out.repaint()

#            _p.setPen(PEN_CLEAR)
#            draw_circle(_p, _inner_center_x, _inner_center_y, r_i)
#            _p.drawLine(_inner_center_x, _inner_center_y, _spiro_x, _spiro_y)

            _p.end()
#            print(angle)

            sleep(0.001)

        sleep(1)
        self.label_out.setVisible(False)
#        self.label_out_final.setVisible(True)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
