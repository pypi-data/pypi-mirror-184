# ganX - a python library to generate MA-XRF raw data out of RGB images

ganX (*generate artificially new XRF*) is a small library to generate Macro mapping X-ray fluorescence (MA-XRF) images out of an RGB input image, and a dictionary comprising pigments' RGBs and characteristic XRF signals.

To generate a synthetic MA-XRF data, it performs the following steps: 

1. Use an interative KNN unsupervised clustering on the RGB space to extract a set of RGB clusters, thus replacing the original RGB with a clustered RGB.
2. Starting from the clustered RGB, it associates a pigment (or a list of pigments) to the colour, by computing the distance of the cluster RGB to the pigments RGB in CIELAB colour space.
3. After that, it builds a distribution out of a weighted average of the pigments distribution found; this distribution is used to randomly generate the XRF signal via a Montecarlo simulation.

Additionaly, the library offers other classes and methods to explore the XRF dataset.

--------------

## Usage

To generate a MA-XRF raw data out of a RGB image, you may call the ```XRFGenerator ``` as
```python
# generator
from ganx.XRF_generator_classes import XRFGenerator
# utils
from ganx.RGB_segmentation_utils import RGBMethods
# open RGB
ex_rgb = rgbMethods.open_image(file_name=file, root_path_to_rgb=subdir)

# init XRF Generator class
_xrf_generator = XRFGenerator(
    # PigmentDataBaseUtils
    pigments_dict_data = pigments_dict_data,
    # RGBKMeansClustering
    rgb_img = ex_rgb,
    N_start = 10, 
    # PigmentDataBaseUtils 
    E_int = [0.5, 38.5],
    rebin_size = 1024,
    # RGBKMeansClustering
    delta_N = 1,
    N_patience = -1,
    score_batch = 1024 
)

# generate XRF 
generated_XRF = _xrf_generator.generate_xrf() 
```
In this exaple, the class ```rgbMethods.open_image``` was used to open the RGB image; users may use their favourite system to open RGB images; ```XRFGenerator``` needs a ```np.array``` of shape ```(height, width, 3|4)```.

If users want to generate a set of MA-XRF out of a set of RGBs, they may use the function ```generate_all``` as
```python
from ganx import generate_all

rootdir = 'path/to/RGB/'
storedir = 'path/to/XRF/'
pigments_dict_data = 'path/to/pigments_dict.json'

generate_all(
    rootdir = rootdir,
    storedir = storedir,
    pigments_dict_data = pigments_dict_data,
)
```

## Code Contents

The ganX project defines three main classes:

1. **MAXRF**: A class defining a MA-XRF object. 
2. **RGBKMeansClustering**: Class for computing iterative KMeans.
3. **XRFGenerator** : Class to perform the MA-XRF generations out of a RGB image. 

those are based on, and use, other classes:

- *XRFUtils*: A class exposing static methods for manipulating XRF data.
- *IterativeKMeans*: Class for computing iterative KMeans Clustering.
- *RGBMethods*: Class offering static methods for plotting of RGB images, clustered or not.
- *PigmentDataBaseUtils*: Class to initialise and use the Pigment XRF - RGB database. 
- *Distances*: Classes furnishing static methods to compute distances in RGB space.

### In depth description

#### MAXRF_class 

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
    
<details>
<summary>XRFUtils</summary>

A class exposing static methods for manipulating XRF data.

Static Methods

    rebin_ma_xrf(img: np.array, n_bins: int = 500)              :   Function to rebin a rank-3 MA-XRF np.array. 

    get_index_from_energy(en: float, _x: np.array)              :   Static method to get the index out of an energy arange.

    convolve_xrf(xrf: np.array, kernel : np.array = _default )  :   Static method to convolve spatially a MA-XRF np.array. (i.e., along axis = 0,1).
    
    open_file(path_to_file: str, key: str = 'img')              :   Method to open a .h5 or .npz file and initialise a MA-XRF np.array.

--------

    XRFUtils.rebin_ma_xrf(img: np.array, n_bins: int = 500) -> np.array
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

    XRFUtils.get_index_from_energy(en: float, _x: np.array) -> int
        Static method to get the index out of an energy arange. 

        Args:
            en (float)      : Energy value (in keV) to extract the index.
            _x (np.array)   : Energy np.arange ndarray representing the energy region.
                                _x = np.arange(E_i, E_f, delta_E)
        Returns:
            int :   Index of en in _x
    

    
    XRFUtils.convolve_xrf(xrf: np.array, kernel : np.array = np.array([[1,2,1],[2,4,2],[1,2,1]])) -> np.array
        Static method to convolve spatially a MA-XRF np.array. (i.e., along axis = 0,1).

            Args:
                xrf     (np.array)          :   Input MA-XRF np.array
                kernel  (np.array, optional):  2D kernel to perform the 2D convolution. Defaults to np.array( [ [1,2,1], [2,4,2], [1,2,1] ] ).

            Returns:
                np.array    : Convolved MA-XRF np.array
    
    XRFUtils.open_file(path_to_file: str, key: str = 'img')
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

