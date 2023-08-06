# -*- coding: utf-8 -*-
"""
AnalogSignalArray
-----------------

Core object definition and implementation for regularly sampled
AnalogSignalArrays.
"""

__all__ = ['AnalogSignalArray']

import warnings
import numpy as np
import copy
import numbers

from functools import wraps
from scipy import interpolate
from scipy.stats import zscore
from sys import float_info
from collections import namedtuple

from .. import core
from .. import auxiliary
from .. import utils
from .. import version

# Force warnings.warn() to omit the source code line in the message
formatwarning_orig = warnings.formatwarning
warnings.formatwarning = lambda message, category, filename, lineno, \
    line=None: formatwarning_orig(
        message, category, filename, lineno, line='')

class EpochSignalSlicer(object):
    def __init__(self, obj):
        self.obj = obj

    def __getitem__(self, *args):
        """epochs, signals"""
        # by default, keep all signals
        signalslice = slice(None, None, None)
        if isinstance(*args, int):
            epochslice = args[0]
        elif isinstance(*args, core.EpochArray):
            epochslice = args[0]
        else:
            try:
                slices = np.s_[args]; slices = slices[0]
                if len(slices) > 2:
                    raise IndexError("only [epochs, signal] slicing is supported at this time!")
                elif len(slices) == 2:
                    epochslice, signalslice = slices
                else:
                    epochslice = slices[0]
            except TypeError:
                # only epoch to slice:
                epochslice = slices

        return epochslice, signalslice

class DataSlicer(object):

    def __init__(self, parent):
        self._parent = parent

    def _data_generator(self, epoch_indices, signalslice):
        for start, stop in epoch_indices:
            yield self._parent._data[signalslice, start: stop]

    def __getitem__(self, idx):
        epochslice, signalslice = self._parent._epochsignalslicer[idx]

        epoch_indices = self._parent._data_epoch_indices()
        epoch_indices = np.atleast_2d(epoch_indices[epochslice])

        if len(epoch_indices) < 2:
            start, stop = epoch_indices[0]
            return self._parent._data[signalslice, start: stop]
        else:
            return self._data_generator(epoch_indices, signalslice)

    def plot_generator(self):
        epoch_indices = self._parent._data_epoch_indices()
        for start, stop in epoch_indices:
            yield self._parent._data[:, start: stop]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        index = self._index

        if index > self._parent.n_epochs - 1:
            raise StopIteration

        epoch_indices = self._parent._data_epoch_indices()
        epoch_indices = epoch_indices[index]
        start, stop = epoch_indices

        self._index +=1

        return self._parent._data[:, start: stop]


class TimestampSlicer(object):

    def __init__(self, parent):
        self._parent = parent

    def _timestamp_generator(self, epoch_indices):
        for start, stop in epoch_indices:
            yield self._parent._time[start: stop]

    def __getitem__(self, idx):
        epochslice, signalslice = self._parent._epochsignalslicer[idx]

        epoch_indices = self._parent._data_epoch_indices()
        epoch_indices = np.atleast_2d(epoch_indices[epochslice])

        if len(epoch_indices) < 2:
            start, stop = epoch_indices[0]
            return self._parent._time[start: stop]
        else:
            return self._timestamp_generator(epoch_indices)

    def plot_generator(self):
        epoch_indices = self._parent._data_epoch_indices()
        for start, stop in epoch_indices:
            yield self._parent._time[start: stop]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        index = self._index

        if index > self._parent.n_epochs - 1:
            raise StopIteration

        epoch_indices = self._parent._data_epoch_indices()
        epoch_indices = epoch_indices[index]
        start, stop = epoch_indices

        self._index +=1

        return self._parent._time[start: stop]

def asa_init_wrapper(func):
    """Decorator that helps figure out timestamps, fs, and sample numbers"""

    @wraps(func)
    def wrapper(*args, **kwargs):

        if kwargs.get('empty', False):
            func(*args, **kwargs)
            return

        if len(args) > 2:
            raise TypeError("__init__() takes 1 positional arguments but {} positional arguments (and {} keyword-only arguments) were given".format(len(args)-1, len(kwargs.items())))

        data = kwargs.get('data', [])
        if data == []:
            data = args[1]

        if data == []:
            warnings.warn('No data! Returning empty AnalogSignalArray.')
            func(*args, **kwargs)
            return

        # handle casting other nelpy objects to AnalogSignalArrays:
        if isinstance(data, core.BinnedSpikeTrainArray):
            timestamps = data.bin_centers
            kwargs['timestamps'] = timestamps
            support = data.support
            kwargs['support'] = support
            fs = 1/data.ds
            kwargs['fs'] = fs
            if list(data.unit_labels):
                labels = data.unit_labels
            else:
                labels = data.unit_ids
            kwargs['labels'] = labels
            data = data.data.astype(float)
        # elif isinstance(data, auxiliary.PositionArray):
        elif isinstance(data, AnalogSignalArray):
            kwargs['data'] = data
            func(args[0], **kwargs)
            return

        #check if single AnalogSignal or multiple AnalogSignals in array
        #and standardize data to 2D
        if not np.any(np.iscomplex(data)):
            data = np.squeeze(data).astype(float)
        try:
            if(data.shape[0] == data.size):
                data = np.array(data,ndmin=2)
        except ValueError:
            raise TypeError("Unsupported data type!")

        re_estimate_fs = False
        no_fs = True
        fs = kwargs.get('fs', None)
        if fs is not None:
            no_fs = False
            try:
                if(fs <= 0):
                    raise ValueError("fs must be positive")
            except TypeError:
                raise TypeError("fs must be a scalar!")
        else:
            fs = 1
            re_estimate_fs = True

        tdata = kwargs.get('tdata', None)
        if tdata is not None:
            warnings.warn("'tdata' has been deprecated! Use 'timestamps' instead. 'tdata' will be interpreted as 'timestamps' in seconds.")
            time = tdata
        else:
            time = kwargs.get('timestamps', None)
        if time is None:
            time = np.linspace(0, data.shape[1]/fs, data.shape[1]+1)
            time = time[:-1]
        else:
            if re_estimate_fs:
                warnings.warn('fs was not specified, so we try to estimate it from the data...')
                fs = 1.0/np.median(np.diff(time))
                warnings.warn('fs was estimated to be {} Hz'.format(fs))
            else:
                if no_fs:
                    warnings.warn('fs was not specified, so we will assume default of 1 Hz...')
                    fs = 1

        kwargs['fs'] = fs
        kwargs['data'] = data
        kwargs['timestamps'] = np.squeeze(time)

        func(args[0], **kwargs)
        return

    return wrapper

