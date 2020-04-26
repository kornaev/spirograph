# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:05:26 2020

@author: crazY
"""


from math import cos, sin, pi


class spirograph():
    def __init__(self, R, r, d):
        self.R = R
        self.r = r
        self.d = d
        self.res = list()

    def __spiro_formula_x(self, a):
        return int(
            self.__scc_x(a) + self.d * cos(((self.R - self.r) / self.r) * a))

    def __spiro_formula_y(self, a):
        return int(
            self.__scc_y(a) - self.d * sin(((self.R - self.r) / self.r) * a))

    def __scc_x(self, a):
        """
        small circle center, x coord

        Parameters
        ----------
        a : float
            current angle.

        Returns
        -------
        int
            the x coord of center of a inner circle.

        """
        return int((self.R - self.r) * cos(a))

    def __scc_y(self, a):
        """
        small circle center, y coord

        Parameters
        ----------
        a : float
            current angle.

        Returns
        -------
        int
            the y coord of center of a inner circle.

        """
        return int((self.R - self.r) * sin(a))

    def __is_done(self):
        if len(self.res) < 2:
            return False
        elif self.res[0] == self.res[len(self.res) - 1]:
            return True

    def calculate(self):
        theta = pi / 50
        angle = 0
        while not self.__is_done():
            self.res.append([
                self.__scc_x(angle),
                self.__scc_y(angle),
                self.__spiro_formula_x(angle),
                self.__spiro_formula_y(angle)])
            angle += theta

    def get_results(self):
        return self.res
