#############################################################################################################################
# C: INFN                                                                                                                   #
#                                        CLASSES TO CLUSTER RGB Images                                                      #
# dev: Alessandro Bombini, INFN                                                                                             #
#############################################################################################################################
import os

import numpy as np
import h5py
import matplotlib.pyplot as plt
import json

import datetime
import gc

# generator
from utils.XRF_generator_classes import XRFGenerator
# utils
from utils.MAXRF_class import MAXRF
from utils.RGB_segmentation_utils import RGBMethods

def save_HDF5_file(
    _data: np.array, 
    path_to_store: str,
    compression_factor: int = 5   
):
    """_summary_
    Method to save a generated MA-XRF into an appropriate HDF5.

    The HDF5 file contains the dataset "img" where the np.array is stored.

    Args:
        _data               (np.array)      : MA-XRF np.array
        path_to_store       (str)           : Full path (comprensive of the file name and extension), where the file will be stored.
        compression_factor  (int, optional) : GZIP compression factor. Defaults to 5.
    """
    f = h5py.File(path_to_store, "w")   
    f.create_dataset("img", data=_data,compression="gzip", compression_opts=compression_factor)
    f.close()

def generate_all(
    rootdir: str, storedir: str, pigments_dict_data: str, _compression_factor: int = 5,
    N_start = 10, E_int = [0.5, 38.5], 
    rebin_size = 1024, delta_N = 1, N_patience = -1, score_batch = 1024
):
    """_summary_
    Method to generate a set of synthetic MA-XRF data out of a set of RGB images.

    Args:
        rootdir             (str)           : Root dir where the RGB files are. 
        storedir            (str)           : Final dir where the XRF HDF5 will be stored.
        pigments_dict_data  (str)           : Path to the Pigments JSON DB.
        
        _compression_factor (int, optional) : GZIP compression factor. Defaults to 5. Defaults to 5..
        N_start             (int, optional) : Starting number of clusters in the Iterative KNN. Defaults to 10.
        E_int               (list, optional): Energy interval (in keV). Defaults to [0.5, 38.5].
        rebin_size          (int, optional) : Rebin size of XRF histograms. Defaults to 1024.
        delta_N             (int, optional) : Delta number of clusters in the Iterative KNN. Defaults to 1.
        N_patience          (int, optional) : Patience in the Iterative KNN. Defaults to -1.
        score_batch         (int, optional) : Batch size in each KNN. Defaults to 1024.
    """
    start_all = datetime.datetime.now()
    # init RGB utils
    rgbMethods = RGBMethods
    # iterate over all the rgbs
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(f"Generating XRF for file {file}")
            # open RGB
            ex_rgb = rgbMethods.open_image(file_name=file, root_path_to_rgb=subdir)

            # init XRF Generator class
            _xrf_generator = XRFGenerator(
                # PigmentDataBaseUtils
                pigments_dict_data = pigments_dict_data,
                # RGBKMeansClustering
                rgb_img = ex_rgb,
                N_start = N_start, 
                # PigmentDataBaseUtils 
                E_int = E_int,
                rebin_size = rebin_size,
                # RGBKMeansClustering
                delta_N = delta_N,
                N_patience = N_patience,
                score_batch = score_batch
            )

            # generate XRF 
            start = datetime.datetime.now()
            generated_XRF = _xrf_generator.generate_xrf()
            print(f"Generation for file {file.split('/')[-1]} done in { datetime.datetime.now() - start}")

            # Save file
            start = datetime.datetime.now()
            file_path_ = os.path.join(storedir, file.split('.')[0] + '.h5' ) 
            print(f"saving into {file_path_}")
            save_HDF5_file(
                _data = generated_XRF,
                path_to_store = file_path_,
                compression_factor = _compression_factor
            )
            print(f"Storing for file {file_path_.split('/')[-1]} done in { datetime.datetime.now() - start}\n")
            # free space
            del ex_rgb, generated_XRF, _xrf_generator
            gc.collect()
            
    print(f"\n\nEverything done in { datetime.datetime.now() - start}")

def inspect_generated_xrf(
    path_to_h5: str,
    pigments_dict_data: str, 
    E_int: list = [0.5, 38.5],
    n_bins: int = 1024, 
    list_of_el_imgs: list = [
        'Ca (Ka)',
        'Fe (Ka)',
        'Cu (Ka)',
        'Au (La)',
        'Hg (La)',
        'Pb (La)',
        'Ag (Ka)'
    ],
    delta_Energy_plot: float = 0.2
):
    """_summary_
    Method to inspect a generated MA-XRF HDF5 file. 
    The file is open, then, for each element line in list_of_el_imgs
    it is computed the integral over an energy range of delta_Energy_plot width, 
    and then plotted.

    Args:
        path_to_h5          (str): Full path to the HDF5 file.
        pigments_dict_data  (str): Path to the Pigments JSON DB.

        E_int               (list, optional)    : Energy interval (in keV). Defaults to [0.5, 38.5].
        n_bins              (int, optional)     : Number of bins in the XRF. Defaults to 1024.
        list_of_el_imgs     (list, optional)    : List of elements to be used in the computation. Defaults to [ 'Ca (Ka)', 'Fe (Ka)', 'Cu (Ka)', 'Au (La)', 'Hg (La)', 'Pb (La)', 'Ag (Ka)' ].
        delta_Energy_plot   (float, optional)   : Integration interval. Defaults to 0.2.
    """
    # Open XRF s
    filename = path_to_h5.split('/')[-1]
    _h5 = h5py.File(path_to_h5,'r')
    _arr = np.array( _h5['img'][()] )
    _h5.close()

    _xrf = MAXRF(
        xrf = _arr,
        n_bins = n_bins
    )

    _xrf.init_XRFLines(path_to_json=pigments_dict_data)
    _xrf.init_calibration_data(E_min=E_int[0], E_max=E_int[1])

    # Cumulative histogram
    plt.figure(figsize=(16,8))
    plt.title(f"Histogram of counts of {filename}")
    plt.plot(
        _xrf._E_range_x_axis,
        _xrf._xrf.sum(axis=0).sum(axis=0)
    )
    plt.xlabel('Energy (keV)')
    plt.ylabel('Counts')
    plt.show()

    # Element images
    _ncols = 4
    _nrows = int( np.ceil( len(list_of_el_imgs) / _ncols ) )

    fig, ax = plt.subplots(
        nrows = _nrows, ncols = _ncols,
        figsize = (24,12)
    )

    for idx, el in enumerate(list_of_el_imgs):
        # get ax indeces
        i = idx // _ncols
        j = idx % _ncols
        # get el value
        el_val = _xrf.get_value_from_element_name(_xrf.XRFLines, el)

        ax[i,j].set_title(f"{el} - {el_val} keV", fontsize=18)
        _el_img = _xrf.get_X_line_image(el = el, delta_Energy_plot=delta_Energy_plot)
        ax[i,j].imshow(
            _el_img
        )
        _ann_text = f"avg counts: {np.round( _el_img.mean(axis=-1).mean(), decimals=2)}"
        ax[i,j].annotate(_ann_text, (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top', fontsize=16)


        del _el_img, _ann_text
        gc.collect()

    fig.suptitle(f"Elements of {filename}", fontsize=20)
    fig.text(0.5, 0.01, f"integration interval: {delta_Energy_plot} keV", ha="center", fontsize=16, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
    fig.show()