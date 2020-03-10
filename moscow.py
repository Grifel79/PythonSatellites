import numpy as np
from PIL import Image
import math
import cv2
import tifffile as tiff

# dir = "Users/gchernomordik/Documents/Strelka KB/Satellite/Moscow/LC08_L1TP_178021_20180511_20180517_01_T1/"
dir = "../../Strelka KB/Satellite/Moscow/LC08_L1TP_178021_20180511_20180517_01_T1/"

b10_path = dir + 'LC08_L1TP_178021_20180511_20180517_01_T1_B10.TIF'
b11_path = dir + 'LC08_L1TP_178021_20180511_20180517_01_T1_B11.TIF'

b4_path = dir + 'LC08_L1TP_178021_20180511_20180517_01_T1_B4.TIF'
b5_path = dir + 'LC08_L1TP_178021_20180511_20180517_01_T1_B5.TIF'
b7_path = dir + 'LC08_L1TP_178021_20180511_20180517_01_T1_B7.TIF'

# b10 = Image.open(b10_path)
# b11 = Image.open(b11_path)
#
# b4 = Image.open(b4_path)
# b5 = Image.open(b5_path)
# b7 = Image.open(b7_path)


b10_tif = tiff.TiffFile(b10_path)
b10_array = b10_tif.asarray()

b11_tif = tiff.TiffFile(b11_path)
b11_array = b11_tif.asarray()

b4_tif = tiff.TiffFile(b4_path)
b4_array = b4_tif.asarray()

b5_tif = tiff.TiffFile(b5_path)
b5_array = b5_tif.asarray()

b7_tif = tiff.TiffFile(b7_path)
b7_array = b7_tif.asarray()



#
# with tiff.tifffile(b11_path) as b11_tif:
#     b11_array = b11_tif.asarray()
#
#
# with tiff.tifffile(b4_path) as b4_tif:
#     b4_array = b4_tif.asarray()
#
# with tiff.tifffile(b5_path) as b5_tif:
#     b5_array = b5_tif.asarray()
#
# with tiff.tifffile(b7_path) as b7_tif:
#     b7_array = b7_tif.asarray()


#tiff.imshow(b10_array)
#b10_scaled = cv2.normalize(b10_array, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)

cv2.namedWindow("b10", cv2.WINDOW_NORMAL)
cv2.resizeWindow('b10', 1000, 1000)
cv2.imshow('b10', b10_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("b11", cv2.WINDOW_NORMAL)
cv2.resizeWindow('b11', 1000, 1000)
cv2.imshow('b11', b11_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("b4", cv2.WINDOW_NORMAL)
cv2.resizeWindow('b4', 1000, 1000)
cv2.imshow('b4', b4_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("b5", cv2.WINDOW_NORMAL)
cv2.resizeWindow('b5', 1000, 1000)
cv2.imshow('b5', b5_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("b7", cv2.WINDOW_NORMAL)
cv2.resizeWindow('b7', 1000, 1000)
cv2.imshow('b7', b7_array)
cv2.waitKey(0)
cv2.destroyAllWindows()


# b10.show()
# b11.show()

# with open(dir + "LC08_L1TP_178021_20180511_20180517_01_T1_MTL.txt", "r") as file:
#            for item in file:
#                print(item)
#                content = item.split(' = ')
#                if content[0] == 'RADIANCE_MULT_BAND_10':
#                    print(content[1])
#                if content[0] == 'RADIANCE_ADD_BAND_10':
#                    print(content[1])

with open(dir + "LC08_L1TP_178021_20180511_20180517_01_T1_MTL.txt") as MTL:
    for line in MTL:
        name, var = line.partition(" =")[::2]
        if name == '    RADIANCE_MULT_BAND_10':
            M10 = float(var)
        if name == '    RADIANCE_ADD_BAND_10':
            A10 = float(var)
        if name == '    RADIANCE_MULT_BAND_11':
            M11 = float(var)
        if name == '    RADIANCE_ADD_BAND_11':
            A11 = float(var)
        if name == '    REFLECTANCE_MULT_BAND_4':
            M4 = float(var)
        if name == '    REFLECTANCE_ADD_BAND_4':
            A4 = float(var)
        if name == '    REFLECTANCE_MULT_BAND_5':
            M5 = float(var)
        if name == '    REFLECTANCE_ADD_BAND_5':
            A5 = float(var)
        if name == '    REFLECTANCE_MULT_BAND_7':
            M7 = float(var)
        if name == '    REFLECTANCE_ADD_BAND_7':
            A7 = float(var)
        if name == '    K1_CONSTANT_BAND_10':
            K1_10 = float(var)
        if name == '    K2_CONSTANT_BAND_10':
            K2_10 = float(var)
        if name == '    K1_CONSTANT_BAND_11':
            K1_11 = float(var)
        if name == '    K2_CONSTANT_BAND_11':
            K2_11 = float(var)
        if name == '    SUN_ELEVATION':
            SUN_ELEV = float(var)

print(M10)
print(A10)

print(M11)
print(A11)

print(M4)
print(A4)

print(M5)
print(A5)

print(M7)
print(A7)

print(K1_10)
print(K2_10)

print(K1_11)
print(K2_11)

print(SUN_ELEV)


# b10_array = np.array(b10)
# b11_array = np.array(b11)
#
# b4_array = np.array(b4)
# b5_array = np.array(b5)
# b7_array = np.array(b7)

# b10_array = np.array(b10.getdata()).reshape(b10.size[::-1])
# b11_array = np.array(b11.getdata()).reshape(b11.size[::-1])
#
# b4_array = np.array(b4.getdata()).reshape(b4.size[::-1])
# b5_array = np.array(b5.getdata()).reshape(b5.size[::-1])
# b7_array = np.array(b7.getdata()).reshape(b7.size[::-1])

L10 = b10_array * M10 + A10
L11 = b11_array * M11 + A11

SIN_SUN_ELEV = np.sin(SUN_ELEV * math.pi / 180)

R4 = (b4_array * M4 + A4) / SIN_SUN_ELEV
R5 = (b5_array * M5 + A5) / SIN_SUN_ELEV
R7 = (b7_array * M7 + A7) / SIN_SUN_ELEV

# use original or R values for ndvi and ndbi? Not sure!

# ndvi = (R5-R4)/(R5+R4)
ndvi = (b5_array - b4_array) / (b5_array + b4_array)
ndvi = np.nan_to_num(ndvi)

ndbi = (R7 - R5) / (R7 + R5)

T_10 = K2_10 / (np.log(K1_10 / L10 + 1)) - 273.15
T_11 = K2_11 / (np.log(K1_11 / L11 + 1)) - 273.15

# Pv = np.square((ndvi - np.min(ndvi)) / (np.max(ndvi) - np.min(ndvi)))
Pv = np.square(ndvi - np.min(ndvi) / np.max(ndvi) - np.min(ndvi))
e = 0.004 * Pv + 0.968

# LST = T_10 / (1 + (10.8 * T_10/14388)*np.log(e))
LST = T_10 / 1 + b10_array * (T_10 / 14380) * np.log(e)

# How to save images in GeoTIFF
cv2.imwrite("/output/ndvi.tif", ndvi)
cv2.imwrite("/output/LST.tif", LST)

cv2.namedWindow("ndvi", cv2.WINDOW_NORMAL)
cv2.resizeWindow('ndvi', 1000, 1000)
cv2.imshow('ndvi', ndvi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("LST", cv2.WINDOW_NORMAL)
cv2.resizeWindow('LST', 1000, 1000)
cv2.imshow('LST', LST)
cv2.waitKey(0)
cv2.destroyAllWindows()
