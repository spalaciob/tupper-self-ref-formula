#!/bin/python3
"""
DESCRIPTION: Implementation of Tupper's Self-Referential Formula

A bit more flexible that the ones found online so far, it allows plotting
the result of applying the formula, given a value of k
Moreover, given a PNG image of appropriate size, it will binarize it and crop
it if necessary, and then calculate the corresponding value of k.

@author: Sebastian Palacio B.
@license: Apache License 2.0
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Global dimensions of the board
H, W = 17, 106

def tupper(x, y):
    """
    Tupper's everything-function. Works with numpy arrays
    :param x: 1d-array. X-coordinates
    :param y: 1d-array. Y-coordinates
    :return: 2d array of bools.
    """
    return 0.5 < ((y//H) // (2**(H*x + y%H))) % 2


def img2binary_map(img):
    """
    Convert an array to a binary map.
    :param img: ndarray. 2d array. It will be normalized between [0, 1] and
                then thresholded by 0.5 to get the binary map. The spatial
                dimensions will be cropped/padded to reach a 17x106 2D array.
    :return: 2d-array. Binary map.
    """
    map = np.zeros((W, H))
    img = img.astype('float') / float(img.max())
    map = img[:W, :H]
    return map > 0.5


def binary_map2k(bmap):
    """
    Go from a binary map to its integer representation.
    :param map: 2d-array. Binary map.
    :return: int. Integer representation of the binary map from img.
    """
    binstr = ''.join(np.array(['1', '0'])[bmap.astype('int').ravel()])
    return int(binstr, base=2)
    return k


if __name__ == "__main__":
    plt.ion()
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--img', help='path to input image')
    parser.add_argument('-k', dest='k', type=int, default=-1,
                        help='Pass a value of K instead of an image.')
    opts = parser.parse_args()

    if opts.k < 0:
        try:
            img = plt.imread(opts.img)
            if img.ndim == 3:
                img = img.mean(axis=(2,))
            elif img.ndim == 4:
                img = img.mean(axis=(2, 3))

            k = binary_map2k(img2binary_map(img))
        except:
            print('failed to generate K from image. Sorry!')
            k = 285793394306920833441610418092098634655629245793956098678773267955742373149291514664653927800704880150373913388420964422623233842047706907315421529784544945553099781467665141947527937768115378927462202029225694838470475677588782452320538001859819285285610917709502100783029895480521778368372918563047043463693747794234001337059033469278602878130645036795758601355772773088837517342039419030785383367558729311477147326456669868945040103723383968188359342791248298007775681749646431977354347601355114152656289715070769940791326910163950321532927
        finally:
            print('k = {}'.format(k))
    else:
        print('Using provided k...')
        k = opts.k
    h, w = H, W
    # k to plot Tupper's Self-Referential Formula
    # k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719

    x = np.arange(w)[:, np.newaxis]
    y = np.arange(h)[np.newaxis, :]
    bin_map = tupper(x, y+k*h)

    plt.imshow(np.rot90(bin_map), plt.cm.Greys)
    # plt.savefig('tupper.png')
    try:
        input("Press key")
    except:
        pass
