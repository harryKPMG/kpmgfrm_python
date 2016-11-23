#!/user/bin/python
# _*_ coding: utf-8 _*_
import math

import scipy.optimize as opt
from scipy.stats import norm
import numpy as np
import scipy.interpolate as Interpolation

__author__ = 'philipshen'


def BSmodel(sigma, K, r1, r2, S, T, flag, MarketPrice):
    d1 = (math.log(S / K) + (r2 - r1 + 0.5 * sigma ** 2) * T) / (sigma * T ** (0.5))
    d2 = d1 - sigma * T ** (0.5)

    if flag == 1:
        result = S * math.exp(-r1 * T) * norm.cdf(d1) - K * math.exp(-r2 * T) * norm.cdf(d2) - MarketPrice
    else:
        result = -S * math.exp(-r1 * T) * norm.cdf(-d1) + K * math.exp(-r2 * T) * norm.cdf(-d2) - MarketPrice

    return result


def BSmodelImpiedVol(K, r1, r2, S, T, flag, MarketPrice):
    return opt.fsolve(BSmodel, [0], (K, r1, r2, S, T, flag, MarketPrice))


def volGenerator(t, k):
    return 1 / (t ** 2 + k ** 2) * k * t


impliedVolatility = BSmodelImpiedVol(K=1.2868, r1=-0.001129501, r2=0.00439209668, S=1.278, T=0.52811, flag=1,
                                     MarketPrice=0.074)

print impliedVolatility

strike = [1.1, 1.105, 1.1, 1.2, 1.21]
t = [1 / 365.0, 7 / 365.0, 14 / 365.0, 1 / 12.0, 1 / 4.0, 1 / 2.0, 1.]

t0, k0 = np.meshgrid(t, strike)
sigma0 = volGenerator(t0, k0)
print sigma0
sigmaCubic = Interpolation.interp2d(t, strike, sigma0, kind='cubic')
print sigmaCubic(1. / 12, 1.1)
