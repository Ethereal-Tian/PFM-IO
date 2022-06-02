import numpy as np
from PIL import Image
from os.path import *
import re
import json
# import OpenEXR
import Imath
import imageio
import cv2
cv2.setNumThreads(0)
cv2.ocl.setUseOpenCL(False)

def readPFM(file):
    file = open(file, 'rb')

    color = None
    width = None
    height = None
    scale = None
    endian = None

    header = file.readline().rstrip()
    if header == b'PF':
        color = True
    elif header == b'Pf':
        color = False
    else:
        raise Exception('Not a PFM file.')

    dim_match = re.match(rb'^(\d+)\s(\d+)\s$', file.readline())
    if dim_match:
        width, height = map(int, dim_match.groups())
    else:
        raise Exception('Malformed PFM header.')

    scale = float(file.readline().rstrip())
    if scale < 0: # little-endian
        endian = '<'
        scale = -scale
    else:
        endian = '>' # big-endian

    data = np.fromfile(file, endian + 'f')
    shape = (height, width, 3) if color else (height, width)

    data = np.reshape(data, shape)
    data = np.flipud(data)
    return data

def writePFM(file, array):
    import os
    assert type(file) is str and type(array) is np.ndarray and \
           os.path.splitext(file)[1] == ".pfm"
    with open(file, 'wb') as f:
        H = array.shape[0]
        W = array.shape[1]
        if len(array.shape) == 2:
          # headers = ["Pf\n", f"{W} {H}\n", "-1\n"]
          headers = ["Pf\n", f"{W} {H}\n", "-1.000000\n"]
        elif len(array.shape) == 3:
          # headers = ["PF\n", f"{W} {H}\n", "-1\n"]
          headers = ["PF\n", f"{W} {H}\n", "-1.000000\n"]
        for header in headers:
            f.write(str.encode(header))
        array = np.flip(array, axis=0).astype(np.float32)
        f.write(array.tobytes())

# def readExr(filename):
#     File = OpenEXR.InputFile(filename)
#     PixType = Imath.PixelType(Imath.PixelType.FLOAT)
#     DW = File.header()['dataWindow']
#     CNum = len(File.header()['channels'].keys())
#     if (CNum > 1):
#     	Channels = ['R', 'G', 'B']
#     	CNum = 3
#     else:
#     	Channels = ['G']
#     Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1)
#     Pixels = [np.fromstring(File.channel(c, PixType), dtype=np.float32) for c in Channels]
#     hdr = np.zeros((Size[1],Size[0],CNum),dtype=np.float32)
#     if (CNum == 1):
#         hdr[:,:,0] = np.reshape(Pixels[0],(Size[1],Size[0]))
#     else:
# 	    hdr[:,:,0] = np.reshape(Pixels[0],(Size[1],Size[0]))
# 	    hdr[:,:,1] = np.reshape(Pixels[1],(Size[1],Size[0]))
# 	    hdr[:,:,2] = np.reshape(Pixels[2],(Size[1],Size[0]))

#     h, w, c = hdr.shape
#     if c == 1:
#         hdr = np.squeeze(hdr)
#     return hdr


if __name__ == '__main__':

  f1_img = np.random.rand(2,3)
  f3_img = np.random.rand(2,3,3)

  for v in range(f1_img.shape[1]):
    for u in range(f1_img.shape[0]):
      f1_img[u,v] = 1.2 * v + 10.0  * u

  for v in range(f3_img.shape[1]):
    for u in range(f3_img.shape[0]):
      for c in range(f3_img.shape[2]):
        f3_img[u,v,c] = 1.2 * v + 10.0  * u + 100.0 * c

  print('f1_img',f1_img.shape,f1_img.dtype,type(f1_img))
  print('f3_img',f3_img.shape,f3_img.dtype,type(f3_img))


  writePFM('/home/tcr/pro_toolkit/PFM_IO/data/f1.pfm',f1_img)
  writePFM('/home/tcr/pro_toolkit/PFM_IO/data/f3.pfm',f3_img)

  f1_img2 = readPFM('/home/tcr/pro_toolkit/PFM_IO/data/f1.pfm').astype(np.float32)
  f3_img2 = readPFM('/home/tcr/pro_toolkit/PFM_IO/data/f3.pfm').astype(np.float32)

  print('f1_img2',f1_img2.shape,f1_img2.dtype,type(f1_img2))
  print('f3_img2',f3_img2.shape,f3_img2.dtype,type(f3_img2))

  for v in range(f1_img.shape[1]):
    for u in range(f1_img.shape[0]):
      print(u,v,f1_img[u,v],f1_img2[u,v])

  for v in range(f3_img.shape[1]):
    for u in range(f3_img.shape[0]):
      print(u,v,f3_img[u,v],f3_img2[u,v])

