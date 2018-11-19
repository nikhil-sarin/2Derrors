import numpy as np

def model(x, m, c, **kwargs):

    y = m*x + c

    return y

def make_data(points, m , c, xerr, yerr, seed):
    np.random.seed(int(seed))
    x_true = np.linspace(10,100,points)
    y_true = model(x = x_true, m = m, c = c)

    xerr = xerr * np.random.randn(points)
    yerr = yerr * np.random.randn(points)
    x_obs = x_true + xerr
    y_obs = y_true + yerr
    np.savetxt('data.txt', X=[x_obs, y_obs, xerr, yerr])

    return None

make_data(points = 100, m = 5, c = 2, xerr = 3, yerr = 5, seed = 123)