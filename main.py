import glob
from Detect import detect_people

# loop through the folder with images
for file_name in glob.iglob('images/*', recursive=True):
    detect_people(file_name)
