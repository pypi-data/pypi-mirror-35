# tofseries.py ---
#
# Filename: tofseries.py
# Description:
#            single time-of-flight data series analysis
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu
#
# Created: Fri May  4 10:53:40 2018 (-0500)
# Version:
# Last-Updated: Tue Jul 31 22:11:08 2018 (-0500)
#           By: yulu
#     Update #: 683
#


import numpy as np
import pandas
from scipy.integrate import quad
import os
import re

from .descriptor import DescriptorMixin
from .common import winPathHandler, loadFile
from .regexp import RegMatch
from . import base
from .gaussian import Gaussian
from . import tofframe
from .plot import PlotTOFSeries
from .peak import SeriesPeak


def read_file(file_path,
              lowerBound = None,
              upperBound = None,
              removeOffset = True,
              cols = 2, usecols = None,
              offset_margin_how = 'outer',
              offset_margin_size = 20,
              skiprows = 0, sep = '\t'):
    """
    Read from sngle file and create an instance of TOFSeries

    Parameters
    ----------
    file_path: str
               path to file
    lowerBound: int or float
                time axis lower boundrary limit for data
    upperBound: int or float
                time axis upper boundrary limit for data
    removeOffset: bool
                  if True (default) remove data offset (set floor to 0 in no-signal region)
    cols: int
          Total number columns in the data file
    usecols: int
          The index of column that will be used out of total number of columns cols
    offset_margin_how: {"outer", "outer left", "out right", "inner", "inner left", "inner right"}, default "outer"

                       Specify the way to handle offset margin, offset floor value is calculated by averaging the
                       value in a given range relative to data lower and upper boundrary, with avaliable options:

                       * "outer" (default):  from both left and right side out of the [lowerBound, upperBound] region
                       * "outer left": like "outer" but from only left side
                       * "outer right": like "outer" but from only right side
                       * "inner": from both left and right side inside of the [lowerBound, upperBound] region
                       * "inner left": like "inner" but from only left side
                       * "inner right": like "inner" but from only left side

    offset_margin_size: int
                        Number of values to use for averaging when calculating offset
    skiprows: int
              number of rows to skip when read in data
    sep: str, defult "\t"
         seperator for columns in the data file

    Returns:
    --------
    Instance of class TOFSeries

    """
    return  TOFSeries.from_file(file_path, lowerBound = lowerBound,
                              upperBound = upperBound, removeOffset = removeOffset,
                              cols = cols, usecols = usecols,
                              offset_margin_how = offset_margin_how,
                              offset_margin_size = offset_margin_size,
                              skiprows = skiprows, sep = sep)


