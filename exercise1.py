import fit_black_box as bb
import numpy as np

def cosx(a, k, x, b):
    return a * np.cos(k * x) + b

filename = 'exercise_data_1/processed/cosx.txt'
x, y, xerr, yerr = bb.load_data(filename)


init_guess = (np.max(y), np.pi, np.mean(y))
print(init_guess)
font_size = 20
xlabel = "Theta [θ]"
ylabel = "Light Intensity [V]"
title = "Cos(θ) Relationship between Intensity [V] and Angle [θ]"



bb.plot_fit(cosx, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
            xlabel=xlabel, ylabel=ylabel)


