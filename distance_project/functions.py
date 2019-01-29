from math import sin, cos
from numpy import deg2rad
from numpy import sqrt

R = 6371

def lat_lon_to_xyz(lat, lon):
    lat = deg2rad(lat)
    lon = deg2rad(lon)
    x = R * cos(lat) * cos(lon)
    y = R * cos(lat) * sin(lon)
    z = R *sin(lat)    
    return x, y, z


def tokyo():

    lat_deg = 35.652832
    lon_deg = 139.839478
    
    latr = deg2rad(lat_deg)
    lonr = deg2rad(lon_deg)
    
    
    print(latr, lonr)
    print(lat_lon_to_xyz(latr, lonr))
    
def sydney():

    lat_deg = -33.865143
    lon_deg = 151.209900
    
    latr = deg2rad(lat_deg)
    lonr = deg2rad(lon_deg)
    
    
    print(latr, lonr)
    print(lat_lon_to_xyz(latr, lonr))


# tokyo()
# sydney()

def distance(x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return sqrt(dx ** 2 + dy ** 2 + dz ** 2)