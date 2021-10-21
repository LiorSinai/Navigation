# Navigation plots

Plot rhumb lines (lines of constant bearing) and great circle arcs (lines of shortest distance) between two points on the earth. This uses [Cartopy](https://scitools.org.uk/cartopy/docs/latest/gallery/index.html).
The image of earth is based on [Natural Earth II](https://www.naturalearthdata.com/downloads/10m-raster-data/10m-natural-earth-2/).
A low resolution image is also included in this repository from [https://map-projections.net/single-view/rectang-0](https://map-projections.net/single-view/rectang-0).


### New York to Cape Town:
<div style="display:flex; justify-content:space-around; ">
    <img src ="images/NY_CT_MercatorNE.png" width="60%"> 
    <img src ="images/NY_CT_orthoNE.png" width="40%" height="40%"  style="margin:auto">
</div>

### Amsterdam to Hong Kong:
<div style="display:flex; justify-content:space-around;" >
    <img src ="images/AMS_HKG_MercatorNE.png" width="60%"> 
    <img src ="images/AMS_HKG_orthoNE.png" width="40%" height="40%" style="margin:auto">
</div>

# Rhumb lines

Rhumb lines are straight lines on a Mercator map. The exterme points can be found using the Mercator projection equation:

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;R\:ln\left|tan&space;\left(\frac{\pi}{4}&space;&plus;&space;\frac{\phi}{2}&space;\right&space;)&space;\right|" title="y = R\:ln\left|tan \left(\frac{\pi}{4} + \frac{\phi}{2} \right ) \right|" />

Other points can be found on the straight line:

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;mx&space;&plus;&space;y_0" title="y = mx + y_0" /></a>

Solving for &phi; gives the latitudes for Plate Carree co-ordinates:

<img src="https://latex.codecogs.com/gif.latex?\phi&space;=&space;2arctan(e^{y/R})&space;-&space;\frac{\pi}{2}" title="\phi = 2arctan(e^{y/R}) - \frac{\pi}{2}" />


# Great circles
<img src ="images/GreatCircle.png" width="40%"> 

It's easiest to convert the spherical co-ordinates to Cartesian co-ordinates. 
A co-ordinate system is defined on the plane with the unit vectors (x&#770;,y&#770;).
x&#770; is defined as:

<img src="https://latex.codecogs.com/gif.latex?\hat{x}&space;=&space;\frac{\overleftarrow{p_1}}{|\overleftarrow{p_1}|}" title="\hat{x} = \frac{\overleftarrow{p_1}}{|\overleftarrow{p_1}|}" />

Using Euclidean geomtry, y&#770; is found with:

<img src="https://latex.codecogs.com/gif.latex?\overleftarrow{p_2}&space;=&space;cos(\alpha)\hat{x}&space;&plus;&space;sin(\alpha)\hat{y}" title="\overleftarrow{p_2} = cos(\alpha)\hat{x} + sin(\alpha)\hat{y}" />

Where &alpha; is found using the dot product:

<img src="https://latex.codecogs.com/gif.latex?cos(\alpha)&space;=&space;\overleftarrow{p_1}&space;\cdot&space;\overleftarrow{p_2}&space;=&space;x_{p_1}x_{p_2}&space;&plus;&space;y_{p_1}y_{p_2}&space;&plus;&space;z_{p_1}z_{p_2}" title="cos(\alpha) = \overleftarrow{p_1} \cdot \overleftarrow{p_2} = x_{p_1}x_{p_2} + y_{p_1}y_{p_2} + z_{p_1}z_{p_2}" />

A general point on the circle is given by:

<img src="https://latex.codecogs.com/gif.latex?\overleftarrow{p}&space;=&space;cos(\theta)\hat{x}&space;&plus;&space;sin(\theta)\hat{y}" title="\overleftarrow{p} = cos(\theta)\hat{x} + sin(\theta)\hat{y}" /></a>

