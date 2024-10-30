import fit_black_box as bb
import numpy as np

def cos2x (a, x, b):
    return a * np.cos(x) ** 2 + b

def cosx (a, x, b):
    return a * np.cos(x) + b

filename = 'exercise_data_2/processed/cosx.txt'
x, y, xerr, yerr = bb.load_data(filename)


init_guess = (1, 1)
font_size = 20
xlabel = "Theta [θ]"
ylabel = "Light Intensity [V]"
title = "Cos^2(θ) Relationship between Intensity [V] and Angle [θ]"


bb.plot_fit(cosx, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
            xlabel=xlabel, ylabel=ylabel)
