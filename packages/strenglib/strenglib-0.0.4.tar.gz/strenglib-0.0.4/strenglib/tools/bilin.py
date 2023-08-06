import numpy as np


class Bilin:
    def __init__(self, xtarget=0.0, dropstrength=0.75, elastoplastic=False, allowa010=True):
        self.x_ini = np.array([])
        self.y_ini = np.array([])
        self.logtext = []
        self.xtarget = xtarget
        self.dropstrength = dropstrength
        self.elastoplastic = elastoplastic
        self.allowa010 = allowa010
        self.EPSILON = 0.00000001

        self.x_results = np.array([])
        self.y_results = np.array([])

    def load_space_delimited(self, fname, delimiter=' '):
        self.x_ini, self.y_ini = np.loadtxt(fname, delimiter=delimiter, usecols=(0, 1), unpack=True)

        self.logtext.append('initial X values')
        self.logtext.append(str(self.x_ini))
        self.logtext.append('')
        self.logtext.append('initial Y values')
        self.logtext.append(str(self.y_ini))

    def load_space_delimited_string(self, text, delimiter=' '):
        self.x_ini = np.array([], dtype=np.float)
        self.y_ini = np.array([], dtype=np.float)
        spl = text.splitlines()
        for ln in spl:
            xy = ln.split(delimiter)
            self.x_ini = np.append(self.x_ini, xy[0])
            self.y_ini = np.append(self.y_ini, xy[1])
        self.x_ini = self.x_ini.astype(float)
        self.y_ini = self.y_ini.astype(float)

    @staticmethod
    def __curve_to_xcheck(x, y, xtarget):
        if xtarget == 0.0:
            return x, y

        if xtarget > max(x):
            xtarget = max(x)
        _ytarget = float(np.interp(xtarget, x, y))

        # Κρατώ μόνο τις τιμές μέχρι μία πρίν από το xtarget
        _x = x[(x < xtarget)]
        _y = y[0:len(_x)]

        # Προσθέτω τα x, y της παρεμβολής
        _x = np.append(_x, xtarget)
        _y = np.append(_y, _ytarget)

        return _x, _y

    @staticmethod
    def __get_area(x, y):
        return np.trapz(y, x)

    def calc(self):
        # Βρίσκω την αρχική μετατόπιση σε περίπτωση που δεν είναι 0
        x_ini0 = self.x_ini[0]

        self.logtext.append('')
        self.logtext.append(f'Αρχική μετατόπιση: {x_ini0}')

        ymax = max(self.y_ini)
        i_ymax = np.argmax(self.y_ini)

        y_max_to_end = self.y_ini[i_ymax:]
        x_max_to_end = self.x_ini[i_ymax:]

        i = 0
        while y_max_to_end[i] > self.dropstrength * ymax and i < len(y_max_to_end) - 1:
            i += 1
        x_for_dropstrength = x_max_to_end[i]

        x_target = min(x_for_dropstrength, self.xtarget)

        # Κρατώ την καμπύλη μέχρι το xtarget, αν υπάρχει
        x_xcheck, y_xcheck = self.__curve_to_xcheck(self.x_ini, self.y_ini, x_target)

        # Αφαιρώ την αρχική μετατόπιση ώστε η καμπύλη να ξεκινά από το (0, 0)
        x_xcheck = x_xcheck - x_ini0

        self.logtext.append('')
        self.logtext.append('X values μέχρι το xtarget, αφαιρώντας (αν υπάρχει) την αρχική μετατόπιση')
        self.logtext.append(str(x_xcheck))
        self.logtext.append('')
        self.logtext.append('Y values μέχρι το xtarget')
        self.logtext.append(str(y_xcheck))

        # Βρίσκω τις δυσκαμψίες σε κάθε βήμα
        # Αλλάχω προσωρινά το x(0) για να μη διαιρεί με 0
        x_xcheck[0] = self.EPSILON
        k = np.divide(y_xcheck, x_xcheck)
        x_xcheck[0] = 0.0

        self.logtext.append('')
        self.logtext.append('Δυσκαμψίες (y(i)/x(i)')
        self.logtext.append(str(k))

        y02 = 0.2 * max(y_xcheck)
        x02 = float(np.interp(y02, y_xcheck, x_xcheck))

        k02 = y02 / x02

        self.logtext.append('')
        self.logtext.append('Έλεγχος στο 20% του ymax')
        self.logtext.append(f'x(02)={x02}, y(02)={y02}. Οπότε k(02)={k02}')

        # Βρίσκω το εμβαρό
        area = self.__get_area(x_xcheck, y_xcheck)
        self.logtext.append('')
        self.logtext.append(f'Εμβαδό καμπύλης: {area}')

        iteration_number = 0
        kel = k02
        error = 100.
        while error > self.EPSILON:
            iteration_number += 1  # This is the same as count = count + 1

            x_y, y_y, x_u, y_u, kinel, k_06 = self.iteration(x_xcheck, y_xcheck, kel, area)
            self.logtext.append('')
            self.logtext.append(f'iteration: {iteration_number}')
            self.logtext.append(f'x_y= {x_y}')
            self.logtext.append(f'y_y= {y_y}')
            self.logtext.append(f'x_u= {x_u}')
            self.logtext.append(f'y_u= {y_u}')
            self.logtext.append(f'kinel= {kinel}')
            self.logtext.append(f'kel= {kel}')
            self.logtext.append(f'k_06= {k_06}')

            self.x_results = np.array([0., x_y, x_u]) + x_ini0
            self.y_results = np.array([0., y_y, y_u])

            error = np.abs((kel - k_06) / k_06)
            kel = k_06
            self.logtext.append(f'error:{error:.7%}')

            self.logtext.append(str(self.x_results))
            self.logtext.append(str(self.y_results))

            if iteration_number > 1000:
                break


    def results_kel(self):
        return self.y_results[1] / self.x_results[1]

    def results_kinel(self):
        return (self.y_results[2] - self.y_results[1]) / (self.x_results[2] - self.x_results[1])

    def results_ductility(self):
        return self.x_results[2] / self.x_results[1]

    def results_hardening(self):
        return self.results_kinel()/self.results_kel()

    def iteration(self, x, y, kel, area):
        rcount = len(x) - 1
        ymax = max(y)

        # ********** Αρχικός υπολογισμός *****************
        # if y[rcount - 1] >= (2 * ymax + y[rcount]) / 3.0 and y[rcount] <= (2 * ymax + y[rcount]) / 3.0:
        #     y_u = y[rcount - 1]
        # else:
        #     y_u = (2 * ymax + y[rcount]) / 3.0
        y_u = (2 * ymax + y[rcount]) / 3.0

        x_u = x[rcount]

        x_y = (2 * area - x[rcount] * y_u) / (kel * x[rcount] - y_u)
        y_y = kel * x_y

        kinel = (y_u - y_y) / (x_u - x_y)

        # ********** 2η περίπτωση kinel/kel>0.1 *****************
        if self.allowa010 == False and kinel / kel > 0.1:
            alpha = 1.
            beta = -2. * x_u * kel
            gamma = 1.8 * area * kel + 0.1 * (kel * x_u) ** 2
            y_u = (-beta - (beta * beta - 4 * alpha * gamma) ** 0.5) / (2. * alpha)
            x_y = (y_u - 0.1 * kel * x_u) / (0.9 * kel)
            y_y = kel * x_y

            # ********** 3η περίπτωση Ελαστοπλαστικό ή kinel<0 *****************
        if self.elastoplastic == True or kinel < 0.0:
            alpha = 1.
            beta = -2. * x_u
            gamma = 2. * area / kel
            x_y = (-beta - (beta * beta - 4 * alpha * gamma) ** 0.5) / (2. * alpha)
            y_y = x_y * kel
            y_u = y_y

        y_06 = 0.6 * y_y
        x_06 = float(np.interp(y_06, y, x))
        k_06 = y_06 / x_06

        return x_y, y_y, x_u, y_u, kinel, k_06

    def __str__(self):
        return ('\n').join((self.logtext))
