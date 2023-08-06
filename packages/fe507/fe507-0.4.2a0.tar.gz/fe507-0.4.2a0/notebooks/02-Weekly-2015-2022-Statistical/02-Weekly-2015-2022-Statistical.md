# 02-Weekly-2015-2022-Statistical


```python
import logging

from matplotlib import pyplot as plt

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
from fe507 import Data, Collection, DataSource, settings, CollectionGroup

settings.data_dir = "../data"
```


```python
exchange_rates = Data(DataSource.EXCHANGE_RATES)
sp500 = Data(DataSource.SP500)
b100 = Data(DataSource.BIST100)
ball = Data(DataSource.BISTALL)
gold = Data(DataSource.GOLD)
btc = Data(DataSource.BTCETH)

year_range = {
    "from_year": 2015,
    "to_year": 2022
}
```

    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/EXCHANGE.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'TL/USD', 'TL/Euro']
    DEBUG:fe507.utils:handling source specific fields for DataSource.EXCHANGE_RATES
    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/SP500.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Index', 'Market cap (m$)', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55', 'Unnamed: 56', 'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69', 'Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76', 'Unnamed: 77', 'Unnamed: 78', 'Unnamed: 79', 'Unnamed: 80', 'Unnamed: 81', 'Unnamed: 82', 'Unnamed: 83', 'Unnamed: 84', 'Unnamed: 85', 'Unnamed: 86', 'Unnamed: 87', 'Unnamed: 88', 'Unnamed: 89', 'Unnamed: 90', 'Unnamed: 91', 'Unnamed: 92', 'Unnamed: 93', 'Unnamed: 94', 'Unnamed: 95', 'Unnamed: 96', 'Unnamed: 97', 'Unnamed: 98', 'Unnamed: 99', 'Unnamed: 100', 'Unnamed: 101', 'Unnamed: 102', 'Unnamed: 103', 'Unnamed: 104', 'Unnamed: 105', 'Unnamed: 106', 'Unnamed: 107', 'Unnamed: 108', 'Unnamed: 109', 'Unnamed: 110', 'Unnamed: 111', 'Unnamed: 112', 'Unnamed: 113', 'Unnamed: 114', 'Unnamed: 115', 'Unnamed: 116', 'Unnamed: 117', 'Unnamed: 118', 'Unnamed: 119', 'Unnamed: 120', 'Unnamed: 121', 'Unnamed: 122', 'Unnamed: 123', 'Unnamed: 124', 'Unnamed: 125', 'Unnamed: 126', 'Unnamed: 127', 'Unnamed: 128', 'Unnamed: 129', 'Unnamed: 130', 'Unnamed: 131', 'Unnamed: 132', 'Unnamed: 133', 'Unnamed: 134', 'Unnamed: 135', 'Unnamed: 136', 'Unnamed: 137', 'Unnamed: 138', 'Unnamed: 139', 'Unnamed: 140', 'Unnamed: 141', 'Unnamed: 142', 'Unnamed: 143', 'Unnamed: 144', 'Unnamed: 145', 'Unnamed: 146', 'Unnamed: 147', 'Unnamed: 148', 'Unnamed: 149', 'Unnamed: 150', 'Unnamed: 151', 'Unnamed: 152', 'Unnamed: 153', 'Unnamed: 154', 'Unnamed: 155', 'Unnamed: 156', 'Unnamed: 157', 'Unnamed: 158', 'Unnamed: 159', 'Unnamed: 160', 'Unnamed: 161', 'Unnamed: 162', 'Unnamed: 163', 'Unnamed: 164', 'Unnamed: 165', 'Unnamed: 166', 'Unnamed: 167', 'Unnamed: 168', 'Unnamed: 169', 'Unnamed: 170', 'Unnamed: 171', 'Unnamed: 172', 'Unnamed: 173', 'Unnamed: 174', 'Unnamed: 175', 'Unnamed: 176', 'Unnamed: 177', 'Unnamed: 178', 'Unnamed: 179', 'Unnamed: 180', 'Unnamed: 181', 'Unnamed: 182', 'Unnamed: 183', 'Unnamed: 184', 'Unnamed: 185', 'Unnamed: 186', 'Unnamed: 187', 'Unnamed: 188', 'Unnamed: 189', 'Unnamed: 190', 'Unnamed: 191', 'Unnamed: 192', 'Unnamed: 193', 'Unnamed: 194', 'Unnamed: 195', 'Unnamed: 196', 'Unnamed: 197', 'Unnamed: 198', 'Unnamed: 199', 'Unnamed: 200', 'Unnamed: 201', 'Unnamed: 202', 'Unnamed: 203', 'Unnamed: 204', 'Unnamed: 205', 'Unnamed: 206', 'Unnamed: 207', 'Unnamed: 208', 'Unnamed: 209', 'Unnamed: 210', 'Unnamed: 211', 'Unnamed: 212', 'Unnamed: 213', 'Unnamed: 214', 'Unnamed: 215']
    DEBUG:fe507.utils:handling source specific fields for DataSource.SP500
    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BIST100.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BIST100
    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BISTALL.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Code', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BISTALL
    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/Gold.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Price ($/t oz)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.GOLD
    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BTCETH.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Bitcoin', 'Ethereum']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BTCETH



