import subprocess
import math

# Google uses EPSG:3857
MIN_LAT = -85.06
MAX_LAT = 85.06
MIN_LON = -180
MAX_LON = 180

def num2deg(x, y, level):

  n = 2 ** level

  lon_deg = x / n * 360.0 - 180.0

  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
  lat_deg = math.degrees(lat_rad)

  return (lat_deg, lon_deg)

def georeference (x, y, z, inputFile, outputFile):

    ul_latitude, ul_longitude = num2deg(x, y, z)

    lr_latitude, lr_longitude = num2deg(x+1, y+1, z)

    translator_exec = "gdal_translate"
    proc = subprocess.run(
        [translator_exec, "-of", "GTiff", "-co", "compress=lzw", "-co", "predictor=2", "-a_ullr", str(ul_longitude), str(ul_latitude), str(lr_longitude), str(lr_latitude), "-a_srs", "EPSG:4326", inputFile, outputFile],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    return proc.returncode