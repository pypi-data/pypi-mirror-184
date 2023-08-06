# SP500-BIST100-Price-Indexes


```python
import logging

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
```


```python
from matplotlib import pyplot as plt
```


```python
from fe507 import settings, WEEK

settings.data_dir = "./../data/"
```


```python
from fe507 import Data, DataSource
```


```python
from fe507 import Collection, CurrencyAwareCollection
```


```python
sp500 = Data(DataSource.SP500)
bist100 = Data(DataSource.BIST100)
exchange_rates = Data(DataSource.EXCHANGE_RATES)
```

    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/SP500.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Index', 'Market cap (m$)', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55', 'Unnamed: 56', 'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69', 'Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76', 'Unnamed: 77', 'Unnamed: 78', 'Unnamed: 79', 'Unnamed: 80', 'Unnamed: 81', 'Unnamed: 82', 'Unnamed: 83', 'Unnamed: 84', 'Unnamed: 85', 'Unnamed: 86', 'Unnamed: 87', 'Unnamed: 88', 'Unnamed: 89', 'Unnamed: 90', 'Unnamed: 91', 'Unnamed: 92', 'Unnamed: 93', 'Unnamed: 94', 'Unnamed: 95', 'Unnamed: 96', 'Unnamed: 97', 'Unnamed: 98', 'Unnamed: 99', 'Unnamed: 100', 'Unnamed: 101', 'Unnamed: 102', 'Unnamed: 103', 'Unnamed: 104', 'Unnamed: 105', 'Unnamed: 106', 'Unnamed: 107', 'Unnamed: 108', 'Unnamed: 109', 'Unnamed: 110', 'Unnamed: 111', 'Unnamed: 112', 'Unnamed: 113', 'Unnamed: 114', 'Unnamed: 115', 'Unnamed: 116', 'Unnamed: 117', 'Unnamed: 118', 'Unnamed: 119', 'Unnamed: 120', 'Unnamed: 121', 'Unnamed: 122', 'Unnamed: 123', 'Unnamed: 124', 'Unnamed: 125', 'Unnamed: 126', 'Unnamed: 127', 'Unnamed: 128', 'Unnamed: 129', 'Unnamed: 130', 'Unnamed: 131', 'Unnamed: 132', 'Unnamed: 133', 'Unnamed: 134', 'Unnamed: 135', 'Unnamed: 136', 'Unnamed: 137', 'Unnamed: 138', 'Unnamed: 139', 'Unnamed: 140', 'Unnamed: 141', 'Unnamed: 142', 'Unnamed: 143', 'Unnamed: 144', 'Unnamed: 145', 'Unnamed: 146', 'Unnamed: 147', 'Unnamed: 148', 'Unnamed: 149', 'Unnamed: 150', 'Unnamed: 151', 'Unnamed: 152', 'Unnamed: 153', 'Unnamed: 154', 'Unnamed: 155', 'Unnamed: 156', 'Unnamed: 157', 'Unnamed: 158', 'Unnamed: 159', 'Unnamed: 160', 'Unnamed: 161', 'Unnamed: 162', 'Unnamed: 163', 'Unnamed: 164', 'Unnamed: 165', 'Unnamed: 166', 'Unnamed: 167', 'Unnamed: 168', 'Unnamed: 169', 'Unnamed: 170', 'Unnamed: 171', 'Unnamed: 172', 'Unnamed: 173', 'Unnamed: 174', 'Unnamed: 175', 'Unnamed: 176', 'Unnamed: 177', 'Unnamed: 178', 'Unnamed: 179', 'Unnamed: 180', 'Unnamed: 181', 'Unnamed: 182', 'Unnamed: 183', 'Unnamed: 184', 'Unnamed: 185', 'Unnamed: 186', 'Unnamed: 187', 'Unnamed: 188', 'Unnamed: 189', 'Unnamed: 190', 'Unnamed: 191', 'Unnamed: 192', 'Unnamed: 193', 'Unnamed: 194', 'Unnamed: 195', 'Unnamed: 196', 'Unnamed: 197', 'Unnamed: 198', 'Unnamed: 199', 'Unnamed: 200', 'Unnamed: 201', 'Unnamed: 202', 'Unnamed: 203', 'Unnamed: 204', 'Unnamed: 205', 'Unnamed: 206', 'Unnamed: 207', 'Unnamed: 208', 'Unnamed: 209', 'Unnamed: 210', 'Unnamed: 211', 'Unnamed: 212', 'Unnamed: 213', 'Unnamed: 214', 'Unnamed: 215']
    DEBUG:fe507.utils:handling source specific fields for DataSource.SP500
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BIST100.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BIST100
    DEBUG:fe507.utils:Set up "data_dir" as: ./../data/
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/EXCHANGE.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'TL/USD', 'TL/Euro']
    DEBUG:fe507.utils:handling source specific fields for DataSource.EXCHANGE_RATES



