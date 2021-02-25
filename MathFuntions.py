import io, os, Commands
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

async def Intconversion(X1, X2, Y1, Y2):
    convert = []
    try:
        X1con = int(X1.content)
        Y1con = int(Y1.content)
        X2con = int(X2.content)
        Y2con = int(Y2.content)
    except ValueError:
        print("int was a str")
    X = [X1con, X2con]
    Y = [Y1con, Y2con]
    answer = linregress(X, Y)
    slope = answer.slope
    convert.append({"slope": slope})
    return convert