#############################################################################################################################
# C: INFN                                                                                                                   #
#                                        CLASSES TO CLUSTER RGB Images                                                      #
# dev: Alessandro Bombini, INFN                                                                                             #
#############################################################################################################################

"""
File containing the Python classes for generating a synthetic MA-XRF .h5 file starting from an RGB.

It imports 
    A. RGBKMeansClustering ( from RGB_segmentation_utils )
    B. XRFUtils ( from MAXRF_class )

It contains the following classes:
    1. PigmentDataBaseUtils(XRFUtils)
    2. Distances
    3. XRFGenerator

The structure 
"""

import os

import numpy as np
import h5py
import matplotlib.pyplot as plt
import json
from scipy import signal
from skimage import color
import gc

from .RGB_segmentation_utils import RGBKMeansClustering
from .MAXRF_class import XRFUtils

#
class PigmentDataBaseUtils(XRFUtils):
    """_summary_
    Class to initialise and use the Pigment XRF - RGB database. 
    To be initialised, we need to pass to it the path to a JSON file containing the DataBase as a nested dict. 
    The JSON dict must have the form
        {
            "pigment_name" : {
                "xrf" : path_to_xrf_h5_file,
                "RGB" : RGB color as list
            },
        }

        e.g. 
        {
            ...
            "LeadWithe" : {
                "xrf": "./infraart_db/XRFSpectrum/MetallicLead.h5",
                "RGB": [240, 235, 229]
            }
        }

    It extends the XRFUtils.

    Attributes
    ----------
        pigments_dict_data  (dict)  :   Nested Dictionary containing the RGB and XRF data of all pigments in the DB.

    Additional Attributes    
        E_int       (list, optional)  :   Energy interval (in keV). Defaults to [0.5, 38.5]
        rebin_size  (int, optional)   :   Final size of the XRF histogram (in bins). Defaults to 1024.

    Methods
    ----------
        set_pigments_dict_data(self, pigments_dict_data: dict)  :   Setter method for the pigments_dict_data attribute.
    
    Static Methods
        open_pigment_dict_json(path_to_pigments_dict_json: str = './utils/pigments_dict.json') -> dict  :   Open the JSON file, parses it and creates the nested dict object.
        get_distr_from_infraart_h5(path_to_infraart_h5: str, E: list = [0.5, 38.5], rebin_size: int = 500)  : Static method to get a distribution from an h5 file.
    """
    import os
    import numpy as np
    import json
    import h5py 
    
    def __init__(
        self, 
        pigments_dict_data,
        E_int: list = [0.5, 38.5],
        rebin_size: int  = 1024
    ):  
        """_summary_
        Init function for the class.

        Args:
            pigments_dict_data  (dict | str)        :   Either the parsed JSON dictionary or the path to the JSON dictionary.
            E_int               (list, optional)    :   Energy interval (in keV). Defaults to [0.5, 38.5]
            rebin_size          (int, optional)     :   Final size of the XRF histogram (in bins). Defaults to 1024.

        Raises:
            Exception:  If E_int inserted is invalid.
            Exception:  if pigments_dict_data inserted is neither a dict nor a valid path to json file.
        """
        # Init superclass
        super().__init__()
        
        if len(E_int) != 2 or E_int[0]>=E_int[1]:
            raise Exception(f"Invalid E_int ({E_int}) inserted.\n")
        self.E_int = E_int 
        
        if rebin_size > 0:            
            self.rebin_size = rebin_size
        else:
            # Set to infinity so no rebin.
            self.rebin_size = np.inf
        
        
        # Set pigment_dict_data
        self.pigments_dict_data = {}
        
        if type(pigments_dict_data) == dict:
            self.set_pigments_dict_data(
                pigments_dict_data
            )
        elif type(pigments_dict_data) == str and os.path.isfile(pigments_dict_data) and pigments_dict_data.split('.')[-1] == 'json':
            self.set_pigments_dict_data(
                self.open_pigment_dict_json(pigments_dict_data)
            )
        else:
            raise Exception(f"Error;\npigments_dict_data inserted ({pigments_dict_data}) is neither a dict nor a valid path to json file.")
        
    ###########################################
    # methods
    ###########################################
    
    def set_pigments_dict_data(self, pigments_dict_data: dict):
        """_summary_
        Setter method for the pigments_dict_data attribute.

        It iterates over all the pigments (the dict key is the pigment name),
        and then 
            1. Open the .h5 XRF files, and assigns both the Energy interval arange (_x) and the XRF histogram (_y)
            2. Define the sub-dict entry as
                {   
                    # THe XRF Data (X and Y)
                    'xrf': {
                        'x': _x, 
                        'y': _y
                    }, 
                    # the 255-base RGB color
                    'RGB': pigment_dict['RGB'],
                    # the float-base rgb color.
                    'rgb': list( np.array(pigment_dict['RGB'])/255.0 )
                }

        Args:
            pigments_dict_data  (dict)  : Nested dict containing the pigment db.
        """
        for pigment_name, pigment_dict in pigments_dict_data.items():
            _x, _y = self.get_distr_from_infraart_h5(
                path_to_infraart_h5 = pigment_dict['xrf'],
                E = self.E_int, 
                rebin_size = self.rebin_size
            )
            
            self.pigments_dict_data[pigment_name] = {
                'xrf': {
                    'x': _x, 
                    'y': _y
                },
                'RGB': pigment_dict['RGB'],
                'rgb': list( np.array(pigment_dict['RGB'])/255.0 )
            }            
    
    ###########################################
    # Static methods
    ###########################################
    
    @staticmethod
    def open_pigment_dict_json(path_to_pigments_dict_json: str = './utils/pigments_dict.json') -> dict:
        """_summary_
        Open the JSON file, parses it and creates the nested dict object.
        
        Args:
            path_to_pigments_dict_json  (str, optional)  : Path to JSON file. Defaults to './utils/pigments_dict.json'.

        Raises:
            Exception: If invalid path is passed.

        Returns:
            dict: parsed nested dict.
        """
        if ( 
            not os.path.isfile(path_to_pigments_dict_json) 
        ) or ( 
            path_to_pigments_dict_json.split('.')[-1] != 'json'
        ) :
            raise Exception(f"Path {path_to_pigments_dict_json} invalid; no valid file found.")

        with open(path_to_pigments_dict_json) as test:
            pigments_dict_data = test.read()

        return json.loads(pigments_dict_data)
    
    @staticmethod
    def get_distr_from_arr(y: np.array) -> np.array:
        """_summary_
        Static method to normalize a numpy histogram to have a unitary distribution. 
        
        Args:
            y (np.array)    :   Numpy histogram

        Returns:
            np.array    :   Unitary numpy histogram
        """
        return y/y.sum()
    
    @staticmethod
    def rebin_hst(prv: np.array, size: int = 500) -> np.array:
        """_summary_
        Method to rebin a 1D Histogram.

        Args:
            prv     (np.array)      : Histogram to be rebinned.
            size    (int, optional) : Rebinned size. Defaults to 500.

        Returns:
            np.array: rebinned histogram.
        """
        reb_prv, _ = np.histogram(
            np.arange(prv.shape[0]),
            bins=size, 
            weights=prv
        ) 

        return reb_prv
    
    @staticmethod
    def get_distr_from_infraart_h5(path_to_infraart_h5: str, E: list = [0.5, 38.5], rebin_size: int = 500):
        """_summary_
        Static method to get a distribution from an h5 file.
        The HDF5 file has to contain 2 dataset:
            'x' : the energy np.arange(E_i, E_f, delta_E)
            'y' : the XRF histogram of counts
        i.e., x and y are np.array of the same length, so that, at index i, y[i] is the number of counts 
        at energy x[i].

        It performs the following steps:
            1. Open the h5 file
            2. Get the X and Y dataset, corresponding to the np.arange() and XRF histogram.

        Args:
            path_to_infraart_h5 (str)               : Path to h5 file.
            E                   (list, optional)    : Energy range (in keV). Defaults to [0.5, 38.5].
            rebin_size          (int, optional)     : Size of the final histogram. Defaults to 500.

        Returns:
            np.array, np.array  : Energy arange, rebinned unitary distribution.
        """
        loaded_hf = h5py.File(
            path_to_infraart_h5, 
            'r'
        )
        _x = np.array(
            loaded_hf.get('x')
        )
        _y = np.array(
            loaded_hf.get('y')
        )

        min_idx = PigmentDataBaseUtils.get_index_from_energy(E[0], _x)
        max_idx = PigmentDataBaseUtils.get_index_from_energy(E[1], _x)

        # get right energy interval 
        _y = _y[min_idx:max_idx]

        # rebin if asked
        if rebin_size < _y.shape[0]:
            _y = PigmentDataBaseUtils.rebin_hst(_y, rebin_size)


        return _x, PigmentDataBaseUtils.get_distr_from_arr(_y)