</details>

<details>
<summary>MAXRF(XRFUtils)</summary>
A class defining a MA-XRF object. 
It extends XRFUtils adding internal args (the MA-XRF) and methods to analyse the MA-XRF.

Attributes
    
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


    init_XRFLines(self, path_to_json: str)                          :   Method to open the JSON file containing the XRFLines and set the self.XRFLines arg. 
    
    init_calibration_data(self, E_min: float, E_max: float)         :   Method to initialise the calibration data _E_int, _delta_E, _E_range_x_axis.
    
    get_X_line_image(self, el: str, delta_Energy_plot: float = 0.5) :   Method to compute the integrated image out of a selected XRF element line, e.g. Pb (La). 

Static methods:
    
    get_key_from_value(mydict: dict, value)                     :   Static method to extract a key from a value.
    
    get_element_name_from_value(XRFvalues: list, value: float)  :   Utils for extracting element name from element value in XRFLines lines(dict).
    
    utils for extracting element value from element name        :   utils for extracting element value from element name
  
-----------------
    
    
</details>

#### RGB_segmentation_utils

File containing the Python classes for performing iterative KMeans clustering on an RGB image.

It contains the following classes:
    1. IterativeKMeans
        Class for computing iterative KMeans.
    2. RGBMethods
        Class offering static methods for plotting of RGB images, clustered or not.
    3. RGBKMeansClustering(RGBMethods, IterativeKMeans)
        Class for computing iterative KMeans.
More details on the classes are reported in the classes docstrings. 

The class architecture is (From Parent to child):

    1   2
     \ /
      3
or

    IterativeKMeans                  RGBMethods
            \                       /
                RGBKMeansClustering

<details>
<summary>IterativeKMeans</summary>
Class for computing iterative KMeans Clustering.
    
The iteration is performed over the number of clusters. 
The performance for each iteration is computed using the Silhouette score. 

Attributes
----------

Init values:
    
    _N_start    (int)   :   Central value for the iteration. It is the central number of cluster
    
    _delta_N    (int)   :   (Optional; default = 3) Delta value; 
    
                            the iteration will be performed from _N_start - _delta_N to _N_start + _delta_N.
    
    _N_patience (int)   :   (Optional; default = -1) Patience in iteration steps before breaking iterations.
                            If after _N_patience epochs we see no improvement, we break the cycle.
    
    score_batch (int)   :   (Optional; default = 1024) Batch value used in MiniBatchKMeans to speed up the process. 
                            if value `<` 0 are inserted, it is set up to +inf; in this case, MiniBatchKMeans becomes
                            a standard KMeans

Additional attributes:
    
    Internal params:
    
    _N_min  (int)               :   Minimal n_cluster parameter used in iteration; the check on it is:
                                        self._N_start - self._delta_N if self._N_start - self._delta_N > 2 else 2
    
    _N_max  (int)               :   Maximal n_cluster parameter used in iteration.
    
    _X      (None | np.array)   :   Internal input array X used in fit `&` prediction.

    Results:
    
    _segmented      (None | np.array)           :   Result of the training process. 
    
    _idx_best       (None | int)                :   Iteration Index of best result.
    
    _best_KMeans    (None | MiniBatchKMeans)    :   Best performing MiniBatchKMeans
    
    __scores        (None | list)               :   List of epoch's score.


Methods 
----------

Extension of sklearn KMeans:
    
    fit(X: np.array) -> None                                        :  Compute KMeans fit 
    
    fit_predict(X: np.array) -> None | np.array                     :  Compute KMeans fit_predict and returns the prediction
    
    predict(X: np.array, use_best: bool = True) ->  None | np.array :  Compute KMeans predict

Custom methods:
    
    set_X(X: np.array) -> None : Set X
    
    compute_score(X: np.array) -> float : Compute the Silhouette score
    
    iter_step(n_clusters: int) -> None  : Method to perform of a single iteration's step
    
    cluster_train(X: np.array) -> None  : Iteration method
    
    cluster_train_predict(X: np.array) -> None | np.array   : Perform both Iteration and prediction

