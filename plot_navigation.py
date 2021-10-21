import matplotlib.pyplot as plt
from matplotlib.image import imread, imsave
from matplotlib.colors import hsv_to_rgb, rgb_to_hsv
import numpy as np

import cartopy.crs as ccrs

from rhumb_lines import make_rhumb_line, distance_rhumb_line
from great_circle import make_great_cicle, distance_great_circle, spherical_to_cartesian

DEG_PER_RAD = 180/np.pi
RADIUS_EARTH = 6371


def edit_image(fname, saturation=0.5, lighten=-40):
    img = imread(fname) 
    img_hsv = rgb_to_hsv(img)
    img_hsv[:, :, 1] *= (1 + saturation)
    img_hsv[:, :, 1] = np.where(img_hsv[:, :, 1] > 1, 1, img_hsv[:, :, 1])
    img_hsv[:, :, 2] += lighten
    img_hsv[:, :, 2] = np.where(img_hsv[:, :, 2] > 255, 255, img_hsv[:, :, 2])
    img_hsv[:, :, 2] = np.where(img_hsv[:, :, 2] < 0, 0, img_hsv[:, :, 2])
    imgout = np.uint8(hsv_to_rgb(img_hsv))
    imsave("NE2_50M_SR_W/NE2_50M_SR_W_edit.png", imgout)


def plot_background(ax, fname):
    source_proj = ccrs.PlateCarree()

    img = imread(fname)  
    
    return ax.imshow(
        img, 
        origin='upper', 
        transform=source_proj, 
        extent=[-180, 180, -90, 90], 
        )


def approx_distance(longitudes, latitudes, radius):
    p = spherical_to_cartesian(longitudes, latitudes)
    pDelta = p[:,  1:] - p[:, :-1]
    return np.sum(np.sqrt(np.sum(pDelta * pDelta, axis=0))) * radius


def plot_navigation(origin, destination):
    fig = plt.figure(figsize=(20, 10))

    lon0 = (origin[0] + destination[0] ) /2
    lat0 = (origin[1] + destination[1] ) /2
    lat0 = 0
    #source_proj = ccrs.Orthographic(central_longitude=lon0, central_latitude=lat0)
    source_proj = ccrs.Mercator()
    ax = fig.add_subplot(1, 1, 1, projection=source_proj)
    
    ax.set_global()
    plot_background(ax, "NE2_50M_SR_W/NE2_50M_SR_W_edit.png")
    xlocs = np.arange(-180, 180, 15)
    ylocs = np.arange(-180, 180, 15)
    ax.gridlines(
        crs=ccrs.PlateCarree(), 
        draw_labels=False, 
        linewidth=1, 
        color='w', 
        alpha=0.5, 
        linestyle='-', 
        xlocs=xlocs,
        ylocs=ylocs
        )
    #ax.stock_img()
    #ax.coastlines()

    ax.plot(origin[0], origin[1], 'ok', transform=ccrs.PlateCarree())
    ax.plot(destination[0], destination[1], 'ok', transform=ccrs.PlateCarree())
    #ax.plot([destination[0], origin[0]], [destination[1], origin[1]], transform=ccrs.PlateCarree(), c='red') #stragiht line on a PlateCaree, not physically useful
    
    lons, lats = make_great_cicle(origin, destination, step=0.01, full_cirlce=True)
    ax.plot(lons, lats, transform=ccrs.PlateCarree(), color='#b0bcff', linewidth=3)

    lons, lats = make_rhumb_line(origin, destination, step=0.01, offset=20)
    ax.plot(lons, lats, transform=ccrs.PlateCarree(), color='r', linewidth=3)

    plt.savefig("nav.png", bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    CapeTown = [18.42, -33.92] # longitude, latitude
    NewYork = [-74.00, 40.71]
    HongKong = [114.17, 22.32]
    Amsterdam = [4.90, 52.37]

    origin = NewYork
    destination = CapeTown

    lons, lats = make_rhumb_line(origin, destination, step=0.01, offset=0)
    dis_rhumb = approx_distance(lons, lats, RADIUS_EARTH)
    print("Approximate distance Rhumb Line:        {:.3f}".format(dis_rhumb))
    dis_rhumb = distance_rhumb_line(origin, destination, RADIUS_EARTH)
    print("Exact distance Rhumb Line:              {:.3f}".format(dis_rhumb))

    lons, lats = make_great_cicle(origin, destination, step=0.01, full_cirlce=False)
    dis_circle = approx_distance(lons, lats, RADIUS_EARTH)
    print("Approximate distance great circle Line: {:.3f}".format(dis_circle))
    dis_circle = distance_great_circle(origin, destination, RADIUS_EARTH)
    print("Exact distance great circle Line:       {:.3f}".format(dis_circle))

    plot_navigation(origin, destination)