#    
class Distances:
    """_summary_
    Classes furnishing static methods to compute distances in RGB space.

    Static Methods
    --------------
        cosine_similarity(x, y) :   returns the cosine similarity
        rgb2lab( rgb )          :   returns the CIELAB image
        CIEdelta1994_similarity(rgb1, rgb2) :   returns the similarity using the CIEdelta1994 distance
        CIEdelta2000_similarity(rgb1, rgb2) :   returns the similarity using the CIEdelta2000 distance
    """
    def __init__(self):
        pass
    
    ###########################################
    # Static methods
    ###########################################
    @staticmethod
    def cosine_similarity(x, y):
        return np.dot(x, y)/( np.sqrt( np.dot(x,x) )*np.sqrt( np.dot(y,y) ) ) 
    
    @staticmethod
    def rgb2lab( rgb ) :
        return color.rgb2lab(rgb)
    
    @staticmethod
    def CIEdelta1994_similarity(rgb1, rgb2):
        # 1. RGB to LAB
        lab1 = Distances.rgb2lab(rgb1)
        lab2 = Distances.rgb2lab(rgb2)

        # 2. Compute distance
        from skimage.color import deltaE_ciede94
        # This is your delta E value as a float.
        delta_e = deltaE_ciede94(lab1, lab2)
        # NB_ delta_e( [255,255,255], [0,0,0] ) = 100; put 101 for numerical errors 
        return (101 - delta_e)/101
    
    @staticmethod
    def CIEdelta2000_similarity(rgb1, rgb2):
        # 1. RGB to LAB
        lab1 = Distances.rgb2lab(rgb1)
        lab2 = Distances.rgb2lab(rgb2)

        # 2. Compute distance
        from skimage.color import deltaE_ciede2000
        # This is your delta E value as a float.
        delta_e = deltaE_ciede2000(lab1, lab2)
        # NB_ delta_e( [255,255,255], [0,0,0] ) = 100; put 101 for numerical errors 
        return (101 - delta_e)/101