Visualization utils:
    
    show_training_stats(
        _figsize: tuple = (12, 8), 
        axis_fontsize: int = 15, 
        title_fontsize: int = 18
    ) -> None                           : Method to plot the training history
    
</details>

<details>
<summary>RGBMethods</summary>
Class offering static methods for plotting of RGB images, clustered or not.


Static Methods:
    
    open_image(file_name: str, root_path_to_rgb: str = './Synthetic_data/RGB/') : Open image with filename file_name located in root path root_path_to_rgb.
    
    show_image(_img: np.array, _figsize: tuple = (12, 8))                       : Method to plot RGB image
    
    return_label_image(segmented: np.array, cluster_idx: int)                   : Method to get greyscale cluster image with index cluster_idx from segmented
    
    show_label_image(segmented: np.array, cluster_idx: int)                     : Method to plot greyscale cluster image with index cluster_idx from segmented

    
    return_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int)    :   Method to get a single cluster in RGB space; 
    
    show_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int)      :   Method to plot a single cluster in RGB space; 
    
</details>

<details>
<summary>RGBKMeansClustering</summary>

Class for computing iterative KMeans.
    
The iteration is performed over the number of clusters. 
The performance for each iteration is computed using the Silhouette score. 

Attributes
----------

IterativeKMeans __init__() Attributes:
    
    _N_start    (int)   :   Central value for the iteration. It is the central number of cluster
    
    _delta_N    (int)   :   (Optional; default = 3) Delta value; 
    
                            the iteration will be performed from _N_start - _delta_N to _N_start + _delta_N.
    
    _N_patience (int)   :   (Optional; default = -1) Patience in iteration steps before breaking iterations.
    
                            If after _N_patience epochs we see no improvement, we break the cycle.
    
    score_batch (int)   :   (Optional; default = 1024) Batch value used in MiniBatchKMeans to speed up the process. 
                            if value `<` 0 are inserted, it is set up to +inf; in this case, MiniBatchKMeans becomes
                            a standard KMeans

New Attributes:
    
Init Params
    
    rgb_img (np.array)  : RGB image to be clustered.

    Internal params:
    
    _rgb_shape  (tuple) : Shape of the RGB image to be clustered.

Result params:
    
    segmented_iter  (None | np.array)   :   Result of the IterativeKMeans iteration;
    
reshaped_segmented_iter (None | np.array)   :   Its reshaped version.
    
    clustered_rgb   (None | np.array)   :   Clustered RGB;
    
    list_of_rgbs    (None | np.array)   :   List of single cluster in RGB space; 

Methods
----------

Class methods:
    
    cluster_rgb() -> np.array                       :   Main method. It performs the whole pipeline, returning the clustered RGB image.
    
    compute_clustered_rgb_from_segmented() -> None  :   Method to compute the clustered RGB out of the segmented tensor.

Viz Methods:
    
    show_average_rgb_clusters(_figsize: tuple = (12,8), _title_fontsize: int = 18)                                      :   Method to plot the computed average RGB cluster.
    
    confront_clustered_with_unclustered(plot_diff: bool = True, _figsize: tuple = (12,8), _title_fontsize: int = 18)    :   Method to confront original RGB with Clustered one.

Static methods:
    
    plot_grey_scale_confront(A: np.array, B: np.array, _figsize: tuple = (12,8),  _title_fontsize: int = 18)    :   Method to confront original RGB with Clustered one in greyscale.

</details>

#### XRF_generator_classes
File containing the Python classes for generating a synthetic MA-XRF .h5 file starting from an RGB.

It imports 
    A. RGBKMeansClustering ( from RGB_segmentation_utils )
    B. XRFUtils ( from MAXRF_class )

It contains the following classes:
    1. PigmentDataBaseUtils(XRFUtils)
    2. Distances
    3. XRFGenerator
    
<details>
<summary>PigmentDataBaseUtils(XRFUtils)</summary>
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
</details>

<details>
<summary>Distances</summary>
Classes furnishing static methods to compute distances in RGB space.

Static Methods
--------------
    
    cosine_similarity(x, y) :   returns the cosine similarity
    
    rgb2lab( rgb )          :   returns the CIELAB image
    
    CIEdelta1994_similarity(rgb1, rgb2) :   returns the similarity using the CIEdelta1994 distance
    
    CIEdelta2000_similarity(rgb1, rgb2) :   returns the similarity using the CIEdelta2000 distance
</details>

<details>
<summary>XRFGenerator</summary>
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
</details>