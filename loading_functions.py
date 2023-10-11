import numpy as np 
import pandas as pd

def load_ten_year_yield(file_path: str = 'ten_year_yield.csv'): 

    yld = pd.read_csv(file_path)

    # Doing formatting on the date
    yld['DATE'] = pd.to_datetime(yld['DATE'])
    yld['DGS10'] = yld['DGS10'].replace('.', np.nan)
    
    # Dropping the values that are na
    yld.dropna(inplace=True)
    yld.set_index('DATE', inplace=True)
    
    # The values come in as strings during coercion
    yld['DGS10'] = yld['DGS10'].astype(float)
    
    # Turning into series since this is one data series
    yld = yld.squeeze()
    
    return yld