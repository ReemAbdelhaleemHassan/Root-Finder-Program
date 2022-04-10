import math
import numpy as np
from math import sin, cos, tan, e
from sympy.parsing.sympy_parser import parse_expr
from sympy import *


def bisection(expr, x_lower, x_upper, list, es, max_iterations):
    k=math.ceil(math.log2(abs((x_upper-x_lower)/(es))))
    print(k)
    f = lambda x: eval(expr)
    if f(x_lower) * f(x_upper) > 0:
        print('No Bracket')
        return None, k
    xr_list = np.array([])
    for i in range(1, 1 + int(max_iterations)):
        xr = (x_lower + x_upper) / 2
        xr_list = np.append(xr_list, xr)  # compute the midpoint
        if f(x_lower) * f(xr) < 0: #root lies in the lower subinterval so xu = xr
            x_upper = xr
        elif f(x_upper) * f(xr) < 0: #root lies in the upper subinterval so xl = xr
            x_lower = xr
        elif f(xr) == 0:
            print("Found exact Root.")
            return xr
        else:
            print("Bisection method fails.")
            return
        if i > 1 and xr_list[i-1] != 0:
            ea = abs((xr_list[i - 1] - xr_list[i - 2]) / xr_list[i - 1])  # approxate relative error
            if ea < es:
                break
        # print(i, xr)
        list.insert('', 'end', text=str(i), values=(str(i), str(x_lower), str(x_upper), str(xr), str(f(xr))))
    return xr, k


# def bisection_lec(expr, x_lower, x_upper, list, es, max_iterations):
#     f = lambda x: eval(expr)
#     if f(x_lower) * f(x_upper) > 0:
#         print('No Bracket')
#         return None
#     for i in range(max_iterations):
#         xr = (x_lower + x_upper) / 2
#
#         test = f(x_lower) * f(xr)  # compute f(xl)* xr
#         if test < 0:
#             xu = xr
#         else:
#             xl = xr
#         # ea = abs((x_upper-x_lower)/x_lower)
#         # if test == 0:
#         #   ea=0
#         # if ea<es:
#         #   break
#         print(i, xr)
#         list.insert('', 'end', text=str(i+1), values=(str(i+1), str(x_lower), str(x_upper), str(xr), str(f(xr))))
#     return xr


def false_position(expr, x_lower, x_upper, list, es, maxit): #same as bisection but different calculation for xr
    f = lambda x: eval(expr)
    if f(x_lower) * f(x_upper) > 0:
        print('No Bracket')
        return
    x_old = 0
    maxit = int(maxit)
    for i in range(1, maxit):
        if (f(x_upper) - f(x_lower)) == 0:
            print('Error dividing by zero')
            return
        xr = (x_lower * f(x_upper) - x_upper * f(x_lower)) / (f(x_upper) - f(x_lower))
        if f(xr) == 0:
            print('Exact Zero Found')
        elif f(xr) * f(x_lower) < 0:
            x_upper = xr
        else:
            x_lower = xr
        if i > 1 and (abs((xr - xr_old)/xr) < es):
            print('False position method has converged')
            break
        iter = i
        xr_old = xr
        # print(i, xr)
        list.insert('', 'end', text=str(i), values=(str(i), str(x_lower), str(x_upper), str(xr), str(f(xr))))
    if iter >= maxit:
        print('zero not found to desired tolerance')
    return xr


def check_converge(g,x0):
    x = symbols('x')
    f = lambda x: eval(g)
    temp = Derivative(g, x).doit()
    df = lambda x: eval(str(temp))
    res = ''
    j=0
    if abs(df(x0))<1 and df(x0)>0:
        res = 'Monotonic Converge'
    elif abs(df(x0))<1 and df(x0)<0:
        res = 'Oscillate Converge'
    elif abs(df(x0))>1 and df(x0)<0:
        res = 'Monotonic Diverge'
        j=1
    else:
        res = 'Oscillate Diverge'
        j=1
    return res, j


def fixed_point(expr, x0, list, es, iter_max):
    res, j = check_converge(expr, x0)
    if j ==1 :
        return None, res
    iter_max = int(iter_max)
    f = lambda x: eval(expr)

    xr = x0
    xr_old = 0
    iter = 0
    i=0
    while True:
        i = i + 1
        xr_old = xr
        xr = f(xr_old)
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        iter = iter + 1
        # print(xr)
        list.insert('', 'end', text=str(i), values=(str(i), str(xr_old), str(xr), str(f(xr))))
        if (ea < es and iter < iter_max):
            break

    return xr, res


def newton_raphson(expr, initial_guess, list, epsilon, max_itr):
    max_itr = int(max_itr)
    x_old = initial_guess
    x = symbols('x')
    f = lambda x: eval(expr)
    temp = Derivative(expr, x).doit()
    df = lambda x: eval(str(temp))

    for i in range(max_itr):
        if f(x_old) == 0:
            print('Error dividing by zero')
            return
        x_new = x_old - (f(x_old) / df(x_old))
        # print(f"{i + 1}  {x_new}")

        # check the tolerance
        if x_new != 0:
            err = abs((x_old - x_new) / x_new)
            if err <= epsilon:
                # print("-------------------------------------------------------------------------")
                # print(f"Root {x_new} with Error = {err} ")
                # print("-------------------------------------------------------------------------")
                break
            else:
                x_old = x_new
        list.insert('', 'end', text=str(i), values=(str(i), str(x_new), str(f(x_new))))
    # max_itreation has reached
    # if i == max_itr - 1:
        # print("-------------------------------------------------------------------------")
        # print(f"{max_itr} has reached")
        # print(f"The last value computed is {x_new} with Error = {err}")
    return x_new


def secant(expr, x1, x2, list, epsilon, max_itr):
    max_itr = int(max_itr)
    f = lambda x: eval(expr)
    for i in range(max_itr):
        if (f(x1) - f(x2)) == 0:
            print('Error dividing by zero')
            return
        x3 = x2 - (f(x2) * (x1 - x2)) / (f(x1) - f(x2))

        err = abs((x3 - x2) / x3)
        if err <= epsilon:
            # print("-------------------------------------------------------------------------")
            # print(f"Root {x3} with Error = {err} ")
            # print("-------------------------------------------------------------------------")
            break
        else:
            x1 = x2
            x2 = x3
        list.insert('', 'end', text=str(i), values=(str(i), str(x1), str(x2), str(x3), str(f(x3))))
    # if i == max_itr - 1:
        # print("-------------------------------------------------------------------------")
        # print(f"{max_itr} has end reached")
        # print(f"The last value computed is {x3} with Error = {err}")

    return x3
