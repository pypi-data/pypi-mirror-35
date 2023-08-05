# -*- coding: utf-8 -*-

from . import FileParser as fp
import matplotlib.pyplot as plt
import glob
import numpy as np
from typing import Dict, List
import os
import re


def median_filtering(df):
    """Removes datapoints outside of 0.1 standard deviations of the median,
    with a rolling interval of 1 minute.
    Filters out bubbles and laser flare, plus compresses data."""
    df.is_copy = False
#    Necessary to avoid SettingWithCopyError in some versions of Pandas.
    df['median'] = df['ls8'].rolling(window=60).median()
    df['stdev'] = df['ls8'].rolling(window=60).std()
    filtered = df[(df['ls8'] <= df['median'] + 0.1 * df['stdev']) &
                  (df['ls8'] >= df['median'] - 0.1 * df['stdev'])]
    return filtered


def plot_experiment_file(file, smoothed=False) -> None:
    """Plots experiment file based on string of filename.
    When passing smoothed=True, data is filtered based on a rolling
    median before plotting"""
    header = fp.get_header_data(file)
    df = fp.parse_experiment_file(file)
    if smoothed:
        clean_df = median_filtering(df)
        ax = clean_df.plot(x='elapsedtime', y='median')
    else:
        ax = df.plot(x='elapsedtime', y='ls8')
    ax.set_title(header['Experiment Title'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Light Scattering')

    plt.show()


def plot_experiment_folder(folder, smoothed=False, save=False) -> None:
    """Parameters
         ----------------
        folder: string name of folder with csvs of data you want to plot, without
                backslash at end.
        smoothed: whether you want to apply a rolling median filter to the data
                (True/False),
        save: Whether want to save the images to your folder or display them
              immediately. (True/False)
        """
    for i, file in enumerate(glob.glob(folder + '/*.csv')):
        plt.figure(figsize=(7, 5))
        plot_experiment_file(file, smoothed)
        if save:
            plt.savefig(folder+file+'_plot')
        else:
            plt.show()


def plot_analysis_file(file, smoothed=False) -> None:
    """Plots analysis file based on string of filename.
    When passing smoothed=True, data is filtered based on a rolling
    median before plotting"""
    header = fp.get_header_data(file)
    df = fp.parse_analysis_file(file)
    if smoothed:
        clean_df = median_filtering(df)
        ax = clean_df.plot(x='elapstedtime', y='median')
    else:
        ax = df.plot(x='elapsedtime', y='lightscattering')
    ax.set_title(header['Analysis Title'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Light Scattering')

    plt.show()


def plot_analysis_folder(folder, smoothed=False, save=False) -> None:
    """Parameters
     ----------------
    folder: string name of folder with csvs of data you want to plot, without
            backslash at end.
    smoothed: whether you want to apply a rolling median filter to the data
            (True/False),
    save: Whether want to save the images to your folder or display them
          immediately. (True/False)
    """
    exp_dict = dict()
    for file in glob.glob(folder + '/*.csv'):
        exp_dict[file] = fp.parse_analysis_file(file)
    for title, file in exp_dict.items():
        plot_analysis_file(file, smoothed)
        if save:
            plt.savefig(folder+title)
        else:
            plt.show()


def subset_plotting(folder, params: Dict[str, List], size: tuple,
                    ordered=True) -> None:
    """Parameters
    ---------------
    folder: Folder name. string of path, without backslash after.
    params: dict of short experiment names (keys), and relevant cells (vals)
            See example in bitbucket readme.
    size: number of subplots. Should be equal to size of dictionary.
    ***Assumes cells are in ascending order in folder***
    ordered: If False, changes filenames in the folder to where they are
             ordered by experiment creation.
    """
    fig, ax = plt.subplots(nrows=size[0], ncols=size[1])
    if not ordered:
        name_stripping(folder)
    filenames = glob.glob(folder + './*.csv')
#   Error checking, makes sure no more than 16 csvs in folder, ax matches params.
    messages = ["Must have same # of subplots and params",
                "More than 16 cells specified",
                "More than 16 .csv files in folder.",
                "It looks like this is an empty folder. Check the filepath"]
    assert len(params) == len(ax.flatten()), messages[0]
    assert sum([len(param) for param in params.values()]) <= 16, messages[1]
    assert len(filenames) <= 16, messages[2]
    assert len(filenames) != 0, messages[3]

    for ix, (title, files) in zip(np.ndindex(ax.shape), params.items()):
        print(f'Starting processing/plotting for {title}')`
        for index in files:
            df = fp.parse_experiment_file(filenames[index-1])
            df_clean = median_filtering(df)
            ax[ix].plot(df_clean['elapsedtime'], df_clean['median'],
                            label=f'Cell #{index}')
            ax[ix].set_title(title)
            ax[ix].set_xlabel('Time')
            ax[ix].set_ylabel('Light Scattering')
            ax[ix].legend()


def name_stripping(folder):
    """Deletes all experimental information besides experiment number and
    date from experiment folder. Is helpful before running subset plotting to
    remove automatic file ordering. Assumes experiments were created in
    ascending order"""
    pattern = re.compile('- Sample -')
    for file in os.listdir(folder):
        m = pattern.search(file)
        if m:
            os.rename(folder + file, folder + file[m.end() + 1:])