```python
csp = Collection(sp500.data, name="S&P500")
cb1 = Collection(bist100.data, name="BIST100")
# SP500-BIST100-Price-Indexes
```


```python
from fe507 import TRY

cb1_usd = CurrencyAwareCollection(bist100, exchange_rates, currency=TRY)
```


```python
csp.raw
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
      <th>date</th>
      <th>quarter</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1964-03-31</th>
      <td>1964-03-31</td>
      <td>78.98</td>
      <td>357907.0</td>
      <td>1964-03-31</td>
      <td>1964Q1</td>
    </tr>
    <tr>
      <th>1964-04-01</th>
      <td>1964-04-01</td>
      <td>79.24</td>
      <td>357907.0</td>
      <td>1964-04-01</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>1964-04-02</th>
      <td>1964-04-02</td>
      <td>79.70</td>
      <td>357907.0</td>
      <td>1964-04-02</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>1964-04-03</th>
      <td>1964-04-03</td>
      <td>79.94</td>
      <td>357907.0</td>
      <td>1964-04-03</td>
      <td>1964Q2</td>
    </tr>
    <tr>
      <th>1964-04-06</th>
      <td>1964-04-06</td>
      <td>80.02</td>
      <td>357907.0</td>
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
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>2022-12-12</td>
      <td>3990.56</td>
      <td>33536670.0</td>
      <td>2022-12-12</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>2022-12-13</td>
      <td>4019.65</td>
      <td>33781200.0</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>2022-12-14</td>
      <td>3995.32</td>
      <td>33576690.0</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>2022-12-15</td>
      <td>3895.75</td>
      <td>32739940.0</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>2022-12-16</td>
      <td>3852.36</td>
      <td>32375300.0</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
  </tbody>
</table>
<p>15319 rows × 5 columns</p>
</div>




```python
cb1.raw
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
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1988-01-04</th>
      <td>1988-01-04</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-04</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>1988-01-05</th>
      <td>1988-01-05</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-05</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>1988-01-06</th>
      <td>1988-01-06</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-06</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>1988-01-07</th>
      <td>1988-01-07</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-07</td>
      <td>1988Q1</td>
    </tr>
    <tr>
      <th>1988-01-08</th>
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
      <th>2022-12-13</th>
      <td>2022-12-13</td>
      <td>5256.19</td>
      <td>4209786.0</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>2022-12-14</td>
      <td>5066.50</td>
      <td>4067326.0</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>2022-12-15</td>
      <td>5188.82</td>
      <td>4180713.0</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>2022-12-16</td>
      <td>5214.29</td>
      <td>4220547.0</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
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
cb1_usd.raw
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
      <th>TL/USD</th>
      <th>TL/Euro</th>
      <th>IndexUSD</th>
      <th>Market cap (m TL)USD</th>
      <th>TL/USDUSD</th>
      <th>TL/EuroUSD</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1988-01-04</th>
      <td>1988-01-04</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-04</td>
      <td>1988Q1</td>
      <td>0.00102</td>
      <td>NaN</td>
      <td>68.627451</td>
      <td>980.392157</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1988-01-05</th>
      <td>1988-01-05</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-05</td>
      <td>1988Q1</td>
      <td>0.00102</td>
      <td>NaN</td>
      <td>68.627451</td>
      <td>980.392157</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1988-01-06</th>
      <td>1988-01-06</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-06</td>
      <td>1988Q1</td>
      <td>0.00102</td>
      <td>NaN</td>
      <td>68.627451</td>
      <td>980.392157</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1988-01-07</th>
      <td>1988-01-07</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-07</td>
      <td>1988Q1</td>
      <td>0.00102</td>
      <td>NaN</td>
      <td>68.627451</td>
      <td>980.392157</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1988-01-08</th>
      <td>1988-01-08</td>
      <td>0.07</td>
      <td>1.0</td>
      <td>1988-01-08</td>
      <td>1988Q1</td>
      <td>0.00102</td>
      <td>NaN</td>
      <td>68.627451</td>
      <td>980.392157</td>
      <td>1.0</td>
      <td>NaN</td>
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
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>2022-12-13</td>
      <td>5256.19</td>
      <td>4209786.0</td>
      <td>2022-12-13</td>
      <td>2022Q4</td>
      <td>18.57500</td>
      <td>19.83705</td>
      <td>282.971198</td>
      <td>226637.200538</td>
      <td>1.0</td>
      <td>1.067943</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>2022-12-14</td>
      <td>5066.50</td>
      <td>4067326.0</td>
      <td>2022-12-14</td>
      <td>2022Q4</td>
      <td>18.62820</td>
      <td>19.83685</td>
      <td>271.980116</td>
      <td>218342.405600</td>
      <td>1.0</td>
      <td>1.064883</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>2022-12-15</td>
      <td>5188.82</td>
      <td>4180713.0</td>
      <td>2022-12-15</td>
      <td>2022Q4</td>
      <td>18.64180</td>
      <td>19.85230</td>
      <td>278.343293</td>
      <td>224265.521570</td>
      <td>1.0</td>
      <td>1.064935</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>2022-12-16</td>
      <td>5214.29</td>
      <td>4220547.0</td>
      <td>2022-12-16</td>
      <td>2022Q4</td>
      <td>18.63930</td>
      <td>19.78620</td>
      <td>279.747094</td>
      <td>226432.698653</td>
      <td>1.0</td>
      <td>1.061531</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>2022-12-19</td>
      <td>5391.91</td>
      <td>4369087.0</td>
      <td>2022-12-19</td>
      <td>2022Q4</td>
      <td>18.65260</td>
      <td>19.73025</td>
      <td>289.070156</td>
      <td>234234.744754</td>
      <td>1.0</td>
      <td>1.057775</td>
    </tr>
  </tbody>
