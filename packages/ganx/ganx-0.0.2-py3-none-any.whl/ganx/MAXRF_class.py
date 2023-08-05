#############################################################################################################################
# C: INFN                                                                                                                   #
#                                      CLASSES TO MANIPULATE XRF IMAGES                                                     #
# dev: Alessandro Bombini, INFN                                                                                             #
#############################################################################################################################

"""
File containing the Python classes for manipulating MA-XRF np.array data.

It contains the following classes:
    1. XRFUtils
        A class exposing static methods for manipulating XRF data
    2. MAXRF(XRFUtils)
        A class extending XRFUtils; it defines the MA-XRF object, furnishing few methods for analysing MA-XRF; 
            NB: To Be Finished; it has basics methods and args for the purpose of the XRF_generator_classes

The class architecture is (From Parent to child):
    XRFUtils 
        |
        |
    MAXRF
"""

import os

import numpy as np
import h5py
import matplotlib.pyplot as plt
import json
from scipy import signal

class XRFUtils:
    """_summary_
    A class exposing static methods for manipulating XRF data.
    
    Static Methods
        rebin_ma_xrf(img: np.array, n_bins: int = 500)              :   Function to rebin a rank-3 MA-XRF np.array. 
        get_index_from_energy(en: float, _x: np.array)              :   Static method to get the index out of an energy arange. 
        convolve_xrf(xrf: np.array, kernel : np.array = _default )  :   Static method to convolve spatially a MA-XRF np.array. (i.e., along axis = 0,1).
        open_file(path_to_file: str, key: str = 'img')              :   Method to open a .h5 or .npz file and initialise a MA-XRF np.array.
    ----------

    """
    import os
    import numpy as np
    import h5py
    from scipy import signal
    
    def __init__(self):
        pass
    
    ################################################
    # Static methods
    ################################################
    
    @staticmethod
    def rebin_ma_xrf(img: np.array, n_bins: int = 500) -> np.array:
        """_summary_
        Function to rebin a rank-3 MA-XRF np.array. 

        It employs at most the numpy slicing to speed-up the rebin process. 

        How it works: 
            1. Compute the divisor, 
                i.e. the integer division of the original number of bins vs the wanted number of bins;
            2. if divisor > 1, i.e. rebinning needed, proceds; 
                else; returns original.
            3. Do rebinning:
                i.  Init rebinned tensor as empty 
                        np.zeros( shape = [img.shape[0], img.shape[1], n_bins] )
                ii. iterate over range(divisor) = [0, 1, ..., divisor-1]:
                    a. at each step, get the view of the original MA-XRF keeping only the bins multiple of step, 
                        i.e. step, step + 1*divisor, step + 2*divisor, ...
                    b. sums it to the rebinned tensor. 
                iii.Return rebinned.
        Args:
            img     (np.array)      : XRF rank-3 tensor.
            n_bins  (int, optional) : Wanted number of energy bins in output. Defaults to 500.

        Raises:
            Exception   :   Raises an exception if XRF has no valid shape, i.e. is not a rank-3 tensor.

        Returns:
            np.array    :   Rebinned MA-XRF
        """
        if len( img.shape ) != 3:
            raise Exception(f"Inserted XRF has no valid shape;\nshape found: {img.shape}")
        _original_hist_size = img.shape[-1]
        divisor = _original_hist_size // n_bins
        #rebinning
        if divisor > 1:
            rebinned = np.zeros(
                [img.shape[0], img.shape[1], n_bins],
                dtype = np.uint16 # 16-bit unsigned integer (0 to 65_535). 
            )

            for step in range(divisor):
                _temp = img[
                    :,:,
                    # start : end : step
                    step : _original_hist_size : divisor
                ]
                rebinned += _temp[:,:, :n_bins  ]

            return rebinned
        # no rebinning
        else:
            print(f"No binning needed.")
            return img

    @staticmethod
    def get_index_from_energy(en: float, _x: np.array) -> int:
        """_summary_
        Static method to get the index out of an energy arange. 

        Args:
            en (float)      : Energy value (in keV) to extract the index.
            _x (np.array)   : Energy np.arange ndarray representing the energy region.
                                _x = np.arange(E_i, E_f, delta_E)

        Returns:
            int :   Index of en in _x
        """
        for index, e in enumerate(_x):
            if e>=en:
                return index
            
    @staticmethod
    def convolve_xrf(
        xrf: np.array, 
        kernel : np.array = np.array(
            [
                [1,2,1],
                [2,4,2],
                [1,2,1]
            ]
        )
    ) -> np.array:
        """_summary_
        Static method to convolve spatially a MA-XRF np.array. (i.e., along axis = 0,1).

        Args:
            xrf     (np.array)          :   Input MA-XRF np.array
            kernel  (np.array, optional):  2D kernel to perform the 2D convolution. Defaults to np.array( [ [1,2,1], [2,4,2], [1,2,1] ] ).

        Returns:
            np.array    : Convolved MA-XRF np.array
        """
        # Init result
        result = np.zeros(xrf.shape)
        # iterate over energy range
        for k in range(0, xrf.shape[-1]):
            # Spatially convolve
            result[:, :, k] = signal.convolve2d(xrf[:, :, k], kernel, boundary='symm', mode='same')

        return result
    
    @staticmethod
    def open_file(path_to_file: str, key: str = 'img'):
        """_summary_
        Method to open a .h5 or .npz file and initialise a MA-XRF np.array.

        Args:
            path_to_file    (str)           : Path to MA-XRF HDF5 or npz file.
            key             (str, optional) : Dataset key. Defaults to 'img'.
                                                NB: the standard LABEC HDF5 file (or NPZ file) is a dataset with metadata and data. 
                                                    MA-XRF data are stored as rank-3 tensor into the 'img' name. 

        Raises:
            Exception   :   if os.path.isfile returns false, i.e. no file found.
            Exception   :   If the extension is neither .h5 nor .npz

        Returns:
            np.array : Loaded np.array
        """
        if not os.path.isfile(path_to_file):
            raise Exception(f"File {path_to_file} not found.")
        
        _ext = path_to_file.split('.')[-1]
        if _ext == 'h5':
            loaded_hf = h5py.File(
                path_to_file, 
                'r'
            )
            return np.array(
                loaded_hf.get(key)
            )
        elif _ext == 'npz':
            return np.array(np.load(path_to_file)[key])
        else: 
            raise Exception(f"The file extension {_ext} is not supported.")

