```python
import logging

import pandas as pd
from matplotlib import pyplot as plt

logging.basicConfig(level=logging.ERROR)  # default logging for other libraries
logging.getLogger('fe507').level = logging.DEBUG
from fe507 import Data, Collection, DataSource, settings, CollectionGroup
from fe507 import WEEK

settings.data_dir = "../data"
```


```python
b100 = Data(DataSource.BIST100)
```

    DEBUG:fe507.utils:Set up "data_dir" as: ../data
    DEBUG:fe507.utils:working on file: /Users/azat/Developer/Learn/FE507-report/data/BIST100.xlsx
    DEBUG:fe507.utils:read dataframe from excel as: 
    ['Date', 'Index', 'Market cap (m TL)']
    DEBUG:fe507.utils:handling source specific fields for DataSource.BIST100


## a.


```python
col = Collection(b100.data, name="BIST100").get_range(from_year=1990, to_year=2022).get(on='Index').frequency(WEEK)
```


```python
col.raw
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
      <th>1990-01-01</th>
      <td>0.22</td>
    </tr>
    <tr>
      <th>1990-01-08</th>
      <td>0.25</td>
    </tr>
    <tr>
      <th>1990-01-15</th>
      <td>0.31</td>
    </tr>
    <tr>
      <th>1990-01-22</th>
      <td>0.36</td>
    </tr>
    <tr>
      <th>1990-01-29</th>
      <td>0.38</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-11-21</th>
      <td>4570.32</td>
    </tr>
    <tr>
      <th>2022-11-28</th>
      <td>4923.23</td>
    </tr>
    <tr>
      <th>2022-12-05</th>
      <td>4957.77</td>
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>5193.30</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>5391.91</td>
    </tr>
  </tbody>
</table>
<p>1542 rows × 1 columns</p>
</div>




```python
df = pd.DataFrame()
df['sma'] = col.raw.dropna().rolling(52).mean()
```


```python
df
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
      <th>sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1990-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1990-01-08</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1990-01-15</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1990-01-22</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1990-01-29</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-11-21</th>
      <td>2662.462500</td>
    </tr>
    <tr>
      <th>2022-11-28</th>
      <td>2722.355577</td>
    </tr>
    <tr>
      <th>2022-12-05</th>
      <td>2780.632115</td>
    </tr>
    <tr>
      <th>2022-12-12</th>
      <td>2840.089615</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>2904.234808</td>
    </tr>
  </tbody>
</table>
<p>1542 rows × 1 columns</p>
</div>




