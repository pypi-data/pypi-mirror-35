# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:55:15 2018

@author: eendebakpt
"""

#%%
import qcodes
import qtt
from qtt.data import *

ds = qcodes.load_data(r'C:\Users\eendebakpt\Documents\VP8_VP7.dat')

qcodes.MatPlot(ds.default_parameter_array('digi'))

A = np.array(ds.default_parameter_array())


def diffDataset(alldata, diff_dir='y', sigma=2, fig=None, meas_arr_name='meas'):
    """ Differentiate a dataset and plot the result.

    Args:
        alldata (qcodes DataSet)
        diff_dir (str): direction to differentiate in
        meas_arr_name (str): name of the measured array to be differentiated
        fig (int): the number for the figure to plot
        sigma (float):  parameter for gaussian filter kernel
    """
    meas_arr_name = alldata.default_parameter_name(meas_arr_name)
    print(meas_arr_name)
    meas_array = alldata.arrays[meas_arr_name]
    imx = qtt.diffImageSmooth(meas_array.ndarray, dy=diff_dir, sigma=sigma)
    name = 'diff_dir_%s' % diff_dir
    name = uniqueArrayName(alldata, name)
    data_arr = qcodes.DataArray(
        name=name, label=name, array_id=name, set_arrays=meas_array.set_arrays, preset_data=imx)

    alldata.add_array(data_arr)

    if fig is not None:
        plt.figure(fig)
        plt.clf()
        plot = MatPlot(interval=0, num=fig)
        plot.add(alldata.arrays[name])
        plot.fig.axes[0].autoscale(tight=True)
        plot.fig.axes[1].autoscale(tight=True)

    return alldata


#%%
ds2 = qtt.data.diffDataset(ds, diff_dir='xy', sigma=1, meas_arr_name='digitizer')

qcodes.MatPlot(ds.diff_dir_xy, num=24)
