import os

import pytesseract as pyt
# import pdf2image
import cv2 #OpenCV library for python
import numpy as np
from PIL import Image
from pdf2image import convert_from_path

# folders to OCR
to_OCR_folders = os.listdir("dir_t1")

#gets the treaties from a given parent directory
def get_treaties_from_dir(dir):
    # iterate through each folder
    for folder in os.walk(dir):
        #iterate through each treaty
        for volume in folder:
            # iterate through each page
            for treaty in volume:
                if treaty[-4:] == ".pdf":
                    print(treaty)

#converts pdf to a folder w/ each page converted to an image (JPEG)
def convert_to_img(path, output_dir):
    """
    name = name of the CTS file to be converted
    path = full path to file
    output_dir = directory to output to 
    """
    # Store Pdf with convert_from_path function
    images = convert_from_path(path)

    if os.path.exists(output_dir):
        print(f'path {output_dir} already exists')
        return
    else:
        os.makedirs(output_dir)
    
    for i in range(len(images)):
        print(f'{output_dir}/page'+ str(i+1) +'.jpg', 'JPEG')
        # Save pages as images in the pdf
        images[i].save(f'{output_dir}/' + str(i+1) +'.jpg', 'JPEG')


##extracts the text from a given folder of images
def extract_text(images_dir, output_dir, treaty_name):
    if os.path.exists(output_dir):
        print(f'path {output_dir} already exists')
        return
    else:
        os.makedirs(output_dir)

    for img_name in sorted(os.listdir(images_dir), key=lambda x: int(x[0:-4])):
        print(img_name)
        inputPath = os.path.join(images_dir, img_name)

        img = Image.open(inputPath)
  
        # applying ocr using pytesseract for python
        text = pyt.image_to_string(img, lang ="eng")


        file1 = open(f'{output_dir}/{treaty_name}.txt', "a+")
  
        # providing the content in the image
        file1.write(text+ "\n")
        file1.close()


# get_treaties_from_dir("test_dir1")

# convert_to_img('test_one/1_CTS_119_eng.pdf', 'test_img')

# text = extract_text('test_img','results1', 'cts1')
# print(text)



"""
TO DO:

- Scale the treaty conversion to multiple treaties
- Store functions in objects
- Create main() script


"""


