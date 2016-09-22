# !/usr/bin/env python
# -*- coding:utf-8 -*-
import math

import sympy

__author__ = 'frm.kpmg'


sympy.init_printing()
u_max, u_star, rho_max, rho_star, A, B = sympy.symbols('u_max u_star rho_max rho_star A B')
eq1 = sympy.Eq( 0, u_max*rho_max*(1 - A*rho_max-B*rho_max**2) )
eq2 = sympy.Eq( 0, u_max*(1 - 2*A*rho_star-3*B*rho_star**2) )
eq3 = sympy.Eq( u_star, u_max*(1 - A*rho_star - B*rho_star**2) )
print eq1
print eq2
print eq3
print eq2-3*eq3
#
x,y=sympy.symbols('x,y')
print sympy.solve('x**2+2*x+1')
print sympy.solve('x**2+2*x')
print sympy.solve('x**2+2*x+3')
print sympy.solve(x**4-1,x)
print sympy.solve([x+5*y-2,-3*x+6*y-15],[x,y])
#
# # x,y,z=sympy.symbols('xyz')
# print sympy.Rational(1,2)
# print sympy.Rational(2)**50/sympy.Rational(10)**50
#
# print sympy.pi**2
# print (sympy.pi**2).evalf()
#
# #分数
#
# print 1/( (x+2)*(x+1) )
# print sympy.apart(1/( (x+2)*(x+1) ),x)
# x,y,z=sympy.symbols('x,y,z')
# print sympy.together(1/x+1/y+1/z)
#
# #limit 微分 ,积分
#
#
# print sympy.limit(x**x,x,0)
# print sympy.limit(x**2,x,0)
#
# print sympy.diff(sympy.sin(x),x)
# print sympy.diff(sympy.sin(2*x),x)
#
# #高阶
#
# print sympy.diff(sympy.sin(2*x),x)
# print sympy.diff(sympy.sin(2*x),x,2)
# print sympy.diff(sympy.sin(2*x),x,3)
#
#
# print (1/sympy.cos(x)).series(x,0,10)
# sympy.pprint((1/sympy.cos(x)).series(x,0,10))
#
#
# print  sympy.integrate(x*sympy.sin(x),x)
# print sympy.integrate(sympy.sin(x),(x,0,sympy.pi/2))
# print sympy.integrate(sympy.exp(-x),(x,0,sympy.oo))
#
# print sympy.integrate(sympy.exp(x),(x,0,sympy.oo))
#
# print sympy.sin(sympy.I*x)
#
# #matrix
#
A=sympy.Matrix([[1,x],[y,1]])
print A
sympy.pprint(A)
print A**2
sympy.pprint(A**2)
print sympy.printing.python(A**2)
print sympy.printing.latex(A**2)
# sympy.preview(A**2)