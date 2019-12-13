from referencer import main

import os

source_directory = "/home/vagrant/shared/source-tiles/google-map-east-kalimantan"
target_directory = "/home/vagrant/shared/geoserver_data/data/world/google-map-east-kalimantan"

start_level = 0
end_level = 15

# reverse folder number (larger number = finer or larger number = more rough)
reverse_order = True

if not os.path.isdir(target_directory):
    os.makedirs(target_directory)

for level in range(start_level, end_level+1):

    target_level = str(level - start_level)

    if (reverse_order):
        target_level = str(end_level - level)
    
    target_level_dir = target_directory + "/" + target_level
    source_level_dir = source_directory + "/" + str(level)

    if not os.path.isdir(target_level_dir):
        os.makedirs(target_level_dir)

    fileList = os.listdir(source_level_dir)

    fileNumber = len(fileList)

    for i, f in enumerate(fileList, start=1):

        slices = f.split(".")[0].split("_")

        x = slices[0]
        y = slices[1]

        source_file = source_level_dir + "/" + f

        if (os.path.isfile(source_file)):
            print("process " + x + ", " + y + ", " + str(level) + " ==> " + str(i) + "/" + str(fileNumber))
            main.georeference (int(x), int(y), level, source_file, target_level_dir + "/" + x + "_" + y + ".tiff")
