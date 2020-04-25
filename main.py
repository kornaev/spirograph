# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:48:47 2020

@author: crazY
"""


import sys
from math import cos,sin
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

import mainwindow

# R = 125 # радиус внешней окружности
# r = 70 # радиус внутренней окружности
# d = 25 # длина плеча
m = 3 # scale multiplyer

pen_outer = QtGui.QPen(QtGui.QColor('red'))
pen_inner = QtGui.QPen(QtGui.QColor('blue'))
pen_plecho = QtGui.QPen(QtGui.QColor('green'))
pen_spiro = QtGui.QPen(QtGui.QColor('black'))
pen_spiro.setWidth(4)


def draw_circle(self, x, y, r):
    self.drawEllipse(int(x - r), int(y - r), r * 2, r * 2)

class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.label_out_final.setVisible(False)
        self.but_save.clicked.connect(self.save_file)
        self.but_draw.clicked.connect(self.draw_image)

        canvas = QtGui.QPixmap(400 * m, 400 * m)
        canvas.fill(QtGui.QColor('#ffffff'))

        canvas_final = QtGui.QPixmap(400 * m, 400 * m)
        canvas_final.fill(QtGui.QColor('#ffffff'))

        self.label_out.setPixmap(canvas)
        self.label_out_final.setPixmap(canvas_final)
        self.update()

    def save_file(self):
        return

    def draw_image(self):
        R = self.spinBox_outer_diameter.value() * m
        r = self.spinBox_inner_diameter.value() * m
        d = self.spinBox_plecho.value() * m
        theta = 0.2
        steps = int(6*3.14/theta)
        angle = 0

        for t in range(steps):
            _inner_center_x = (R - r) * cos(angle)
            _inner_center_y = (R - r) * sin(angle)

            _spiro_x = _inner_center_x + d * cos(((R-r)/r)*angle)
            _spiro_y = _inner_center_y - d * sin(((R-r)/r)*angle)

            _p = QtGui.QPainter(self.label_out.pixmap())
            _p.translate(200 * m, 200 * m)

            _p.setPen(pen_outer)
            _p.drawPoint(0, 0)
            draw_circle(_p, 0, 0, R)

            _p.setPen(pen_inner)
            _p.drawPoint(_inner_center_x, _inner_center_y)
            draw_circle(_p, _inner_center_x, _inner_center_y, r)

            _p.setPen(pen_plecho)
            _p.drawLine(_inner_center_x, _inner_center_y, _spiro_x, _spiro_y)

            _p.setPen(pen_spiro)
            _p.drawPoint(_spiro_x, _spiro_y)
            _p.end()

            _p_final = QtGui.QPainter(self.label_out_final.pixmap())
            _p_final.translate(200 * m, 200 * m)
            _p_final.setPen(pen_spiro)
            _p_final.drawPoint(_spiro_x, _spiro_y)
            _p_final.end()

            sleep(0.01)
            angle += theta
            self.label_out.update()
            self.label_out.setVisible(True)
            print('updating %s' % t)

        sleep(1)
        self.label_out.setVisible(False)
        self.label_out_final.setVisible(True)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
