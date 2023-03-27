# MIT License

"""Copyright (c) 2023 JeongHan-Bae

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import random


class array:
    def __init__(self, liste):
        self.arraylist = liste

    def twin_c(self):
        for i in range(0, len(self.arraylist) - 1):
            for j in range(0, len(self.arraylist[0])):
                if self.arraylist[i][j] == self.arraylist[i + 1][j] != 0:
                    return True
        return False

    def twin_l(self):
        for i in range(0, len(self.arraylist)):
            for j in range(0, len(self.arraylist[0]) - 1):
                if self.arraylist[i][j] == self.arraylist[i][j + 1] != 0:
                    return True
        return False

    def NoneNul_l_g(self, k, m):
        for j in range(m + 1, len(self.arraylist[0])):
            if self.arraylist[k][j] != 0:
                return True
        return False

    def NoneNul_l_d(self, k, m):
        for j in range(0, m):
            if self.arraylist[k][j] != 0:
                return True
        return False

    def NoneNul_c_h(self, k, m):
        for i in range(m + 1, len(self.arraylist[0])):
            if self.arraylist[i][k] != 0:
                return True
        return False

    def NoneNul_c_b(self, k, m):
        for i in range(0, m):
            if self.arraylist[i][k] != 0:
                return True
        return False

    def gauche(self):
        for i in range(0, len(self.arraylist)):
            j = 0
            while j < len(self.arraylist[0]):
                if self.arraylist[i][j] == 0 and self.NoneNul_l_g(i, j):
                    for k in range(j, len(self.arraylist[0]) - 1):
                        self.arraylist[i][k] = self.arraylist[i][k + 1]
                    self.arraylist[i][len(self.arraylist[0]) - 1] = 0
                else:
                    j += 1
        for i in range(0, len(self.arraylist)):
            for j in range(0, len(self.arraylist[0]) - 1):
                if self.arraylist[i][j] == self.arraylist[i][j + 1] != 0:
                    self.arraylist[i][j] = 2 * self.arraylist[i][j]
                    for k in range(j + 1, len(self.arraylist[0]) - 1):
                        self.arraylist[i][k] = self.arraylist[i][k + 1]
                    self.arraylist[i][len(self.arraylist[0]) - 1] = 0
        return self

    def Acces_g(self):
        if self.twin_l():
            return True
        else:
            for i in range(0, len(self.arraylist)):
                for j in range(0, len(self.arraylist[0]) - 1):
                    if self.arraylist[i][j] == 0 and self.NoneNul_l_g(i, j):
                        return True
        return False

    def droite(self):
        for i in range(0, len(self.arraylist)):
            v = 0
            while v < len(self.arraylist[0]):
                j = len(self.arraylist[0]) - v - 1
                if self.arraylist[i][j] == 0 and self.NoneNul_l_d(i, j):
                    for w in range(v, len(self.arraylist[0]) - 1):
                        k = len(self.arraylist[0]) - w - 1
                        self.arraylist[i][k] = self.arraylist[i][k - 1]
                    self.arraylist[i][0] = 0
                else:
                    v += 1
        for i in range(0, len(self.arraylist)):
            for v in range(0, len(self.arraylist[0]) - 1):
                j = len(self.arraylist[0]) - v - 1
                if self.arraylist[i][j] == self.arraylist[i][j - 1] != 0:
                    self.arraylist[i][j] = 2 * self.arraylist[i][j]
                    for w in range(v + 1, len(self.arraylist[0])):
                        k = len(self.arraylist[0]) - w - 1
                        self.arraylist[i][k] = self.arraylist[i][k - 1]
                    self.arraylist[i][0] = 0
        return self

    def Acces_d(self):
        if self.twin_l():
            return True
        else:
            for i in range(0, len(self.arraylist)):
                for v in range(0, len(self.arraylist[0]) - 1):
                    j = len(self.arraylist[0]) - v - 1
                    if self.arraylist[i][j] == 0 and self.NoneNul_l_d(i, j):
                        return True
        return False

    def haut(self):
        for j in range(0, len(self.arraylist)):
            i = 0
            while i < len(self.arraylist[0]):
                if self.arraylist[i][j] == 0 and self.NoneNul_c_h(j, i):
                    for k in range(i, len(self.arraylist[0]) - 1):
                        self.arraylist[k][j] = self.arraylist[k + 1][j]
                    self.arraylist[len(self.arraylist[0]) - 1][j] = 0
                else:
                    i += 1
        for j in range(0, len(self.arraylist)):
            for i in range(0, len(self.arraylist[0]) - 1):
                if self.arraylist[i][j] == self.arraylist[i + 1][j] != 0:
                    self.arraylist[i][j] = 2 * self.arraylist[i][j]
                    for k in range(i + 1, len(self.arraylist[0]) - 1):
                        self.arraylist[k][j] = self.arraylist[k + 1][j]
                    self.arraylist[len(self.arraylist[0]) - 1][j] = 0
        return self

    def Acces_h(self):
        if self.twin_c():
            return True
        else:
            for j in range(0, len(self.arraylist)):
                for i in range(0, len(self.arraylist[0]) - 1):
                    if self.arraylist[i][j] == 0 and self.NoneNul_c_h(j, i):
                        return True
        return False

    def bas(self):
        for j in range(0, len(self.arraylist)):
            v = 0
            while v < len(self.arraylist[0]):
                i = len(self.arraylist[0]) - v - 1
                if self.arraylist[i][j] == 0 and self.NoneNul_c_b(j, i):
                    for w in range(v, len(self.arraylist[0]) - 1):
                        k = len(self.arraylist[0]) - w - 1
                        self.arraylist[k][j] = self.arraylist[k - 1][j]
                    self.arraylist[0][j] = 0
                else:
                    v += 1
        for j in range(0, len(self.arraylist)):
            for v in range(0, len(self.arraylist[0]) - 1):
                i = len(self.arraylist[0]) - v - 1
                if self.arraylist[i][j] == self.arraylist[i - 1][j] != 0:
                    self.arraylist[i][j] = 2 * self.arraylist[i][j]
                    for w in range(v + 1, len(self.arraylist[0])):
                        k = len(self.arraylist[0]) - w - 1
                        self.arraylist[k][j] = self.arraylist[k - 1][j]
                    self.arraylist[0][j] = 0
        return self

    def Acces_b(self):
        if self.twin_c():
            return True
        else:
            for j in range(0, len(self.arraylist)):
                for v in range(0, len(self.arraylist[0]) - 1):
                    i = len(self.arraylist[0]) - v - 1
                    if self.arraylist[i][j] == 0 and self.NoneNul_c_b(j, i):
                        return True
        return False

    def Mort(self):
        if self.Acces_h() or self.Acces_b() or self.Acces_d() or self.Acces_g():
            return False
        return True

    def Gagne(self, puis: int):
        for i in range(0, len(self.arraylist)):
            for j in range(0, len(self.arraylist[0])):
                if self.arraylist[i][j] == 2 ** puis:
                    return True
        return False

    def Neuf(self):
        listeligne = []
        for i in range(0, len(self.arraylist)):
            for j in range(0, len(self.arraylist[0])):
                if self.arraylist[i][j] == 0:
                    listeligne.append(i)
        ligne = random.choice(listeligne)
        listecolonne = []
        for j in range(0, len(self.arraylist[0])):
            if self.arraylist[ligne][j] == 0:
                listecolonne.append(j)
        colonne = random.choice(listecolonne)
        self.arraylist[ligne][colonne] = random.choice([2, 4])