</table>
<p>9121 rows × 11 columns</p>
</div>




```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2000-2008)'}, xlabel='date'>




    
![png](output_12_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2000-2008)'}, xlabel='date'>




    
![png](output_13_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2009-2022)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2009-2022)'}, xlabel='date'>




    
![png](output_14_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').raw.plot(title="S&P500 Weekly Price Index (All Time)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (All Time)'}, xlabel='date'>




    
![png](output_15_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').ror().raw.plot(title="S&P500 Weekly Rate of Return (All Time)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (All Time)'}, xlabel='date'>




    
![png](output_16_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').ror().raw.plot(title="S&P500 Weekly Rate of Return (All Time)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (All Time)'}, ylabel='Frequency'>




    
![png](output_17_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2009-2022)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2009-2022)'}, xlabel='date'>




    
![png](output_18_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2009-2022)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2009-2022)'}, ylabel='Frequency'>




    
![png](output_19_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2000-2008)'}, xlabel='date'>




    
![png](output_20_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_21_1.png)
    



```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (1990-1999)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (1990-1999)'}, xlabel='date'>




    
![png](output_22_1.png)
    



```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (1990-1999)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (1990-1999)'}, ylabel='Frequency'>




    
![png](output_23_1.png)
    



```python
cb1.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, xlabel='date'>




    
![png](output_24_1.png)
    