#
class XRFGenerator:
    """_summary_
    Class to perform the MA-XRF generations out of a RGB image. 

    It generates the MA-XRF np.array by extracting randomly a certain number of counts, pixel-by-pixel,
    from an XRF signal probability distribution obtained, pixel-by-pixel, by similarity with pigments in a passed database.

    The RGB image is firstly segmented to reduce the RGB thriples, thus the noise.

    Attributes
    ----------
        _distances              (Distances)             :   Distences class instance. Is used to compute distances in color space between the RGB cluster and the RGB in the DataBase
        _pigmentDataBaseUtils   (PigmentDataBaseUtils)  :   PigmentDataBaseUtils class instance to handle the database
        _rgbKMeansClustering    (RGBKMeansClustering)   :   RGBKMeansClustering class instance to cluster the RGB image.

        _num_of_counts  (int)   :   Final XRF histogram number of pixel counts. Defaults to 400.
        _lambda         (int)   :    XRF Pixel Noise lambda - TBUsed

        _list_of_rgbs               (np.array | None)   :   Results of the Iterative KNN on RGB; list of RGB clusters
        _clustered_rgb              (np.array | None)   :   Results of the Iterative KNN on RGB; Clustered RGB
        _reshaped_segmented_iter    (np.array | None)   :   Results of the Iterative KNN on RGB; list of cluster mask.

        _generated_XRF  (np.array)  : generated MA-XRF np.array 

    Methods
    ----------
        do_cluster()    :   Performs the whole RGB clustering process.
        generate_xrf() -> np.array  :   Method to generate the MA-XRF out of an RGB image.
        get_distribution_from_rgb(
            rgb: np.array, 
            pigments_dict: dict, 
            threshold: float = 0.2, 
            debug: bool = False, 
            use_cie_similarity: bool = True
        ) -> np.array   :   Method to get an XRF synthetic histogram out of an RGB color.

    Static Methods
        get_xrf_distr_2D(num_of_counts: int, distr: np.array, size: tuple) -> np.array  :   Static method to randomly generate A fake MA-XRF rank-3 tensor out of a unitary distribution
        bincount2d(arr: np.array, bins=None) -> np.array    :   Static method to compute a 2D bincount.

    """
    import os
    import numpy as np
    import json
    import h5py 
    from scipy.stats import rv_discrete
    
    def __init__(
        self, 
        #####################################################
        # Needed Args - PigmentDataBaseUtils
        pigments_dict_data,
        # Needed Args - RGBKMeansClustering
        rgb_img: np.array, 
        N_start: int,
        # Needed Args - NEW
        num_of_counts: int = 400, # Average counts in pixel
        #####################################################
        # Optional Args - PigmentDataBaseUtils
        E_int: list = [0.5, 38.5],
        rebin_size: int  = 1024,
        # Optional Args - RGBKMeansClustering 
        delta_N: int = 3, 
        N_patience: int = -1, 
        score_batch: int = 1024,
        # Optional Args - NEW
        xrf_pixel_noise_lambda: float = -1 
    ):  
        """_summary_
        Init method.

        It initialises all the attributes, comprising the class instances:
            1. _pigmentDataBaseUtils; using PigmentDataBaseUtils class
            2. _rgbKMeansClustering; using RGBKMeansClustering class

        Args:
            pigments_dict_data  (str | dict)    : Either the Nested Dictionary containing the RGB and XRF data of all pigments in the DB, or the path to the JSON file containing it.
            rgb_img             (np.array)      : RGB image as np.array.
            N_start             (int)           : Initial KNN cluster number.
            num_of_counts           (int, optional)     : Final XRF histogram number of pixel counts. Defaults to 400.
            rebin_size              (int, optional)     : Final XRF histogram bins. Defaults to 1024.
            delta_N                 (int, optional)     : Iterative KNN delta N. Defaults to 3.
            N_patience              (int, optional)     : Iterative KNN patience. Defaults to -1.
            score_batch             (int, optional)     : Iterative KNN batch size. Defaults to 1024.
            xrf_pixel_noise_lambda  (float, optional)   : XRF Pixel Noise lambda - TBUsed. Defaults to -1.
        """
        super().__init__()
        # Distances
        self._distances = Distances()
        
        # PigmentDataBaseUtils init
        self._pigmentDataBaseUtils = PigmentDataBaseUtils(
            pigments_dict_data = pigments_dict_data,
            E_int = E_int,
            rebin_size = rebin_size
        ) 
        
        # RGBKMeansClustering init
        self._rgbKMeansClustering = RGBKMeansClustering(
            rgb_img = rgb_img,
            N_start = N_start,
            delta_N = delta_N,
            N_patience = N_patience,
            score_batch = score_batch
        )
        
        # Init new args
        self._num_of_counts = num_of_counts
        if xrf_pixel_noise_lambda <=0:
            self._lambda = np.inf # i.e., no noise
        else:
            self._lambda = xrf_pixel_noise_lambda
            
        
        # Now, Init empy
        self._list_of_rgbs  = None
        self._clustered_rgb = None
        self._reshaped_segmented_iter = None
        
        # init xrf
        self._generated_XRF = np.zeros(
            (
                rgb_img.shape[0], rgb_img.shape[1],
                rebin_size
            )
        )
           
    ###########################################
    # Class methods
    ###########################################
    # Method to compute the cluster
    def do_cluster(self):
        """_summary_
        Perform the whole RGB clustering process, by
            1. Calling self._rgbKMeansClustering.cluster_rgb()
            2. Extract the useful data, and set the relative class attributes:
                - _list_of_rgbs: the RGB clusters
                - _reshaped_segmented_iter: the cluster masks
        """
        self._clustered_rgb = self._rgbKMeansClustering.cluster_rgb()
        # Now the others
        self._list_of_rgbs  = self._rgbKMeansClustering._list_of_rgbs
        self._reshaped_segmented_iter = self._rgbKMeansClustering.reshaped_segmented_iter
    
    # Method to generate the XRF
    def generate_xrf(self) -> np.array:
        """_summary_
        Method to generate the MA-XRF out of the RGB.
        
        It does the following steps:
            0. If the clustering process was not performed, performs it.
            1. Performs the generation for each cluster, by
                i.  Compute cluster rgb average
                ii. Compute XRF distribution for the color out from the pigments_dict_data
                iii.Compute the cluster's boolean mask out of the cluster
                iv. Generate the XRF and mask it.
                v.  Add it to the MA-XRF np.array

        Returns:
            np.array    :   Generated MA-XRF.
        """
        # Try/Except is more pythonic
        # Check if do_cluster() was flashed
        try:
            self._list_of_rgbs.shape # if it initialised, is ok; if not, goes into except
        except:
            # launch do_cluster
            self.do_cluster()
            
        # Go on
        # generate XRF for each cluster
        for _idx in range(0, self._list_of_rgbs.shape[0]):
            print(f"Generating XRF for {_idx}-th cluster;")
            # Get cluster rgb value
            _avg_rgb = self._list_of_rgbs[_idx].max(axis=0).max(axis=0) # all numbers here are either 0 or the rgb

            # Compute XRF distribution for the color out from the pigments_dict_data
            _distr = self.get_distribution_from_rgb(
                rgb = _avg_rgb,
                pigments_dict = self._pigmentDataBaseUtils.pigments_dict_data
            )
            
            # compute the _mask out of the cluster
            _mask = np.array(
                np.array(
                    self._list_of_rgbs[_idx].sum(axis=-1),# sum over the rgb, so [0,0,0] -> 0, color -> something 
                    dtype = bool # then booleanize it
                ),
                dtype = int # then back to int; now it is only made by 0 and 1
            )
            
            # Then the generated xrf is mask x 
            _gen_xrf = self.get_xrf_distr_2D(
                num_of_counts = self._num_of_counts, 
                distr = _distr, 
                size = _mask.shape
            )
        
            self._generated_XRF += _mask[:,:, None] * _gen_xrf

            # free memory
            del _gen_xrf, _mask, _distr, _avg_rgb
            gc.collect()
            
        # return
        return self._generated_XRF
    
    # Method to get the distribution from the RGB triple
    def get_distribution_from_rgb(
        self, 
        rgb: np.array, 
        pigments_dict: dict, 
        threshold: float = 0.2, 
        debug: bool = False, 
        use_cie_similarity: bool = True
    ) -> np.array:
        """_summary_
        Method to get an XRF synthetic histogram out of an RGB color.

        It works this way: 
            0. Init the final distribution as zeros.
            1. Iterate over all the pigments in the pigments_dict dictionary 
                i.  Get the RGB and XRF hist associated to it
                ii. compute the distance between the pigment RGB and the input RGB.
                    If the distance is above the threshold, keep the result. Else, set it to zero.
                iii.Add the pigment distribution to the final distribution, weighted by the distance.
            2. Normalise the distribution. 
        
        i.e., the final distribution is the averaged sum of the XRF distrubution associated to
        the nearest pigments in RGB space. The weights are the distances in RGB space 
        (divided by an overall normalising factor)

        Args:
            rgb                 (np.array)  : Input RGB color
            pigments_dict       (dict)      : Pigment ditionary to be used to associate RGB to pigments and then pigments to XRF count unitary distribution.
            
            threshold           (float, optional)   : _description_. Defaults to 0.2.
            debug               (bool, optional)    : Set to true to have a verbose output. Defaults to False.
            use_cie_similarity  (bool, optional)    : Use CIE similarity to compute distances in RGB space. Defaults to True.

        Returns:
            np.array : Generated XRF distribution
        """
        color_type = 'RGB'
        if rgb.max() <= 1.0:
            color_type = 'rgb'
        
        list_of_pigments = []
        distr = 0
        total_alpha = 10e-7 # a numeric zero 
        max_alpha = 0
        index_max_alpha = -1
        name_max_alpha = None

        if debug:
            print("Using CIE delta 2000" if use_cie_similarity else "Using cosine similarity")

        for index, pigment_name in enumerate(pigments_dict.keys()):
            pigment = pigments_dict[pigment_name] #pigment has three keys: xrf, RGB, rgb

            if use_cie_similarity:
                alpha = self._distances.CIEdelta2000_similarity( np.array(rgb), np.array( pigment[color_type] ) )
            else:
                alpha = self._distances.cosine_similarity( np.array(rgb), np.array( pigment[color_type] ) )

            if alpha > max_alpha:
                max_alpha = alpha
                index_max_alpha = index
                name_max_alpha = pigment_name

            if alpha >= threshold:
                list_of_pigments.append(
                    {
                        'alpha': alpha,
                        'pigment': pigment_name
                    }
                )
                total_alpha += alpha

                if index == 0 or (type(distr) == int):
                    distr = alpha * pigment['xrf']['y']#get_distr_from_infraart_h5(pigment['xrf'], rebin_hist=rebin_hist, rebin_size=rebin_size)
                else:
                    # they may have different numbers due to numerical retrieval of index
                    _distr = pigment['xrf']['y'] #get_distr_from_infraart_h5(pigment['xrf'], rebin_hist=rebin_hist, rebin_size=rebin_size)
                    try:
                        if _distr.shape[0] == distr.shape[0]:
                            distr += alpha * _distr
                        elif _distr.shape[0] > distr.shape[0]:
                            distr += alpha * _distr[:distr.shape[0]]
                        elif _distr.shape[0] < distr.shape[0]:
                            distr = distr[:_distr.shape[0]]
                            distr += alpha * _distr
                    except Exception as e:
                        print(f"_distr: {_distr}")
                        print(f"distr: {distr}")
                        print(f"Error;\n{e}\n")

        # If no alpha above threshold,. put max alpha
        if (type(distr) == int):
            pigment = pigments_dict[name_max_alpha]
            distr = pigment['xrf']['y'] #get_distr_from_infraart_h5(pigment['xrf'], rebin_hist=rebin_hist, rebin_size=rebin_size)

            list_of_pigments.append(
                {
                    'alpha': max_alpha,
                    'pigment': name_max_alpha
                }
            )
        # Else, normal attribution
        else:
            distr = distr/total_alpha
            distr = distr/distr.sum()

        return distr
    
    ###########################################
    # Static methods
    ###########################################
    
    @staticmethod
    def get_xrf_distr(num_of_counts, distr):
        return np.bincount(
            np.random.choice(
                np.arange(0, distr.size),
                size=num_of_counts,
                p=distr
            ),
            minlength = distr.size
        )
    
    @staticmethod
    def slow_get_xrf_distr_2D(num_of_counts, distr, size):
        xrf = np.zeros([size[0]*size[1], distr.size])

        for idx in range(size[0]*size[1]):
            xrf[idx] = XRFGenerator.get_xrf_distr(num_of_counts, distr)

        return xrf.reshape(size[0], size[1], distr.size)
    
    @staticmethod
    def get_xrf_distr_2D(num_of_counts: int, distr: np.array, size: tuple) -> np.array:
        """_summary_
        Static method to randomly generate A fake MA-XRF rank-3 tensor out of a unitary distribution

        It works this way:
            1. Extract randomly (height*width, num_of_counts)-elements out of a distribution
            2. Use the staticmethod bincount2d to parse the extracted counts into a histogram.
        
        Args:
            num_of_counts   (int)       : Number of extractions. It is the number of synthetic photon scintillations.
            distr           (np.array)  : Unitary XRF distribution.
            size            (tuple)     : Shape (height, width) of the MA-XRF.

        Returns:
            np.array: generated XRF of shape (size[0], size[1], distr.shape[0]) and with num_of_counts.
        """
        rng = np.random.default_rng()
        return XRFGenerator.bincount2d( 
            rng.choice(
                distr.size,
                size=(size[0]*size[1], num_of_counts),
                p=distr,
                axis=-1
            )
        ).reshape(size[0], size[1], distr.size)
    
    @staticmethod
    def bincount2d(arr: np.array, bins=None) -> np.array:
        """_summary_
        Static method to compute a 2D bincount.

        It does:
            0. If bins is None, set it to the max in arr, +1. 
                (so the final shape is either bins or np.max(arr)).
            1. Initialise the np.array to be returned as a zero-filled array of shape (len(arr), bins)
            2. COmpute the indexig array (i.e. the array of elements to be counted)
            3. Using the np.add.at method, add 1 to the count array the appropriate number of time at the appropriate index
        
        Args:
            arr     (np.array)      : 2D array to be rebinned
            bins    (int, optional) : Final size. Defaults to None.

        Returns:
            np.array    : 2D bincounted array 
        """
        # thanks to https://stackoverflow.com/questions/19201972/can-numpy-bincount-work-with-2d-arrays
        if bins is None:
            bins = np.max(arr) + 1
        count = np.zeros(shape=[len(arr), bins], dtype=np.int64)
        indexing = (np.ones_like(arr).T * np.arange(len(arr))).T
        np.add.at(count, (indexing, arr), 1)

        return count