```python
## Create Collection
csp = Collection(sp500.data, name="S&P500").get_range(**year_range).get(on='Index')
cb1 = Collection(b100.data, name="BIST100").get_range(**year_range).get(on='Index')
cba = Collection(ball.data, name="BIST ALL").get_range(**year_range).get(on='Index')
cg = Collection(gold.data, name='Gold').get_range(**year_range).get(on='Price ($/t oz)')
cbtc = Collection(btc.data, name="Bitcoin").get_range(**year_range).get(on='Bitcoin')
```

## SP500


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
      <th>Index</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015-01-01</th>
      <td>2058.90</td>
    </tr>
    <tr>
      <th>2015-01-02</th>
      <td>2058.20</td>
    </tr>
    <tr>
      <th>2015-01-05</th>
      <td>2020.58</td>
    </tr>
    <tr>
      <th>2015-01-06</th>
      <td>2002.61</td>
    </tr>
    <tr>
      <th>2015-01-07</th>
      <td>2025.90</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>3990.56</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>4019.65</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>3995.32</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>3895.75</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>3852.36</td>
    </tr>
  </tbody>
</table>
<p>1995 rows × 1 columns</p>
</div>




```python
csp.mean
```




    Index    2980.835895
    dtype: float64




```python
csp.variance
```




    Index    660569.74855
    dtype: float64




```python
g = CollectionGroup([csp, cb1, cba, cg, cbtc])
```


```python
g.mean
```




    S&P500       2980.835895
    BIST100      1264.851276
    BIST ALL     1348.761589
    Gold         1465.749102
    Bitcoin     12676.917011
    dtype: float64




```python
g.variance
```




    S&P500      6.605697e+05
    BIST100     5.413134e+05
    BIST ALL    7.094168e+05
    Gold        7.512064e+04
    Bitcoin     2.620194e+08
    dtype: float64




```python
g.standard_deviation
```




    S&P500        812.754421
    BIST100       735.740021
    BIST ALL      842.268817
    Gold          274.081452
    Bitcoin     16187.014105
    dtype: float64




```python
g.max
```




    S&P500       4796.56000
    BIST100      5391.91000
    BIST ALL     6027.50000
    Gold         2052.79500
    Bitcoin     67553.94893
    dtype: float64




```python
g.min
```




    S&P500      1829.080000
    BIST100      685.680000
    BIST ALL     699.860000
    Gold        1051.970000
    Bitcoin      178.016008
    dtype: float64




```python
g.inter_quartile_range
```




    S&P500     NaN
    BIST100    NaN
    BIST ALL   NaN
    Gold       NaN
    Bitcoin    NaN
    dtype: float64




```python
csp.inter_quartile_range
```




    Index    1404.975
    dtype: float64




```python
cb1.inter_quartile_range
```




    Index    501.355
    dtype: float64




```python
cba.inter_quartile_range
```




    Index    684.845
    dtype: float64




```python
cg.inter_quartile_range
```




    Price ($/t oz)    519.08
    dtype: float64




```python
cbtc.inter_quartile_range
```




    Bitcoin    13331.746091
    dtype: float64




```python
g.skewness
```




    S&P500      0.590823
    BIST100     2.865820
    BIST ALL    2.769847
    Gold        0.420385
    Bitcoin     1.616225
    dtype: float64




```python
g.kurtosis
```




    S&P500     -0.861520
    BIST100     9.278058
    BIST ALL    8.859743
    Gold       -1.376691
    Bitcoin     1.519731
    dtype: float64




