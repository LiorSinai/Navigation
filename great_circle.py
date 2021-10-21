import numpy as np

DEG_PER_RAD = 180/np.pi
RADIUS_EARTH = 6371

def spherical_to_cartesian(longitude, latitude):
    latitude /= DEG_PER_RAD
    longitude /= DEG_PER_RAD
    x = np.cos(latitude) * np.cos(longitude)
    y = np.cos(latitude) * np.sin(longitude)
    z = np.sin(latitude)
    return np.array([x, y, z])[:, np.newaxis].reshape(3, -1)


def cartesian_to_spherical(points):
    latitudes = np.arcsin(points[2, :]) * DEG_PER_RAD
    longitudes = np.arctan2(points[1, :], points[0, :]) * DEG_PER_RAD
    return longitudes, latitudes


def make_great_cicle(origin, destination, step=0.01, full_cirlce=False):
    vOrigin = spherical_to_cartesian(origin[0], origin[1])
    vDest   = spherical_to_cartesian(destination[0], destination[1])

    cosAlpha = np.sum(vOrigin * vDest)
    sinAlpha = np.sqrt(1 - cosAlpha * cosAlpha)
    xUnit = vOrigin / np.sqrt(np.sum(vOrigin ** 2))
    yUnit = (vDest - cosAlpha * xUnit) /sinAlpha

    alpha = np.arccos(cosAlpha)
    if full_cirlce:
        # y = cos(latitude) * sin(-pi) = 0 = cos(a0) * xUnit[1] + sin(a0) * yUnit[1]
        a0 = np.arctan(-xUnit[1]/yUnit[1]) #-np.pi # ? How to know when need Pi offset?
        a1 = a0 + 2 * np.pi
    else:
        a0 = min(0, alpha)
        a1 = max(0, alpha)
    angles = np.arange(a0, a1, step)
    points = np.cos(angles) * xUnit + np.sin(angles) * yUnit
    lons, lats = cartesian_to_spherical(points)
    if full_cirlce: # hack to fix pi offset issue
        idx = np.argmin(lons)
        lons = np.concatenate([lons[idx + 1:], lons[:idx]])
        lats = np.concatenate([lats[idx + 1:], lats[:idx]])
    return lons, lats


def distance_great_circle(origin, destination, radius):
    vOrigin = spherical_to_cartesian(origin[0], origin[1])
    vDest   = spherical_to_cartesian(destination[0], destination[1])
    cosAlpha = np.sum(vOrigin * vDest)
    alpha = np.arccos(cosAlpha)
    return radius * alpha
    