# Data Preparation


```python
import logging

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
```


```python
from matplotlib import pyplot as plt
```


```python
from fe507 import settings
```


```python
settings.data_dir = "./../data/"
```


```python
from fe507 import Data, DataSource, RateOfReturnType, TimeFrameType
```


```python
sp500 = Data(DataSource.SP500)
bist100 = Data(DataSource.BIST100)
bistall = Data(DataSource.BISTALL)
gold = Data(DataSource.GOLD)
btceth = Data(DataSource.BTCETH)
exchange_rates = Data(DataSource.EXCHANGE_RATES)
interest_rates = Data(DataSource.INTEREST_RATE)
inflation = Data(DataSource.INFLATION)
```

    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/SP500.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of             Date    Index  Market cap (m$)  Unnamed: 3  Unnamed: 4  \
    0     1964-03-31    78.98           357907         NaN         NaN   
    1     1964-04-01    79.24           357907         NaN         NaN   
    2     1964-04-02    79.70           357907         NaN         NaN   
    3     1964-04-03    79.94           357907         NaN         NaN   
    4     1964-04-06    80.02           357907         NaN         NaN   
    ...          ...      ...              ...         ...         ...   
    15314 2022-12-12  3990.56         33536670         NaN         NaN   
    15315 2022-12-13  4019.65         33781200         NaN         NaN   
    15316 2022-12-14  3995.32         33576690         NaN         NaN   
    15317 2022-12-15  3895.75         32739940         NaN         NaN   
    15318 2022-12-16  3852.36         32375300         NaN         NaN   
    
           Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  Unnamed: 9  ...  \
    0             NaN         NaN         NaN         NaN         NaN  ...   
    1             NaN         NaN         NaN         NaN         NaN  ...   
    2             NaN         NaN         NaN         NaN         NaN  ...   
    3             NaN         NaN         NaN         NaN         NaN  ...   
    4             NaN         NaN         NaN         NaN         NaN  ...   
    ...           ...         ...         ...         ...         ...  ...   
    15314         NaN         NaN         NaN         NaN         NaN  ...   
    15315         NaN         NaN         NaN         NaN         NaN  ...   
    15316         NaN         NaN         NaN         NaN         NaN  ...   
    15317         NaN         NaN         NaN         NaN         NaN  ...   
    15318         NaN         NaN         NaN         NaN         NaN  ...   
    
           Unnamed: 206  Unnamed: 207  Unnamed: 208  Unnamed: 209  Unnamed: 210  \
    0               NaN           NaN           NaN           NaN           NaN   
    1               NaN           NaN           NaN           NaN           NaN   
    2               NaN           NaN           NaN           NaN           NaN   
    3               NaN           NaN           NaN           NaN           NaN   
    4               NaN           NaN           NaN           NaN           NaN   
    ...             ...           ...           ...           ...           ...   
    15314           NaN           NaN           NaN           NaN           NaN   
    15315           NaN           NaN           NaN           NaN           NaN   
    15316           NaN           NaN           NaN           NaN           NaN   
    15317           NaN           NaN           NaN           NaN           NaN   
    15318           NaN           NaN           NaN           NaN           NaN   
    
           Unnamed: 211  Unnamed: 212  Unnamed: 213  Unnamed: 214  Unnamed: 215  
    0               NaN           NaN           NaN           NaN           NaN  
    1               NaN           NaN           NaN           NaN           NaN  
    2               NaN           NaN           NaN           NaN           NaN  
    3               NaN           NaN           NaN           NaN           NaN  
    4               NaN           NaN           NaN           NaN           NaN  
    ...             ...           ...           ...           ...           ...  
    15314           NaN           NaN           NaN           NaN           NaN  
    15315           NaN           NaN           NaN           NaN           NaN  
    15316           NaN           NaN           NaN           NaN           NaN  
    15317           NaN           NaN           NaN           NaN           NaN  
    15318           NaN           NaN           NaN           NaN           NaN  
    
    [15319 rows x 216 columns]>
    ['Date', 'Index', 'Market cap (m$)', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55', 'Unnamed: 56', 'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69', 'Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76', 'Unnamed: 77', 'Unnamed: 78', 'Unnamed: 79', 'Unnamed: 80', 'Unnamed: 81', 'Unnamed: 82', 'Unnamed: 83', 'Unnamed: 84', 'Unnamed: 85', 'Unnamed: 86', 'Unnamed: 87', 'Unnamed: 88', 'Unnamed: 89', 'Unnamed: 90', 'Unnamed: 91', 'Unnamed: 92', 'Unnamed: 93', 'Unnamed: 94', 'Unnamed: 95', 'Unnamed: 96', 'Unnamed: 97', 'Unnamed: 98', 'Unnamed: 99', 'Unnamed: 100', 'Unnamed: 101', 'Unnamed: 102', 'Unnamed: 103', 'Unnamed: 104', 'Unnamed: 105', 'Unnamed: 106', 'Unnamed: 107', 'Unnamed: 108', 'Unnamed: 109', 'Unnamed: 110', 'Unnamed: 111', 'Unnamed: 112', 'Unnamed: 113', 'Unnamed: 114', 'Unnamed: 115', 'Unnamed: 116', 'Unnamed: 117', 'Unnamed: 118', 'Unnamed: 119', 'Unnamed: 120', 'Unnamed: 121', 'Unnamed: 122', 'Unnamed: 123', 'Unnamed: 124', 'Unnamed: 125', 'Unnamed: 126', 'Unnamed: 127', 'Unnamed: 128', 'Unnamed: 129', 'Unnamed: 130', 'Unnamed: 131', 'Unnamed: 132', 'Unnamed: 133', 'Unnamed: 134', 'Unnamed: 135', 'Unnamed: 136', 'Unnamed: 137', 'Unnamed: 138', 'Unnamed: 139', 'Unnamed: 140', 'Unnamed: 141', 'Unnamed: 142', 'Unnamed: 143', 'Unnamed: 144', 'Unnamed: 145', 'Unnamed: 146', 'Unnamed: 147', 'Unnamed: 148', 'Unnamed: 149', 'Unnamed: 150', 'Unnamed: 151', 'Unnamed: 152', 'Unnamed: 153', 'Unnamed: 154', 'Unnamed: 155', 'Unnamed: 156', 'Unnamed: 157', 'Unnamed: 158', 'Unnamed: 159', 'Unnamed: 160', 'Unnamed: 161', 'Unnamed: 162', 'Unnamed: 163', 'Unnamed: 164', 'Unnamed: 165', 'Unnamed: 166', 'Unnamed: 167', 'Unnamed: 168', 'Unnamed: 169', 'Unnamed: 170', 'Unnamed: 171', 'Unnamed: 172', 'Unnamed: 173', 'Unnamed: 174', 'Unnamed: 175', 'Unnamed: 176', 'Unnamed: 177', 'Unnamed: 178', 'Unnamed: 179', 'Unnamed: 180', 'Unnamed: 181', 'Unnamed: 182', 'Unnamed: 183', 'Unnamed: 184', 'Unnamed: 185', 'Unnamed: 186', 'Unnamed: 187', 'Unnamed: 188', 'Unnamed: 189', 'Unnamed: 190', 'Unnamed: 191', 'Unnamed: 192', 'Unnamed: 193', 'Unnamed: 194', 'Unnamed: 195', 'Unnamed: 196', 'Unnamed: 197', 'Unnamed: 198', 'Unnamed: 199', 'Unnamed: 200', 'Unnamed: 201', 'Unnamed: 202', 'Unnamed: 203', 'Unnamed: 204', 'Unnamed: 205', 'Unnamed: 206', 'Unnamed: 207', 'Unnamed: 208', 'Unnamed: 209', 'Unnamed: 210', 'Unnamed: 211', 'Unnamed: 212', 'Unnamed: 213', 'Unnamed: 214', 'Unnamed: 215']
    DEBUG:fe507.utils:handling source specific fields for DataSource.SP500
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BIST100.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of            Date    Index  Market cap (m TL)
    0    1988-01-04     0.07                  1
    1    1988-01-05     0.07                  1
    2    1988-01-06     0.07                  1
    3    1988-01-07     0.07                  1
    4    1988-01-08     0.07                  1
    ...         ...      ...                ...
    9117 2022-12-13  5256.19            4209786
    9118 2022-12-14  5066.50            4067326
    9119 2022-12-15  5188.82            4180713
    9120 2022-12-16  5214.29            4220547
    9121 2022-12-19  5391.91            4369087
    
    [9122 rows x 3 columns]>
    ['Date', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BIST100
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BISTALL.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of            Code    Index  Market cap (m TL)
    0    1997-01-02     9.94               2992
    1    1997-01-03    10.30               3084
    2    1997-01-06    10.50               3143
    3    1997-01-07    10.87               3235
    4    1997-01-08    11.32               3408
    ...         ...      ...                ...
    6768 2022-12-13  5915.50            5570492
    6769 2022-12-14  5714.06            5393263
    6770 2022-12-15  5835.87            5521100
    6771 2022-12-16  5869.89            5577080
    6772 2022-12-19  6027.50            5727575
    
    [6773 rows x 3 columns]>
    ['Code', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BISTALL
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/Gold.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of             Date  Price ($/t oz)
    0     1968-01-03           35.16
    1     1968-01-04           35.16
    2     1968-01-05           35.16
    3     1968-01-08           35.16
    4     1968-01-09           35.16
    ...          ...             ...
    14334 2022-12-13         1813.45
    14335 2022-12-14         1811.05
    14336 2022-12-15         1777.45
    14337 2022-12-16         1789.78
    14338 2022-12-19         1785.97
    
    [14339 rows x 2 columns]>
    ['Date', 'Price ($/t oz)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.GOLD
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BTCETH.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of            Date       Bitcoin  Ethereum
    0    2014-11-04    324.467934       NaN
    1    2014-11-05    328.644408       NaN
    2    2014-11-06    337.921358       NaN
    3    2014-11-07    348.992860       NaN
    4    2014-11-08    341.459753       NaN
    ...         ...           ...       ...
    2858 2022-11-21  15787.280000   1142.47
    2859 2022-11-22  16189.770000   1108.35
    2860 2022-11-23  16610.710000   1135.17
    2861 2022-11-24  16604.470000   1183.20
    2862 2022-11-25  16521.840000   1203.98
    
    [2863 rows x 3 columns]>
    ['Date', 'Bitcoin', 'Ethereum']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BTCETH
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/EXCHANGE.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of            Date    TL/USD   TL/Euro
    0    1987-12-31   0.00102       NaN
    1    1988-01-01   0.00102       NaN
    2    1988-01-04   0.00102       NaN
    3    1988-01-05   0.00102       NaN
    4    1988-01-06   0.00102       NaN
    ...         ...       ...       ...
    9118 2022-12-13  18.57500  19.83705
    9119 2022-12-14  18.62820  19.83685
    9120 2022-12-15  18.64180  19.85230
    9121 2022-12-16  18.63930  19.78620
    9122 2022-12-19  18.65260  19.73025
    
    [9123 rows x 3 columns]>
    ['Date', 'TL/USD', 'TL/Euro']
    DEBUG:fe507.utils:handling source specific fields for DataSource.EXCHANGE_RATES
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/TLDEPO.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of      Quarter  Deposit rate
    0    Q4 1978          6.00
    1    Q1 1979          6.00
    2    Q2 1979          7.33
    3    Q3 1979          8.00
    4    Q4 1979          8.00
    ..       ...           ...
    167  Q3 2020         12.52
    168  Q4 2020         17.42
    169  Q1 2021         19.72
    170  Q2 2021         20.25
    171  Q3 2021         20.00
    
    [172 rows x 2 columns]>
    ['Quarter', 'Deposit rate']
    DEBUG:fe507.utils:handling source specific fields for DataSource.INTEREST_RATE
    DEBUG:fe507.utils:reference field is None, skipping (None)
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/TLINF.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: <bound method DataFrame.info of          Month  CPI (%YOY)
    0   1995-01-15      125.90
    1   1995-02-15      122.40
    2   1995-03-15      119.70
    3   1995-04-15       88.40
    4   1995-05-15       79.80
    ..         ...         ...
    328 2022-05-31       57.92
    329 2022-06-30       64.59
    330 2022-07-29       69.94
    331 2022-08-31       70.60
    332 2022-09-30       67.73
    
    [333 rows x 2 columns]>
    ['Month', 'CPI (%YOY)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.INFLATION
    DEBUG:fe507.utils:reference field is None, skipping (None)


### S&P 500

```python
sp500._dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Index</th>
      <th>Market cap (m$)</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>...</th>
      <th>Unnamed: 208</th>
      <th>Unnamed: 209</th>
      <th>Unnamed: 210</th>
      <th>Unnamed: 211</th>
      <th>Unnamed: 212</th>
      <th>Unnamed: 213</th>
      <th>Unnamed: 214</th>
      <th>Unnamed: 215</th>
      <th>date</th>
      <th>quarter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1964-03-31</td>
      <td>78.98</td>
      <td>357907.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1964-03-31</td>
      <td>1964Q1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1964-04-01</td>
      <td>79.24</td>
      <td>357907.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1964-04-01</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1964-04-02</td>
      <td>79.70</td>
      <td>357907.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1964-04-02</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1964-04-03</td>
      <td>79.94</td>
      <td>357907.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1964-04-03</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964-04-06</td>
      <td>80.02</td>
      <td>357907.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1964-04-06</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>15314</th>
      <td>2022-12-12</td>
      <td>3990.56</td>
      <td>33536670.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-12-12</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>15315</th>
      <td>2022-12-13</td>
      <td>4019.65</td>
      <td>33781200.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>15316</th>
      <td>2022-12-14</td>
      <td>3995.32</td>
      <td>33576690.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>15317</th>
      <td>2022-12-15</td>
      <td>3895.75</td>
      <td>32739940.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>15318</th>
      <td>2022-12-16</td>
      <td>3852.36</td>
      <td>32375300.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>15319 rows × 218 columns</p>
</div>




```python
ror_d_sp500 = sp500.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.DAY)
```


```python
ror_d_sp500
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Index</th>
      <th>Market cap (m$)</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1964-03-31</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1964-04-01</th>
      <td>0.003287</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-04-02</th>
      <td>0.005788</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-04-03</th>
      <td>0.003007</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-04-06</th>
      <td>0.001000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>0.014178</td>
      <td>0.014178</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>0.007263</td>
      <td>0.007265</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>-0.006071</td>
      <td>-0.006072</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>-0.025237</td>
      <td>-0.025236</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>-0.011200</td>
      <td>-0.011200</td>
    </tr>
  </tbody>
</table>
<p>15319 rows × 2 columns</p>
</div>




```python
ror_d_sp500['Index'].plot(title='S&P500 Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'S&P500 Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_11_1.png)
    



```python
ror_w_sp500 = sp500.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.WEEK)
```


```python
ror_w_sp500
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Index</th>
      <th>Market cap (m$)</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1964-04-06</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1964-04-13</th>
      <td>-0.003129</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-04-20</th>
      <td>0.009110</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-04-27</th>
      <td>-0.014389</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1964-05-04</th>
      <td>0.014016</td>
      <td>0.014182</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-11-21</th>
      <td>-0.001849</td>
      <td>-0.001850</td>
    </tr>
    <tr>
      <th>2022-11-28</th>
      <td>0.003538</td>
      <td>0.003539</td>
    </tr>
    <tr>
      <th>2022-12-05</th>
      <td>0.008766</td>
      <td>0.008766</td>
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>-0.002073</td>
      <td>-0.002074</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>-0.035246</td>
      <td>-0.035244</td>
    </tr>
  </tbody>
</table>
<p>3064 rows × 2 columns</p>
</div>




```python
ror_d_sp500['Index'].plot(title='S&P500 Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_14_1.png)
    



```python
ror_m_sp500 = sp500.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.MONTH)
```


```python
ror_m_sp500
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Index</th>
      <th>Market cap (m$)</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1964-03-01</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1964-04-01</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1964-05-01</th>
      <td>0.011668</td>
      <td>0.014182</td>
    </tr>
    <tr>
      <th>1964-06-01</th>
      <td>-0.000749</td>
      <td>0.007741</td>
    </tr>
    <tr>
      <th>1964-07-01</th>
      <td>0.026606</td>
      <td>0.018304</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-08-01</th>
      <td>0.073876</td>
      <td>0.073864</td>
    </tr>
    <tr>
      <th>2022-09-01</th>
      <td>-0.037548</td>
      <td>-0.037559</td>
    </tr>
    <tr>
      <th>2022-10-01</th>
      <td>-0.101041</td>
      <td>-0.104349</td>
    </tr>
    <tr>
      <th>2022-11-01</th>
      <td>0.072725</td>
      <td>0.073167</td>
    </tr>
    <tr>
      <th>2022-12-01</th>
      <td>0.055600</td>
      <td>0.055638</td>
    </tr>
  </tbody>
</table>
<p>706 rows × 2 columns</p>
</div>




```python
ror_d_sp500['Index'].plot(title='S&P500 Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'S&P500 Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_17_1.png)
    





```python
ror_d_sp500['Index'].plot(kind='hist', title="S&P500 Daily Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'S&P500 Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_19_1.png)
    



```python
ror_w_sp500['Index'].plot(kind='hist', title="S&P500 Weekly Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_20_1.png)
    



```python
ror_m_sp500['Index'].plot(kind='hist', title="S&P500 Monthly Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'S&P500 Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_21_1.png)
    


### BIST 100

```python
bist100._dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Index</th>
      <th>Market cap (m TL)</th>
      <th>date</th>
      <th>quarter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1988-01-04</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-04</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1988-01-05</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-05</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1988-01-06</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-06</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1988-01-07</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-07</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1988-01-08</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-08</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9117</th>
      <td>2022-12-13</td>
      <td>5256.19</td>
      <td>4209786.0</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>9118</th>
      <td>2022-12-14</td>
      <td>5066.50</td>
      <td>4067326.0</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>9119</th>
      <td>2022-12-15</td>
      <td>5188.82</td>
      <td>4180713.0</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>9120</th>
      <td>2022-12-16</td>
      <td>5214.29</td>
      <td>4220547.0</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>9121</th>
      <td>2022-12-19</td>
      <td>5391.91</td>
      <td>4369087.0</td>
      <td>2022-12-19</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>9121 rows × 5 columns</p>
</div>




```python
ror_d_bist100 = bist100.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.DAY)
ror_w_bist100 = bist100.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.WEEK)
ror_m_bist100 = bist100.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.MONTH)
```


```python
ror_d_bist100['Index'].plot(title='BIST100 Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BIST100 Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_26_1.png)
    



```python
ror_d_bist100['Index'].plot(kind='hist', title="BIST100 Daily Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'BIST100 Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_27_1.png)
    



```python
ror_w_bist100['Index'].plot(title='BIST100 Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_28_1.png)
    



```python
ror_w_bist100['Index'].plot(kind='hist', title="BIST100 Weekly Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_29_1.png)
    



```python
ror_m_bist100['Index'].plot(title='BIST100 Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BIST100 Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_30_1.png)
    



```python
ror_m_bist100['Index'].plot(kind='hist', title="BIST100 Monthly Rate of Return (Logarithmic) Histogram")
```




    <AxesSubplot: title={'center': 'BIST100 Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_31_1.png)
    


### BISTALL

```python
bistall._dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Code</th>
      <th>Index</th>
      <th>Market cap (m TL)</th>
      <th>date</th>
      <th>quarter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1997-01-02</td>
      <td>9.94</td>
      <td>2992.0</td>
      <td>1997-01-02</td>
      <td>1997Q1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1997-01-03</td>
      <td>10.30</td>
      <td>3084.0</td>
      <td>1997-01-03</td>
      <td>1997Q1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997-01-06</td>
      <td>10.50</td>
      <td>3143.0</td>
      <td>1997-01-06</td>
      <td>1997Q1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1997-01-07</td>
      <td>10.87</td>
      <td>3235.0</td>
      <td>1997-01-07</td>
      <td>1997Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1997-01-08</td>
      <td>11.32</td>
      <td>3408.0</td>
      <td>1997-01-08</td>
      <td>1997Q1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6768</th>
      <td>2022-12-13</td>
      <td>5915.50</td>
      <td>5570492.0</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>6769</th>
      <td>2022-12-14</td>
      <td>5714.06</td>
      <td>5393263.0</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>6770</th>
      <td>2022-12-15</td>
      <td>5835.87</td>
      <td>5521100.0</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>6771</th>
      <td>2022-12-16</td>
      <td>5869.89</td>
      <td>5577080.0</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>6772</th>
      <td>2022-12-19</td>
      <td>6027.50</td>
      <td>5727575.0</td>
      <td>2022-12-19</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>6773 rows × 5 columns</p>
</div>




```python
ror_d_bistall = bistall.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.DAY)
ror_w_bistall = bistall.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.WEEK)
ror_m_bistall = bistall.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.MONTH)
```


```python
ror_d_bistall['Index'].plot(title='BISTALL Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BISTALL Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_35_1.png)
    



```python
ror_d_bistall['Index'].plot(kind='hist', title='BISTALL Daily Rate of Return (Logarithmic) Histogram')
```




    <AxesSubplot: title={'center': 'BISTALL Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_36_1.png)
    



```python
ror_w_bistall['Index'].plot(title='BISTALL Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BISTALL Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_37_1.png)
    



```python
ror_w_bistall['Index'].plot(kind='hist', title='BISTALL Weekly Rate of Return (Logarithmic) Histogram')
```




    <AxesSubplot: title={'center': 'BISTALL Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_38_1.png)
    



```python
ror_m_bistall['Index'].plot(title='BISTALL Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'BISTALL Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_39_1.png)
    



```python
ror_m_bistall['Index'].plot(kind='hist', title='BISTALL Monthly Rate of Return (Logarithmic) Histogram')
```




    <AxesSubplot: title={'center': 'BISTALL Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_40_1.png)
    


### Gold

```python
gold._dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Price ($/t oz)</th>
      <th>date</th>
      <th>quarter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1968-01-03</td>
      <td>35.16</td>
      <td>1968-01-03</td>
      <td>1968Q1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1968-01-04</td>
      <td>35.16</td>
      <td>1968-01-04</td>
      <td>1968Q1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1968-01-05</td>
      <td>35.16</td>
      <td>1968-01-05</td>
      <td>1968Q1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1968-01-08</td>
      <td>35.16</td>
      <td>1968-01-08</td>
      <td>1968Q1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1968-01-09</td>
      <td>35.16</td>
      <td>1968-01-09</td>
      <td>1968Q1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14334</th>
      <td>2022-12-13</td>
      <td>1813.45</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>14335</th>
      <td>2022-12-14</td>
      <td>1811.05</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>14336</th>
      <td>2022-12-15</td>
      <td>1777.45</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>14337</th>
      <td>2022-12-16</td>
      <td>1789.78</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>14338</th>
      <td>2022-12-19</td>
      <td>1785.97</td>
      <td>2022-12-19</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>14339 rows × 4 columns</p>
</div>




```python
ror_d_gold = gold.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.DAY)
ror_w_gold = gold.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.WEEK)
ror_m_gold = gold.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.MONTH)
```


```python
ror_d_gold.info()
```

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 14339 entries, 1968-01-03 to 2022-12-19
    Data columns (total 1 columns):
     #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
     0   Price ($/t oz)  14338 non-null  float64
    dtypes: float64(1)
    memory usage: 224.0 KB



```python
ror_d_gold['Price ($/t oz)'].plot(title='Gold Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Gold Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_45_1.png)
    



```python
ror_d_gold['Price ($/t oz)'].plot(title='Gold Daily Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Gold Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_46_1.png)
    



```python
ror_w_gold['Price ($/t oz)'].plot(title='Gold Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Gold Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_47_1.png)
    



```python
ror_w_gold['Price ($/t oz)'].plot(title='Gold Weekly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Gold Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_48_1.png)
    



```python
ror_m_gold['Price ($/t oz)'].plot(title='Gold Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Gold Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_49_1.png)
    



```python
ror_m_gold['Price ($/t oz)'].plot(title='Gold Monthly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Gold Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_50_1.png)
    


### Crypto (Bitcoin and Ethereum)

```python
btceth._dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Bitcoin</th>
      <th>Ethereum</th>
      <th>date</th>
      <th>quarter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2014-11-04</td>
      <td>324.467934</td>
      <td>NaN</td>
      <td>2014-11-04</td>
      <td>2014Q4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2014-11-05</td>
      <td>328.644408</td>
      <td>NaN</td>
      <td>2014-11-05</td>
      <td>2014Q4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2014-11-06</td>
      <td>337.921358</td>
      <td>NaN</td>
      <td>2014-11-06</td>
      <td>2014Q4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2014-11-07</td>
      <td>348.992860</td>
      <td>NaN</td>
      <td>2014-11-07</td>
      <td>2014Q4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2014-11-08</td>
      <td>341.459753</td>
      <td>NaN</td>
      <td>2014-11-08</td>
      <td>2014Q4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2858</th>
      <td>2022-11-21</td>
      <td>15787.280000</td>
      <td>1142.47</td>
      <td>2022-11-21</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2859</th>
      <td>2022-11-22</td>
      <td>16189.770000</td>
      <td>1108.35</td>
      <td>2022-11-22</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2860</th>
      <td>2022-11-23</td>
      <td>16610.710000</td>
      <td>1135.17</td>
      <td>2022-11-23</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2861</th>
      <td>2022-11-24</td>
      <td>16604.470000</td>
      <td>1183.20</td>
      <td>2022-11-24</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2862</th>
      <td>2022-11-25</td>
      <td>16521.840000</td>
      <td>1203.98</td>
      <td>2022-11-25</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>2863 rows × 5 columns</p>
</div>




```python
ror_d_btceth = btceth.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.DAY)
ror_w_btceth = btceth.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.WEEK)
ror_m_btceth = btceth.rate_of_return(mode=RateOfReturnType.LOGARITHMIC, timeframe=TimeFrameType.MONTH)
```


```python
ror_d_btceth['Bitcoin'].plot(title='Bitcoin Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Bitcoin Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_54_1.png)
    



```python
ror_d_btceth['Ethereum'].plot(title='Ethereum Daily Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Ethereum Daily Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_55_1.png)
    



```python
ror_d_btceth['Bitcoin'].plot(title='Bitcoin Daily Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Bitcoin Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_56_1.png)
    



```python
ror_d_btceth['Ethereum'].plot(title='Ethereum Daily Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Ethereum Daily Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_57_1.png)
    



```python
ror_w_btceth['Bitcoin'].plot(title='Bitcoin Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Bitcoin Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_58_1.png)
    



```python
ror_m_btceth['Bitcoin'].plot(title='Bitcoin Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Bitcoin Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_59_1.png)
    



```python
ror_w_btceth['Bitcoin'].plot(title='Bitcoin Weekly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Bitcoin Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_60_1.png)
    



```python
ror_m_btceth['Bitcoin'].plot(title='Bitcoin Monthly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Bitcoin Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_61_1.png)
    



```python
ror_w_btceth['Ethereum'].plot(title='Ethereum Weekly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Ethereum Weekly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_62_1.png)
    



```python
ror_m_btceth['Ethereum'].plot(title='Ethereum Monthly Rate of Return (Logarithmic)')
```




    <AxesSubplot: title={'center': 'Ethereum Monthly Rate of Return (Logarithmic)'}, xlabel='date'>




    
![png](output_63_1.png)
    



```python
ror_w_btceth['Ethereum'].plot(title='Ethereum Weekly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Ethereum Weekly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_64_1.png)
    



```python
ror_m_btceth['Ethereum'].plot(title='Ethereum Monthly Rate of Return (Logarithmic) Histogram', kind='hist')
```




    <AxesSubplot: title={'center': 'Ethereum Monthly Rate of Return (Logarithmic) Histogram'}, ylabel='Frequency'>




    
![png](output_65_1.png)
    



```python

```
