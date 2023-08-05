# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np

### imports from ##############################################################
from sklearn.linear_model import LinearRegression

###############################################################################
def lin_reg_without_intercept(x, y):
    linearRegression = LinearRegression(fit_intercept=False)
    linearRegression.fit(x.reshape(-1, 1), y)
    m = linearRegression.coef_[0]

    residuum = np.sum((m * x - y)**2)

    N = x.size
    df = N-2
    sy = np.sqrt(1 / df * residuum)
    
    sm = sy * np.sqrt(1 / N / np.var(x))

    return m, sm