```python
g.autocorrelation
```




    S&P500      0.999004
    BIST100     0.999462
    BIST ALL    0.999584
    Gold        0.998797
    Bitcoin     0.998691
    dtype: float64




```python
g.covariance
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
      <th>S&amp;P500</th>
      <th>BIST100</th>
      <th>BIST ALL</th>
      <th>Gold</th>
      <th>Bitcoin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>S&amp;P500</th>
      <td>6.605697e+05</td>
      <td>3.905255e+05</td>
      <td>4.650232e+05</td>
      <td>1.974475e+05</td>
      <td>1.205746e+07</td>
    </tr>
    <tr>
      <th>BIST100</th>
      <td>3.905255e+05</td>
      <td>5.413134e+05</td>
      <td>6.236793e+05</td>
      <td>1.182902e+05</td>
      <td>5.673533e+06</td>
    </tr>
    <tr>
      <th>BIST ALL</th>
      <td>4.650232e+05</td>
      <td>6.236793e+05</td>
      <td>7.094168e+05</td>
      <td>1.428434e+05</td>
      <td>6.967881e+06</td>
    </tr>
    <tr>
      <th>Gold</th>
      <td>1.974475e+05</td>
      <td>1.182902e+05</td>
      <td>1.428434e+05</td>
      <td>7.512064e+04</td>
      <td>3.430805e+06</td>
    </tr>
    <tr>
      <th>Bitcoin</th>
      <td>1.205746e+07</td>
      <td>5.673533e+06</td>
      <td>6.967881e+06</td>
      <td>3.430805e+06</td>
      <td>2.620194e+08</td>
    </tr>
  </tbody>
</table>
</div>




```python
g.correlation
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
      <th>S&amp;P500</th>
      <th>BIST100</th>
      <th>BIST ALL</th>
      <th>Gold</th>
      <th>Bitcoin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>S&amp;P500</th>
      <td>1.000000</td>
      <td>0.655270</td>
      <td>0.682664</td>
      <td>0.882725</td>
      <td>0.904527</td>
    </tr>
    <tr>
      <th>BIST100</th>
      <td>0.655270</td>
      <td>1.000000</td>
      <td>0.998345</td>
      <td>0.580547</td>
      <td>0.527380</td>
    </tr>
    <tr>
      <th>BIST ALL</th>
      <td>0.682664</td>
      <td>0.998345</td>
      <td>1.000000</td>
      <td>0.612273</td>
      <td>0.565746</td>
    </tr>
    <tr>
      <th>Gold</th>
      <td>0.882725</td>
      <td>0.580547</td>
      <td>0.612273</td>
      <td>1.000000</td>
      <td>0.762223</td>
    </tr>
    <tr>
      <th>Bitcoin</th>
      <td>0.904527</td>
      <td>0.527380</td>
      <td>0.565746</td>
      <td>0.762223</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
