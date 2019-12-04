import subprocess

# Google uses EPSG:3857
MIN_LAT = -85.06
MAX_LAT = 85.06
MIN_LON = -180
MAX_LON = 180

def georeference (x, y, z, inputFile, outputFile):

    tiles_num = 2**z

    lat_interval = (MAX_LAT - MIN_LAT) / tiles_num
    lon_interval = (MAX_LON - MIN_LON) / tiles_num

    ul_latitude = MAX_LAT - y * lat_interval
    ul_longitude = MIN_LON + x * lon_interval

    lr_latitude = ul_latitude - lat_interval
    lr_longitude = ul_longitude + lon_interval

    translator_exec = "gdal_translate"
    proc = subprocess.run(
        [translator_exec, "-of", "GTiff", "-a_ullr", ul_longitude, ul_latitude, lr_longitude, lr_latitude, "-a_srs", "EPSG:4326", inputFile, outputFile],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
        )
    return proc.returncode