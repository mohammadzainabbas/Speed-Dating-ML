#! /usr/bin/python

import warnings
warnings.filterwarnings("ignore") # disable warnings
# from os import getcwd, listdir, environ, system, pardir
# from os.path import join, exists, isfile, isdir, abspath
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

from scipy.stats import ttest_ind
from scipy.stats.stats import pearsonr
from scipy.stats import chi2_contingency
from IPython.core.interactiveshell import InteractiveShell

if __name__ != "__main__":
    print("Imported utils.py")
    