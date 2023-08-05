# stdlib imports
import json
import pathlib
import warnings

# third party imports
import matplotlib.pyplot as plt
import numpy as np
from geopy.distance import distance as geodetic
from pyproj import Proj
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiPolygon,
    Point,
    Polygon,
    shape,
)
from shapely.ops import split, transform

TECTONIC_REGIONS = {
    "stable": "DistanceToStable",
    "active": "DistanceToActive",
    "volcanic": "DistanceToHotSpot",
    "subduction": "DistanceToSubduction",
    "ocean": "DistanceToOceanic",
}


def get_distance_to_shape(cutshape, clat, clon, projection):
    """Calculate distance to input geometry from lat/lon in given projection.

    Args:
        cutshape (shapely Geometry): Shape (usually Polygon) to calculate distance to.
        clat (float): Earthquake latitude.
        clon (float): Earthquake longitude.
        projection (Proj): Proj4 class defining an input projection.
    Returns:
        float: Distance in km from shape to lat/lon.
    """
    x, y = projection(clon, clat)
    utmpoint = Point(x, y)
    utmshape = transform(projection, cutshape)
    # the authors are aware that some of these distance calculations will return invalid
    # values, so we're suppressing the warnings to that effect.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        distance = utmshape.distance(utmpoint) / 1000
    return distance


def get_min_distance(geometry, clat, clon):
    """Calculate minimum distance to input (world-spanning) geometry from lat/lon.

    Args:
        geometry (shapely Geometry): Complex world-spanning geometry to calculate
                                     distance to.
        clat (float): Earthquake latitude.
        clon (float): Earthquake longitude.
    Returns:
        float: Distance in km from geometry to lat/lon.
    """
    # geometry is some kind of shapely geometry
    mindist = 1e9
    hemis = ["+south", ""]
    for j, xmin in enumerate(range(-180, 180, 6)):
        xmax = xmin + 6
        zone = j + 1
        for i, ymin in enumerate([-90, 0]):
            ymax = ymin + 90
            pstr = f"+proj=utm +zone={zone} +ellps=WGS84 {hemis[i]}"
            utm_proj = Proj(pstr)
            utm_box = Polygon(
                [(xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin), (xmin, ymax)]
            )
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                cutshape = geometry.intersection(utm_box)
            if isinstance(cutshape, (Polygon, MultiPolygon)):
                distance = get_distance_to_shape(cutshape, clat, clon, utm_proj)
            elif isinstance(cutshape, GeometryCollection):
                distance = 1e9
                for polygon in cutshape.geoms:
                    tdistance = get_distance_to_shape(cutshape, clat, clon, utm_proj)
                    if tdistance < distance:
                        distance = tdistance
            if distance < mindist:
                mindist = distance

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                iscontained = cutshape.contains(Point(clon, clat))
            # occasionally the projected point will fall out of the projected polygon
            # this is a sanity check in lat/lon space to catch those errors
            if iscontained:
                mindist = 0.0

    return mindist


def calc_distances(lat, lon):
    """Calculate distances from input lat/lon to nearest tectonic regime polygons.

    Args:
        lat (float): Earthquake latitude.
        lon (float): Earthquake longitude.
    Returns:
        dict: Dictionary of distances in km:
              - DistanceToActive
              - DistanceToStable
              - DistanceToSubduction
              - DistanceToHotSpot
              - DistanceToOceanic
              - DistanceToContinental
    """
    root = pathlib.Path(__file__).parent / "data"
    bigfiles = ["active", "stable"]
    distances = {}
    for tfile in bigfiles:
        mindist = 1e9
        datafile = root / f"{tfile}.geojson"
        with open(datafile, "rt") as f:
            jdict = json.load(f)
        for i, feature in enumerate(jdict["features"]):
            geometry = shape(feature["geometry"])
            distance = get_min_distance(geometry, lat, lon)
            if distance < mindist:
                mindist = distance
        distances[tfile] = mindist

    smallfiles = ["subduction", "volcanic"]
    ortho_proj = Proj(f"+proj=ortho +lon_0={lon:.6f} +lat_0={lat:.6f} +ellps=WGS84")
    for tfile in smallfiles:
        mindist = 1e9
        datafile = root / f"{tfile}.geojson"
        with open(datafile, "rt") as f:
            jdict = json.load(f)
        for feature in jdict["features"]:
            geometry = shape(feature["geometry"])
            cx, cy = geometry.centroid.xy
            cdist = geodetic((lat, lon), (cy[0], cx[0])).km
            if cdist > 3000:
                continue
            dist = get_distance_to_shape(geometry, lat, lon, ortho_proj)
            if dist < mindist:
                mindist = dist

        distances[tfile] = mindist

    for oldkey, newkey in TECTONIC_REGIONS.items():
        if oldkey not in distances:
            continue
        distances[newkey] = distances[oldkey]
        del distances[oldkey]

    # figure out if point is inside ocean polygon
    datafile = root / "ocean.geojson"
    with open(datafile, "rt") as f:
        jdict = json.load(f)

    distances["DistanceToOceanic"] = 9999999
    distances["DistanceToContinental"] = 9999999
    distances
    for feature in jdict["features"]:
        geometry = shape(feature["geometry"])
        if geometry.contains(Point(lon, lat)):
            distances["DistanceToOceanic"] = 0.0
            break

    if distances["DistanceToOceanic"] > 0:
        # we're over land, we need distance to ocean
        distances["DistanceToContinental"] = 0.0
        mindist = 1e9
        for feature in jdict["features"]:
            ocean = shape(feature["geometry"])
            distance = get_min_distance(ocean, lat, lon)
            # trap for 0 distances, why is this happening?
            if distance < mindist and distance > 0:
                mindist = distance
        distances["DistanceToOceanic"] = mindist
    else:  # we're over ocean, we need distance to land
        world_vertices = [(-180, 90), (180, 90), (180, -90), (-180, -90), (-180, 90)]
        world_polygon = Polygon(world_vertices)
        mindist = 1e9
        for feature in jdict["features"]:
            ocean = shape(feature["geometry"])
            land = world_polygon.difference(ocean)
            distance = get_min_distance(land, lat, lon)
            # trap for 0 distances, why is this happening?
            if distance < mindist and distance > 0:
                mindist = distance
        distances["DistanceToContinental"] = mindist
    return distances
