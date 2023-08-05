#############################################################################################################################
# C: INFN                                                                                                                   #
#                                        CLASSES TO CLUSTER RGB Images                                                      #
# dev: Alessandro Bombini, INFN                                                                                             #
#############################################################################################################################

"""
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

"""

import numpy as np
import PIL
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score


class IterativeKMeans:
    """
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
                                if value < 0 are inserted, it is set up to +inf; in this case, MiniBatchKMeans becomes
                                a standard KMeans
    
    Additional attributes:
        Internal params:
        _N_min  (int)               :   Minimal n_cluster parameter used in iteration; the check on it is:
                                            self._N_start - self._delta_N if self._N_start - self._delta_N > 2 else 2
        _N_max  (int)               :   Maximal n_cluster parameter used in iteration.
        _X      (None | np.array)   :   Internal input array X used in fit & prediction.
        
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

    """
    import numpy as np
    from sklearn.cluster import MiniBatchKMeans
    from sklearn.metrics import silhouette_score
    import matplotlib.pyplot as plt
    
    ################################################
    # Init
    ################################################
    
    def __init__(self, N_start: int, delta_N: int = 3, N_patience: int = -1, score_batch: int = 1024):
        """_summary_
        Class __init__ method. 

        Args:
            N_start     (int)           :   Central value for the iteration. It is the central number of cluster
            delta_N     (int, optional) :   Delta value; the iteration will be performed from 
                                                _N_start - _delta_N to _N_start + _delta_N . 
                                            Defaults to 3.
            N_patience  (int, optional) :   Patience in iteration steps before breaking iterations.
                                            If after _N_patience epochs we see no improvement, we break the cycle.
                                            Defaults to -1.
            score_batch (int, optional) :   Maximal n_cluster parameter used in iteration. 
                                            Defaults to 1024.

        Raises:
            Exception: Raises exception if _score_batch has not been properly parsed. 
        """
        # init params
        self._N_start = N_start
        self._delta_N = delta_N
        self._N_patience = N_patience
        
        self._N_min = self._N_start - self._delta_N if self._N_start - self._delta_N > 2 else 2
        self._N_max = self._N_start + self._delta_N
        
        # Init clustering method
        self._KMeans = None
        # Result
        self._segmented = None
        # Init best index
        self._idx_best = -1
        self._best_KMeans  = None
        # Init iteration results
        self._scores = []
        self._score_batch = score_batch if score_batch > 0 else np.inf
        if self._score_batch < 0:
            raise Exception("Invalid score_batch value inserted; must be a positive integer number.") 
            
        # Init internal data
        self._X = None
    
    ################################################
    # Extension of sklearn KMeans
    ################################################
    
    def fit(self, X: np.array):
        """_summary_
        Compute KMeans fit 

        Args:
            X (np.array)    : Input array for the KMeans clustering fit.

        Raises:
            Exception   : Raises exception if X has not the wanted Sci-Kit learn shape: (n_samples, n_features)
        """
        if len(X.shape) != 2:
            raise Exception("The X variable must be of shape (n_samples, n_features)") 
        # Compute KMeans Fit
        self._KMeans.fit(X)
        
    def fit_predict(self, X: np.array):
        """_summary_
        Compute KMeans fit_predict and returns the prediction

        Args:
            X (np.array)    :   Input array for the KMeans clustering fit.

        Raises:
            Exception   :   Raises exception if X has not the wanted Sci-Kit learn shape: (n_samples, n_features)

        Returns:
            None | np.array :   Predicted cluster labels 
        """
        if len(X.shape) != 2:
            raise Exception("The X variable must be of shape (n_samples, n_features)") 
        # Compute KMeans Fit Predict
        self._segmented = self._KMeans.fit_predict(X)
        
        return self._segmented
        
    def predict(self, X: np.array, use_best: bool = True):
        """_summary_
        Compute KMeans predict

        Args:
            X (np.array)                :   Input array for the KMeans clustering fit.
            use_best (bool, optional)   :   Parameter to use best trained model. Defaults to True.

        Raises:
            Exception   :   Raises exception if X has not the wanted Sci-Kit learn shape: (n_samples, n_features)

        Returns:
            None | np.array :   Predicted cluster labels 
        """
        if len(X.shape) != 2:
            raise Exception("The X variable must be of shape (n_samples, n_features)") 
        return self._best_KMeans.predict(X) if use_best and self._best_KMeans else self._KMeans.predict(X) 
                    
    ################################################
    # Custom methods
    ################################################
    # Setter X
    def set_X(self, X: np.array):
        """_summary_
        Setter method for the internal X variable, used in fit & prediction.

        Args:
            X   (np.array)  :   Internal input array X used in fit & prediction.

        Raises:
            Exception   :   Raises exception if X has not the wanted Sci-Kit learn shape: (n_samples, n_features)
        """
        if len(X.shape) != 2:
            raise Exception("The X variable must be of shape (n_samples, n_features)") 
        # Set X
        self._X = X    
        
    # score
    def compute_score(self, X: np.array):
        """_summary_
        Compute the Silhouette score 

        Args:
            X   (np.array)  :   Internal input array X used to compute the Silhouette score

        Raises:
            Exception   :   Raises exception if X has not the wanted Sci-Kit learn shape: (n_samples, n_features)

        Returns:
            float   :   Computed Silhouette score
        """
        if len(X.shape) != 2:
            raise Exception("The X variable must be of shape (n_samples, n_features)") 
            
        s_score =  silhouette_score(
            X, 
            self._KMeans.labels_,
            metric='euclidean',
            sample_size = min(self._score_batch, len(self._KMeans.labels_) )
        )
        
        return s_score
    
    # function of a single iteration
    def iter_step(self, n_clusters: int):
        """_summary_
        Method for the single step in the iteration. 
        It performs the MiniBatchKMeans init, fit & prediction.

        Steps:
            1. Init MiniBatchKMeans;
            2. Fit & Predict MiniBatchKMeans;
            3. Compute score
                3.1. Append it to self._scores
            4. Update best model if needed.
                |- It is updated only if 
                    a. it is the zeroth-step 
                        (i.e.: len(self._scores) == 0 );
                    b. It is the best scores
                        (i.e.: np.argmax(self._scores) + 1 == len(self._scores) )

        Args:
            n_clusters (int): _description_
        """
        # 1. Init
        self._KMeans = MiniBatchKMeans(
            n_clusters = n_clusters
        )
        
        # 2. Fit&Predict
        _ = self.fit_predict(self._X)
        
        # 3. Compute score
        s_score = self.compute_score(self._X)
        # 3.1. Append score
        self._scores.append(
            s_score
        )
        
        # Update best model if needed
        if len(self._scores) == 0 or np.argmax(self._scores) + 1 == len(self._scores):
            self._idx_best = len(self._scores)
            self._best_KMeans  = self._KMeans
            
        print(f"Step {len(self._scores)} (n_clusters = {n_clusters}) concluded with score: {s_score}")
            
    # Iteration function
    def cluster_train(self, X: np.array):
        """_summary_
        Method to perform the whole iterations. 

        Steps:
            1. Set X
            2. Iterate over the interval 
                    (i.e.: range(self._N_min, self._N_max) )
                
                Each iteration calls:
                    a. Perfomer single step via
                        self.iter_step( n_clusters = n_clusters )
                    b. Check patience; if overcomed, break the loop



        Args:
            X   (np.array)  :   Internal input array X used to perform the Fit, Predict and Score computations.

        """
        print(f"Starting training with n_clusters in {(self._N_min, self._N_max)}\n")
        # set X
        self.set_X(X)
        # iterate
        for _idx, n_clusters in enumerate(range(self._N_min, self._N_max)):
            # iterate
            self.iter_step( n_clusters = n_clusters )
            # check patience, else break
            if self._N_patience > 0 and len(self._scores) >= self._N_patience and (len(self._scores) - np.argmax(self._scores) + 1) > self._N_patience:
                print(f"Early stopping condition found at epoch {_idx}.")
                # break cycle
                break
        
    # Iteration function + prediction  
    def cluster_train_predict(self, X: np.array):
        """_summary_
        Method to perform the whole iterations AND the prediction.

        It simply calls:
            1. self.cluster_train(X = X)
            2. self.predict(X = X, use_best = True)
        
        Args:
            X   (np.array)  :   Internal input array X used to perform the Fit, Predict and Score computations.

        Returns:
            None | np.array :   Predicted cluster labels 
        """
        self.cluster_train(X = X)
        print(f"Training finished.")
        print(f"Best model has n_cluster = {self._best_KMeans.labels_.max() + 1}.\nSilhouette score best model: {np.array(self._scores).max()}")
        return self.predict(X = X, use_best = True)
        
    # Viz util funciton
    def show_training_stats(self, _figsize: tuple = (12, 8), axis_fontsize: int = 15, title_fontsize: int = 18):
        """_summary_
        Util Method for plotting training statistics. 

        Args:
            _figsize        (tuple, optional)   : Fig size. Defaults to (12, 8).
            axis_fontsize   (int, optional)     : Fontsize for the X- and Y- axes. Defaults to 15.
            title_fontsize   (int, optional)    : Title Fontsize. Defaults to 18.
        """
        plt.figure(figsize=_figsize)
        plt.plot(
            np.array( self._scores )
        )
        plt.title("Training History", fontsize = title_fontsize)
        plt.ylabel("silhouette score", fontsize = axis_fontsize)
        plt.xlabel("epoch", fontsize = axis_fontsize)
        plt.show()
    
