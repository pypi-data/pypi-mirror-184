# fe507 / test.py
# Created by azat at 5.01.2023
import logging

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
from fe507 import Data, Collection, DataSource, settings, MONTH, CurrencyAwareCollection, USD, TRY

settings.data_dir = "../data"

sp500 = Data(DataSource.SP500)
exchange_rates = Data(DataSource.EXCHANGE_RATES)
b100 = Data(DataSource.BIST100)
c = CurrencyAwareCollection(sp500, exchange_rates, currency=USD)
b = CurrencyAwareCollection(b100, exchange_rates, currency=TRY)

