import numpy as np
import cv2
from matplotlib import pyplot as plt
from os.path import splitext

import micral_grain_core

def printImg(img, name, step, plotNum):
    if img.max()-img.min() != 0:
        img = np.uint8((img - img.min())/(img.max()-img.min()) * 255.0)
    else:
        img = np.uint8(img)
    img_out = cv2.applyColorMap(np.clip(img, 0, 255).astype('uint8'), cv2.COLORMAP_RAINBOW)
    cv2.imwrite(name + "_" + str(plotNum) + "_" + step + ".png", img_out)
    return img, plotNum+1

def printDetail(img, name, step, plotNum):
    if(len(img.shape)>1):
        cv2.imwrite(name + "_details_" + str(plotNum) + "_" + step + ".png", img)
    else:
        plt.figure()
        plt.plot(img/255)
        plt.title(step)
        plt.xlabel('pixels')
        plt.ylabel('relative intensity')
        plt.savefig(name + "_details_" + str(plotNum) + "_" + step + ".png")
        plt.close()

def grainPrint(dict_input, plotFull, plotDetails):
    output_coarse = dict()
    if dict_input != None:
        for nameImg, dictImg in dict_input.items():
            name = splitext(nameImg)[0]
            if 'process' in dictImg:
                for key, subDict in dictImg['process'].items():
                    if 'id' in subDict:
                        num = subDict['id']
                    else:
                        num = 0
                    if plotFull and 'full' in subDict:
                        printImg(subDict['full'], name, key, num)
                    if plotDetails and 'details' in subDict:
                        printDetail(subDict['details'], name, key, num)
            if 'overlay' in dictImg:
                cv2.imwrite(name + "_overlay.png", cv2.cvtColor(dictImg['overlay'], cv2.COLOR_RGB2BGR))
            if 'coarse' in dictImg:
                output_coarse[nameImg] = "%.2f%%" % dictImg['coarse']
            
    return output_coarse

def grainSeparator(inputs, plot, plotFull, plotDetails, parameters):
    out = micral_grain_core.analyse(inputs, plot, plotFull, plotDetails, parameters)
    return grainPrint(out, plotFull, plotDetails)