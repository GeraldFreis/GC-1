import pandas as pd
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file

class Transferring_Region():
    def __init__(self):
        self.main_df = pd.read_csv("Database_files/Compiled_csv.csv", low_memory=False)
        # self.title_df = pd.read_csv("Database_files/title.akas.tsv", sep="\t", low_memory=False)
        self.region_df = pd.read_csv("newdataframe.csv", low_memory=False)
    
    """
    POA
    - iterate over every line in the main_df
    - get an index list of the titleId equal to the current TitleId in the line of main_df
    - iterate over that index list until type == "original" 
    - if the region is "\\N"
        - iterate over the index list again until the 'title' is equal to the 'title' of the index with the original type attribute
        then add the region of this index to that of the original line in the main_df
    """
    def transferring_data(self):

        # for line in range(len(self.main_df)):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)

        for line in range(200000, 400000):
            print(line)
            try:
                index = self.region_df[self.region_df["tconst"] == self.main_df.loc[line]["tconst"]].index.to_list()
                self.main_df.at[line, "region"] = self.region_df.at[index[0], "region"]
            except:
                continue;

        write_data_to_file(self.main_df, "main_database_new.csv")
    
    def creating_new_db(self):
        newdf = pd.read_csv("newdataframe.csv")
        counter = 365390
        hit_list = list()

        # for line in range(len(self.title_df)):
        for line in range(14000000, len(self.title_df)):
            if(self.title_df.loc[line]["types"] == "original"):
                if(line >= 10 and line <= len(self.title_df)-10):
                    for index in range(line-10, line+10):
                        if(self.title_df.loc[line]["title"] == self.title_df.loc[index]["title"]):
                            newdf.at[counter, "tconst"] = self.title_df.loc[line]["titleId"]
                            newdf.at[counter, "region"] = self.title_df.loc[index]["region"]
                            counter += 1
                            break;
                else:
                    for index in range(line-4, line+10):
                        if(self.title_df.loc[line]["title"] == self.title_df.loc[index]["title"]):
                            newdf.at[counter, "tconst"] = self.title_df.loc[line]["titleId"]
                            newdf.at[counter, "region"] = self.title_df.loc[index]["region"]
                            counter += 1
                            break;
            print(line)
                

        
        write_data_to_file(newdf, "newdataframe.csv")


first_transfer = Transferring_Region()
first_transfer.transferring_data()
# first_transfer.creating_new_db()
