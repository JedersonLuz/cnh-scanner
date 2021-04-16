import re
import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.io import imread, imsave
from skimage.util import img_as_ubyte
from skimage.exposure import adjust_gamma, rescale_intensity

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

pattern = r'\d{3}.\d{3}.\d{3}-\d{2}'

def search_cpf(filename, is_testing=False):
  '''
  Receive a filename of a document and return the CPF extracted from it.

  Parameters:
    filename (string): Path of the document.
    is_testing (bool): If True, present advanced depuration.

  Returns:
    String of the CPF extracted from document.
  
  '''
  
  img = imread(filename).astype(np.uint8)
  img_gray = rgb2gray(img)
  img_powered = adjust_gamma(img_gray, 0.4, 10)
  img_rescaled = rescale_intensity(img_powered)
  img_ubyte = img_as_ubyte(img_rescaled)
  img_text = pytesseract.image_to_string(img_ubyte)

  if is_testing:
    _, ax = plt.subplots(1, 3, figsize=(50, 40))
    ax[0].imshow(img_gray, cmap='gray')
    ax[1].imshow(img_powered, cmap='gray')
    ax[2].imshow(img_rescaled, cmap='gray')
    plt.show()
    print([img_text.strip()])

  for row in img_text.split('\n'):
    row = row.replace(' ', '')
    row = row.replace('=', '')
    result = re.findall(pattern, row)

    if result:
      print('Search successful.')
      print(f'The CPF founded is {result[0]}')
      return result[0]
  
  print('Search unsuccessful.')