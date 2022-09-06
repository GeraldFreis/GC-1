import pandas as pd
import matplotlib.pyplot as plt
import webbrowser as wb

def get_year(givenname: str)->int:
    link = "https://www.imdb.com/find?q=" + givenname
    import requests
    url = requests.get(link)
    htmltext = url.text()

    for line in htmltext:
        line.split(" ")

        if(givenname in line):
            for index, val in enum(line):
                if(val.isnumber() is True):
                    year = val + line[index+1] + line[index+2] + line[index+3]
                    return year


    # get the data of the website


class Cleaning_data():
    def __init__(self):
        self.df = pd.read_csv("Database_files/Compiled_csv.csv", sep=",", low_memory=False)
    
    def change_values(self):
        year_list = list(["1890", "1891", "1892", "1893", "1894", "1895", "1896", "1897", "1898", "1899"])
        
        for year in year_list:
            index_list = self.df.index[self.df["startYear"] == year].to_list()

            for index in index_list:
                name = self.df.at[index, "primaryTitle"]

                online_year = get_year(name)
                if(online_year == self.df.at[index, "startYear"]):
                    pass
                else:
                    self.df.at[index, "startYear"] = online_year

