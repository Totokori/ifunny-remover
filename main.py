import time
from PIL import Image
from exif import Image as img
import glob, os

while(True):
    # gets all the .jpg files into a group
    for infile in glob.glob('*.jpg'):
        #opens readble file to check whether it has a tag
        with open(infile, 'rb') as img_file:
            image = img(img_file)
        if not(image.has_exif and image.user_comment == 'True'):
            # Crops the image
            input = Image.open(infile)
            width, height = input.size
            output = input.crop((0, 0, width, (height - 20)))

            # Could be moved into another directory
            # if not os.path.exists('output'):
            #     os.makedirs('output')
            output.save(infile)
            
            # Adds the tag so that it doesn't get cropped again
            with open(infile, 'rb') as img_file:
                image = img(img_file)
            image.set('user_comment', 'True')
            with open(infile,'wb') as new_img_file:
                new_img_file.write(image.get_file())
        else:
            # Skips over file if tag is found
            continue
        #Continues in the background so you can keep scrolling through iFunny
    time.sleep(120)