```python
df.plot(title="BIST100 52 Weeks Moving Average (1990-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 52 Weeks Moving Average (1990-2022)'}, xlabel='date'>




    
![png](output_7_1.png)
    



```python
df['std'] = col.raw.dropna().rolling(52).std()
```


```python
df.plot(title="BIST100 52 Weeks Moving Average & Standard Deviation (1990-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 52 Weeks Moving Average & Standard Deviation (1990-2022)'}, xlabel='date'>




    
![png](output_9_1.png)
    



```python
df['std'].plot(title="BIST100 52 Weeks Standard Deviation (1990-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 52 Weeks Standard Deviation (1990-2022)'}, xlabel='date'>




    
![png](output_10_1.png)
    


## b.


```python
col_d = Collection(b100.data, name="BIST100").get_range(from_year=2002, to_year=2022)
```


```python
col_d.raw
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
      <th>2002-01-01</th>
      <td>2002-01-01</td>
      <td>137.83</td>
      <td>62752.0</td>
      <td>2002-01-01</td>
      <td>2002Q1</td>
    </tr>
    <tr>
      <th>2002-01-02</th>
      <td>2002-01-02</td>
      <td>140.78</td>
      <td>63822.0</td>
      <td>2002-01-02</td>
      <td>2002Q1</td>
    </tr>
    <tr>
      <th>2002-01-03</th>
      <td>2002-01-03</td>
      <td>142.73</td>
      <td>64514.0</td>
      <td>2002-01-03</td>
      <td>2002Q1</td>
    </tr>
    <tr>
      <th>2002-01-04</th>
      <td>2002-01-04</td>
      <td>142.73</td>
      <td>64514.0</td>
      <td>2002-01-04</td>
      <td>2002Q1</td>
    </tr>
    <tr>
      <th>2002-01-07</th>
      <td>2002-01-07</td>
      <td>150.00</td>
      <td>67790.0</td>
      <td>2002-01-07</td>
      <td>2002Q1</td>
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
<p>5470 rows × 5 columns</p>
</div>




```python
ror_d = col_d.get(on="Index").ror().raw
```


```python
ror_d.plot(title="BIST100 Daily Rate of Return (2002-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 Daily Rate of Return (2002-2022)'}, xlabel='date'>




    
![png](output_15_1.png)
    



```python
ror_d.plot(title="BIST100 Daily Rate of Return (2002-2022) Histogram", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Daily Rate of Return (2002-2022) Histogram'}, ylabel='Frequency'>




    
![png](output_16_1.png)
    


## Normality Test

### Using The maximum absolute scaling

https://www.geeksforgeeks.org/data-normalization-with-pandas/


```python
ror_d_max_scaled = ror_d.copy()
```


```python
for column in ror_d_max_scaled.columns:
    ror_d_max_scaled[column] = ror_d_max_scaled[column] / ror_d_max_scaled[column].abs().max()
```


```python
display(ror_d_max_scaled)
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
      <th>2002-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2002-01-02</th>
      <td>0.158800</td>
    </tr>
    <tr>
      <th>2002-01-03</th>
      <td>0.103153</td>
    </tr>
    <tr>
      <th>2002-01-07</th>
      <td>0.372534</td>
    </tr>
    <tr>
      <th>2002-01-08</th>
      <td>-0.060734</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>0.090261</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>-0.275619</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>0.178887</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>0.036718</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>0.251178</td>
    </tr>
  </tbody>
</table>
<p>5143 rows × 1 columns</p>
</div>



```python
ror_d_max_scaled.plot()
```




    <AxesSubplot: xlabel='date'>




    
![png](output_22_1.png)
    



```python
ror_d_max_scaled.plot(kind="hist")
```




    <AxesSubplot: ylabel='Frequency'>




    
![png](output_23_1.png)
    


### Using The min-max feature scaling


```python
df_min_max_scaled = ror_d.copy()
```


```python
for column in df_min_max_scaled.columns:
    df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (
            df_min_max_scaled[column].max() - df_min_max_scaled[column].min())
```


```python
df_min_max_scaled
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
      <th>2002-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2002-01-02</th>
      <td>0.606881</td>
    </tr>
    <tr>
      <th>2002-01-03</th>
      <td>0.577738</td>
    </tr>
    <tr>
      <th>2002-01-07</th>
      <td>0.718816</td>
    </tr>
    <tr>
      <th>2002-01-08</th>
      <td>0.491908</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>0.570986</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>0.379369</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>0.617401</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>0.542945</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>0.655261</td>
    </tr>
  </tbody>
</table>
<p>5143 rows × 1 columns</p>
</div>




```python
df_min_max_scaled.plot()
```




    <AxesSubplot: xlabel='date'>




    
![png](output_28_1.png)
    



```python
df_min_max_scaled.plot(kind='hist')
```




    <AxesSubplot: ylabel='Frequency'>




    
![png](output_29_1.png)
    



```python
df_min_max_scaled.mean()
```




    Index    0.526515
    dtype: float64



### Using The z-score method


```python
df_z_scaled = ror_d.copy()
```


```python
# apply normalization techniques
for column in df_z_scaled.columns:
    df_z_scaled[column] = (df_z_scaled[column] -
                           df_z_scaled[column].mean()) / df_z_scaled[column].std()
```


```python
df_z_scaled
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
      <th>2002-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2002-01-02</th>
      <td>1.148067</td>
    </tr>
    <tr>
      <th>2002-01-03</th>
      <td>0.731741</td>
    </tr>
    <tr>
      <th>2002-01-07</th>
      <td>2.747127</td>
    </tr>
    <tr>
      <th>2002-01-08</th>
      <td>-0.494388</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-12-13</th>
      <td>0.635289</td>
    </tr>
    <tr>
      <th>2022-12-14</th>
      <td>-2.102065</td>
    </tr>
    <tr>
      <th>2022-12-15</th>
      <td>1.298346</td>
    </tr>
    <tr>
      <th>2022-12-16</th>
      <td>0.234701</td>
    </tr>
    <tr>
      <th>2022-12-19</th>
      <td>1.839198</td>
    </tr>
  </tbody>
</table>
<p>5143 rows × 1 columns</p>
</div>




```python
df_z_scaled.plot()
```




    <AxesSubplot: xlabel='date'>




    
![png](output_35_1.png)
    



```python
df_z_scaled.plot(kind='hist')
```




    <AxesSubplot: ylabel='Frequency'>




    
![png](output_36_1.png)
    


## c


```python
from fe507 import MONTH

ror_m = col_d.frequency(MONTH).ror().raw['Index']
```


```python
ror_m
```




    date
    2002-01-01         NaN
    2002-02-01   -0.030049
    2002-03-01   -0.153565
    2002-04-01    0.013078
    2002-05-01   -0.012293
                    ...   
    2022-08-01    0.083400
    2022-09-01    0.168153
    2022-09-30    0.011783
    2022-11-01    0.242991
    2022-12-01    0.218764
    Name: Index, Length: 252, dtype: float64




```python
ror_m.plot(title="BIST100 Monthly Rate of Return (2002-2022)")
```




    <AxesSubplot: title={'center': 'BIST100 Monthly Rate of Return (2002-2022)'}, xlabel='date'>




    
![png](output_40_1.png)
    



```python
ror_m.plot(title="BIST100 Monthly Rate of Return (2002-2022) Histogram", kind='hist')
```




    <AxesSubplot: title={'center': 'BIST100 Monthly Rate of Return (2002-2022) Histogram'}, ylabel='Frequency'>




    
![png](output_41_1.png)
    



```python
df_max_scaled1 = pd.DataFrame(ror_m.copy())
for column in df_max_scaled1.columns:
    df_max_scaled1[column] = df_max_scaled1[column] / df_max_scaled1[column].abs().max()
```


```python
df_max_scaled1.plot()
```




    <AxesSubplot: xlabel='date'>




    
![png](output_43_1.png)
    



```python
df_max_scaled1.plot(kind='hist')
```




    <AxesSubplot: ylabel='Frequency'>




    
![png](output_44_1.png)
    



```python

```