```python
cb1_usd.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, xlabel='date'>




    
![png](output_25_1.png)
    



```python
cb1.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, ylabel='Frequency'>




    
![png](output_26_1.png)
    



```python
cb1_usd.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, ylabel='Frequency'>




    
![png](output_27_1.png)
    



```python
cb1.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, xlabel='date'>




    
![png](output_28_1.png)
    



```python
cb1_usd.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, xlabel='date'>




    
![png](output_29_1.png)
    



```python
cb1.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_30_1.png)
    



```python
cb1_usd.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_31_1.png)
    



```python
cb1_usd.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_32_1.png)
    



```python
cb1.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, xlabel='date'>




    
![png](output_33_1.png)
    



```python
cb1.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, ylabel='Frequency'>




    
![png](output_34_1.png)
    



```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2000-2008)'}, xlabel='date'>




    
![png](output_35_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2000-2008)'}, xlabel='date'>




    
![png](output_36_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').raw.plot(
    title="S&P500 Weekly Price Index (2009-2022)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (2009-2022)'}, xlabel='date'>




    
![png](output_37_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').raw.plot(title="S&P500 Weekly Price Index (All Time)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Price Index (All Time)'}, xlabel='date'>




    
![png](output_38_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').ror().raw.plot(title="S&P500 Weekly Rate of Return (All Time)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (All Time)'}, xlabel='date'>




    
![png](output_39_1.png)
    



```python
csp.frequency(WEEK).get(on='Index').ror().raw.plot(title="S&P500 Weekly Rate of Return (All Time)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (All Time)'}, ylabel='Frequency'>




    
![png](output_40_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2009-2022)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2009-2022)'}, xlabel='date'>




    
![png](output_41_1.png)
    



```python
csp.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2009-2022)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2009-2022)'}, ylabel='Frequency'>




    
![png](output_42_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2000-2008)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2000-2008)'}, xlabel='date'>




    
![png](output_43_1.png)
    



```python
csp.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_44_1.png)
    



```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (1990-1999)")
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (1990-1999)'}, xlabel='date'>




    
![png](output_45_1.png)
    



```python
csp.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="S&P500 Weekly Rate of Return (1990-1999)", kind='hist')
```




    <AxesSubplot: title={'center': 'S&P500 Weekly Rate of Return (1990-1999)'}, ylabel='Frequency'>




    
![png](output_46_1.png)
    



```python
cb1.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, xlabel='date'>




    
![png](output_47_1.png)
    



```python
cb1.get_range(from_year=1990, to_year=1999).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (1990-1999)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (1990-1999)'}, ylabel='Frequency'>




    
![png](output_48_1.png)
    



```python
cb1.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, xlabel='date'>




    
![png](output_49_1.png)
    



```python
cb1.get_range(from_year=2000, to_year=2008).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2000-2008)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2000-2008)'}, ylabel='Frequency'>




    
![png](output_50_1.png)
    



```python
cb1.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, xlabel='date'>




    
![png](output_51_1.png)
    



```python
cb1.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='Index').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, ylabel='Frequency'>




    
![png](output_52_1.png)
    



```python
cb1_usd.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, ylabel='Frequency'>




    
![png](output_53_1.png)
    



```python
cb1_usd.get_range(from_year=2009, to_year=2022).frequency(WEEK).get(on='IndexUSD').ror().raw.plot(
    title="BIST100 Weekly Rate of Return (2009-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 Weekly Rate of Return (2009-2022)'}, xlabel='date'>




    
![png](output_54_1.png)
    



```python

```
