#!/usr/bin/env python3
__author__ = 'Feng Zhu'
__email__ = 'fengzhu@usc.edu'
__version__ = '0.0.2'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import CubicSpline
#  from scipy.interpolate import splev, splrep
from scipy.signal import argrelmin, argrelmax
from scipy.signal import hilbert


def spl_extrema(ts, ys, extrema_func):
    extrema_loc = extrema_func(ys)
    ys_extrema = ys[extrema_loc]
    ts_extrema = ts[extrema_loc]
    cs = CubicSpline(ts_extrema, ys_extrema, bc_type='natural')
    spl_extrema = cs(ts)
    return spl_extrema


def sifting(ts, ys):
    spl_minima = spl_extrema(ts, ys, argrelmin)
    spl_maxima = spl_extrema(ts, ys, argrelmax)
    spl_mean = (spl_maxima + spl_minima)/2.
    h = ys - spl_mean
    return h


def stoppage_criterion(h_last, h_now, threshold=1e-2):
    sd = np.sum(((h_last - h_now)/h_last)**2)
    find_next_h = sd >= threshold
    return find_next_h


def imf_finding_criterion(ys):
    n_minima = np.size(argrelmin(ys))
    n_maxima = np.size(argrelmax(ys))
    find_next_imf = (n_minima > 1) & (n_maxima > 1)
    return find_next_imf


def emd(ts, ys, threshold=1e-2):
    imfs = []

    r_last = np.copy(ys)
    find_next_imf = imf_finding_criterion(r_last)

    while find_next_imf:
        find_next_h = True
        h_last = np.copy(ts)
        while find_next_h:
            h_now = sifting(ts, r_last)
            find_next_h = stoppage_criterion(h_last, h_now, threshold=np.std(ys)*threshold)
            h_last = np.copy(h_now)

        imfs.append(h_last)
        r_last = r_last - h_last
        find_next_imf = imf_finding_criterion(r_last)

    trend = np.copy(r_last)
    return imfs, trend


def hht(ts, imfs):
    ht = hilbert(imfs)

    amplitude = np.abs(ht)
    phase = np.angle(ht)
    omega = np.gradient(phase)


def plot_imfs(ts, ys, threshold=1e-2, imfs=None, trend=None, subplot_size=[10, 1.5], output_imfs=False):
    if imfs is None or trend is None:
        imfs, trend = emd(ts, ys, threshold=threshold)

    nimfs = np.shape(imfs)[0]

    sns.set(style="darkgrid", font_scale=1.5)
    fig, ax = plt.subplots(nimfs+2, 1, figsize=[subplot_size[0], subplot_size[1]*(nimfs+2)])

    ax[0].plot(ts, ys)
    ax[0].set_ylabel('Input')
    for i in range(nimfs):
        ax[i+1].plot(ts, imfs[i])
        ax[i+1].set_ylabel('IMF{}'.format(i+1))

    ax[-1].plot(ts, trend)
    ax[-1].set_ylabel('Trend')
    ax[-1].set_xlabel('Time')
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.55, wspace=0.35)

    if output_imfs:
        return imfs, trend
    else:
        return fig