class TOFSeries(pandas.Series):
    pandas.set_option('precision', 9)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return TOFSeries
    @property
    def _constructor_expanddim(self):
        return tofframe.TOFFrame

    @property
    def _make_mixin(self):
        return self.copy()

    def _toTOFSeries(func):
        """
        Decorator to wrap series returns for method chain
        """
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == pandas.core.series.Series:
                return TOFSeries(result)
            else:
                return result
        return wrapper

    @classmethod
    def from_file(cls, file_path, lowerBound = None, upperBound = None, removeOffset = True,
                cols = 2, usecols = None, offset_margin_how = 'outer', offset_margin_size = 20,
                skiprows = 0, sep = '\t'):
        """
        Buid TOF instance from given file
        Current only works for '\t' seperated txt and lvm file
        """

        file_path = winPathHandler(file_path)
        # If given folder path
        if os.path.isdir(file_path):
            raise ValueError("[*] TOFSeries only take single file as series source!")

        # if given file path
        else:
            data = loadFile(file_path, cols = cols, usecols = usecols,skiprows = skiprows,  sep = sep)
            if lowerBound and upperBound:
                lb, ub = TOFSeries.find_time_idx(data[:,0], lowerBound, upperBound)
                time = data[lb : ub, 0]
                if removeOffset:
                    value = TOFSeries.remove_data_offset(data[:, 1], lowerBoundIdx = lb, upperBoundIdx = ub, how = offset_margin_how, margin_size = offset_margin_size)[lb:ub]
                else:
                    value = data[lb:ub, 1]
            else:
                time = data[:,0]
                value = data[:,1]
        return cls(value, index = time)




    @staticmethod
    def find_time_idx(time, *args):
        """
        Generator of time index for a given time value
        args: can be a single number, e.g. 1000e-6
              or a few numbers, e.g.  100e-6, 200e-6, 300e-6

        """
        time = np.array(time)
        t_max_gap = np.max(np.diff(time))
        for arg_elem in args:
            if hasattr(arg_elem, '__iter__'):
                for t in arg_elem:
                    candi_idx = np.argmin(abs(t - time))
                    if abs(t - time[candi_idx]) > t_max_gap:
                        raise ValueError("[*] Error: find_time_idx didn't find closest match !\n" +
                                         "[!] Searching for time %f while the closest match is %f, you may consider check the unit!"
                                         %(t, time[candi_idx]))
                    else:
                        yield candi_idx

            else:
                candi_idx = np.argmin(abs(arg_elem - time))
                if abs(arg_elem - time[candi_idx]) > t_max_gap:
                        raise ValueError("[*] Error: find_time_idx didn't find closest match !\n" +
                                         "[!] Searching for time %f while the closest match is %f, you may consider check the unit!"
                                         %(arg_elem, time[candi_idx]))
                else:
                    candi_idx
                    yield candi_idx

    @staticmethod
    def remove_data_offset(data, lowerBoundIdx = None, upperBoundIdx = None, how = 'outer', margin_size = 10):
        """
        remove offset in 1D array data
        """
        # check bound index assignment
        if lowerBoundIdx is None and upperBoundIdx is None:
            lowerBoundIdx = 0
            upperBoundIdx = len(data)
            if 'outer' in how:
                how = 'inner'
                print("[*] No bound index specified, using default full range !")
                print("[*] Outer margin offset forced to be *inner* !")
            else:
                pass
        elif lowerBoundIdx is None:
            lowerBoundIdx = 0
            if how in ['outer', 'outer left']:
                how = how.replace('outer', 'inner')
                print("[*] No lower bound index specified, using default 0 !")
                print("[*] Outer margin offset forced to be *inner* !")
            else:
                pass
        elif upperBoundIdx is None:
            upperBoundIdx = len(data)
            if how in ['outer', 'outer right']:
                how = how.replace('outer', 'inner')
                print("[*] No lower bound index specified, using default max length !")
                print("[*] Outer margin offset forced to be *inner* !")
            else:
                pass
        else:
            pass

        if how == 'outer':
            offset = (np.mean(data[lowerBoundIdx-margin_size: lowerBoundIdx]) + np.mean(data[upperBoundIdx : upperBoundIdx + margin_size]))  / 2.
        elif how == 'outer left':
            offset = np.mean(data[lowerBoundIdx-margin_size: lowerBoundIdx])
        elif how == 'outer right':
            offset = np.mean(data[upperBoundIdx : upperBoundIdx + margin_size])
        elif how == 'inner':
            offset = (np.mean(data[lowerBoundIdx: lowerBoundIdx + margin_size]) + np.mean(data[upperBoundIdx - margin_size: upperBoundIdx]))  / 2
        elif how == 'inner left':
            offset = np.mean(data[lowerBoundIdx: lowerBoundIdx + margin_size])
        elif how == 'inner right':
            offset = np.mean(data[upperBoundIdx - margin_size: upperBoundIdx])
        else:
            raise ValueError(("[*] how: %s not understood !\n" +
                              "[!] possible values of how: 'outer', 'outer left', 'outer right', 'inner', 'inner left', 'inner right'") % how)

        data = np.array(data) - offset
        return data

    @_toTOFSeries
    def selectTimeSlice(self, *args, inplace = False):
        """
        makeSlice
        -------------
        Create descrete time sliced series, if want continus range, use makeTimeRange()
        [Input]
        :args: descrete time slicing values, can use timeSlice(1,2,3,4))
        [Output]
        Series of sliced data
        """

        slice_value = []
        for arg_elem in args:
            arg_elem = self.find_time_idx(self.index, arg_elem)
            if hasattr(arg_elem, '__iter__'):
                for t in arg_elem:
                    slice_value.append(self.iloc[t])
            else:
                slice_value.append(self.iloc[arg_elem])
        slice_series = pandas.Series(slice_value)
        if inplace:
            self.__init__(slice_series)
        else:
            return slice_series

    @_toTOFSeries
    def selectTimeRange(self, lowerBound, upperBound, inplace = False):
        """
        makeTimeRange
        Select continious data in a provided time range
        --------------
        """
        lb, ub = TOFSeries.find_time_idx(self.index, lowerBound, upperBound)
        selected = self.iloc[lb:ub, :].copy()
        if inplace:
            self.__init__(selected)
        else:
            return selected


    def sec_to_microsec(self, offset_sec = 0, inplace = False):
        """
        convert seconds in index to microseconds
        """
        times = (self.index - offset_sec) * 1e6
        if inplace:
            self.index = times
        else:
            return times

    def gausFit(self, offset = False):
        """
        1D gauss fit
        """
        popt, pcov = Gaussian.gausFit(x = self.index, y = self.values, offset = offset)
        return popt, pcov


    ###
    # Below func might be redundant
    ###

    def gausCenter(self, offset = False):
        """
        gaus fit center
        """
        popt, pcov = self.gausFit(offset = offset)
        center = popt[1]
        std = np.sqrt(pcov[1,1])
        return center, std

    def gausStd(self, offset = False):
        """
        gaus fit std
        """
        popt, pcov = self.gausFit(offset = offset)
        sigma = popt[2]
        std = np.sqrt(pcov[2,2])
        return sigma, std

    # Descriptors
    plot1d = DescriptorMixin(PlotTOFSeries)
    peak = DescriptorMixin(SeriesPeak)