#
class MAXRF(XRFUtils):
    """_summary_
    A class defining a MA-XRF object. 
    It extends XRFUtils adding internal args (the MA-XRF) and methods to analyse the MA-XRF.

    Attributes
    ----------
        img     (np.array)      : XRF rank-3 tensor.
        n_bins  (int, optional) : Wanted number of energy bins in output. Defaults to 1024.

    Additiona Args
        XRFLines (None | list)  : Dictionary of the XRF Lines. 
                                    Note: it has to have the form of list(dict), 
                                    where each list item has to be
                                    {
                                        "element"   : (str)     # element line name - Siegbahn notation
                                        "value"     : (float)   # element line value (keV)
                                    }
        _E_int  (None | list)   : List list(float) of energy interval. len(_E_int) = 2. 
                                    Note: _E_int = [E_i, E_f]
        _delta_E(None | float)  : Bin size in energy.
        _E_range_x_axis (None | np.array)   : np.array describing the energy range;
                                                np.arange(_E_int[0], _E_int[1], _delta_E)

    Methods
    ----------

        init_XRFLines(self, path_to_json: str)                          :   Method to open the JSON file containing the XRFLines and set the self.XRFLines arg. 
        init_calibration_data(self, E_min: float, E_max: float)         :   Method to initialise the calibration data _E_int, _delta_E, _E_range_x_axis.
        get_X_line_image(self, el: str, delta_Energy_plot: float = 0.5) :   Method to compute the integrated image out of a selected XRF element line, e.g. Pb (La). 
    
    Static methods:
        get_key_from_value(mydict: dict, value)                     :   Static method to extract a key from a value. 
        get_element_name_from_value(XRFvalues: list, value: float)  :   Utils for extracting element name from element value in XRFLines lines(dict).
        utils for extracting element value from element name        :   utils for extracting element value from element name
    """
    import os
    import numpy as np
    import h5py
    import json
    from scipy import signal
    
    ###########################################
    # init
    ###########################################
    
    def __init__(self, xrf: np.array, n_bins: int = 1024):
        """_summary_
        Init method. Sets the args.

        Args:
            img     (np.array)      : XRF rank-3 tensor.
            n_bins  (int, optional) : Wanted number of energy bins in output. Defaults to 1024.

            XRFLines (None | list)  : Dictionary of the XRF Lines. 
                                        Note: it has to have the form of list(dict), 
                                        where each list item has to be
                                        {
                                            "element"   : (str)     # element line name - Siegbahn notation
                                            "value"     : (float)   # element line value (keV)
                                        }
            _E_int  (None | list)   : List list(float) of energy interval. len(_E_int) = 2. 
                                        Note: _E_int = [E_i, E_f]
            _delta_E(None | float)  : Bin size in energy.
            _E_range_x_axis (None | np.array)   : np.array describing the energy range;
                                                    np.arange(_E_int[0], _E_int[1], _delta_E)


        Raises:
            Exception   :   Raises exception if the XRF rank-3 tensor. has an invalid shape.
        """
        # Init XRFUtils
        super().__init__()
        
        # init new params
        if len( xrf.shape ) != 3:
            raise Exception(f"Inserted XRF has no valid shape;\nshape found: {xrf.shape}")
        self._xrf = self.rebin_ma_xrf(xrf, n_bins)
        
        # Additional args
        
        # XRFLines
        self.XRFLines = None
        # Calibration data
        self._E_int = None
        self._delta_E = None
        self._E_range_x_axis = None
    
    ###########################################
    # Additional methods
    ###########################################
    
    def init_XRFLines(self, path_to_json: str):
        """_summary_
        Method to open the JSON file containing the XRFLines and set the self.XRFLines arg. 

        Args:
            path_to_json    (str)   :   Path to the JSON file containing the XRFLines. 
                                            Note: it has to have the form of list(dict), 
                                                where each list item has to be
                                                {
                                                    "element"   : (str)     # element line name - Siegbahn notation
                                                    "value"     : (float)   # element line value (keV)
                                                }

        Raises:
            Exception   :   Raises an exception if the file does not exists or if it is not a json file. 
        """
        if (
            not os.path.isfile(path_to_json)
        ) or (
            path_to_json.split('.')[-1] != 'json'
        ):
            raise Exception(f"Path {path_to_json} invalid; no valid file found.")
        
        with open(path_to_json) as test:
            _dict_data = test.read()
        
        self.XRFLines = json.loads( _dict_data )
    
    def init_calibration_data(self, E_min: float, E_max: float):
        """_summary_
        Method to initialise the calibration data _E_int, _delta_E, _E_range_x_axis.

        Args:
            E_min (float): Left  enrgy bound (in keV)
            E_max (float): Right enrgy bound (in keV)

        Raises:
            Exception : Raises an exception if E_min is bigger than E_max
        """
        if E_min>= E_max:
            raise Exception(f"E_min is bigger than E_max.\nPlease insert valid Energy range (in keV).")
        
        self._E_int = [E_min, E_max]
        self._delta_E = ( E_max - E_min ) / self._xrf.shape[-1]
        self._E_range_x_axis = np.arange(
            self._E_int[0], self._E_int[1], 
            self._delta_E
        )        
    
    def get_X_line_image(self, el: str, delta_Energy_plot: float = 0.5) -> np.array:
        """_summary_
        Method to compute the integrated image out of a selected XRF element line, e.g. Pb (La). 

        Args:
            el                  (str)               : Name of the element line.
            delta_Energy_plot   (float, optional)   : integrationdelta energy (in keV). Defaults to 0.5.

        Raises:
            Exception: Raises an exception if the XRFLines are not initialised.
            Exception: Raises an exception if the Calibration data are not initialised. 

        Returns:
            np.array    : Greyscale matrix representing the integrated element line image. 
        """
        if not self.XRFLines:
            raise Exception(f"XRFLines not properly initialised.")
            
        if self._E_int == None:
            raise Exception(f"Calibration data not initialised.")
            
        el_en = self.get_value_from_element_name( XRFvalues = self.XRFLines, el_line_name = el )
        if el_en == None:
            print(f"Element not found")
            
            return self._xrf.sum(axis=-1)
            
        en_1 = np.clip(
            el_en - delta_Energy_plot, 
            self._E_int[0], self._E_int[1]
        )
        en_2 = np.clip(
            el_en + delta_Energy_plot, 
            self._E_int[0], self._E_int[1]
        )
        
        idx_1 = self.get_index_from_energy(en_1, self._E_range_x_axis)
        idx_2 = self.get_index_from_energy(en_2, self._E_range_x_axis)
        
        return self._xrf[
            :,:,
            idx_1:idx_2
        ].sum(axis=-1)
            
    ###########################################
    # Static methods
    ###########################################
    @staticmethod
    # utils for retrieving dict key from value
    def get_key_from_value(mydict: dict, value) -> list:
        """_summary_
        Static method to extract a key from a value. 

        Args:
            mydict  (dict)  : Dictionary from whom we extract the value
            value   (any)   : Value

        Returns:
            list    : list of keys with value in mydict
        """
        return list(mydict.keys())[list(mydict.values()).index(value)]

    # utils for extracting element name from element value
    @staticmethod
    def get_element_name_from_value(XRFvalues: list, value: float) -> str:
        """_summary_
        Utils for extracting element name from element value in XRFLines lines(dict).

        Args:
            XRFvalues   (list)  : XRFLines lines(dict)
            value       (float) : Element Line value (in keV)

        Returns:
            str :   Extracted value
        """
        for el in XRFvalues:
            if el['value'] == value:
                return el['element']
        return ''
    
    # utils for extracting element value from element name
    @staticmethod
    def get_value_from_element_name(XRFvalues: list, el_line_name: str) -> float:
        """_summary_
        utils for extracting element value from element name

        Args:
            XRFvalues       (list)  : XRFLines lines(dict)
            el_line_name    (str)   : Element Line name in Siegbahn notation (e.g. 'Pb (La)')

        Returns:
            float   :   extracted value (in keV)
        """
        for el in XRFvalues:
            if el['element'] == el_line_name:
                return el['value']            
        return None
