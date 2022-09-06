import pandas as pd

def write_data_to_file(dataframe, filename:str)->None:
    dataframe.to_csv(filename)