corr = g.correlation
```


```python
corr.style.background_gradient(cmap='coolwarm')
```




<style type="text/css">
#T_4f027_row0_col0, #T_4f027_row1_col1, #T_4f027_row1_col2, #T_4f027_row2_col1, #T_4f027_row2_col2, #T_4f027_row3_col3, #T_4f027_row4_col4 {
  background-color: #b40426;
  color: #f1f1f1;
}
#T_4f027_row0_col1 {
  background-color: #94b6ff;
  color: #000000;
}
#T_4f027_row0_col2 {
  background-color: #93b5fe;
  color: #000000;
}
#T_4f027_row0_col3 {
  background-color: #f6a586;
  color: #000000;
}
#T_4f027_row0_col4 {
  background-color: #ee8468;
  color: #f1f1f1;
}
#T_4f027_row1_col0, #T_4f027_row1_col3, #T_4f027_row1_col4, #T_4f027_row4_col1, #T_4f027_row4_col2 {
  background-color: #3b4cc0;
  color: #f1f1f1;
}
#T_4f027_row2_col0, #T_4f027_row2_col4 {
  background-color: #536edd;
  color: #f1f1f1;
}
#T_4f027_row2_col3 {
  background-color: #516ddb;
  color: #f1f1f1;
}
#T_4f027_row3_col0 {
  background-color: #f7ba9f;
  color: #000000;
}
#T_4f027_row3_col1 {
  background-color: #5d7ce6;
  color: #f1f1f1;
}
#T_4f027_row3_col2 {
  background-color: #5b7ae5;
  color: #f1f1f1;
}
#T_4f027_row3_col4 {
  background-color: #dcdddd;
  color: #000000;
}
#T_4f027_row4_col0 {
  background-color: #f6a385;
  color: #000000;
}
#T_4f027_row4_col3 {
  background-color: #cad8ef;
  color: #000000;
}
</style>
<table id="T_4f027">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_4f027_level0_col0" class="col_heading level0 col0" >S&P500</th>
      <th id="T_4f027_level0_col1" class="col_heading level0 col1" >BIST100</th>
      <th id="T_4f027_level0_col2" class="col_heading level0 col2" >BIST ALL</th>
      <th id="T_4f027_level0_col3" class="col_heading level0 col3" >Gold</th>
      <th id="T_4f027_level0_col4" class="col_heading level0 col4" >Bitcoin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_4f027_level0_row0" class="row_heading level0 row0" >S&P500</th>
      <td id="T_4f027_row0_col0" class="data row0 col0" >1.000000</td>
      <td id="T_4f027_row0_col1" class="data row0 col1" >0.655270</td>
      <td id="T_4f027_row0_col2" class="data row0 col2" >0.682664</td>
      <td id="T_4f027_row0_col3" class="data row0 col3" >0.882725</td>
      <td id="T_4f027_row0_col4" class="data row0 col4" >0.904527</td>
    </tr>
    <tr>
      <th id="T_4f027_level0_row1" class="row_heading level0 row1" >BIST100</th>
      <td id="T_4f027_row1_col0" class="data row1 col0" >0.655270</td>
      <td id="T_4f027_row1_col1" class="data row1 col1" >1.000000</td>
      <td id="T_4f027_row1_col2" class="data row1 col2" >0.998345</td>
      <td id="T_4f027_row1_col3" class="data row1 col3" >0.580547</td>
      <td id="T_4f027_row1_col4" class="data row1 col4" >0.527380</td>
    </tr>
    <tr>
      <th id="T_4f027_level0_row2" class="row_heading level0 row2" >BIST ALL</th>
      <td id="T_4f027_row2_col0" class="data row2 col0" >0.682664</td>
      <td id="T_4f027_row2_col1" class="data row2 col1" >0.998345</td>
      <td id="T_4f027_row2_col2" class="data row2 col2" >1.000000</td>
      <td id="T_4f027_row2_col3" class="data row2 col3" >0.612273</td>
      <td id="T_4f027_row2_col4" class="data row2 col4" >0.565746</td>
    </tr>
    <tr>
      <th id="T_4f027_level0_row3" class="row_heading level0 row3" >Gold</th>
      <td id="T_4f027_row3_col0" class="data row3 col0" >0.882725</td>
      <td id="T_4f027_row3_col1" class="data row3 col1" >0.580547</td>
      <td id="T_4f027_row3_col2" class="data row3 col2" >0.612273</td>
      <td id="T_4f027_row3_col3" class="data row3 col3" >1.000000</td>
      <td id="T_4f027_row3_col4" class="data row3 col4" >0.762223</td>
    </tr>
    <tr>
      <th id="T_4f027_level0_row4" class="row_heading level0 row4" >Bitcoin</th>
      <td id="T_4f027_row4_col0" class="data row4 col0" >0.904527</td>
      <td id="T_4f027_row4_col1" class="data row4 col1" >0.527380</td>
      <td id="T_4f027_row4_col2" class="data row4 col2" >0.565746</td>
      <td id="T_4f027_row4_col3" class="data row4 col3" >0.762223</td>
      <td id="T_4f027_row4_col4" class="data row4 col4" >1.000000</td>
    </tr>
  </tbody>
</table>





```python
plt.matshow(corr)
plt.title("Correlation Matrix")
```




    Text(0.5, 1.0, 'Correlation Matrix')




    
![png](output_27_1.png)
    



```python
csp.geometric_mean
```




    Index    2876.389799
    dtype: float64




```python
cb1.geometric_mean
```




    Index    1141.14455
    dtype: float64




```python
cba.geometric_mean
```




    Index    1196.126707
    dtype: float64




```python
cg.geometric_mean
```




    Price ($/t oz)    1441.021045
    dtype: float64




```python
cbtc.geometric_mean
```




    Bitcoin    4399.118256
    dtype: float64


