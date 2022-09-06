import pandas as pd;
import matplotlib.pyplot as plt
from extraneous_functions import write_data_to_file


class Regions_analysis():
    def __init__(self):
        self.regions_df = pd.read_csv("Database_files/Regions_analysis/newdataframe.csv", low_memory=False)
        
    def most_common_region(self):
        plotable_df = pd.DataFrame(columns=["region", "occurrence"])
        counter = 1
        regions_list = list()

        for line in range(len(self.regions_df)-1):
            # if the region is in the plotable data frame then we just add one to its occurrence
            print(line)
            region = self.regions_df.at[line, "region"]
            if(region not in regions_list):
                regions_list.append(region)

                plotable_df.at[counter, "region"] = region
                plotable_df.at[counter, "occurrence"] = 1
            
            else:
                region = self.regions_df.at[line, "region"]
                print(region)
                try:
                    index = plotable_df.index[plotable_df["region"] == region].to_list()[0]
                except:
                    index = counter;
                    counter += 1
                    plotable_df.at[index, "occurrence"] = 1

                plotable_df.at[index, "region"] = region
                plotable_df.at[index, "occurrence"] = plotable_df.at[index, "occurrence"] + 1
                # index = plotable_df.index[plotable_df["region"] == region].to_list()[0]
                # plotable_df.at[index, "occurrence"] = int(plotable_df.at[index, "occurrence"]) + 1
                # print(index)

        
        write_data_to_file(plotable_df, "region_vs_occurrence.csv")
        plt.bar(plotable_df["region"], plotable_df["occurrence"])

        plt.show()
    
    def plotting_most_common_region(self):
        plotable_df = pd.read_csv("Database_files/Regions_analysis/region_vs_occurrence.csv", low_memory=False)
        # plt.plot(plotable_df["region"], plotable_df["occurrence"])
        plt.bar(plotable_df["region"].astype(str).head(20), plotable_df["occurrence"].astype(int).head(20))
        plt.title("Movies produced vs Region")
        plt.xlabel("Region")
        plt.ylabel("Number of movies produced")
        plt.show()
    
    def region_vs_time(self):
        self.main_df = pd.read_csv("main_database_new.csv", low_memory=False)

        for line in range(len(self.regions_df)):
            print(line)
            tconst = self.regions_df.loc[line]["tconst"]
            try:
                index = self.main_df.index[self.main_df["tconst"] == tconst].to_list()[0]
                print(index)
                self.regions_df.at[line, "year"] = self.main_df.loc[index]["startYear"]
            except:
                continue;
        
        write_data_to_file(self.regions_df, "Database_files/Regions_analysis/region_vs_year.csv")
    

analysis = Regions_analysis()
analysis.region_vs_time()