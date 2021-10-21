import numpy as np

DEG_PER_RAD = 180/np.pi
RAD_PER_DEG = np.pi/180

def project_Mercator(latitude, radius):
    return radius * np.log(np.tan(latitude/2 * RAD_PER_DEG + np.pi/4))


def inverse_Mercator(y, radius):
     return (2 * np.arctan(np.exp(y / radius)) - np.pi/2) * DEG_PER_RAD


def make_rhumb_line(origin, destination, step=0.1, offset=20):
    xmin = min(destination[0], origin[0]) - offset
    xmax = max(destination[0], origin[0]) + offset
    lons = np.arange(xmin, xmax, step)
    # Mercator coordinates
    R = 360 / (2 * np.pi) 
    yDest = project_Mercator(destination[1], R)
    yOrig = project_Mercator(origin[1], R)
    grad = (yDest - yOrig)/(destination[0] - origin[0])
    y0 = yDest - grad * destination[0]
    y = grad * lons + y0
    # PlateCarre coordinates
    lats = inverse_Mercator(y, R)
    return lons, lats


def distance_rhumb_line(origin, destination, radius):
    R = 360 / (2 * np.pi) 
    yDest = project_Mercator(destination[1], R)
    yOrig = project_Mercator(origin[1], R)
    grad = (yDest - yOrig)/(destination[0] - origin[0])
    beta = np.arctan(1/grad)
    return radius * abs((destination[1] - origin[1]) /DEG_PER_RAD * (1/np.cos(beta)))
