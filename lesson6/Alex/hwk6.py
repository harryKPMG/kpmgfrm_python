#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scipy.stats import norm
from math import log, sqrt, exp
import scipy.optimize as opt

__author__ = 'alexyli1'

# r,t,k,s,pv
r=0.05
t=0.25
k=2.50
s=2.45
pv=0.1133

def call_option_pricer(sigma,s, k, t, r, pv):
    d1 = (log(s/k) + (r + 0.5 * sigma *sigma) * t) / sigma / sqrt(t)
    d2 = d1 -sigma * sqrt(t)
    return s * norm.cdf(d1) - k * exp(-r*t) * norm.cdf(d2)-pv

result = opt.fsolve(call_option_pricer,[1.0],(s,k,t,r,pv))
a= (k,t,result)
print a


