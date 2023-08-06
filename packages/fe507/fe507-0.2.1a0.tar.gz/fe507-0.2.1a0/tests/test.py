# fe507 / test.py
# Created by azat at 5.01.2023
import logging
import numpy as np
import pandas as pd
from scipy import stats

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
from matplotlib import pyplot as plt
from fe507 import Data, Collection, DataSource, settings, SIMPLE, DAY, WEEK, LOGARITHMIC, MONTH

settings.data_dir = "../data"

sp500 = Data(DataSource.SP500)

collection = Collection(sp500.data, name="S&P500")

ret = collection.get_range(from_year=1999, to_year=2022).frequency(MONTH).get(on='Index')
