# !/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import pandas as pd
import numpy as np
from scipy.optimize import fsolve
from scipy.stats import norm
from scipy import interpolate

__author__ = 'harry'


# BS公式
def bs_price(r, t, k, s, sigma):
    '''
    BS公式
    :param r:连续复利计无风险利率
    :param t:期权有效期
    :param k:期权执行价格
    :param s:金融资产现价
    :param sigma:波动率
    :return:price: 期权价格
    '''
    d1 = float(math.log(s / k) + (r + 0.5 * (sigma ** 2)) * t) / (sigma * math.sqrt(t))
    d2 = float(d1 - sigma * math.sqrt(t))
    price = float(s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2))
    return price


# 求解波动率
def im_volatility(r, t, k, s, pv, sig1, precision):
    '''
    求解波动率
    :param r: 连续复利计无风险利率
    :param t: 期权有效期
    :param k: 期权执行价格
    :param s: 金融资产现价
    :param pv: 期权价格
    :param sig1: 初始参数
    :param precision: 计算精度
    :return: (k,t,sigma_f：求解出的波动率)
    '''

    def f(sig):
        return bs_price(r, t, k, s, sig) - pv

    sigma_f = fsolve(f, sig1, xtol=precision)[0]
    x = (k, t, sigma_f)
    return x


if __name__ == '__main__':
    r = 0.1
    t = 0.5
    k = 40
    s = 42
    pv = 4.76
    result = im_volatility(r, t, k, s, pv, 0.1, 1e-10)
    print "k0为 %.2f,t0为 %.2f时,求解出的波动率为: %f" % (result[:])

    # 插值
    k0 = 6.3
    t0 = 1.3
    sigma = pd.read_csv('sigma.csv')
    ts = sigma['yearfrac']
    sigmas = sigma['sigma']

    # 线性插值
    f = interpolate.interp1d(ts, sigmas)
    interSig1 = f(t0)
    print "线性插值结果为: %f" % interSig1

    # cubic插值
    curve = interpolate.splrep(ts, sigmas)
    interSig2 = interpolate.splev(t0, curve)
    print "Cubic插值结果为：%f" % interSig2
