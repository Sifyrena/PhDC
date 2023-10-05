import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Define the Arrays

DivArr = np.array([(1,50,182),(1,86,157), (255,255,250), (255,0,26), (136,10,44)])/255 

CycArr = np.array([(75,56,72), (1,86,157), (200,198,200), (180,60,1), (75,56,72)])/255


ChnArr = np.array([(1,86,157),
                                         (233,117,29),
                                         (218,187,78),
                                         (115,86,52),
                                         (16,130,128),
                                         (240,228,202),
                                         (79,132,41),
                                         (127,106,103),
                                         (180,60,1),
                                         (52,52,39)]) / 255

PArr = np.array([(171, 28, 7), (226, 177, 25), (26, 55, 90), (96, 94, 82),
                   (54, 56, 16), (16, 60, 32), (192, 128, 61),
                   (190, 190, 190)]) / 255

PBArr = np.array([(255, 38, 10), (255, 199, 27), (61, 149, 255),
                   (215, 210, 182), (159, 166, 34), (43, 231, 110),
                   (255, 158, 74), (227, 227, 231)]) / 255

TArr = np.array([
    (128, 168, 59), 
    (59, 91, 14), 
    (99, 167, 137),
    (45, 100, 75),
    (235, 216, 155),
    (172, 167, 109),
    (100, 116, 142),
    (75, 83, 95)]) / 255

BArr = np.array([
    (0,0,0),
    (25,37,48),
    (64,87,107),
    (20,88,87),
    (105,124,94),
    (143,157,128),
    (178,175,112),
    (227,177,75),
    (224,82,42),
    (255,0,50)]) / 255

B2Arr = np.array([
    (0,0,0),
    (25,37,48),
    (64,87,107),
    (20,88,87),
    (105,124,94),
    (143,157,128),
    (178,175,112),
    (227,177,75),
    (255,82,42)]) / 255


# Definitions

China = mcolors.ListedColormap(ChnArr)


Plates = mcolors.ListedColormap(PArr)

Plates_B = mcolors.ListedColormap(PBArr)

Teacups = mcolors.ListedColormap(TArr)

CNCyc = mcolors.LinearSegmentedColormap.from_list("MyDiv",CycArr)

Bowls = mcolors.LinearSegmentedColormap.from_list("MyDiv",BArr)

Bowls2 = mcolors.LinearSegmentedColormap.from_list("MyDiv",B2Arr)


Div = mcolors.LinearSegmentedColormap.from_list('myDiv', DivArr)

Def = China
Lines = Plates
Scatter = Plates_B
Duo = Teacups
CM = Bowls
CMP = Bowls2
Cyc = CNCyc