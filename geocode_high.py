from multiprocessing import Pool, cpu_count
from utils.geo_tools import geocode
from utils.tools import dump_failure, dump_success
import pandas as pd
import json
import re

if __name__ == '__main__':

    # Importing data
    df = pd.read_csv('data/tmp/bobaadr.txt', 
                    dtype=str, 
                    index_col=False,
                    usecols=['physical_id',  #unique ID column 
                            'hhnd', #house number 
                            'stname', #street name 
                            'boro']) #borough or borough code, we can also use zipcode

    df=df.dropna(axis=0, how='all') #remove null

    #rename them to the format that could be recognized by geosupport
    df = df.rename(columns={'physical_id':'uid', 
                            'stname':'street_name', 
                            'hhnd':'house_number', 
                            'boro':'borough_code'})

    df.house_number = df.house_number.apply(lambda x: x.strip())
    df = df[df.house_number != '']
    #convert dataframe to list of dictionaries
    nrows = df.shape[0]
    print(f'Total number of records: {nrows}')
    records = df.to_dict('records')
    
    # Multiprocess
    with Pool(processes=cpu_count()) as pool:
        # map the function geocode on to the entire 
        it = pool.map(geocode, records, 10000) 
    
    ## Dump Success records
    success = dump_success(it)
    # pd.DataFrame(success).to_csv('output/high/success.csv', index=False)
    
    ## Dump Failure records
    failure = dump_failure(it)
    pd.DataFrame(failure).to_csv('output/high/failure.csv', index=False)