########################################################################
# class AnalogSignalArray
########################################################################
class AnalogSignalArray:
    """Continuous analog signal(s) with regular sampling rates (irregular
    sampling rates can be corrected with operations on the support) and same
    support. NOTE: data that is not equal dimensionality will NOT work
    and error/warning messages may/may not be sent out. Also, in this
    current rendition, I am assuming timestamps are the exact same for all
    signals passed through. As such, timestamps are expected to be single
    dimensional.

    Parameters
    ----------
    data : np.array(dtype=np.float,dimension=N)
    timestamps : np.array(dtype=np.float,dimension=N), optional
        Timestamps in seconds (ideally). Timestamps are assumed to be sampled
        regularly in order to generate epochs. Irregular sampling rates can be
        corrected with operations on the support.
    fs : float, optional
        Sampling rate in Hz. timestamps are still expected to be in units of
        time and fs is expected to be in the corresponding sampling rate (e.g.
        timestamps in seconds, fs in Hz)
    support : EpochArray, optional
        EpochArray array on which LFP is defined.
        Default is [0, last spike] inclusive.
    step : int
        specifies step size of samples passed as tdata if fs is given,
        default is None. If not passed it is inferred by the minimum
        difference in between samples of tdata passed in (based on if FS
        is passed). e.g. decimated data would have sample numbers every
        ten samples so step=10
    merge_sample_gap : float, optional
        Optional merging of gaps between support epochs. If epochs are within
        a certain amount of time, gap, they will be merged as one epoch. Example
        use case is when there is a dropped sample
    labels : np.array(dtype=np.str,dimension=N)
        Labeling each one of the signals in AnalogSignalArray. By default this
        will be set to None. It is expected that all signals will be labeled if
        labels are passed in. If any signals are not labeled we will label them
        as Nones and if more labels are passed in than the number of signals
        given, the extras will be truncated. If we're nice (which we are for
        the most part), we will display a warning upon doing any of these
        things! :P Lastly, it is worth noting that most logical and type error
        checking for this is expected to be done by the user. Inputs are casted
        to string snad stored in a numpy array.
    empty : bool
        Return an empty AnalogSignalArray if true else false. Default
        set to false.

    Attributes
    ----------
    data : np.array
        With shape (n_data,N).
    timestamps : np.array
        With shape (n_tdata,N).
    fs : float, scalar, optional
        See Parameters
    step : int
        See Parameters
    support : EpochArray, optional
        See Parameters
    labels : np.array
        See Parameters
    interp : array of interpolation objects from scipy.interpolate

        See Parameters
    """
    __attributes__ = ['_data','_time', '_fs', '_support', \
                      '_interp', '_step', '_labels']

    @asa_init_wrapper
    def __init__(self, data=[], *, timestamps=None, fs=None,
                 step=None, merge_sample_gap=0, support=None,
                 in_memory=True, labels=None, empty=False):

        self._epochsignalslicer = EpochSignalSlicer(self)
        self._epochdata = DataSlicer(self)
        self._epochtime = TimestampSlicer(self)

        self.__version__ = version.__version__

        # cast derivatives of AnalogSignalArray back into AnalogSignalArray:
        # if isinstance(data, auxiliary.PositionArray):
        if isinstance(data, AnalogSignalArray):
            self.__dict__ = copy.deepcopy(data.__dict__)
            # if self._has_changed:
                # self.__renew__()
            self.__renew__()
            return

        if(empty):
            for attr in self.__attributes__:
                exec("self." + attr + " = None")
            self._support = core.EpochArray(empty=True)
            self._data = np.array([])
            self.__bake__()
            return

        self._step = step
        self._fs = fs

        # Note; if we have an empty array of data with no dimension,
        # then calling len(data) will return a TypeError
        try:
            # if no data are given return empty AnalogSignalArray
            if data.size == 0:
                self.__init__(empty=True)
                return
        except TypeError:
            warnings.warn("unsupported type; creating empty AnalogSignalArray")
            self.__init__(empty=True)
            return

        # Note: if both time and data are given and dimensionality does not
        # match, then TypeError!

        time = np.squeeze(timestamps).astype(float)
        if(time.shape[0] != data.shape[1]):
            # self.__init__([],empty=True)
            raise TypeError("time and data size mismatch! Note: data "
                            "is expected to have rows containing signals")
        #data is not sorted and user wants it to be
        # TODO: use faster is_sort from jagular
        if not utils.is_sorted(time):
            warnings.warn("Data is _not_ sorted! Data will be sorted "\
                            "automatically.")
            ind = np.argsort(time)
            time = time[ind]
            data = np.take(a=data, indices=ind, axis=-1)

        self._data = data
        self._time = time

        #handle labels
        if labels is not None:
            labels = np.asarray(labels,dtype=np.str)
            #label size doesn't match
            if labels.shape[0] > data.shape[0]:
                warnings.warn("More labels than data! labels are sliced to "
                              "size of data")
                labels = labels[0:data.shape[0]]
            elif labels.shape[0] < data.shape[0]:
                warnings.warn("Less labels than time! labels are filled with "
                              "None to match data shape")
                for i in range(labels.shape[0],data.shape[0]):
                    labels.append(None)
        self._labels = labels

        # Alright, let's handle all the possible parameter cases!
        if support is not None:
            self._restrict_to_epoch_array_fast(epocharray=support)
        else:
            warnings.warn("creating support from time and "
                            "sampling rate, fs!")
            self._support = core.EpochArray(
                utils.get_contiguous_segments(
                    self.time,
                    step=self._step,
                    fs=fs,
                    in_memory=in_memory))
            if merge_sample_gap > 0:
                self._support = self._support.merge(gap=merge_sample_gap)

        if np.abs((self.fs - self._estimate_fs())/self.fs) > 0.01:
            warnings.warn("estimated fs and provided fs differ by more than 1%")

    def __bake__(self):
        """Fix object as-is, and bake a new hash.

        For example, if a label has changed, or if an interp has been attached,
        then the object's hash will change, and it needs to be baked
        again for efficiency / consistency.
        """
        self._stored_hash_ = self.__hash__()

    # def _has_changed_data(self):
    #     """Compute hash on timestamps and data and compare to cached hash."""
    #     return self.data.__hash__ elf._data_hash_

    def _has_changed(self):
        """Compute hash on current object, and compare to previously stored hash"""
        return self.__hash__() == self._stored_hash_

    def __renew__(self):
        """Re-attach data slicers."""
        self._epochsignalslicer = EpochSignalSlicer(self)
        self._epochdata = DataSlicer(self)
        self._epochtime = TimestampSlicer(self)
        self._interp = None
        self.__bake__()

    def __call__(self, *args):
        """AnalogSignalArray callable method; by default returns interpolated yvals"""
        f = lambda x: self.asarray(at=x).yvals
        return f(args)

    def _data_epoch_indices(self):
        """Docstring goes here.
        We use this to get the indices of samples / timestamps within epochs
        """
        tmp = np.insert(np.cumsum(self.lengths),0,0)
        indices = np.vstack((tmp[:-1], tmp[1:])).T
        return indices

    def ddt(self, rectify=False):
        """Returns the time derivative of each signal in the AnalogSignalArray.

        asa.data = f(t)
        asa.ddt = d/dt (asa.data)

        Parameters
        ----------
        rectify : boolean, optional
            If True, the absolute value of the time derivative will be returned.
            Default is False.

        Returns
        -------
        ddt : AnalogSignalArray
            Time derivative of each signal in the AnalogSignalArray.

        Note
        ----
        Second order central differences are used here, and it is assumed that
        the signals are sampled uniformly. If the signals are not uniformly
        sampled, it is recommended to resample the signal before computing the
        time derivative.
        """
        ddt = utils.ddt_asa(self, rectify=rectify)
        return ddt

    @property
    def signals(self):
        """Returns a list of AnalogSignalArrays, each array containing
        a single signal (channel).

        WARNING: this method creates a copy of each signal, so is not
        particularly efficient at this time.

        Example
        =======
        >>> for channel in lfp.signals:
            print(channel)
        """
        signals = []
        for ii in range(self.n_signals):
            signals.append(self[:,ii])
        return signals
        # return np.asanyarray(signals).squeeze()

    @property
    def isreal(self):
        """Returns True if entire signal is real."""
        return np.all(np.isreal(self.data))
        # return np.isrealobj(self._data)

    @property
    def iscomplex(self):
        """Returns True if any part of the signal is complex."""
        return np.any(np.iscomplex(self.data))
        # return np.iscomplexobj(self._data)

    @property
    def abs(self):
        """AnalogSignalArray with absolute value of (potentially complex) data."""
        out = copy.copy(self)
        out._data = np.abs(self.data)
        out.__renew__()
        return out

    @property
    def angle(self):
        """AnalogSignalArray with only phase angle (in radians) of data."""
        out = copy.copy(self)
        out._data = np.angle(self.data)
        out.__renew__()
        return out

    @property
    def imag(self):
        """AnalogSignalArray with only imaginary part of data."""
        out = copy.copy(self)
        out._data = self.data.imag
        out.__renew__()
        return out

    @property
    def real(self):
        """AnalogSignalArray with only real part of data."""
        out = copy.copy(self)
        out._data = self.data.real
        out.__renew__()
        return out

    def __mul__(self, other):
        """overloaded * operator."""
        if isinstance(other, numbers.Number):
            newasa = copy.copy(self)
            newasa._data = self.data * other
            newasa.__renew__()
            return newasa
        else:
            raise TypeError("unsupported operand type(s) for *: 'AnalogSignalArray' and '{}'".format(str(type(other))))

    def __add__(self, other):
        """overloaded + operator."""
        if isinstance(other, numbers.Number):
            newasa = copy.copy(self)
            newasa._data = self.data + other
            newasa.__renew__()
            return newasa
        else:
            raise TypeError("unsupported operand type(s) for +: 'AnalogSignalArray' and '{}'".format(str(type(other))))

    def __sub__(self, other):
        """overloaded - operator."""
        if isinstance(other, numbers.Number):
            newasa = copy.copy(self)
            newasa._data = self.data - other
            newasa.__renew__()
            return newasa
        else:
            raise TypeError("unsupported operand type(s) for -: 'AnalogSignalArray' and '{}'".format(str(type(other))))

    def zscore(self):
        """Returns an object where each signal has been normalized using z scores."""
        out = copy.deepcopy(self)
        out._data = zscore(out._data, axis=1)
        return out

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """overloaded / operator."""
        if isinstance(other, numbers.Number):
            newasa = copy.copy(self)
            newasa._data = self.data / other
            newasa.__renew__()
            return newasa
        else:
            raise TypeError("unsupported operand type(s) for /: 'AnalogSignalArray' and '{}'".format(str(type(other))))

    def __len__(self):
        return self.n_epochs

    def _drop_empty_epochs(self):
        """Drops empty epochs from support. In-place."""
        keep_epoch_ids = np.argwhere(self.lengths).squeeze().tolist()
        self._support = self.support[keep_epoch_ids]
        return self

    def _estimate_fs(self, timestamps=None):
        """Estimate the sampling rate of the data."""
        if timestamps is None:
            timestamps = self.time
        return 1.0/np.median(np.diff(timestamps))

    def downsample(self, *, fs_out, aafilter=True, inplace=False):
        out = utils.downsample_analogsignalarray(self, fs_out=fs_out, aafilter=aafilter, inplace=inplace)
        out.__renew__()
        return out

    def add_signal(self, signal, label=None):
        """Docstring goes here.
        Basically we add a signal, and we add a label. THIS HAPPENS IN PLACE?
        """
        # TODO: add functionality to check that supports are the same, etc.
        if isinstance(signal, AnalogSignalArray):
            signal = signal.data

        signal = np.squeeze(signal)
        if signal.ndim > 1:
            raise TypeError("Can only add one signal at a time!")
        if self.data.ndim==1:
            self._data = np.vstack([np.array(self.data, ndmin=2), np.array(signal, ndmin=2)])
        else:
            self._data = np.vstack([self.data, np.array(signal, ndmin=2)])
        if label == None:
            warnings.warn("None label appended")
        self._labels = np.append(self._labels,label)
        return self

    def _restrict_to_epoch_array_fast(self, *, epocharray=None, update=True):
        """Restrict self._time and self._data to an EpochArray. If no
        EpochArray is specified, self._support is used.

        Parameters
        ----------
        epocharray : EpochArray, optional
        	EpochArray on which to restrict AnalogSignal. Default is
        	self._support
        update : bool, optional
        	Overwrite self._support with epocharray if True (default).
        """
        if epocharray is None:
            epocharray = self._support
            update = False # support did not change; no need to update

        try:
            if epocharray.isempty:
                warnings.warn("Support specified is empty")
                # self.__init__([],empty=True)
                exclude = ['_support','_data','_fs','_step']
                attrs = (x for x in self.__attributes__ if x not in exclude)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    for attr in attrs:
                        exec("self." + attr + " = None")
                self._data = np.zeros([0,self.data.shape[0]])
                self._data[:] = np.nan
                self._support = epocharray
                return
        except AttributeError:
            raise AttributeError("EpochArray expected")

        indices = []
        for eptime in epocharray.merge().time:
            t_start = eptime[0]
            t_stop = eptime[1]
            frm, to = np.searchsorted(self._time, (t_start, t_stop))
            indices.append((frm, to))
        indices = np.array(indices, ndmin=2)
        if np.diff(indices).sum() < len(self._time):
            warnings.warn(
                'ignoring signal outside of support')
        try:
            data_list = []
            for start, stop in indices:
                data_list.append(self._data[:,start:stop])
            self._data = np.hstack(data_list)
        except IndexError:
            self._data = np.zeros([0,self.data.shape[0]])
            self._data[:] = np.nan
        time_list = []
        for start, stop in indices:
            time_list.extend(self._time[start:stop])
        self._time = np.array(time_list)
        if update:
            self._support = epocharray

    def _restrict_to_epoch_array(self, *, epocharray=None, update=True):
        """Restrict self._time and self._data to an EpochArray. If no
        EpochArray is specified, self._support is used.

        This function is quite slow, as it checks each sample for inclusion.
        It does this in a vectorized form, which is fast for small or moderately
        sized objects, but the memory penalty can be large, and it becomes very
        slow for large objects. Consequently, _restrict_to_epoch_array_fast
        should be used when possible.

        Parameters
        ----------
        epocharray : EpochArray, optional
        	EpochArray on which to restrict AnalogSignal. Default is
        	self._support
        update : bool, optional
        	Overwrite self._support with epocharray if True (default).
        """
        if epocharray is None:
            epocharray = self._support
            update = False # support did not change; no need to update

        try:
            if epocharray.isempty:
                warnings.warn("Support specified is empty")
                # self.__init__([],empty=True)
                exclude = ['_support','_data','_fs','_step']
                attrs = (x for x in self.__attributes__ if x not in exclude)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    for attr in attrs:
                        exec("self." + attr + " = None")
                self._data = np.zeros([0,self.data.shape[0]])
                self._data[:] = np.nan
                self._support = epocharray
                return
        except AttributeError:
            raise AttributeError("EpochArray expected")

        indices = []
        for eptime in epocharray.merge().time:
            t_start = eptime[0]
            t_stop = eptime[1]
            indices.append((self._time >= t_start) & (self._time < t_stop))
        indices = np.any(np.column_stack(indices), axis=1)
        if np.count_nonzero(indices) < len(self._time):
            warnings.warn(
                'ignoring signal outside of support')
        try:
            self._data = self.data[:,indices]
        except IndexError:
            self._data = np.zeros([0,self.data.shape[0]])
            self._data[:] = np.nan
        self._time = self._time[indices]
        if update:
            self._support = epocharray

    def smooth(self, *, fs=None, sigma=None, bw=None, inplace=False):
        """Smooths the regularly sampled AnalogSignalArray with a Gaussian kernel.

        Smoothing is applied in time, and the same smoothing is applied to each
        signal in the AnalogSignalArray.

        Smoothing is applied within each epoch.

        Parameters
        ----------
        fs : float, optional
            Sampling rate (in Hz) of AnalogSignalArray. If not provided, it will
            be obtained from asa.fs
        sigma : float, optional
            Standard deviation of Gaussian kernel, in seconds. Default is 0.05 (50 ms)
        bw : float, optional
            Bandwidth outside of which the filter value will be zero. Default is 4.0
        inplace : bool
            If True the data will be replaced with the smoothed data.
            Default is False.

        Returns
        -------
        out : AnalogSignalArray
            An AnalogSignalArray with smoothed data is returned.
        """
        kwargs = {'inplace' : inplace,
                'fs' : fs,
                'sigma' : sigma,
                'bw' : bw}

        out = utils.gaussian_filter(self, **kwargs)
        out.__renew__()
        return out

    @property
    def lengths(self):
        """(list) The number of samples in each epoch."""
        indices = []
        for eptime in self.support.time:
            t_start = eptime[0]
            t_stop = eptime[1]
            frm, to = np.searchsorted(self._time, (t_start, t_stop))
            indices.append((frm, to))
        indices = np.array(indices, ndmin=2)
        lengths = np.atleast_1d(np.diff(indices).squeeze())
        return lengths

    @property
    def labels(self):
        """(list) The number of samples in each epoch."""
        # TODO: make this faster and better!
        return self._labels

    @property
    def n_signals(self):
        """(int) The number of signals."""
        try:
            return utils.PrettyInt(self.data.shape[0])
        except AttributeError:
            return 0

    def __repr__(self):
        address_str = " at " + str(hex(id(self)))
        if self.isempty:
            return "<empty AnalogSignal" + address_str + ">"
        if self.n_epochs > 1:
            epstr = " ({} segments)".format(self.n_epochs)
        else:
            epstr = ""
        try:
            if(self.n_signals > 0):
                nstr = " %s signals%s" % (self.n_signals, epstr)
        except IndexError:
            nstr = " 1 signal%s" % epstr
        dstr = " for a total of {}".format(utils.PrettyDuration(self.support.duration))
        return "<AnalogSignalArray%s:%s>%s" % (address_str, nstr, dstr)

    def partition(self, ds=None, n_epochs=None):
        """Returns an AnalogSignalArray whose support has been
        partitioned.

        # Irrespective of whether 'ds' or 'n_epochs' are used, the exact
        # underlying support is propagated, and the first and last points
        # of the supports are always included, even if this would cause
        # n_points or ds to be violated.

        Parameters
        ----------
        ds : float, optional
            Maximum duration (in seconds), for each epoch.
        n_points : int, optional
            Number of epochs. If ds is None and n_epochs is None, then
            default is to use n_epochs = 100

        Returns
        -------
        out : AnalogSignalArray
            AnalogSignalArray that has been partitioned.
        """

        out = copy.copy(self)
        out._support = out.support.partition(ds=ds, n_epochs=n_epochs)
        out.__renew__()
        return out

    @property
    def ydata(self):
        """(np.array N-Dimensional) data with shape (n_signals, n_samples)."""
        # LEGACY
        return self.data

    @property
    def data(self):
        """(np.array N-Dimensional) data with shape (n_signals, n_samples)."""
        try:
            return self._data
        except AttributeError:
            # legacy support:
            self._data = self._ydata
        return self._data

    @property
    def support(self):
        """(nelpy.EpochArray) The support of the underlying AnalogSignalArray
        (in seconds).
         """
        return self._support

    @property
    def step(self):
        """ steps per sample
        Example 1: sample_numbers = np.array([1,2,3,4,5,6]) #aka time
        Steps per sample in the above case would be 1

        Example 2: sample_numbers = np.array([1,3,5,7,9]) #aka time
        Steps per sample in Example 2 would be 2
        """
        return self._step

    @property
    def time(self):
        """(np.array 1D) Time in seconds."""
        return self._time

    @property
    def fs(self):
        """(float) Sampling frequency."""
        if self._fs is None:
            warnings.warn("No sampling frequency has been specified!")
        return self._fs

    @property
    def isempty(self):
        """(bool) checks length of data input"""
        try:
            return self.data.shape[1] == 0
        except IndexError: #TypeError should happen if _data = []
            return True

    @property
    def n_bytes(self):
        """Approximate number of bytes taken up by object."""
        return utils.PrettyBytes(self.data.nbytes + self.time.nbytes)

    @property
    def n_epochs(self):
        """(int) number of epochs in AnalogSignalArray"""
        return self._support.n_epochs

    @property
    def n_samples(self):
        """(int) number of time samples where signal is defined."""
        if self.isempty:
            return 0
        return utils.PrettyInt(len(self.time))

    def __iter__(self):
        """AnalogSignal iterator initialization"""
        # initialize the internal index to zero when used as iterator
        self._index = 0
        return self

    def __next__(self):
        """AnalogSignal iterator advancer."""
        index = self._index
        if index > self.n_epochs - 1:
            raise StopIteration
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            epoch = core.EpochArray(empty=True)
            exclude = ["_time"]
            attrs = (x for x in self._support.__attributes__ if x not in exclude)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                for attr in attrs:
                    exec("epoch." + attr + " = self._support." + attr)
                try:
                    epoch._time = self._support.time[[index], :]  # use np integer indexing! Cool!
                except IndexError:
                    # index is out of bounds, so return an empty EpochArray
                    pass

        self._index += 1

        asa = AnalogSignalArray([],empty=True)
        exclude = ['_interp','_support']
        attrs = (x for x in self.__attributes__ if x not in exclude)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for attr in attrs:
                exec("asa." + attr + " = self." + attr)
        asa._restrict_to_epoch_array_fast(epocharray=epoch)
        if(asa.support.isempty):
            warnings.warn("Support is empty. Empty AnalogSignalArray returned")
            asa = AnalogSignalArray([],empty=True)

        asa.__renew__()
        return asa

    def empty(self, inplace=True):
        """Remove data (but not metadata) from AnalogSignalArray."""
        if not inplace:
            out = self._copy_without_data()
            out._support = core.EpochArray(empty=True)
            return out
        out = self
        out._data = np.zeros((out.n_signals,0))
        out._support = core.EpochArray(empty=True)
        out._time = []
        out.__renew__()
        return out

    def __getitem__(self, idx):
        """AnalogSignalArray index access.

        Parameters
        ----------
        idx : EpochArray, int, slice
            intersect passed epocharray with support,
            index particular a singular epoch or multiple epochs with slice
        """
        epochslice, signalslice = self._epochsignalslicer[idx]

        asa = self._subset(signalslice)

        if asa.isempty:
            asa.__renew__()
            return asa

        if isinstance(epochslice, slice):
            if epochslice.start == None and epochslice.stop == None and epochslice.step == None:
                asa.__renew__()
                return asa

        newepochs = self._support[epochslice]
        # TODO: this needs to change so that n_signals etc. are preserved
        ################################################################
        if newepochs.isempty:
            warnings.warn("Index resulted in empty epoch array")
            return self.empty(inplace=False)
        ################################################################

        asa._restrict_to_epoch_array_fast(epocharray=newepochs)
        asa.__renew__()
        return asa

    def _subset(self, idx):
        asa = self.copy()
        try:
            asa._data = np.atleast_2d(self.data[idx,:])
        except IndexError:
            raise IndexError("index {} is out of bounds for n_signals with size {}".format(idx, self.n_signals))
        asa.__renew__()
        return asa

    def _copy_without_data(self):
        """Return a copy of self, without data."""
        out = copy.copy(self) # shallow copy
        out._time = None
        out._data = np.zeros((self.n_signals,0))
        out = copy.deepcopy(out) # just to be on the safe side, but at least now we are not copying the data!
        out.__renew__()
        return out

    def copy(self):
        """Return a copy of the current object."""
        out = copy.deepcopy(self)
        out.__renew__()
        # asa = AnalogSignalArray([], empty=True)
        # exclude = ['_interp']
        # attrs = (x for x in self.__attributes__ if x not in exclude)
        # with warnings.catch_warnings():
        #     warnings.simplefilter("ignore")
        #     for attr in attrs:
        #         exec("asa." + attr + " = self." + attr)
        # try:
        #     exec("asa._interp = self._interp")
        # except AttributeError:
        #     pass
        # asa.__renew__()
        return out

    def mean(self,*,axis=1):
        """Returns the mean of each signal in AnalogSignalArray."""
        try:
            means = np.mean(self.data, axis=axis).squeeze()
            if means.size == 1:
                return np.asscalar(means)
            return means
        except IndexError:
            raise IndexError("Empty AnalogSignalArray cannot calculate mean")

    def std(self,*,axis=1):
        """Returns the standard deviation of each signal in AnalogSignalArray."""
        try:
            stds = np.std(self.data,axis=axis).squeeze()
            if stds.size == 1:
                return np.asscalar(stds)
            return stds
        except IndexError:
            raise IndexError("Empty AnalogSignalArray cannot calculate standard deviation")

    def max(self,*,axis=1):
        """Returns the maximum of each signal in AnalogSignalArray"""
        try:
            maxes = np.amax(self.data,axis=axis).squeeze()
            if maxes.size == 1:
                return np.asscalar(maxes)
            return maxes
        except ValueError:
            raise ValueError("Empty AnalogSignalArray cannot calculate maximum")

    def min(self,*,axis=1):
        """Returns the minimum of each signal in AnalogSignalArray"""
        try:
            mins = np.amin(self.data,axis=axis).squeeze()
            if mins.size == 1:
                return np.asscalar(mins)
            return mins
        except ValueError:
            raise ValueError("Empty AnalogSignalArray cannot calculate minimum")

    def clip(self, min, max):
        """Clip (limit) the values of each signal to min and max as specified.

        Parameters
        ----------
        min : scalar
            Minimum value
        max : scalar
            Maximum value

        Returns
        ----------
        clipped_analogsignalarray : AnalogSignalArray
            AnalogSignalArray with the signal clipped with the elements of data, but where the values <
            min are replaced with min and the values > max are replaced
            with max.
        """
        new_data = np.clip(self.data, min, max)
        newasa = self.copy()
        newasa._data = new_data
        newasa.__renew__()
        return newasa

    def trim(self, start, stop=None, *, fs=None):
        """Trim the AnalogSignalArray to a single time/sample interval.

        Parameters
        ----------
        start : float or two element array-like
            (float) Left boundary of interval in time (seconds) if
            fs=None, otherwise left boundary is start / fs.
            (2 elements) Left and right boundaries in time (seconds) if
            fs=None, otherwise boundaries are left / fs. Stop must be
            None if 2 element start is used.
        stop : float, optional
            Right boundary of interval in time (seconds) if fs=None,
            otherwise right boundary is stop / fs.
        fs : float, optional
            Sampling rate in Hz.

        Returns
        -------
        trim : AnalogSignalArray
            The AnalogSignalArray on the interval [start, stop].

        Examples
        --------
        >>> as.trim([0, 3], fs=1)  # recommended for readability
        >>> as.trim(start=0, stop=3, fs=1)
        >>> as.trim(start=[0, 3])
        >>> as.trim(0, 3)
        >>> as.trim((0, 3))
        >>> as.trim([0, 3])
        >>> as.trim(np.array([0, 3]))
        """
        warnings.warn("AnalogSignalArray: Trim may not work!")
        # TODO: do comprehensive input validation
        if stop is not None:
            try:
                start = np.array(start, ndmin=1)
                if len(start) != 1:
                    raise TypeError("start must be a scalar float")
            except TypeError:
                raise TypeError("start must be a scalar float")
            try:
                stop = np.array(stop, ndmin=1)
                if len(stop) != 1:
                    raise TypeError("stop must be a scalar float")
            except TypeError:
                raise TypeError("stop must be a scalar float")
        else:  # start must have two elements
            try:
                if len(np.array(start, ndmin=1)) > 2:
                    raise TypeError(
                        "unsupported input to AnalogSignalArray.trim()")
                stop = np.array(start[1], ndmin=1)
                start = np.array(start[0], ndmin=1)
                if len(start) != 1 or len(stop) != 1:
                    raise TypeError(
                        "start and stop must be scalar floats")
            except TypeError:
                raise TypeError(
                    "start and stop must be scalar floats")

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            epoch = self._support.intersect(
                core.EpochArray(
                    [start, stop],
                    fs=fs))
            if not epoch.isempty:
                analogsignalarray = self[epoch]
            else:
                analogsignalarray = AnalogSignalArray([],empty=True)
        analogsignalarray.__renew__()
        return analogsignalarray

    @property
    def _ydata_rowsig(self):
        """returns wide-format data s.t. each row is a signal."""
        # LEGACY
        return self.data

    @property
    def _ydata_colsig(self):
        # LEGACY
        """returns skinny-format data s.t. each column is a signal."""
        return self.data.T

    @property
    def _data_rowsig(self):
        """returns wide-format data s.t. each row is a signal."""
        return self.data

    @property
    def _data_colsig(self):
        """returns skinny-format data s.t. each column is a signal."""
        return self.data.T

    def _get_interp1d(self,* , kind='linear', copy=True, bounds_error=False,
                      fill_value=np.nan, assume_sorted=None):
        """returns a scipy interp1d object, extended to have values at all epoch
        boundaries!
        """

        if assume_sorted is None:
            assume_sorted = utils.is_sorted(self.time)

        if self.n_signals > 1:
            axis = 1
        else:
            axis = -1

        time = self.time
        yvals = self._data_rowsig
        lengths = self.lengths
        empty_epoch_ids = np.argwhere(lengths==0).squeeze().tolist()
        first_timestamps_per_epoch_idx = np.insert(np.cumsum(lengths[:-1]),0,0)
        first_timestamps_per_epoch_idx[empty_epoch_ids] = 0
        last_timestamps_per_epoch_idx = np.cumsum(lengths)-1
        last_timestamps_per_epoch_idx[empty_epoch_ids] = 0
        first_timestamps_per_epoch = self.time[first_timestamps_per_epoch_idx]
        last_timestamps_per_epoch = self.time[last_timestamps_per_epoch_idx]

        boundary_times = []
        boundary_vals = []
        for ii, (start, stop) in enumerate(self.support.time):
            if lengths[ii] == 0:
                continue
            if first_timestamps_per_epoch[ii] > start:
                boundary_times.append(start)
                boundary_vals.append(yvals[:,first_timestamps_per_epoch_idx[ii]])
                # print('adding {} at time {}'.format(yvals[:,first_timestamps_per_epoch_idx[ii]], start))
            if last_timestamps_per_epoch[ii] < stop:
                boundary_times.append(stop)
                boundary_vals.append(yvals[:,last_timestamps_per_epoch_idx[ii]])

        if boundary_times:
            insert_locs = np.searchsorted(time, boundary_times)
            time = np.insert(time, insert_locs, boundary_times)
            yvals = np.insert(yvals, insert_locs, np.array(boundary_vals).T, axis=1)

            time, unique_idx = np.unique(time, return_index=True)
            yvals = yvals[:,unique_idx]

        f = interpolate.interp1d(x=time,
                                 y=yvals,
                                 kind=kind,
                                 axis=axis,
                                 copy=copy,
                                 bounds_error=bounds_error,
                                 fill_value=fill_value,
                                 assume_sorted=assume_sorted)
        return f

    def asarray(self,*, where=None, at=None, kind='linear', copy=True,
                bounds_error=False, fill_value=np.nan, assume_sorted=None,
                recalculate=False, store_interp=True, n_points=None,
                split_by_epoch=False):
        """returns a data_like array at requested points.

        Parameters
        ----------
        where : array_like or tuple, optional
            array corresponding to np where condition
            e.g., where=(data[1,:]>5) or tuple where=(speed>5,tspeed)
        at : array_like, optional
            Array of oints to evaluate array at. If none given, use
            self.time together with 'where' if applicable.
        n_points: int, optional
            Number of points to interplate at. These points will be
            distributed uniformly from self.support.start to stop.
        split_by_epoch: bool
            If True, separate arrays by epochs and return in a list.
        Returns
        -------
        out : (array, array)
            namedtuple tuple (xvals, yvals) of arrays, where xvals is an
            array of time points for which (interpolated) data are
            returned.
        """

        # TODO: implement splitting by epoch

        if split_by_epoch:
            raise NotImplementedError("split_by_epoch not yet implemented...")

        XYArray = namedtuple('XYArray', ['xvals', 'yvals'])

        if at is None and where is None and split_by_epoch is False and n_points is None:
            xyarray = XYArray(self.time, self._data_rowsig.squeeze())
            return xyarray

        if where is not None:
            assert at is None and n_points is None, "'where', 'at', and 'n_points' cannot be used at the same time"
            if isinstance(where, tuple):
                y = np.array(where[1]).squeeze()
                x = where[0]
                assert len(x) == len(y), "'where' condition and array must have same number of elements"
                at = y[x]
            else:
                x = np.asanyarray(where).squeeze()
                assert len(x) == len(self.time), "'where' condition must have same number of elements as self.time"
                at = self.time[x]
        elif at is not None:
            assert n_points is None, "'at' and 'n_points' cannot be used at the same time"
        else:
            at = np.linspace(self.support.start, self.support.stop, n_points)

        # if we made it this far, either at or where has been specified, and at is now well defined.

        kwargs = {'kind':kind,
                  'copy':copy,
                  'bounds_error':bounds_error,
                  'fill_value':fill_value,
                  'assume_sorted':assume_sorted}

        # retrieve an existing, or construct a new interpolation object
        if recalculate:
            interpobj = self._get_interp1d(**kwargs)
        else:
            try:
                interpobj = self._interp
                if interpobj is None:
                    interpobj = self._get_interp1d(**kwargs)
            except AttributeError: # does not exist yet
                interpobj = self._get_interp1d(**kwargs)

        # store interpolation object, if desired
        if store_interp:
            self._interp = interpobj

        # do the actual interpolation
        try:
            out = interpobj(at)
        except SystemError:
            interpobj = self._get_interp1d(**kwargs)
            if store_interp:
                self._interp = interpobj
            out = interpobj(at)

        # TODO: set all values outside of self.support to fill_value

        xyarray = XYArray(xvals=np.asanyarray(at), yvals=np.asanyarray(out).squeeze())
        return xyarray

    def subsample(self, *, fs):
        """Returns an AnalogSignalArray where the data has been
        subsampled to a new rate of fs.

        WARNING! Aliasing can occur! It is better to use downsample when
        lowering the sampling rate substantially.
        """

        return self.simplify(ds=1/fs)

    def simplify(self, *, ds=None, n_points=None):
        """Returns an AnalogSignalArray where the data has been
        simplified / subsampled.

        This function is primarily intended to be used for plotting and
        saving vector graphics without having too large file sizes as
        a result of too many points.

        Irrespective of whether 'ds' or 'n_points' are used, the exact
        underlying support is propagated, and the first and last points
        of the supports are always included, even if this would cause
        n_points or ds to be violated.

        WARNING! Simplify can create nan samples, when requesting a timestamp
        within an epoch, but outside of the (first, last) timestamps within that
        epoch, since we don't extrapolate, but only interpolate. # TODO: fix

        Parameters
        ----------
        ds : float, optional
            Time (in seconds), in which to step points.
        n_points : int, optional
            Number of points at which to intepolate data. If ds is None
            and n_points is None, then default is to use n_points=5,000

        Returns
        -------
        out : AnalogSignalArray
            Copy of AnalogSignalArray where data is only stored at the
            new subset of points.
        """

        if self.isempty:
            return self

        if ds is not None and n_points is not None:
            raise ValueError("ds and n_points cannot be used together")

        if n_points is not None:
            assert float(n_points).is_integer(), "n_points must be a positive integer!"
            assert n_points > 1, "n_points must be a positive integer > 1"
            # determine ds from number of desired points:
            ds = self.support.duration / (n_points-1)

        if ds is None:
            # neither n_points nor ds was specified, so assume defaults:
            n_points = np.min((5000, 250+self.n_samples//2, self.n_samples))
            ds = self.support.duration / (n_points-1)

        # build list of points at which to evaluate the AnalogSignalArray

        # we exclude all empty epochs:
        at = []
        lengths = self.lengths
        empty_epoch_ids = np.argwhere(lengths==0).squeeze().tolist()
        first_timestamps_per_epoch_idx = np.insert(np.cumsum(lengths[:-1]),0,0)
        first_timestamps_per_epoch_idx[empty_epoch_ids] = 0
        last_timestamps_per_epoch_idx = np.cumsum(lengths)-1
        last_timestamps_per_epoch_idx[empty_epoch_ids] = 0
        first_timestamps_per_epoch = self.time[first_timestamps_per_epoch_idx]
        last_timestamps_per_epoch = self.time[last_timestamps_per_epoch_idx]

        for ii, (start, stop) in enumerate(self.support.time):
            if lengths[ii] == 0:
                continue
            newxvals = utils.frange(first_timestamps_per_epoch[ii], last_timestamps_per_epoch[ii], step=ds).tolist()
            at.extend(newxvals)
            try:
                if newxvals[-1] < last_timestamps_per_epoch[ii]:
                    at.append(last_timestamps_per_epoch[ii])
            except IndexError:
                at.append(first_timestamps_per_epoch[ii])
                at.append(last_timestamps_per_epoch[ii])

        _, yvals = self.asarray(at=at, recalculate=True, store_interp=False)
        yvals = np.array(yvals, ndmin=2)

        asa = copy.copy(self)
        asa._time = np.asanyarray(at)
        asa._data = yvals
        asa._fs = 1/ds

        asa.__renew__()
        return asa

    def join(self, other, *, mode=None, inplace=False):
        """Join another AnalogSignalArray to this one.

        Parameters
        ----------
        other : AnalogSignalArray
            AnalogSignalArray (or derived type) to join to the current
            AnalogSignalArray. Other must have the same number of signals as
            the current AnalogSignalArray.
        mode : string, optional
            One of ['max', 'min', 'left', 'right', 'mean']. Specifies how the
            signals are merged inside overlapping epochs. Default is 'left'.
        inplace : boolean, optional
            If True, then current AnalogSignalArray is modified. If False, then
            a copy with the joined result is returned. Default is False.

        Returns
        -------
        out : AnalogSignalArray
            Copy of AnalogSignalArray where the new AnalogSignalArray has been
            joined to the current AnalogSignalArray.
        """

        if mode is None:
            mode = 'left'

        asa = copy.deepcopy(self)

        times = np.zeros((1,0))
        data = np.zeros((asa.n_signals,0))

        # if ASAs are disjoint:
        if self.support[other.support].isempty:
            # do a simple-as-butter join (concat) and sort
            times = np.append(times, self.time)
            data = np.hstack((data, self.data))
            times = np.append(times, other.time)
            data = np.hstack((data, other.data))
        else: # not disjoint
            both_eps = self.support[other.support]
            self_eps = self.support - both_eps - other.support
            other_eps = other.support - both_eps - self.support

            if mode=='left':
                self_eps += both_eps
                print(self_eps)

                tmp = self[self_eps]
                times = np.append(times, tmp.time)
                data = np.hstack((data, tmp.data))

                if not other_eps.isempty:
                    tmp = other[other_eps]
                    times = np.append(times, tmp.time)
                    data = np.hstack((data, tmp.data))
            elif mode=='right':
                other_eps += both_eps

                tmp = other[other_eps]
                times = np.append(times, tmp.time)
                data = np.hstack((data, tmp.data))

                if not self_eps.isempty:
                    tmp = self[self_eps]
                    times = np.append(times, tmp.time)
                    data = np.hstack((data, tmp.data))
            else:
                raise NotImplementedError("asa.join() has not yet been implemented for mode '{}'!".format(mode))

        sample_order = np.argsort(times)
        times = times[sample_order]
        data = data[:,sample_order]

        asa._data = data
        asa._time = times
        asa._support = (self.support + other.support).merge()

        return asa

    def _pdf(self, bins=None, n_points=None):
        """Return the probability distribution function for each signal."""
        from scipy import integrate

        if bins is None:
            bins = 100

        if n_points is None:
            n_points = 100

        if self.n_signals > 1:
            raise NotImplementedError('multiple signals not supported yet!')

        # fx, bins = np.histogram(self.data.squeeze(), bins=bins, normed=True)
        fx, bins = np.histogram(self.data.squeeze(), bins=bins)
        bin_centers = (bins + (bins[1]-bins[0])/2)[:-1]

        Ifx = integrate.simps(fx, bin_centers)

        pdf = AnalogSignalArray(timestamps=bin_centers,
                                data=fx/Ifx,
                                fs=1/(bin_centers[1]-bin_centers[0]),
                                support=core.EpochArray(self.data.min(), self.data.max())
                               ).simplify(n_points=n_points)

        return pdf

        # data = []
        # for signal in self.data:
        #     fx, bins = np.histogram(signal, bins=bins)
        #     bin_centers = (bins + (bins[1]-bins[0])/2)[:-1]



    def _cdf(self, n_points=None):
        """Return the probability distribution function for each signal."""

        if n_points is None:
            n_points = 100

        if self.n_signals > 1:
            raise NotImplementedError('multiple signals not supported yet!')

        X = np.sort(self.data.squeeze())
        F = np.array(range(self.n_samples))/float(self.n_samples)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cdf = AnalogSignalArray(timestamps=X,
                                     data=F,
                                     support=core.EpochArray(self.data.min(), self.data.max())
                                   ).simplify(n_points=n_points)

        return cdf

#----------------------------------------------------------------------#
#======================================================================#