class RGBMethods:
    """ 
    Class offering static methods for plotting of RGB images, clustered or not.

    Attributes
    ----------
    
    Methods
    ----------

    Static Methods:
        open_image(file_name: str, root_path_to_rgb: str = './Synthetic_data/RGB/') : Open image with filename file_name located in root path root_path_to_rgb.
        show_image(_img: np.array, _figsize: tuple = (12, 8))                       : Method to plot RGB image
        return_label_image(segmented: np.array, cluster_idx: int)                   : Method to get greyscale cluster image with index cluster_idx from segmented
        show_label_image(segmented: np.array, cluster_idx: int)                     : Method to plot greyscale cluster image with index cluster_idx from segmented
        
        return_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int)    :   Method to get a single cluster in RGB space; 
        show_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int)      :   Method to plot a single cluster in RGB space; 
    """
    import numpy as np
    import PIL
    import matplotlib.pyplot as plt
    
    def __init__(self):
        pass
    
    ################################################
    # Static methods
    ################################################
    @staticmethod
    def open_image(file_name: str, root_path_to_rgb: str = './Synthetic_data/RGB/'):
        from PIL import Image
        try:
            _img = Image.open(
                root_path_to_rgb + file_name
            ).convert('RGB')
            
            return np.array(_img)
        except Exception as e:
            print(e)

    @staticmethod
    def show_image(_img: np.array, _figsize: tuple = (12, 8)):
        """_summary_
        Method to plot RGB image.

        Args:
            _img        (np.array)          :   RGB Image to show
            _figsize    (tuple, optional)   :   Figsize of the plotted Imshow. Defaults to (12, 8).
        """
        plt.figure(figsize = _figsize)
        plt.imshow(_img)
        plt.show()
    
    @staticmethod
    def return_label_image(segmented: np.array, cluster_idx: int):
        """_summary_
        Method to get greyscale cluster image with index cluster_idx from segmented cluster.

        Args:
            segmented   (np.array)  : Segmented cluster (From KMeans)
            cluster_idx (int)       : Wanted cluster index. 

        Returns:
            np.array    :   Grayscale cluster_idx-th cluster image 
        """
        _divisor = cluster_idx if cluster_idx>0 else 1
        _adder   = 0 if cluster_idx>0 else 1
        if len(segmented.shape) == 3:
            return ( segmented[:,:,0] + _adder ) * ( segmented[:,:,0] == cluster_idx ) / _divisor
        if len(segmented.shape) == 2:
            return ( segmented[:,:] + _adder ) * ( segmented[:,:] == cluster_idx)  / _divisor
    
    @staticmethod
    def show_label_image(segmented: np.array, cluster_idx: int):
        """_summary_
        Method to plot greyscale cluster image with index cluster_idx from segmented

        Args:
            segmented   (np.array)  : Segmented cluster (From KMeans)
            cluster_idx (int)       : Wanted cluster index.
        """
        RGBMethods.show_image(
            RGBMethods.return_label_image(segmented, cluster_idx)
        )
    
    @staticmethod
    def return_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int):
        """_summary_
        Method to get a single cluster in RGB space; 
        It plots in black ([0.0.0]) the pixels not belonging to the cluster, 
        and uses the RGB image rgb value for the pixels belonging to the cluster.

        Args:
            _img        (np.array)  :   RGB Image
            segmented   (np.array)  : Clustered image
            cluster_idx (int)       : Cluster index

        Returns:
            np.array    :   Single cluster rgb tensor.
        """
        _mask = RGBMethods.return_label_image(segmented=segmented, cluster_idx=cluster_idx)
        return np.array(_mask[:,:, None], dtype=bool) * _img
    
    @staticmethod
    def show_single_rgb_cluster(_img: np.array, segmented: np.array, cluster_idx: int):
        """_summary_
        Method to plot a single cluster in RGB space;

        Args:
            _img        (np.array)  :   RGB Image
            segmented   (np.array)  : Clustered image
            cluster_idx (int)       : Cluster index
        """
        RGBMethods.show_image(
            RGBMethods.return_single_rgb_cluster(
                _img, segmented, cluster_idx
            )
        )
        
