from referencer import main

import os

source_directory = "./data/source"
target_directory = "./data/target"

start_level = 0
end_level = 3

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

    max = 2**level

    for x in range(0, max):
        for y in range(0, max):

            source_file = source_level_dir + "/" + str(x) + "_" + str(y) + ".jpg"

            if (os.path.isfile(source_file)):
                print("process " + str(x) + ", " + str(y) + ", " + str(level))
                main.georeference (x, y, level, source_file, target_level_dir + "/" + str(x) + "_" + str(y) + ".tiff")