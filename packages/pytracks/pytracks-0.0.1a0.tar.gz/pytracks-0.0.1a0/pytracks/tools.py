"""


Author: Alexandre Fioravante de Siqueira
Version: march, 2016
"""

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from skimage.io import imread

import numpy as np
import matplotlib.pyplot as plt


def acquire_dataset(image_name, depth):
    """
    acquiredataset(image_name, depth)

    Acquires the images which will be used
    on the 3D representation.

    Returns stack.
    """

    while True:
        try:
            aux = imread(image_name, as_grey=True)
            break
        except:
            print('Could not read image.')
            img_name = input('Please type the name of the first image: ')

    row, col = np.shape(aux)

    while True:
        try:
            images = np.zeros((int(depth), row, col))
            break
        except:
            print('Could not determine the dataset size.')
            depth = input('Please type the number of images on the dataset: ')

    images[0] = aux

    try:
        for stack in range(1, depth):
            aux = image_name[:-5] + str(stack + 1) + image_name[-4:]
            images[stack] = imread(aux, as_grey=True)
    except:
        print('Could not read image #{0}.'.format(stack))
        raise

    return images


def progress_bar(prog, mesg='Please wait...'):
    """
    progressbar(prog, mesg='Please wait...')

    Presents a nice progress bar and a text message.

    Original code by user aviraldg on StackOverflow:
    http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """

    print(' '*int(40), end='')  # resetting current message
    print('\r[{0}{1}] {2}% - '.format('#'*int(prog/10), ' '*int((100-prog)/10),
          prog) + str(mesg), end='')

    return None


def save_info_uwt(bin_h, bin_v, bin_d, stk_plot='n', alg='o'):
    """
    saveinfouwt(bin_h, bin_v, bin_d, stk_plot='n', alg='o')

    Saves UWT results.
    """

    _, _, dep, lev = np.shape(bin_h)

    for num in range(lev):
        if str(stk_plot) is 'y':  # plotting stack
            showstackcont(bin_h[:, :, :, num], cm.gray)
            plt.savefig('stackbin_h'+str(alg)+str(num)+'.png',
                        bbox_inches='tight')
            showstackcont(bin_v[:, :, :, num], cm.gray)
            plt.savefig('stackbin_v'+str(alg)+str(num)+'.png',
                        bbox_inches='tight')
            showstackcont(bin_d[:, :, :, num], cm.gray)
            plt.savefig('stackbin_d'+str(alg)+str(num)+'.png',
                        bbox_inches='tight')

        # plotting cross sections:
        showcrosstest(bin_h[:, :, :, num], cm.gray)
        plt.savefig('crossbin_h'+str(alg)+str(num)+'.png',
                    bbox_inches='tight')
        showcrosstest(bin_v[:, :, :, num], cm.gray)
        plt.savefig('crossbin_v'+str(alg)+str(num)+'.png',
                    bbox_inches='tight')
        showcrosstest(bin_d[:, :, :, num], cm.gray)
        plt.savefig('crossbin_d'+str(alg)+str(num)+'.png',
                    bbox_inches='tight')

    plt.close('all')

    return None


def show_stack_cont(stack, color_map=cm.YlGnBu):
    """
    showstackcont(stack, color_map=cm.YlGnBu)

    Presents the stack visualization based
    on contours.
    """

    row, col, dep = np.shape(stack)

    x = np.linspace(0, row, row)
    y = np.linspace(0, col, col)
    xx, yy = np.meshgrid(x, y)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_zlim(-(dep+1), 1)

    for curr_dep in range(dep):
        ax.contourf(xx, yy, np.transpose(stack[:, :, curr_dep]),
                    zdir='z', offset=-curr_dep, cmap=color_map)

    return None


def dtcwt_nameangle(num_slice):
    num2angle = {
        0: '15 degrees',
        1: '45 degrees',
        2: '75 degrees',
        3: '-75 degrees',
        4: '-45 degrees',
        5: '-15 degrees'
    }
    return num2angle.get(num_slice, 'nothing')