class RGBKMeansClustering(RGBMethods, IterativeKMeans):
    """
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
                                if value < 0 are inserted, it is set up to +inf; in this case, MiniBatchKMeans becomes
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
    """
    
    import numpy as np
    from sklearn.cluster import MiniBatchKMeans
    from sklearn.metrics import silhouette_score
    import matplotlib.pyplot as plt
    
    ################################################
    # Init
    ################################################
    
    def __init__(self, rgb_img: np.array, N_start: int, delta_N: int = 3, N_patience: int = -1, score_batch: int = 1024):
        """_summary_

        Args:
            New Args:
            rgb_img (np.array)  : RGB Image  (i.e. a 3D np.array of shape (width, height, 3|4) ).
            
            IterativeKMeans Args:
            _N_start    (int)   :   Central value for the iteration. It is the central number of cluster
            _delta_N    (int)   :   (Optional; default = 3) Delta value; 
                                    the iteration will be performed from _N_start - _delta_N to _N_start + _delta_N.
            _N_patience (int)   :   (Optional; default = -1) Patience in iteration steps before breaking iterations.
                                    If after _N_patience epochs we see no improvement, we break the cycle.
            score_batch (int)   :   (Optional; default = 1024) Batch value used in MiniBatchKMeans to speed up the process. 
                                    if value < 0 are inserted, it is set up to +inf; in this case, MiniBatchKMeans becomes
                                    a standard KMeans

        Raises:
            Exception   :   Raises exception if rgb_img is not an image (i.e. a 3D np.array of shape (width, height, 3|4) )
        """
        # this calls all constructors up to RGBMethods
        super().__init__()
        # IterativeKMeans Super class init
        super(RGBMethods, self).__init__(
            N_start = N_start, 
            delta_N = delta_N,
            N_patience = N_patience,
            score_batch = score_batch
        ) #  this calls all constructors after RGBMethods and up to IterativeKMeans

        # init new params
        if len(rgb_img.shape) != 3 and ( rgb_img.shape[-1] != 3 or rgb_img.shape[-1] != 4):
            raise Exception(f"Insert a valid image.\nInserted image has invalid shape {rgb_img.shape}")
        # remove alpha channel, if present AND # put everything into float range [0,1]
        self.ex_rgb = rgb_img[:,:,:3] if rgb_img[:,:,:3].max() <= 1.0 else rgb_img[:,:,:3]/255.0
        # Set shape
        self._rgb_shape = rgb_img[:,:,:3].shape
        
        #print(self.ex_rgb.shape)
        
        # Init results 
        self.segmented_iter = None
        self.clustered_rgb  = None
        self._list_of_rgbs   = None
        self.reshaped_segmented_iter = None
    ################################################
    # Class methods
    ################################################

    # Perform all the clustering process and return the clustered rgb
    def cluster_rgb(self):
        """_summary_
        Main method. It performs the whole pipeline, returning the clustered RGB image.

        It performs:
            1. Set X by reshaping the RGB Image into (n_samples, n_features)
            2. Compute the IterativeKMeans cluster_train_predict
            3. Compute RGB clustered image from segmented tensor using cluster_train_predict

        Returns:
            np.array : Clustered RGB image.
        """
        # Set X
        _ics = self.ex_rgb.reshape(-1, self._rgb_shape[-1])
        # Compute the training
        self.segmented_iter = self.cluster_train_predict(X = _ics)

        # Compute rgb
        self.compute_clustered_rgb_from_segmented()
        
        return self.clustered_rgb
    
    # Compute cluster RGB from KMeans segmented 
    def compute_clustered_rgb_from_segmented(self):
        """_summary_
        Method to compute the clustered RGB out of the segmented tensor.

        It performs: 
            1. Init returned args
                a. _list_of_rgbs
                b. _clustered_rgb
            2. Compute the Average RGB per channel
                i.  Reshape RGB in (n_samples, n_features)
                ii. Compute cluster mask using RGBMethods.return_label_image()
                iii.Compute single cluster rgb using RGBMethods.return_single_rgb_cluster() and then averaging it. 
                        Note: We need to compute the sum over all the pixels RGB and then divide by the number of 1 in _mask to perform the cluster average.
                                NOT use .mean(). (it counts also the zeros.)
                iv. Perform tensordot to compute the average RGB cluster Image 
                v.  Append it to _list_of_rgbs
                vi. Add to _clustered_rgb
            3. Set the class args _list_of_rgbs and _clustered_rgb.
                
        """
        # Init util args
        _list_of_rgbs = np.zeros(
            (  self.segmented_iter.max()+1, *self._rgb_shape )
            , dtype=float
        )
        _clustered_rgb = np.zeros(self._rgb_shape, dtype=float)

        # Compute the Average RGB per channel
        # Reshape appropriate
        _reshaped_segmented_iter = self.segmented_iter.reshape(
            self._rgb_shape[0], self._rgb_shape[1]
        )
        for _idx in range( self.segmented_iter.max() + 1 ):
            
            # Compute mask
            _mask = self.return_label_image(
                _reshaped_segmented_iter,
                _idx
            )
            # Compute single cluster average
            _avg_rgb_cluster = self.return_single_rgb_cluster(
                self.ex_rgb,
                _reshaped_segmented_iter,
                _idx
            ).sum(axis=0).sum(axis=0) / _mask.sum(axis=0).sum(axis=0)

            # Perform tensordot
            _avg_cluster = np.tensordot(
                _mask,
                _avg_rgb_cluster,
                axes=-1
            )
            # append to _list_of_rgbs
            _list_of_rgbs[_idx, :,:,:] = _avg_cluster[:,:,:] if _avg_cluster[:,:,:].max() <= 1 else _avg_cluster[:,:,:] / 255.0

            # Add to _clustered_rgb
            _clustered_rgb = _clustered_rgb + _avg_cluster
            
        # Set results
        self.clustered_rgb = _clustered_rgb
        self._list_of_rgbs = _list_of_rgbs
        self.reshaped_segmented_iter = _reshaped_segmented_iter

    
    ################################################
    # Viz methods
    ################################################
    def show_average_rgb_clusters(self, _figsize: tuple = (12,8), _title_fontsize: int = 18):
        """_summary_
        Method to plot the computed average RGB cluster.

        Args:
            _figsize        (tuple, optional)   : Plot size. Defaults to (12,8).
            _title_fontsize (int, optional)     : Title font. Defaults to 18.
        """
        for _idx in range(self.segmented_iter.max() + 1 ):
            plt.figure(figsize=_figsize)
            plt.title(f"Cluster {_idx}-th", fontsize = _title_fontsize)
            plt.imshow( self._list_of_rgbs[_idx, :,:,:] )
            plt.show()
            
    def confront_clustered_with_unclustered(self, plot_diff: bool = True, _figsize: tuple = (12,8), _title_fontsize: int = 18):
        """_summary_
        Method to confront original RGB with Clustered one.

        Args:
            plot_diff (bool, optional)      : Boolean. If True, the method also plots the Difference image (i.e. the abs of original RGB minus the clustered RGB.). Defaults to True.
            _figsize (tuple, optional)      : Plot size. Defaults to (12,8).
            _title_fontsize (int, optional) : Title font. Defaults to 18.
        """
        fig, (ax1, ax2) = plt.subplots(
            nrows=1, ncols=2, 
            figsize=_figsize 
        )
        # Original
        ax1.set_title("Oringinal RGB", fontsize = _title_fontsize)
        ax1.imshow(self.ex_rgb)
        # CLustered
        ax2.set_title("Clustered RGB", fontsize = _title_fontsize)
        ax2.imshow(self.clustered_rgb)
        
        fig.show()
        
        # Plot diff
        if plot_diff:
            self.show_image(
                np.abs(self.ex_rgb - self.clustered_rgb),
                _figsize=_figsize
            )
        
    ################################################
    # Static methods
    ################################################
    @staticmethod
    def plot_grey_scale_confront(A: np.array, B: np.array, _figsize: tuple = (12,8),  _title_fontsize: int = 18):
        """_summary_
        Method to confront original RGB with Clustered one in greyscale.
        
        Args:
            A   (np.array)  : Image 1. (range [0,1])
            B   (np.array)  : Image 2. (range [0,1])

            _figsize        (tuple, optional)   : Figure size. Defaults to (12,8).
            _title_fontsize (int, optional)     : Title Fontsize. Defaults to 18.
        """
        plt.figure(figsize = _figsize)
        plt.title("Greyscale confront", fontsize = _title_fontsize)
        plt.imshow(
            np.abs(A - B).sum(axis=-1)/3.0,
            vmin=0.0,
            vmax=1.0,
            cmap='gray'
        )
        plt.show()
